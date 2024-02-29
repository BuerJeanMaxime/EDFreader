import mne
from mne.io.edf.edf import RawEDF


class MNEReader:

    @staticmethod
    def read_edf_file(path):
        raw_edf: RawEDF = mne.io.read_raw_edf(path)
        return raw_edf