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
    if (isset($_POST['first_name'])) {
        $infoQuery = "INSERT INTO users_info (student_email, f_name, l_name, bday) VALUES (?,?,?,?);";
        $progQuery = "INSERT INTO users_program (student_id, program) VALUES (?,?);";
        $avatarQuery = "INSERT INTO users_avatar (student_id, avatar) VALUES (?,?);";
        $addrQuery = "INSERT INTO users_address (student_id, street_num, street_name, city, province, postal_code) 
                    VALUES (?,?,?,?,?,?);";
        $conn = connect();

        $_SESSION['fName'] = $_POST['first_name'];
        $_SESSION['lName'] = $_POST['last_name'];
        $_SESSION['dob'] = $_POST['DOB'];
        $_SESSION['email'] = $_POST['student_email'];
        $_SESSION['prog'] = $_POST['Program'];

        try {
            $toDB = $conn->prepare($infoQuery);
            $toDB->bind_param("ssss", ...[$_SESSION['email'], $_SESSION['fName'], $_SESSION['lName'], $_SESSION['dob']]);
            $toDB->execute();

            $idQuery = "SELECT student_id FROM users_info WHERE student_email = '" . $_SESSION['email'] . "' AND 
                            f_name ='" . $_SESSION['fName'] . "' AND l_name ='" . $_SESSION['lName'] . "' AND bday ='" . $_SESSION['dob'] . "'";

            $_SESSION['id'] = $conn->query($idQuery)->fetch_assoc()['student_id'];

            $toDB = $conn->prepare($progQuery);
            $toDB->bind_param("is", $_SESSION['id'], $program);
            $toDB->execute();

            $toDB = $conn->prepare($avatarQuery);
            $toDB->bind_param("is", $_SESSION['id'], 'NULL');
            $toDB->execute();

            $toDB = $conn->prepare($addrQuery);
            $toDB->bind_param("iissss", $_SESSION['id'], 0, 'NULL', 'NULL', 'NULL', 'NULL');
            $toDB->execute();
        } catch (\Throwable $th) {
            echo ("<br>SQL ERROR: {$th}");
            die(1);
        }

        $toDB->close();
        $conn->close();


        header("Location: profile.php");
    }
}

function writeFromRegister()
{
    // Write data from prev. page to input elements
    try {
        $conn = connect();

        $fNameInput = "<input class='no-show' value='" . $_SESSION['fName'] . "' id='first_name'>";
        $lNameInput = "<input class='no-show' value='" . $_SESSION['lName'] . "' id='last_name'>";
        $dobInput = "<input class='no-show' value='" . $_SESSION['dob'] . "' id='DOB'>";
        $emailInput = "<input class='no-show' value='" . $_SESSION['email'] . "' id='student_email'>";
        $programInput = "<input class='no-show' value='" . $_SESSION['prog'] . "' id='Program'>";

        echo ("$fNameInput $lNameInput $dobInput $emailInput $programInput");
    } catch (\Throwable $th) {
        echo ("PROBLEM: $th");
    }
}

function processProfile()
{
    if (isset($_POST['street_number'])) {
        
        $addrQuery = "UPDATE users_address SET street_num=?, street_name=?, city=?, province=?, postal_code=? WHERE student_id=?;";
        $avatarQuery = "UPDATE users_avatar SET avatar=? WHERE student_id=?;";
        $infoQuery = "UPDATE users_info SET student_email=?, f_name=?, l_name=?, bday=? WHERE student_id=?;";
        $progQuery = "UPDATE users_program SET program=? WHERE student_id=?;";

        $conn = connect();

        $street_number = $_POST['street_number'];
        $street_name = $_POST['street_name'];
        $city = $_POST['city'];
        $province = $_POST['province'];
        $postal_code = $_POST['postal_code'];
        $avatar = $_POST['avatar'];

        try {
            $toDB = $conn->prepare($addrQuery);
            $toDB->bind_param("issss", ...[$street_number, $street_name, $city, $province, $postal_code, $_SESSION['id']]);
            $toDB->execute();

            $toDB = $conn->prepare($avatarQuery);
            $toDB->bind_param("ii", ...[$avatar, $_SESSION['id']]);
            $toDB->execute();

            $toDB = $conn->prepare($infoQuery);
            $toDB->bind_param("ssssi", ...[$_SESSION['email'], $_SESSION['fName'], $_SESSION['lName'], $_SESSION['email'], $_SESSION['id']]);
            $toDB->execute();

            $toDB = $conn->prepare($progQuery);
            $toDB->bind_param("si", $_SESSION['prog'], $_SESSION['id']);
            $toDB->execute();

            echo ("Done!");
        } catch (\Throwable $th) {
            echo ("<br>ERROR: {$th}");
            die(1);
        }

        $toDB->close();
        $conn->close();

        // header("Location: index.php");
    }
}

function showPosts()
{
    $conn = connect();
    $postQuery = "SELECT * FROM users_posts WHERE student_id=".$_SESSION['id']." ORDER BY post_id DESC LIMIT 5";
    $results = $conn->query($postQuery);
    while ($row = $results->fetch_assoc()) {
        $postID = $row['post_id'];
        $postContent = $row['new_post'];
        $postTimestamp = $row['post_date'];

        $userID = $row['student_id'];
        $userInfo = $conn->query("SELECT * FROM users_info WHERE student_id='$userID'")->fetch_assoc();
        $username = $userInfo['f_name'] . " " . $userInfo['l_name'];

        $postStructure = "<details open class='post'> <summary>Post $postID</summary>
                            <br>
                            <p>$postContent</p>
                            <p>Posted By: $username On: $postTimestamp</p></details>";
        print($postStructure);
    }
}

function processNewPost()
{
    if (isset($_POST['new_post'])) {
        $postQuery = "INSERT INTO users_posts (student_id, new_post, post_date) VALUES (?,?,?);";

        $postContent = $_POST['new_post'];

        $conn = connect();

        try {
            $toDB = $conn->prepare($postQuery);
            $toDB->bind_param("iss", ...[$_SESSION['id'], $postContent, date('dd/MM/YY')]);
            $toDB->execute();
        } catch (\Throwable $th) {
            echo ("<br>ERROR: {$th}");
            die(1);
        }

        $toDB->close();
        $conn->close();
    }
}
