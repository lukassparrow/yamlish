# -*- coding: utf-8 -*-
import unittest

class TestBasics(unittest.TestCase):
    def test_import(self):
        import yamlish
        from yamlish import Reader #IGNORE:W0612
        from yamlish import Writer #IGNORE:W0612
        self.assertTrue(yamlish.__version__,
            "Testing import of yamlish, version %s." % yamlish.__version__)

if __name__ == "__main__":
    unittest.main()
