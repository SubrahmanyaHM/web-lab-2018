#! /usr/bin/perl -wT
use CGI':standard';
use DBI;

BEGIN{
    $|=1;
    print "Content-type:text/html\n\n";
    use CGI::Carp('fatalsToBrowser');
}

$dbh = DBI->connect('DBI:mysql:wp', 'root', 'password');
$name = param('name');
$age = param('age');

$qs = $dbh->prepare("insert into p10 values('$name','$age');");
$qs->execute();

$qs = $dbh->prepare("select * from p10;");
$qs->execute();

print "<table border=5><tr><th>NAME</th><th>AGE</th></tr>";


while(($name, $age) = $qs->fetchrow()) 
{
    print "<tr><td>$name</td><td>$age</td></tr>";
}
print "</table>";


$qs->finish();
$dbh->disconnect();
   

