<?php

include 'database.php';

$id=$_POST['Username'];
$qry="DELETE FROM 'login' WHERE 'Username'='$id'";
mysqli_query($conn,$qry);

//header("Location:delete.php?id=Record Deleted Successfully");

?>