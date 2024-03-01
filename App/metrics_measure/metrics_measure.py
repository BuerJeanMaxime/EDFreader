from pyedflib import highlevel

from App.mne_reader.mne_reader import MNEReader


class MetricsMeasure:

    @staticmethod
    def compute_AIH(path):
        signals, signal_headers, header = MNEReader.read_edf_file_pyedflib(path)
        airflow_signal = signals[0]

        sample_frequency = header['sample_rate'][0]

        apnea_threshold = 0.5  # Adjust according to your signal characteristics
        hypopnea_threshold = 0.3  # Adjust according to your signal characteristics

        # Detect apneas and hypopneas
        apnea_events = (airflow_signal < apnea_threshold).astype(int)
        hypopnea_events = ((airflow_signal >= apnea_threshold) & (airflow_signal < hypopnea_threshold)).astype(int)

        total_apneas = apnea_events.sum()
        total_hypopneas = hypopnea_events.sum()
        total_sleep_time_hours = header['file_duration'] / 3600  # Convert seconds to hours

        ahi = (total_apneas + total_hypopneas) / total_sleep_time_hours * 60
        return ahi

