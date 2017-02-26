import unittest
import os
from .. import srt_parser
from .. import record


class TestSrtParser(unittest.TestCase):

    def test_sample(self):
        parser = srt_parser.SrtParser()
        file = open(os.path.dirname(__file__) + '/samples/srt_sample.srt', 'r')
        srt_record = next(parser.parse(file))

        self.assertIsInstance(srt_record, record.Record)

        self.assertEqual(srt_record.start, '00:00:01,383')
        self.assertEqual(srt_record.latitude, '49,231384')
        self.assertEqual(srt_record.longtitude, '16,595253')
        self.assertEqual(srt_record.time, 1.383)

        srt_record = next(parser.parse(file))

        self.assertIsInstance(srt_record, record.Record)

        self.assertEqual(srt_record.start, '00:00:04,383')
        self.assertEqual(srt_record.latitude, '49,231393')
        self.assertEqual(srt_record.longtitude, '16,595234')
        self.assertEqual(srt_record.time, 4.383)

if __name__ == '__main__':
    unittest.main()
