<?php
session_start();
include 'database.php';
?>
<!DOCTYPE html>
<html>
<head>
	<title>CMS Panel</title>
	<style type="text/css">
		body {background-color: black ; margin: 75px}
		p, a {color: red ; font-weight: bold; font-size: 20px ; font-family: comic sans ms}
		a:link, a:visited {color: yellow ; text-decoration: none;background-color: purple ; padding: 5px}
		a:hover {color: blue}
		.style1 {color: white ; font-family: comic sans ms ; font-size: 16px ; text-align: justify; letter-spacing: 2px ; line-height: 25px}
		.style2 {color: white ; font-family: comic sans ms ; font-size: 14px ; text-align: center; letter-spacing: 2px ;}
		label {color: orange ; font-size: 16px ; font-family: comic sans ms}
		.buttons {color: white ; background-color: black ; font-family: impact ; font-size: 18px}
	</style>
</head>
<body>

<?php
echo "<hr>";
echo "<p>";
//echo "Welcome " . $_SESSION['admin'];
echo "<a href='logout.php' style='float:right'> Sign Out </a>";
echo "</p>";

echo "<hr>";

echo "<a href='cms.php'> Home </a> &nbsp; &nbsp;"; 
echo "<a href='add.php'> Add Records </a> &nbsp; &nbsp;";
echo "<a href='update.php'> Update Records </a> &nbsp; &nbsp;";
echo "<a href='delete.php'> Delete Records </a> &nbsp; &nbsp;";
echo "<a href='view.php'> View Records </a>";

?>
<!-- Changes starts here -->

<p class="style1">
	Change the contents of form-
</p>

<?php
$empid=$_GET['Username'];
$qry="SELECT * from login where Username='$empid'";
$res=mysqli_query($conn,$qry);
$row=mysqli_fetch_array($res);
?>

<form action="record_updated.php" method="POST">
	<table border="5" cellpadding="10" cellspacing="10" style="margin-left: auto;margin-right: auto;">
		<tr>
			<td> <label> First Name </label> </td>
			<td> <input type="text" name="emp_first" value="<?php echo $row['First'] ?>" required readonly> </td>
		</tr>
		<tr>
			<td> <label> Last Name </label> </td>
			<td> <input type="text" name="emp_last" value="<?php echo $row['Last'] ?>" required> </td>
		</tr>
		<tr>
			<td> <label> Email </label> </td>
			<td> <input type="email" name="emp_mail" value="<?php echo $row['Email'] ?>" required> </td>
		</tr>
		<tr>
			<td> <label> Location </label> </td>
			<td> <input type="text" name="emp_loc" value="<?php echo $row['Location'] ?>" required> </td>
		</tr>
		<tr>
			<td> <label> PIN </label> </td>
			<td> <input type="number" name="emp_pin" value="<?php echo $row['PIN'] ?>" required> </td>
		</tr>
		<tr>
			<td> <label> Phone </label> </td>
			<td> <input type="number" name="emp_ph" value="<?php echo $row['Phone'] ?>" required> </td>
		</tr>
		<tr>
			<td> <label> Username </label> </td>
			<td> <input type="text" name="emp_user" value="<?php echo $row['Username'] ?>" required> </td>
		</tr>
		<tr>
			<td> <label> Password </label> </td>
			<td> <input type="password" name="emp_pass" value="<?php echo $row['Password'] ?>" required> </td>
		</tr>
		<tr>
			<th colspan="2"> 
				<input type="submit" value="Update Records" class="buttons">
				<input type="reset" value="Clear" class="buttons">
			</th> 
		</tr>

	</table>
</form>

<br>

<!-- Changes ends here -->

<hr>
<p class="style2"> Copyright &copy; Boomerang </p>
<hr>

</body>
</html>