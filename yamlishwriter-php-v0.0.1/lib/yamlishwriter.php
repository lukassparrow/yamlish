<?php

    // Would be nice if this weren't a global function - but I can't find
    // out how to make a class member work in preg_replace_callback
    function __escape_unprintable($matched) {
        $unprintable = array(
            'z',   'x01', 'x02', 'x03', 'x04', 'x05', 'x06', 'a',
            'x08', 't',   'n',   'v',   'f',   'r',   'x0e', 'x0f',
            'x10', 'x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17',
            'x18', 'x19', 'x1a', 'e',   'x1c', 'x1d', 'x1e', 'x1f',
        );
        
        return '\\' . $unprintable[ ord( $matched[0] ) ];
    }

    class YAMLishWriter {
        function YAMLishWriter() {
            
        }
        
        function write( $obj ) {
            $out = array();
            
            $this->_write_obj( $out, '---', $obj );
            $out[] = '...';

            return $out;
        }
        
        function _write_hash( &$out, $obj, $indent, $pad ) {
            while ( list($k, $v) = each( $obj ) ) {
                $this->_write_obj(
                    $out,
                    $pad . $this->_enc_scalar($k) . ':',
                    $v, $indent + 1
                );
            }
        }
        
        function _write_array( &$out, $obj, $indent ) {
            $pad = '';
            for ( $i = 0; $i < $indent; $i++ ) {
                $pad .= '  ';
            }

            $nout = array();
            $idx = 0;
            while ( list($k, $v) = each( $obj ) ) {
                if (gettype($k) != 'integer' || $k != $idx) {
                    # If we find it's not actually an array discard what we've done
                    # and write a hash instead. Usually we should find out pretty
                    # early.
                    $this->_write_hash( $out, $obj, $indent, $pad );
                    return;
                }

                $this->_write_obj( $nout, "$pad-", $v, $indent + 1);
                $idx++;
            }
            
            array_splice( $out, count($out), 0, $nout );
        }

        function _enc_string ( $str ) {
            if (preg_match('/[\x00-\x1f\"]/', $str)) {
                $str = preg_replace('/\\\\/', '\\\\', $str);
                $str = preg_replace('/"/', '\\"', $str);
                $str = preg_replace_callback( '/([\x00-\x1f])/', '__escape_unprintable', $str );
                return '"' . $str . '"';
            }
            
            if ( strlen($str) == 0 || preg_match( '/\s/', $str ) ) {
                return "'" . preg_replace('/\'/', "''", $str) . "'";
            }
            
            return $str;
        }

        function _enc_scalar( $obj ) {
            $type = gettype( $obj );
            switch ($type) {
                case 'boolean':
                    return $obj ? '1' : '0';
                    
                case 'double' :
                case 'integer':
                    return "$obj";

                case 'NULL':
                    return '~';

                case 'string':
                    return $this->_enc_string( $obj );
                
                default:
                    die('Unhandled scalar type ' . $type);
            }
        }
        
        function _write_obj( &$out, $prefix, $obj, $indent = 0 ) {
            $type = gettype( $obj );
            
            switch ($type) {
                case 'boolean':
                case 'integer':
                case 'double' :
                case 'string':
                case 'NULL':
                    $out[] = "$prefix " . $this->_enc_scalar( $obj );
                    break;
                    
                case 'array':
                    $out[] = $prefix;
                    $this->_write_array( $out, $obj, $indent );
                    break;
            
                case 'object':
                case 'resource':
                default:
                    die('Unhandled type ' . $type);
            }
        }
    }

?>
