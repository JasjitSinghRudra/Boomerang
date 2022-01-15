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
		/*.style1 {color: white ; font-family: comic sans ms ; font-size: 16px ; text-align: justify; letter-spacing: 2px ; line-height: 25px}*/
		.style2 {color: white ; font-family: comic sans ms ; font-size: 14px ; text-align: center; letter-spacing: 2px ;}
		label {color: orange ; font-size: 16px ; font-family: comic sans ms}
		.buttons {color: white ; background-color: black ; font-family: impact ; font-size: 18px}
		table {color: white;font-family: comic sans ms;font-size: 16px;margin-left: auto;margin-right: auto;}
	</style>
</head>
<body>

<?php
echo "<hr>";
echo "<p>";

echo "Welcome " . $_SESSION['admin'];
echo "<a href='logout.php' style='float:right'> Sign Out </a>";
echo "</p>";

echo "<hr>";

echo "<a href='cms.php'> Home </a> &nbsp; &nbsp;"; 
echo "<a href='add.php'> Add Records </a> &nbsp; &nbsp;";
echo "<a href='update.php'> Update Records </a> &nbsp; &nbsp;";
echo "<a href='delete.php'> Delete Records </a> &nbsp; &nbsp;";
echo "<a href='view.php'> View Records </a>";
echo "<br><br><br>";
?>
<!-- Changes starts here -->

<?php
$qry="SELECT * from login";

$res=mysqli_query($conn,$qry);

echo "<table border='5' cellpadding='5' cellspacing='5'>";

echo "<tr>";
echo "<td> First Name </td>";
echo "<td> Last Name </td>";
echo "<td> Email </td>";
echo "<td> Location </td>";
echo "<td> PIN </td>";
echo "<td> Phone </td>";
echo "<td> Username </td>";
echo "</tr>";

while ($row=mysqli_fetch_array($res))
{
	echo "<tr>";
	echo "<td>";
	echo $row['First'];
	echo "</td>";
	echo "<td>";
	echo $row['Last'];
	echo "</td>";
	echo "<td>";
	echo $row['Email'];
	echo "</td>";
	echo "<td>";
	echo $row['Location'];
	echo "</td>";
	echo "<td>";
	echo $row['PIN'];
	echo "</td>";
	echo "<td>";
	echo $row['Phone'];
	echo "</td>";
	echo "<td>";
	echo $row['Username'];
	echo "</td>";
	echo "</tr>";
}

echo "</table>";

?>
<br>

<!-- Changes ends here -->
<hr>
<p class="style2"> Copyright &copy; Boomerang </p>
<hr>

</body>
</html>