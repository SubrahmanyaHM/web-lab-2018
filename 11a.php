<?php

$inTwoMonths = 60*60*24*60+time();
setcookie('lastVisit', date("G:i d/m/y"), $inTwoMonths);

if (isset($_COOKIE['lastVisit']))
{
    $visit = $_COOKIE['lastVisit'];
    print "You last visted time is $visit";
}
else
{
    print "You have some stale cookie";
}
?>
