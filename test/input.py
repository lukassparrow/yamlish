# -*- coding: utf-8 -*-
import logging
import unittest
import yamlish

IN = """
  ---
  bill-to:
    address:
      city: "Royal Oak"
      lines: "458 Walkman Dr.\nSuite #292\n"
      postal: 48046
      state: MI
    family: Dumars
    given: Chris
  comments: "Late afternoon is best. Backup contact is Nancy Billsmer @ 338-4338\n"
  date: 2001-01-23
  invoice: 34843
  product:
    -
      description: Basketball
      price: 450.00
      quantity: 4
      sku: BL394D
    -
      description: "Super Hoop"
      price: 2392.00
      quantity: 1
      sku: BL4438H
  tax: 251.42
  total: 4443.52
  ...
"""

OUT = {
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
  'comments':
   "Late afternoon is best. Backup contact is Nancy Billsmer @ 338-4338\n",
  'total': '4443.52'
}

class TestInput(unittest.TestCase):
    """FIXME description of this class"""
    def test_reader(self):
        scalar = IN
        source = [
          {
            "name": 'Array reference',
            "source": IN.split("\n"),
          },
#          {
#            "name": 'Closure',
#            "source": sub { shift @lines },
#          },
          {
            "name": 'Scalar',
            "source": IN,
          }
        ]

        for src in source:
          name = src['name']
          yaml = yamlish.Reader()
          self.assert_(True, "$name: Created")
          self.assert_(isinstance(yaml, yamlish.Reader))

          #my $got = eval { $yaml -> read($src -> {source}) };
          got = yaml.read(src['source'])
          self.assertEqual(got, OUT, """%s: Result matches
          expected = %s
          
          observed = %s
          """ % (name, OUT, got))

if __name__ == "__main__":
    unittest.main()
