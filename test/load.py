# -*- coding: utf-8 -*-
import unittest

class TestBasics(unittest.TestCase):
    def test_import(self):
        import yamlish
        from yamlish import Reader
        from yamlish import Writer
        self.assert_(True,
            "Testing import of yamlish, version %s." % yamlish.__version__)
