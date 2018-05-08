<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

session_start();

if (isset($_SESSION['views']))
{
    $_SESSION['views'] = $_SESSION['views'] + 1;
}
else
{
    $_SESSION['views'] = 1;
}
$count = $_SESSION['views'];
print "This page has been visited $count times";
?>
