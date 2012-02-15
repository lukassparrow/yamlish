<?php

    error_reporting(E_ALL);

    include_once('./t/lib/TestLite.php');

    plan(1);
    ok(@include_once('./lib/yamlishwriter.php'), 'include library');
?>
