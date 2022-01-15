<!DOCTYPE html>
<html>
<head>
	<title>Login Form</title>
	<style type="text/css">
		body {background-color: black ; margin: 200px}
		label {color: yellow ; font-family: forte ; font-size:16px;}
		.buttons {color: red ; background-color: black ; font-family: forte ; font-size: 18px}
	</style>
</head>
<body>

<form action="verify.php" method="POST">
	
	<table border="5" cellspacing="15" cellpadding="15" style="margin-left: auto;margin-right: auto;">
		<tr>
			<td> <label>User Name</label> </td>
			<td> <input type="text" name="user" required> </td>
		</tr>
		<tr>
			<td> <label>Password</label> </td>
			<td> <input type="password" name="password" required> </td>
		</tr>
		<tr>
			<th colspan="2">
			<input type="submit" value="Sign In" class="buttons">
			<input type="reset" value="Clear" class="buttons">
			</th>
		</tr>
		<tr>
			<th colspan="2">
			<?php
			if (isset($_GET['Username']))
			{
				echo "<span style='color:red ; font-size:20px ; font-family:forte'>" . $_GET['Username'] . "</span>";
			}
			?>
			</th>
		</tr>

	</table>

</form>

</body>
</html>