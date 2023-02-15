import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('sumit'.upper(), 'SUMIT')

    def test_isupper(self):
        self.assertTrue('SUMIT'.isupper())
        self.assertFalse('Sumit'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)







