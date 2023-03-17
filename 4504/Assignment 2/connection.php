<?php
    function connect()
    {
        $serverName = 'localhost';
        $dbName = 'aksh_ravi_syscbook';
        $username = 'root';
        $pass = '';

        $conn = new mysqli($serverName, $username, $pass, $dbName);

        if ($conn->connect_error) {
            die("Error: Couldn't connect to database.\n" . $conn->connect_error);
        }

        return $conn;
    }

    function processRegister()
    {
        if (isset($_POST['submit'])) {
            $infoQuery = "INSERT INTO users_info (student_email, f_name, l_name, bday) VALUES (?,?,?,?);";
            $progQuery = "INSERT INTO users_program (program) VALUES (?);";
            
            $conn = connect();

            $fName = $_POST['first_name'];
            $lName = $_POST['last_name'];
            $dob = $_POST['DOB'];
            $email = $_POST['student_email'];
            $program = $_POST['Program'];

            $toDB = $conn->prepare($infoQuery);
            $toDB->bind_param("ssss", ...[$email, $fName, $lName, $dob]);

            $toDB->execute();

            $toDB = $conn->prepare($progQuery);
            $toDB->bind_param("s", $program);

            $toDB->execute();

            $toDB->close();
            $conn->close();
        }
    }

    // function processProfile()
    // {
        
    // }
?>