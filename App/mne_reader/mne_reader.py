import mne
from mne.io.edf.edf import RawEDF
from pyedflib import highlevel


class MNEReader:

    @staticmethod
    def read_edf_file_mne(path):
        raw_edf: RawEDF = mne.io.read_raw_edf(path)
        return raw_edf

    @staticmethod
    def read_edf_file_pyedflib(path):
        signals, signal_headers, header = highlevel.read_edf(path)
        return signals, signal_headers, header