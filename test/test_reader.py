# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
import re
import unittest
import yamlish

SCHEDULE = [
  {
    "name": 'Hello World',
    "in": [ '--- Hello, World', '...', ],
    "out": "Hello, World",
  },
  {
    "name": 'Hello World 2',
    "in": [ '--- \'Hello, \'\'World\'', '...', ],
    "out": "Hello, 'World",
  },
  {
    "name": 'Hello World 3',
    "in": [ '--- "Hello, World"', '...', ],
    "out": "Hello, World",
  },
  {
    "name": 'Hello World 4',
    "in": [ '--- "Hello, World"', '...', ],
    "out": "Hello, World",
  },
  {
    "name": 'Hello World 4',
    "in": [ '--- >', '   Hello,', '      World', '...', ],
    "out": "Hello, World\n",
  },
  {
    "name": 'Hello World 5',
    "in": [ '--- >', '   Hello,', '  World', '...', ],
    "error": re.compile(r"Missing\s+'[.][.][.]'"),
  },
  {
    "name": 'Simple array',
    "in": [ '---', '- 1', '- 2', '- 3', '...', ],
    "out": [ '1', '2', '3' ],
  },
  {
    "name": 'Mixed array',
    "in": [ '---', '- 1', '- \'two\'', '- "three\n"', '...', ],
    "out": [ '1', 'two', "three\n" ],
  },
  {
    "name": 'Hash in array',
    "in": [ '---', '- 1', '- two: 2', '- 3', '...', ],
    "out": [ '1', { "two": '2' }, '3' ],
  },
  {
    "name": 'Hash in array 2',
    "in": [ '---', '- 1', '- two: 2', '  three: 3', '- 4', '...', ],
    "out": [ '1', { "two": '2', "three": '3' }, '4' ],
  },
  {
    "name": 'Nested array',
    "in": [
      '---',
      '- one',
      '-',
      '  - two',
      '  -',
      '    - three',
      '  - four',
      '- five',
      '...',
    ],
    "out": [ 'one', [ 'two', ['three'], 'four' ], 'five' ],
  },
  {
    "name": 'Nested hash',
    "in": [
      '---',
      'one:',
      '  five: 5',
      '  two:',
      '    four: 4',
      '    three: 3',
      'six: 6',
      '...',
    ],
    "out": {
      "one": { "two": { "three": '3', "four": '4' }, "five": '5' },
      "six": '6'
    },
  },

  {
    "name": 'Original YAML::Tiny test',
    "in": [
      '---',
      'invoice: 34843',
      'date   : 2001-01-23',
      'bill-to:',
      '    given  : Chris',
      '    family : Dumars',
      '    address:',
      '        lines: |',
      '            458 Walkman Dr.',
      '            Suite #292',
      '        city    : Royal Oak',
      '        state   : MI',
      '        postal  : 48046',
      'product:',
      '    - sku         : BL394D',
      '      quantity    : 4',
      '      description : Basketball',
      '      price       : 450.00',
      '    - sku         : BL4438H',
      '      quantity    : 1',
      '      description : Super Hoop',
      '      price       : 2392.00',
      'tax  : 251.42',
      'total: 4443.52',
      'comments: >',
      '    Late afternoon is best.',
      '    Backup contact is Nancy',
      '    Billsmer @ 338-4338',
      '...',
    ],
    "out": {
      "bill - to": {
        "given": 'Chris',
        "address": {
          "city": 'Royal Oak',
          "postal": '48046',
          "lines": "458 Walkman Dr.\nSuite #292\n",
          "state": 'MI'
        },
        "family": 'Dumars'
      },
      "invoice": '34843',
      "date": '2001-01-23',
      "tax": '251.42',
      "product": [
        {
          "sku": 'BL394D',
          "quantity": '4',
          "price": '450.00',
          "description": 'Basketball'
        },
        {
          "sku": 'BL4438H',
          "quantity": '1',
          "price": '2392.00',
          "description": 'Super Hoop'
        }
      ],
      'comments':
       "Late afternoon is best. Backup contact is Nancy Billsmer @ 338-4338\n",
      "total": '4443.52'
    }
  },

  # Tests harvested from YAML::Tiny
  {
    "in": ['...'],
    "name": 'Regression: empty',
    "error": re.compile(r"document\s+header\s+not\s+found")
  },
  {
    "in": [ '# comment', '...' ],
    "name": 'Regression: only_comment',
    "error": re.compile(r"document\s+ header\s+ not\s+ found")
  },
  {
    "out": None,
    "in": [ '---', '...' ],
    "name": 'Regression: only_header',
    "error": re.compile(r"Premature\s+end", re.I),
  },
  {
    "out": None,
    "in": [ '---', '---', '...' ],
    "name": 'Regression: two_header',
    "error": re.compile(r"Unexpected\s+start", re.I),
  },
  {
    "out": None,
    "in": [ '--- ~', '...' ],
    "name": 'Regression: one_undef'
  },
  {
    "out": None,
    "in": [ '---  ~', '...' ],
    "name": 'Regression: one_undef2'
  },
  {
    "in": [ '--- ~', '---', '...' ],
    "name": 'Regression: two_undef',
    "error": re.compile(r"Missing\s+'[.][.][.]'"),
  },
  {
    "out": 'foo',
    "in": [ '--- foo', '...' ],
    "name": 'Regression: one_scalar',
  },
  {
    "out": 'foo',
    "in": [ '---  foo', '...' ],
    "name": 'Regression: one_scalar2',
  },
  {
    "in": [ '--- foo', '--- bar', '...' ],
    "name": 'Regression: two_scalar',
    "error": re.compile(r"Missing\s+'[.][.][.]'"),
  },
  {
    "out": ['foo'],
    "in": [ '---', '- foo', '...' ],
    "name": 'Regression: one_list1'
  },
  {
    "out": [ 'foo', 'bar' ],
    "in": [ '---', '- foo', '- bar', '...' ],
    "name": 'Regression: one_list2'
  },
  {
    "out": [ None, 'bar' ],
    "in": [ '---', '- ~', '- bar', '...' ],
    "name": 'Regression: one_listundef'
  },
  {
    "out": { 'foo': 'bar' },
    "in": [ '---', 'foo: bar', '...' ],
    "name": 'Regression: one_hash1'
  },
  {
    "out": {
      "foo": 'bar',
      "this": None
    },
    "in": [ '---', 'foo: bar', 'this: ~', '...' ],
    "name": 'Regression: one_hash2'
  },
  {
    "out": { 'foo': [ 'bar', None, 'baz' ] },
    "in": [ '---', 'foo:', '  - bar', '  - ~', '  - baz', '...' ],
    "name": 'Regression: array_in_hash'
  },
  {
    "out": {
      "bar": { 'foo': 'bar' },
      "foo": None
    },
    "in": [ '---', 'foo: ~', 'bar:', '  foo: bar', '...' ],
    "name": 'Regression: hash_in_hash'
  },
  {
    "out": [
      {
        "foo": None,
        "this": 'that'
      },
      'foo', None,
      {
        "foo": 'bar',
        "this": 'that'
      }
    ],
    "in": [
      '---',
      '-',
      '  foo: ~',
      '  this: that',
      '- foo',
      '- ~',
      '-',
      '  foo: bar',
      '  this: that',
      '...'
    ],
    "name": 'Regression: hash_in_array'
  },
  {
    "out": ['foo'],
    "in": [ '---', '- \'foo\'', '...' ],
    "name": 'Regression: single_quote1'
  },
  {
    "out": ['  '],
    "in": [ '---', '- \'  \'', '...' ],
    "name": 'Regression: single_spaces'
  },
  {
    "out": [''],
    "in": [ '---', '- \'\'', '...' ],
    "name": 'Regression: single_null'
  },
  {
    "out": '  ',
    "in": [ '--- "  "', '...' ],
    "name": 'Regression: only_spaces'
  },
  {
    "out": [
      None,
      {
        "foo": 'bar',
        "this": 'that'
      },
      'baz'
    ],
    "in":
     [ '---', '- ~', '- foo: bar', '  this: that', '- baz', '...' ],
    "name": 'Regression: inline_nested_hash'
  },
  {
    "name": "Unprintables",
    "in": [
      " - - -",
      " - \"\\z\\x01\\x02\\x03\\x04\\x05\\x06\\a\\x08\\t\\n\\v\\f\\r\\x0e\\x0f\"",
      "- \"\\x10\\x11\\x12\\x13\\x14\\x15\\x16\\x17\\x18\\x19\\x1a\\e\\x1c\\x1d\\x1e\\x1f\"",
      "- \" !\\\"#\$%&'()*+,-./\"",
      "- 0123456789:;<=>?",
      "- '\@ABCDEFGHIJKLMNO'",
      "- 'PQRSTUVWXYZ[\\]^_'",
      "- '`abcdefghijklmno'",
      "- 'pqrstuvwxyz{|}~\177'",
      "- \200\201\202\203\204\205\206\207\210\211\212\213\214\215\216\217",
      "- \220\221\222\223\224\225\226\227\230\231\232\233\234\235\236\237",
      "- \240\241\242\243\244\245\246\247\250\251\252\253\254\255\256\257",
      "- \260\261\262\263\264\265\266\267\270\271\272\273\274\275\276\277",
      "- \300\301\302\303\304\305\306\307\310\311\312\313\314\315\316\317",
      "- \320\321\322\323\324\325\326\327\330\331\332\333\334\335\336\337",
      "- \340\341\342\343\344\345\346\347\350\351\352\353\354\355\356\357",
      "- \360\361\362\363\364\365\366\367\370\371\372\373\374\375\376\377",
      "..."
    ],
    "out": [
      "\0\1\2\3\4\5\6\a\b\t\n\13\f\r\16\17",
      "\20\21\22\23\24\25\26\27\30\31\32\e\34\35\36\37",
      " !\"#\$%&'()*+,-./",
      "0123456789:;<=>?",
      "\@ABCDEFGHIJKLMNO",
      "PQRSTUVWXYZ[\\]^_",
      "`abcdefghijklmno",
      "pqrstuvwxyz{|}~\177",
      "\200\201\202\203\204\205\206\207\210\211\212\213\214\215\216\217",
      "\220\221\222\223\224\225\226\227\230\231\232\233\234\235\236\237",
      "\240\241\242\243\244\245\246\247\250\251\252\253\254\255\256\257",
      "\260\261\262\263\264\265\266\267\270\271\272\273\274\275\276\277",
      "\300\301\302\303\304\305\306\307\310\311\312\313\314\315\316\317",
      "\320\321\322\323\324\325\326\327\330\331\332\333\334\335\336\337",
      "\340\341\342\343\344\345\346\347\350\351\352\353\354\355\356\357",
      "\360\361\362\363\364\365\366\367\370\371\372\373\374\375\376\377"
    ],
  },
  {
    "name": 'Quoted hash keys',
    "in": [
      '---', '  "quoted": Magic!', '  "\n\t": newline, tab', '...',
    ],
    "out": {
      "quoted": 'Magic!',
      "\n\t": 'newline, tab',
    },
  },
]

