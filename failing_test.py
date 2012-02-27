#!/usr/bin/python
from __future__ import absolute_import, print_function, unicode_literals
import yaml

inobj = {
      "date": "2001-01-23",
      "state": "MI",
      "quantity": 4
      }

print("type inobj = %s" % type(inobj))
print(inobj)
res = yaml.dump(inobj, encoding="utf-8", default_flow_style=False,
                     default_style=False, canonical=False, Dumper=yaml.SafeDumper)
print("'%s'" % res)
