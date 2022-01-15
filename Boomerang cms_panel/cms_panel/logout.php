<?php
session_start();

if (session_destroy())
{
	header("Location:login.php?id=You've successfully logged out");
}

?>