<?php

include 'database.php';

$empfirst=$_POST['emp_first'];
$emplast=$_POST['emp_last'];
$empmail=$_POST['emp_mail'];
$emploc=$_POST['emp_loc'];
$emppin=$_POST['emp_pin'];
$empph=$_POST['emp_ph'];
$empuser=$_POST['emp_user'];
$emppass=$_POST['emp_pass'];

$qry="SELECT * from login where Username='$empuser'";

$res=mysqli_query($conn,$qry);

$count=mysqli_num_rows($res);

if ($count>0)
{
	header("Location:add.php?id=Record Already Exists");
}
else
{
	$qry1="INSERT into login (First,Last,Email,Location,PIN,Phone,Username,Password) values ('$empfirst','$emplast','$empmail','$emploc','$emppin','$empph','$empuser','$emppass')";

	$res1=mysqli_query($conn,$qry1);

	$count=mysqli_affected_rows($conn);

	if ($count>0)
	{
		header("Location:add.php?id=Record Added Successfully");
	}
}

?>