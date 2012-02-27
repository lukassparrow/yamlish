# -*- coding: utf-8 -*-
"""
Test general output functionality.

Without much stress on the format itself.
"""
from __future__ import absolute_import, print_function, unicode_literals
from StringIO import StringIO
import re
import unittest
import yamlish

OUT = [
  "---",
  "bill-to:",
  "  address:",
  "    city: 'Royal Oak'",
  "    lines: \"458 Walkman Dr.\\nSuite #292\\n\"",
  "    postal: 48046",
  "    state: MI",
  "  family: Dumars",
  "  given: Chris",
  "comments: \"Late afternoon is best. Backup contact is Nancy Billsmer \@ 338-4338\\n\"",
  "date: 2001-01-23",
  "invoice: 34843",
  "product:",
  "  -",
  "    description: Basketball",
  "    price: 450.00",
  "    quantity: 4",
  "    sku: BL394D",
  "  -",
  "    description: 'Super Hoop'",
  "    price: 2392.00",
  "    quantity: 1",
  "    sku: BL4438H",
  "tax: 251.42",
  "total: 4443.52",
  "...",
]

IN = {
  'bill-to': {
    'given': 'Chris',
    'address': {
      'city': 'Royal Oak',
      'postal': '48046',
      'lines': "458 Walkman Dr.\nSuite #292\n",
      'state': 'MI'
    },
    'family': 'Dumars'
  },
  'invoice': '34843',
  'date': '2001-01-23',
  'tax': '251.42',
  'product': [
    {
      'sku': 'BL394D',
      'quantity': '4',
      'price': '450.00',
      'description': 'Basketball'
    },
    {
      'sku': 'BL4438H',
      'quantity': '1',
      'price': '2392.00',
      'description': 'Super Hoop'
    }
  ],
  'comments': "Late afternoon is best. Backup contact is Nancy Billsmer @ 338-4338\n",
  'total': '4443.52'
}

buf1 = []
buf2 = []
buf3 = ""

destination = [
  {
    "name": 'Array reference',
    "destination": buf1,
    "normalise": (lambda : buf1),
  },
#  {
#    "name": 'Closure',
#    "destination": sub { push @buf2, shift },
#    "normalise": sub { return \@buf2 },
#  },
  {
    "name": 'Scalar',
    "destination": buf3,
    "normalise": (lambda : re.split(r" \n ", buf3))
  }
]

class TestOuptut(unittest.TestCase):
    def setUp(self):
        """
        Transform expected list into string which we actually use.
        """
        self._expected = ""
        for line in OUT:
            self._expected += "%s\n" % line


    def test_file_output(self):
        """
        Test output to a file.
        """
        outf = StringIO()
        yamlish.dump(IN, outf)
        outf.seek(0)
        got = outf.read()
        outf.close()
        self.assertEqual(got, self._expected, """Result matches
              expected = %s

              observed = %s
              """ % (self._expected, got))

    def test_string_output(self):
        """
        Test output to a string.
        """
        got = yamlish.dumps(IN)
        self.assertEqual(got, self._expected, """Result matches
              expected = %s
              
              observed = %s
              """ % (self._expected, got))

if __name__ == "__main__":
    unittest.main()
