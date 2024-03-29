<!DOCTYPE html>

<html lang="en">

<head>
	<title>Xbox Info Hub</title>
	<link rel="stylesheet" href="assets/css/style.css" />
	<link rel="icon" href="images/images/XBOX_logo.png" />
</head>

<body>
	<header id="home_link_dest">
		<h1 class="page-title">Xbox Info Hub</h1>
		<h2>By: Aksh Ravishankar</h2>
		<time datetime="2023-01-23 17:25">Monday Jan 23, 2023</time>
	</header>
	<div id="top_nav">
		<nav>
			<ul>
				<li><a href="index.html">Home</a></li>
				<li><a href="catalog.html">Catalog</a></li>
				<li>
					<a href="https://www.microsoft.com/en-ca">
						<img src="images/Microsoft_logo.png" alt="Microsoft Logo" class="nav-logo" />Company Website</a>
				</li>
				<li>
					<a href="contact.html">Contact Us</a>
				</li>
				<li><a class="active" href="escape_js.html">Escape Room</a></li>
				<li><a href="add_game.php">Add Game</a></li>
			</ul>
		</nav>
	</div>
	<div class="form">
		<form method="POST" action="">
			<fieldset>
				<legend>Add game information</legend>
				<label>Game Name: </label><input type="text" name="game_name"><br>
				<label>Release date: </label><input type="date" name="release_date"><br>
				<label>Price: </label><input type="text" name="game_price"><br>
				<label>Game Description: </label><br><textarea name="game_description" rows="4" cols="50" placeholder="max 500 characters"></textarea><br>
				<input type="submit" name="submit">
			</fieldset>
		</form>

		<?php

		include("connection.php");

		if (isset($_POST['game_name'])) {
			$conn = new mysqli($serverName, $username, $pass, $dbName);

			if ($conn->connect_error) {
				die("Error: Couldn't connect to database.<br>" . $conn->connect_error);
			}

		?>

		<p>Connected to Database!</p>

		<?php
		$name = $_POST["game_name"];
		$date = $_POST["release_date"];
		$price = $_POST["game_price"];
		$desc = $_POST["game_description"];

		$addLine = "INSERT INTO game_details (game_name, release_date, game_price, game_description) 
				VALUES ('$name', '$date', '$price', '$desc')";

		try {
			$conn->query($addLine);
		} catch (\Throwable $th) {
			echo ("Could not add entry, SQL error: $th");
		}
		?>

		<h2>Game Record Created Successfully!</h2>
		<div class="game-table-div">
			<table class="game-table">
				<thead>
					<tr>
						<td><strong>#</strong></td>
						<td><strong>Game ID</strong></td>
						<td><strong>Game Name</strong></td>
						<td><strong>Release Date</strong></td>
						<td><strong>Game Price</strong></td>
						<td><strong>Game Description</strong></td>
					</tr>
				</thead>
				<tbody>
				<?php
				$fetchLine = 'SELECT * FROM game_details ORDER BY release_date';

				$lines = $conn->query($fetchLine);
				$count = 0;
				foreach ($lines as $line) {
					$count++;
					$newRow = "<tr>
						<td><p>{$count}</p></td>
						<td><p>{$line["game_ID"]}</p></td>
						<td><p>{$line["game_name"]}</p></td>
						<td><p>{$line["release_date"]}</p></td>
						<td><p>{$line["game_price"]}</p></td>
						<td><p>{$line["game_description"]}</p></td>
						</tr>";

					print($newRow);
				}
			}
				?>
				</tbody>
			</table>
		</div>


	</div>
	<div class="footer">
		<hr id="bottom_line" />
		<footer>
			Copyright &copy; Aksh Ravishankar - Carleton University
			<a href="mailto:akshravishankar@cmail.carleton.ca">
				akshravishankar@cmail.carleton.ca
			</a>
		</footer>
	</div>
</body>

</html>