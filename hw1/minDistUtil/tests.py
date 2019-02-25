from levenshtein import Levenshtein
from io import StringIO
import unittest

class TestBasicFunctionality(unittest.TestCase):
    def test_example(self):
        examples = { 
            ("", "") : 0,
            ("a a a", "a a a") : 0,
            ("a b", "a a a") : 1,
            ("a b c a", "a a a") : 1,
            ("foo", "bar") : 6,
            ("foo", "fooo") : 1
        }

        for words, distance in examples.items():
            out = StringIO()
            Levenshtein(words[0], words[1], " ", True, False, False, out=out)
            self.assertEqual("Minimum edit distance: " + str(distance) + '\n', out.getvalue())

    def test_wer(self):
        examples = {
            ("foo", "bar") : 1.0,
            ("foo bar", "foo baz") : 1/2,
            ("foo foo", "bar baz") : 1.0,
            ("", "") : 0.0
        }

        for words, wer in examples.items():
            out = StringIO()
            Levenshtein(words[0], words[1], " ", False, False, True, out=out)
            self.assertEqual("WER: " + str(wer) + '\n', out.getvalue())



if __name__ == "__main__":
    unittest.main()