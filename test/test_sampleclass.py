# test_sampleclass
#
# Author: Oliver Schneider
# Email: 
# Student ID: 1234567890
#
# these are the unit tests for SampleClass


import unittest
from sampleclass.sampleclass import SampleClass


class TestSampleClass(unittest.TestCase):

    #TODO: comment
    def test_constructor1(self):
        sc = SampleClass(1)
        self.assertIsNotNone(sc)


    #TODO: comment
    def test_sampleVariableAccessor1(self):
        sc = SampleClass(1)
        self.assertEqual(sc.getSampleVariable(), 1)


    #TODO: comment
    def test_sampleVariableMutator1(self):
        sc = SampleClass(1)
        self.assertEqual(sc.getSampleVariable(), 1)
        sc.setSampleVariable(2)
        self.assertEqual(sc.getSampleVariable(), 2)
