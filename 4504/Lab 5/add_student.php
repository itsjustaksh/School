<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Student</title>
</head>

<body>
    <main>
        <form action="" method="post">
            <fieldset>
                <label for="Name">Name: </label>
                <input type="text" placeholder="Name" name="Name">
                <label for="DOB">Date of Birth</label>
                <input type="date" name="DOB">
                <label for="ID">Student ID: </label>
                <input type="number" name="ID">
                <label for="Income">Income: </label>
                <input type="number" name="Income">
                <label for="CourseID">Course ID</label>
                <input type="number" name="CourseID">
                <input type="submit" value="Submit">
            </fieldset>
        </form>
    </main>
</body>

</html>

<?php

    include("connection.php");

    $name = 0;
    $id = 0;
    $DOB = 0;
    $income = 0;
    $courseID = 0;

    if (isset($_POST["Name"])) {
        $conn = new mysqli($serverName, $username, $pass, $dbName);

        if ($conn->connect_error) {
            die("Error: Couldn't connect to database.<br>" . $conn->connect_error);
        }

        echo("Connected to Database!<br>");

        $name = $_POST["Name"];
        $id = $_POST["ID"];
        $DOB = $_POST["DOB"];
        $income = $_POST["Income"];
        $courseID = $_POST["CourseID"];

        $addLine = "INSERT INTO student (ID, NAME, DOB, INCOME, COURSE_ID) VALUES (
            '$id', '$name', '$DOB', '$income', '$courseID')";
    
        //TODO: Add content to db
        try {
            $conn -> query($addLine);
            echo("Successfully Registered!<br><hr>");
        } catch (Exception $th) {
            echo("Could not add entry, SQL error: $th");
        }

        try {
            $fetchLine = "SELECT * FROM student WHERE ID='$id'";
            $res = $conn -> query($fetchLine) -> fetch_assoc();

            if ($res) {
                echo("Submitted Info: <br>");
                foreach ($res as $key => $value) {
                    print("{$key}: {$value}<br>");
                }
            }
        } catch (Throwable $th) {
            echo("Could not display results. <br>SQL Error: $th");
        }
    }

    $conn->close();

?>