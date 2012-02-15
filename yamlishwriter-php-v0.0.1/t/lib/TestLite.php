<?php

    $NEXT_TEST = 1;

    function plan($tests) {
        print "1..$tests\n";
    }

    function ok($ok, $message = null) {
        global $NEXT_TEST;
        $out = "ok " . ($NEXT_TEST++);
        if (!$ok) {
            $out = 'not ' . $out;
        }
        if ($message) {
            $out .= " $message";
        }
        print "$out\n";
    }

    function pass($message) {
        ok(true, $message);
    }
    
    function fail($message) {
        ok(false, $message);
    }
    
    function diag($message) {
        $stdout = fopen('php://stderr', 'w'); 
        fwrite( $stdout, "# $message\n" );
        fclose( $stdout );             
    }

    function is_deeply_array( $got, $expected, $message ) {
        if ( gettype($got) != 'array' ) {
            fail($message);
            diag('$got is not an array');
            return;
        }
        
        if ( gettype($expected) != 'array' ) {
            fail($message);
            diag('$expected is not an array');
            return;
        }

        $ok         = true;
        $diag       = array();
        $got_c      = count( $got );
        $expected_c = count( $expected );

        if ($got_c != $expected_c) {
            $ok = false;
            $diag[] = 'Array sizes differ:';
            $diag[] = '      $got: ' . $got_c;
            $diag[] = ' $expected: ' . $expected_c;
        }

        $count = max( $got_c, $expected_c );
  
        for ($i = 0; $i < $count; $i++) {
            if ( $got[$i] != $expected[$i] ) {
                if ($ok) {
                    $ok = false;
                    $diag[] = 'Arrays differ:';
                }
                $diag[] = "       \$got[$i]: $got[$i]";
                $diag[] = "  \$expected[$i]: $expected[$i]";
            }
        }
        
        ok($ok, $message);
        foreach ($diag as $d) {
            diag($d);
        }
    }

?>
