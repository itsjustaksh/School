<?php

    include("connection.php");
    $conn = new mysqli($serverName, $username, $pass, $dbName);

    if ($conn->connect_error) {
        die("Error: Couldn't connect to database.\n" . $conn->connect_error);
    }

    echo("Connected successfully");

    $name = 0;
    $id = 0;
    $DOB = 0;
    $income = 0;
    $courseID = 0;

    if (isset($_POST["Name"])) {
        $name = $_POST["Name"];
        $id = $_POST["ID"];
        $DOB = $_POST["DOB"];
        $income = $_POST["Income"];
        $courseID = $_POST["CourseID"];
    }

    $sqlLine = "INSERT INTO student (ID, NAME, DOB, INCOME, COURSE_ID) VALUES (" 
    . $id . ',' . $name . ',' . $DOB . ',' . $income . ',' . $courseID . ')';

    //TODO: Add content to db

    $conn->close();

?>