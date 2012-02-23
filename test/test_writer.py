# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import unittest
import yamlish

test_data_list = [
  {
    "name": 'Simple scalar',
    "in": 1,
    "out": [ '--- 1', '...', ],
  },
  {
    "name": 'Undef',
    "in": None,
    "out": [ '--- ~', '...', ],
  },
  {
    "name": 'Unprintable',
    "in": "\x01\n\t",
    "out": [ '--- "\x01\n\t"', '...', ],
  },
  {
    "name": 'Simple array',
    "in": [ 1, 2, 3 ],
    "out": [ '---', '- 1', '- 2', '- 3', '...', ],
  },
  {
    "name": 'Array, two elements, None',
    "in": [ None, None ],
    "out": [ '---', '- ~', '- ~', '...', ],
  },
  {
    "name": 'Nested array',
    "in": [ 1, 2, [ 3, 4 ], 5 ],
    "out":
     [ '---', '- 1', '- 2', '-', '  - 3', '  - 4', '- 5', '...', ],
  },
  {
    "name": 'Simple hash',
    "in": { "one": '1', "two": '2', "three": '3' },
    "out": [ '---', 'one: 1', 'three: 3', 'two: 2', '...', ],
  },
  {
    "name": 'Nested hash',
    "in": {
      "one": '1',
      "two": '2',
      "more": { "three": '3', "four": '4' }
    },
    "out": [
      '---',
      'more:',
      '  four: 4',
      '  three: 3',
      'one: 1',
      'two: 2',
      '...',
    ],
  },
  {
    "name": 'Unprintable key',
    "in": { "one": '1', "\x02": '2', "three": '3' },
    "out": [ '---', '"\x02": 2', 'one: 1', 'three: 3', '...', ],
  },
  {
    "name": 'Empty key',
    "in": { '': 'empty' },
    "out": [ '---', "'': empty", '...', ],
  },
  {
    "name": 'Empty value',
    "in": { '': '' },
    "out": [ '---', "'': ''", '...', ],
  },
  {
    "name": 'Complex',
    "in": {
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
    },
    "out": [
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
    ],
  },
]

# plan(tests = len(test_data_list) * 5)

class TestWriter(unittest.TestCase):
    def test_writer(self):
        for test in test_data_list:
            name = test['name']
            data = test['in']

            got = []
            # We currently don't throw any exceptions in Writer, so this
            # this is always false
            if 'error' in test:
                self.assertRaises(test['error'], yamlish.write, test['in'])
            else:
                want = test['out']
                yamlish.write(test['in'], got)
                self.assertEqual(got, want, """%s: Result matches
                    expected = %s
                    
                    observed = %s
                    """ % (name, want, got))

                # Now try parsing it
                parsed = yamlish.load(got) # FIXME got has an iterator
                self.assertEqual(parsed, data, """%s: Reparse OK
                    expected = %s
                    
                    observed = %s
                    """ % (name, data, parsed))
