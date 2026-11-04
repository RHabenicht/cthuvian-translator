import unittest
from rlyehian_reference.__main__ import analyze, lookup, data

class LexiconTests(unittest.TestCase):
    def test_source_soul(self):
        self.assertEqual(lookup('soul'), ["orr'e"])
    def test_phrase(self):
        self.assertEqual(analyze('cross over, soul!')['gloss'], "ch', orr'e!")
    def test_ambiguous(self):
        self.assertEqual(set(lookup('call')), {"'ai", 'uln'})
        self.assertEqual(analyze('call')['issues'][0]['type'], 'ambiguous')
    def test_unrecognized(self):
        self.assertEqual(analyze('placeholder')['issues'][0]['type'], 'unknown')
    def test_line_breaks(self):
        self.assertEqual(analyze('soul\nspirit')['gloss'], "orr'e\norr'e")
    def test_public_reference_only(self):
        info=data()
        self.assertEqual(info['source']['revision'], '482bd14e19d6a25094af800e6e2a65836484d319')
        self.assertNotIn('names', info)

if __name__ == '__main__':
    unittest.main()