# FIXME plan(tests=(len(SCHEDULE) * 5))

#sub iter {
#  my $ar = shift;
#  return sub {
#    return shift @$ar;
#  };
#}

class TestReader(unittest.TestCase):
    def test_reader(self):
        for test in SCHEDULE:
            name = test['name']
            yaml = yamlish.Reader()
            self.assert_(True, "%s: Created" % name)
            self.assert_(isinstance(yaml, yamlish.Reader))

            #     diag "$name\n";

            # unless ( $test->{in} ) {
            #     pass for 1 .. 2;
            #     use YAML;
            #     diag "Input for test:\n";
            #     diag( Dump( $test->{out} ) );
            #     next;
            # }

            source = "\n".join([line for line in test['in']]) + "\n"

            try:
                got = yaml.read(test['in']) # expecting test['in'] being an iterator
            except IOError as exc: # FIXME no idea what
                dollar_at = exc

            raw = yaml.get_raw()

            err = test['error'] # RE for testing results
            if err: # if we have err, use it
                if not err.search(dollar_at): # FIXME $@ (or dollar_at) is described
                    # in perlvar(1) the error status of the last eval(), which
                    # means that yaml.read(test['in'])
                    # if everything is alright, then it is None
                    self.assertFalse("%s: Error message" % name)
                    raise Exception(dollar_at)
                self.assert_(not got, "%s: No result" % name)
            else:
                want = test['out']
                self.assert_(not dollar_at, "%s: No error\n%s" % (name, dollar_at))

                self.assertEqual(got, want, """%s: Result matches
                expected = %s
                
                observed = %s
                """ % (name, want, got))
                self.assertEqual(raw, source, """%s: Captured source matches
                expected = %s
                
                observed = %s
                """ % (name, raw, source))
