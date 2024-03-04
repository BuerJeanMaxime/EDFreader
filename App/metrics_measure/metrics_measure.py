import numpy as np

from App.custom_types import FloatArray
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
        apnea_events: np.array = (airflow_signal < apnea_threshold).astype(int)
        hypopnea_events: np.array = ((airflow_signal >= apnea_threshold) & (airflow_signal < hypopnea_threshold)).astype(int)

        total_apneas: int = apnea_events.sum()
        total_hypopneas: int = hypopnea_events.sum()
        total_sleep_time_hours: float = duration_seconds / 3600  # Convert seconds to hours

        ahi: float = (total_apneas + total_hypopneas) / total_sleep_time_hours * 60
        return ahi

    @staticmethod
    def compute_RDI(path):

        def detect_apneas_hypopneas_reras(airflow_data=None, thoracic_data=None, abdominal_data=None):
            apneas_hypopneas_reras = 1
            #need help
            return apneas_hypopneas_reras

        signals, signal_headers, header = MNEReader.read_edf_file_pyedflib(path)

        # Read data from relevant channels
        airflow_data = signals[0]
        thoracic_data = signals[1]
        abdominal_data = signals[2]

        num_samples: int = len(signals[0])
        sample_frequency: float = signal_headers[0]['sample_rate']

        # Example: Compute the RDI (sum of apneas, hypopneas, and RERAs per hour)
        apneas_hypopneas_reras = detect_apneas_hypopneas_reras(airflow_data, thoracic_data, abdominal_data)
        total_events = len(apneas_hypopneas_reras)

        # Assuming the recording duration is in seconds
        recording_duration_hours = num_samples / sample_frequency

        RDI = (total_events / recording_duration_hours)

        return RDI
