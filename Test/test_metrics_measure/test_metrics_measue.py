import os
import unittest

from App.metrics_measure.metrics_measure import MetricsMeasure

cwd = os.getcwd()
class TestMetricsMeasure(unittest.TestCase):

    def test_compute_AIH(self):
        path = cwd + "/../../Data/DreemCPAP_test_file.edf"
        output = MetricsMeasure.compute_AIH(path)
        expected = 0
        self.assertEqual(expected,output)