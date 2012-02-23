# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import logging
from test import test_reader, test_input
import yamlish
import unittest
import yaml
logging.basicConfig(level=logging.DEBUG)

def generate_test_name(source):
    out = source.replace(' ', '_').replace(':', '').lower()
    return "test_%s" % out

def create_test(test_src, tested_function):
    def do_test_expected(self):
        #self.assertEqual(under_test(pair[0]), pair[1])
        if ('skip' in test_src) and test_src['skip']:
            logging.info("test_src skipped!")
            return

        # rather keep original tests in lists even though we could
        # do multiline strings 
        source = "\n".join(test_src['in']) + "\n"
        logging.debug("source = %s", source)

        got = ""
        if 'error' in test_src:
            self.assertRaises(test_src['error'], tested_function, test_src['in'])
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
    for in_test in test_data:
        if ('skip' in in_test) and in_test['skip']:
            logging.info("test %s skipped!", in_test['name'])
            continue
        name = generate_test_name(in_test['name'])
        test_method = create_test (in_test, test_fce)
        test_method.__name__ = str('test_%s' % name)
        setattr (test_case_shell, test_method.__name__, test_method)

class TestInput(unittest.TestCase):
    pass

class TestReader(unittest.TestCase):
    pass

if __name__ == "__main__":
    generate_testsuite(test_reader.test_data_list, TestReader, yamlish.load)
    generate_testsuite(test_input.test_data_list, TestInput, yamlish.load)
    unittest.main()
