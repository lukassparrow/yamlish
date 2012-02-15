<?php

    error_reporting(E_ALL);

    include_once('./t/lib/TestLite.php');

    $schedule = array(
        array(
            'name' => 'Simple scalar',
            'in'   => 1,
            'out'  => array(
                '--- 1',
                '...',
            ),
        ),
        array(
            'name' => 'Undef',
            'in'   => null,
            'out'  => array(
                '--- ~',
                '...',
            ),
        ),
        array(
            'name' => 'Unprintable',
            'in'   => "\x01\n\t",
            'out'  => array(
                '--- "\x01\n\t"',
                '...',
            ),
        ),
        array(
            'name' => 'Simple array',
            'in'   => array( 1, 2, 3 ),
            'out'  => array(
                '---',
                '- 1',
                '- 2',
                '- 3',
                '...',
            ),
        ),
        array(
            'name' => 'Array, two elements, null',
            'in'   => array( null, null ),
            'out'  => array(
                '---',
                '- ~',
                '- ~',
                '...',
            ),
        ),
        array(
            'name' => 'Nested array',
            'in'   => array( 1, 2, array( 3, 4 ), 5 ),
            'out'  => array(
                '---',
                '- 1',
                '- 2',
                '-',
                '  - 3',
                '  - 4',
                '- 5',
                '...',
            ),
        ),
        array(
            'name' => 'Simple hash',
            'in'   => array( 'one' => '1', 'two' => '2', 'three' => '3' ),
            'out'  => array(
                '---',
                'one: 1',
                'two: 2',
                'three: 3',
                '...',
            ),
        ),
        array(
            'name' => 'Nested hash',
            'in'   => array(
                'one' => '1', 'two' => '2', 'more' => array( 'three' => '3', 'four' => '4' )
            ),
            'out' => array(
                '---',
                'one: 1',
                'two: 2',
                'more:',
                '  three: 3',
                '  four: 4',
                '...',
            ),
        ),
        array(
            'name' => 'Unprintable key',
            'in'   => array( 'one' => '1', "\x02" => '2', 'three' => '3' ),
            'out'  => array(
                '---',
                'one: 1',
                '"\x02": 2',
                'three: 3',
                '...',
            ),
        ),
        array(   
            'name' => 'Complex',
            'in'   => array(
                'bill-to' => array(
                    'given'   => 'Chris',
                    'address' => array(
                        'city'   => 'Royal Oak',
                        'postal' => '48046',
                        'lines'  => "458 Walkman Dr.\nSuite #292\n",
                        'state'  => 'MI'
                    ),
                    'family' => 'Dumars'
                ),
                'invoice' => '34843',
                'date'    => '2001-01-23',
                'tax'     => '251.42',
                'product' => array(
                    array(
                        'sku'         => 'BL394D',
                        'quantity'    => '4',
                        'price'       => '450.00',
                        'description' => 'Basketball'
                    ),
                    array(
                        'sku'         => 'BL4438H',
                        'quantity'    => '1',
                        'price'       => '2392.00',
                        'description' => 'Super Hoop'
                    )
                ),
                'comments' =>
                  "Late afternoon is best. Backup contact is Nancy Billsmer @ 338-4338\n",
                'total' => '4443.52'
            ),
            'out' => array(
                "---",
                "bill-to:",
                "  given: Chris",
                "  address:",
                "    city: 'Royal Oak'",
                "    postal: 48046",
                "    lines: \"458 Walkman Dr.\\nSuite #292\\n\"",
                "    state: MI",
                "  family: Dumars",
                "invoice: 34843",
                "date: 2001-01-23",
                "tax: 251.42",
                "product:",
                "  -",
                "    sku: BL394D",
                "    quantity: 4",
                "    price: 450.00",
                "    description: Basketball",
                "  -",
                "    sku: BL4438H",
                "    quantity: 1",
                "    price: 2392.00",
                "    description: 'Super Hoop'",
                "comments: \"Late afternoon is best. Backup contact is Nancy Billsmer @ 338-4338\\n\"",
                "total: 4443.52",
                "...",
            ),
        ),
    );

    plan( count($schedule) * 1 );
    
    include_once('./lib/yamlishwriter.php');
    
    foreach ($schedule as $test) {
        $name = $test['name'];
        $writer = new YAMLishWriter;
        $got = $writer->write($test['in']);
        is_deeply_array($got, $test['out'], "$name: output matches");
    }
    
?>
