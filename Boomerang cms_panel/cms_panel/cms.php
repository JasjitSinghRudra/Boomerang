<?php
session_start();
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

?>

<p class="style1">
Boomerang CMS Panel. View, Create, Update or Delete records by accessing the respective modules through navbar.
<br> <br>
Caution:

</p>

<ol class="style1">
	<li> Do not delete records without confirmation. </li>
	<li> Each administrator should access CMS using his/her login id. </li>
	<li> Updated records must be confirmed with users. </li>
</ol>

<hr>
<p class="style2"> Copyright &copy; Boomerang </p>
<hr>

</body>
</html>