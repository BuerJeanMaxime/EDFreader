from pyedflib import highlevel

from App.custom_types import FloatArray, IntArray
from App.mne_reader.mne_reader import MNEReader


class MetricsMeasure:

    @staticmethod
    def compute_AIH(path):
        signals, signal_headers, header = MNEReader.read_edf_file_pyedflib(path)
        airflow_signal: FloatArray = signals[0]

        apnea_threshold: float = 0.5  # Adjust according to your signal characteristics
        hypopnea_threshold: float = 0.3  # Adjust according to your signal characteristics
        sample_frequency: float = signal_headers[0]['sample_rate']
        num_samples: int = len(signals[0])

        # Calculate the duration
        duration_seconds: float = num_samples / sample_frequency
        # Detect apneas and hypopneas
        apnea_events: IntArray = (airflow_signal < apnea_threshold).astype(int)
        hypopnea_events: float = ((airflow_signal >= apnea_threshold) & (airflow_signal < hypopnea_threshold)).astype(int)

        total_apneas: int = apnea_events.sum()
        total_hypopneas: int = hypopnea_events.sum()
        total_sleep_time_hours: float = duration_seconds / 3600  # Convert seconds to hours

        ahi: float = (total_apneas + total_hypopneas) / total_sleep_time_hours * 60
        return ahi

