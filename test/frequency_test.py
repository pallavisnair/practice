import unittest
from frequency import word_cloud

class FrequencyTest(unittest.TestCase):
    avoid = ["i", "the", "and"]
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    def test_simple_string(self):
        str = 'pallavi yadu pallavi'
        expected_result = {"pallavi": 2, "yadu": 1}
        result = word_cloud(str, self.avoid, self.punctuations)
        self.assertEqual(result, expected_result)

