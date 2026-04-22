from EmotionDetection.emotion_detection import emotion_detector
import unittest
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector("I am so glad this happened")
        self.assertEqual(result_1[dom_emote_label], 'joy')

unittest.main()