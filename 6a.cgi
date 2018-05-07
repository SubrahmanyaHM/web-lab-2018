#! /usr/bin/perl -wT
use CGI':standard';

print "Content-type:text/html\n\n",
      "<html><head><title>SERVER INFO</title></head>",
      "<body><h1>SERVER INFORMATION</h1><br>",
      "SERVER NAME : $ENV{'SERVER_NAME'}<br>",
      "SERVER SOFTWARE : $ENV{'SERVER_SOFTWARE'}<br>",
      "SERVER PROTOCOL : $ENV{'SERVER_PROTOCOL'}<br>",
      "CGI VERSION : $ENV{'GATEWAY_INTERFACE'}<br>",
      "</body></html>";
