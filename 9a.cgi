#! /usr/bin/perl -wT
use CGI':standard';


print header();

$webmaster = "subrahma";

($sec, $min, $hr) = localtime(time);
if($hr < 12)
{
    $greet = "Good morning";
}
elsif(($hr >= 12) && ($hr <=20))
{
    $greet = "good afternoon";
}
else
{
    $greet = "Good night";
}

open(check,'w -h -s $webmaster|');
if(<check>=~/"$webmaster"/)
{
    print "$webmaster currently logged in<br>";
}
else
{
    print "$webmaster logged off<br>";
}
print "$greet";    

