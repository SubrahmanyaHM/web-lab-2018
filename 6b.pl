#! /usr/bin/perl -wT

use CGI':standard';

print "Enter 1st number\n";
chomp($a = <STDIN>);
print "Enter 2nd number\n";
chomp($b = <STDIN>);
print "Enter 3rd number\n";
chomp($c = <STDIN>);

@num = ($a, $b, $c);
$big = $a;
foreach $x (@num){
    if($big<$x)
    {
        $big = $x;
     }
}

print "Biggest :$big";

