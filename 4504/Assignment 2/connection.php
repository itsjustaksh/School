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
            $progQuery = "INSERT INTO users_program (student_id, program) VALUES (?,?);";
            
            $conn = connect();

            $fName = $_POST['first_name'];
            $lName = $_POST['last_name'];
            $dob = $_POST['DOB'];
            $email = $_POST['student_email'];
            $program = $_POST['Program'];

            try {
                $toDB = $conn->prepare($infoQuery);
                $toDB->bind_param("ssss", ...[$email, $fName, $lName, $dob]);

                $toDB->execute();

                $idQuery = "SELECT student_id FROM users_info WHERE student_email = '$email' AND 
                            f_name = '$fName' AND l_name = '$lName' AND bday = '$dob'";

                $newID = $conn->query($idQuery)->fetch_assoc();

                $toDB = $conn->prepare($progQuery);
                $toDB->bind_param("is", $newID['student_id'], $program);

                $toDB->execute();

                echo "Success!";
            } catch (\Throwable $th) {
                echo("<br>SQL ERROR: {$th}");
            }

            $toDB->close();
            $conn->close();
        }
    }

    function processProfile()
    {
        if (isset($_POST['street_number'])) {
            $avatrQuery = "INSERT INTO users_avatar (student_id, avatar) VALUES (?,?);";
            $addrQuery = "INSERT INTO users_address (student_id, street_number, street_name, city, province, postal_code) 
                    VALUES (?,?,?,?,?,?);";
            $infoQuery = "UPDATE users_info SET student_email=?, f_name=?, l_name=?, bday=? WHERE student_id=?;";
            $progQuery = "UPDATE users_program SET student_id=?, program=?  WHERE student_id=?;";

            $conn = connect();

            $fName = $_POST['first_name'];
            $lName = $_POST['last_name'];
            $dob = $_POST['DOB'];
            $email = $_POST['student_email'];
            $program = $_POST['Program'];
            $street_number = $_POST['street_number'];
            $street_name = $_POST['street_name'];
            $city = $_POST['city'];
            $province = $_POST['province'];
            $postal_code = $_POST['postal_code'];
            $avatar = $_POST['avatar'];

            try {
                $idQuery = "SELECT student_id FROM users_info 
                WHERE f_name = '$fName' AND l_name = '$lName' AND bday = '$dob'";

                $id = $conn->query($idQuery)->fetch_assoc();

                $toDB = $conn->prepare($addrQuery);
                $toDB->bind_param("iissss", ...[$id['student_id'], $street_number, $street_name, $city, $province, $postal_code]);
                $toDB->execute();

                $toDB = $conn->prepare($avatrQuery);
                $toDB->bind_param("ii", ...[$id['student_id'], $avatar]);
                $toDB->execute();

                $toDB = $conn->prepare($infoQuery);
                $toDB->bind_param("ssssi", ...[$email, $fName, $lName, $dob, $id['student_id']]);
                $toDB->execute();

                $toDB = $conn->prepare($progQuery);
                $toDB->bind_param("is", $id['student_id'], $program);
                $toDB->execute();

            } catch (\Throwable $th) {
                echo "ERROR: $th";
            }
            
            $conn = connect();
        }
    }
?>