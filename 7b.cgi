#! /usr/bin/perl -wT
use CGI':standard';


print header();
$num = param('num');
$prime = 1;
for($i = 2;$i<$num/2;$i++)
{
    if($num % $i == 0)
    {
        $prime = 0;
    }
}    
if ($prime == 1)
{
    print "$num is prime";
}
else
{
    print "$num is not a prime";
}
