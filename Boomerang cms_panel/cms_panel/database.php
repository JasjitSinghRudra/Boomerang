<?php

define ("SERVER","localhost","");
define ("USER","root","");
define ("PASSWORD","","");
define ("DATANAME","boomerang","");

$conn=mysqli_connect(SERVER,USER,PASSWORD,DATANAME);

if (!$conn)
{
	die ("Unable to connect the server ") . mysqli_error($conn);
}

?>