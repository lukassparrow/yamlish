# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import re
import unittest
import yamlish
from . import TODO

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
    "normalise": (lambda x: buf1),
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
    @TODO
    def test_output(self):
        for dest in destination:
            name = dest['name']
            yaml = yamlish.Writer()
            self.assert_(True, "%s: Created" % name)
            self.assert_(isinstance(yaml, yamlish.Writer))

            yaml.write(IN, dest[destination])
            got = dest['normalise']()

            self.assertEqual(got, OUT, """%s: Result matches
              expected = %s
              
              observed = %s
              """ % (name, OUT, got))
