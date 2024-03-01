import datetime
import os
import unittest

from numpy import array

from App.mne_reader.mne_reader import MNEReader

cwd = os.getcwd()


class TestMNEReader(unittest.TestCase):

    def helper_assert_read_edf_file(self, raw_edf):
        return {
            "nchan": raw_edf.info['nchan'],
            "ch_names": raw_edf.ch_names
        }

    def test_read_edf_file_mne(self):
        raw_edf = MNEReader.read_edf_file_mne(cwd + "/../../Data/DreemCPAP_test_file.edf")
        output = self.helper_assert_read_edf_file(raw_edf)
        expected = {'ch_names': ['Accelero Norm',
                                 'EEG F7-O1',
                                 'EEG F8-O2',
                                 'EEG F8-F7',
                                 'EEG F8-O1',
                                 'EEG F7-O2',
                                 'Positiongram',
                                 'Respiration x',
                                 'Respiration y',
                                 'Respiration z'],
                    'nchan': 10}
        self.assertEqual(expected, output)

    def test_read_edf_file_pyedflib(self):
        signals, signal_headers, header = MNEReader.read_edf_file_pyedflib(cwd + "/../../Data/DreemCPAP_test_file.edf")
        output = [signals, signal_headers, header]
        expected = 3
        self.assertEqual(expected, len(output))
