import unittest
import load, input, reader, output, writer

add_tests_from_class = unittest.TestLoader().loadTestsFromTestCase

suite = unittest.TestSuite()
suite.addTest(add_tests_from_class(load.TestBasics))
suite.addTest(add_tests_from_class(TestHappyPath))
suite.addTest(add_tests_from_class(TestBadPath))
suite.addTest(add_tests_from_class(TestPiglitData))
suite.addTest(add_tests_from_class(TestMainArgsMgmt))
