<?php

    include("connection.php");
    $conn = new mysqli($serverName, $username, $pass, $dbName);

    if ($conn->connect_error) {
        die("Error: Couldn't connect to database.\n" . $conn->connect_error);
    }

    echo("Connected successfully");

    $conn->close();

?>