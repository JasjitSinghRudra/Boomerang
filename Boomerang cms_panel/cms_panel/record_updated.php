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

$qry="UPDATE employees set First='$empfirst',Last='$emplast',Email='$empmail',Location='$emploc',PIN='$emppin',Location='$emploc',Phone='$empph',Username='$empuser',Password='$emppass' where Username=='$empuser'";

$res=mysqli_query($conn,$qry);

header("Location:update.php?id=Record Updated Successfully");

?>