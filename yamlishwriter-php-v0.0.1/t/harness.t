use strict;
use warnings;

my $php = $ENV{PHP} || 'php';

my $TESTS = 't/*.php';

my $planned = 0;

for my $test ( glob( $TESTS ) ) {
    warn "# $test\n";
    my $offset = $planned;
    my @command = ( $php, $test );
    open my $th, '-|', @command or die "Can't run $test ($?)\n";
    while ( defined( my $line = <$th> ) ) {
        chomp $line;
        if ( $line =~ /^1..(\d+)/ ) {
            $planned += $1;
        }
        else {
            $line =~ s/^((?:not\s+)?ok\s+)(\d+)/$1 . ($2 + $offset)/e;
            print "$line\n";
        }
    }
    close $th or die "Can't run $test ($?)\n";
}

# Trailing plan
print "1..$planned\n";
