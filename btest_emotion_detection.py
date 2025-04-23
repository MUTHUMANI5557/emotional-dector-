import unittest
from emotion_detector import mock_emotion_detection

class TestEmotionDetection(unittest.TestCase):

    def test_detect_anger(self):
        result = mock_emotion_detection("I hate working long hours")
        self.assertGreater(result['anger'], 0.5)
        self.assertLess(result['joy'], 0.1)

    def test_detect_joy(self):
        result = mock_emotion_detection("I love sunny days")
        self.assertGreater(result['joy'], 0.5)
        self.assertLess(result['anger'], 0.1)

    def test_neutral_input(self):
        result = mock_emotion_detection("Today is an ordinary day.")
        self.assertIn('sadness', result)
        self.assertIn('joy', result)
        self.assertIn('fear', result)
        self.assertIn('disgust', result)
        self.assertIn('anger', result)

if __name
