# -*- coding: utf-8 -*-

import yaml
import pprint

__version__ = "0.1"

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

class Reader(object):
    def __init__(self):
        pass

    def get_raw(self):
        pass

    def read(self, source):
        pass

class Writer(object):
    def __init__(self):
        pass

    def write(self, source, destination):
        pass

#print yaml.dump(OUT, canonical=False, default_flow_style=False, default_style=False)
