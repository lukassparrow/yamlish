# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import yamlish
import test
import unittest

test_data_list = [{
    "name": 'Non UTF8 test',
    "in": ['--- \xbd\xd0\xe1 \xd1\xeb\xdb\xde \xdc\xdd\xde\xd3\xde' +
           '\xdd\xd0 \xe7\xd5\xdb\xdd\xd5;\n', '...', ],
    "out": "Нас было много на челне;",
}]


class TestReader(unittest.TestCase):  # IGNORE:C0111
    pass

test.generate_testsuite(test_data_list, TestReader, yamlish.load)

if __name__ == "__main__":
    unittest.main()
