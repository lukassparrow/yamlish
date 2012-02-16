# -*- coding: utf-8 -*-
import unittest

class TestBasics(unittest.TestCase):
    def test_import(self):
        import yamlish
        from yamlish import Reader
        self.assert_(True, "Importing Reader.")
        from yamlish import Writer
        self.assert_(True, "Importing Writer.")
        self.assert_(True,
            "Testing import of yamlish, version %s." % yamlish.__version__)

if __name__ == "__main__":
    unittest.main()
