#! /usr/bin/perl -wT
use CGI':standard';


print header();
$name = param('name');
@greet = ("HI", "Hello", "Bitch!", "gracias");

$ran = rand(4);

print "$greet[$ran] , $name";
