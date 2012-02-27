# -*- coding: utf-8 -*-  IGNORE:C0111
from __future__ import absolute_import, print_function, unicode_literals
import logging
from test import test_reader, test_input
import yamlish
import unittest
import yaml
logging.basicConfig(level=logging.INFO)

def _generate_test_name(source):
    """
    Clean up human-friendly test name into a method name.
    """
    out = source.replace(' ', '_').replace(':', '').lower()
    return "test_%s" % out

def _create_test(test_src, tested_function):
    """
    Decorate tested function to be used as a method for TestCase.
    """
    def do_test_expected(self):
        """
        Execute a test by calling a tested_function on test_src data.
        """
        if ('skip' in test_src) and test_src['skip']:
            logging.info("test_src skipped!")
            return

        got = ""
        if 'error' in test_src:
            self.assertRaises(test_src['error'], tested_function,
                              test_src['in'])
        else:
            want = test_src['out']
            got = tested_function(test_src['in'])
            logging.debug("test_src['out'] = %s", unicode(test_src['out']))
            self.assertEqual(got, want, """Result matches
            expected = %s
            
            observed = %s
            """ % (want, got))

    return do_test_expected


def generate_testsuite(test_data, test_case_shell, test_fce):
    """
    Generate tests from the test data, class to build upon and function to use for testing.
    """
    for in_test in test_data:
        if ('skip' in in_test) and in_test['skip']:
            logging.info("test %s skipped!", in_test['name'])
            continue
        name = _generate_test_name(in_test['name'])
        test_method = _create_test (in_test, test_fce)
        test_method.__name__ = str('test_%s' % name)  # IGNORE:W0622
        setattr (test_case_shell, test_method.__name__, test_method)
