#! /usr/bin/perl -wT

use CGI':standard';

print "Enter 1st number\n";
chomp($a = <STDIN>);
print "Enter 2nd number\n";
chomp($b = <STDIN>);
print "Enter 3rd number\n";
chomp($c = <STDIN>);

findbig($a,$b,$c);


sub findbig{
@arr= @_;
$big=$arr[0];
foreach $x (@_){
    if($big<$x)
    {
        $big = $x;
     }
}

print "Biggest :$big";

}


