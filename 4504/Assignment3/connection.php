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

function isLoggedIn()
{
    if (!isset($_SESSION['id'])) {
        header("Location: login.php");
    }
}

function processRegister()
{
    if (isset($_POST['first_name'])) {
        $infoQuery = "INSERT INTO users_info (student_email, f_name, l_name, bday) VALUES (?,?,?,?);";
        $progQuery = "INSERT INTO users_program (student_id, program) VALUES (?,?);";
        $avatarQuery = "INSERT INTO users_avatar (student_id, avatar) VALUES (?,?);";
        $addrQuery = "INSERT INTO users_address (student_id, street_num, street_name, city, province, postal_code) 
                    VALUES (?,?,?,?,?,?);";
        $passQuery = "INSERT INTO users_passwords (student_id, pass) VALUES (?,?)";
        $conn = connect();

        $empty = NULL;
        $zero = 0;

        $_SESSION['lName'] = $_POST['last_name'];
        $_SESSION['fName'] = $_POST['first_name'];
        $_SESSION['dob'] = $_POST['DOB'];
        $_SESSION['email'] = $_POST['student_email'];
        $_SESSION['prog'] = $_POST['Program'];
        $pass = password_hash($_POST['password-n'], PASSWORD_BCRYPT);


        try {
            $checkEmail = "SELECT student_email FROM users_info WHERE student_email=?";
            $toDB = $conn->prepare($checkEmail);
            $toDB->execute([$_SESSION['email']]);
            if ($toDB->get_result()->fetch_assoc()) {
                // Email in use, try again
                $_SESSION['bad_email'] = true;

                return;
            }
            else{
                unset($_SESSION['bad_email']);
            }
            
            $toDB = $conn->prepare($infoQuery);
            $toDB->bind_param("ssss", ...[$_SESSION['email'], $_SESSION['fName'], $_SESSION['lName'], $_SESSION['dob']]);
            $toDB->execute();

            $_SESSION['id'] = $toDB->insert_id;

            $toDB = $conn->prepare($progQuery);
            $toDB->bind_param("is", $_SESSION['id'], $program);
            $toDB->execute();

            $toDB = $conn->prepare($avatarQuery);
            $toDB->bind_param("ii", $_SESSION['id'], $zero);
            $toDB->execute();

            $toDB = $conn->prepare($addrQuery);
            $toDB->bind_param("iissss", $_SESSION['id'], $zero, $empty, $empty, $empty, $empty);
            $toDB->execute();

            $toDB = $conn->prepare($passQuery);
            $toDB->bind_param("is", $_SESSION['id'], $pass);
            $toDB->execute();

            $toDB->close();
            $conn->close();

            header("Location: profile.php");
        } catch (\Throwable $th) {
            echo ("<br>SQL ERROR: {$th}");
            try {
                $toDB->close();
                $conn->close();
            } catch (\Throwable $th) {
                die(1);
            }
            die(1);
        }

        
    }
}

function writeFromRegister()
{
    // Write data from prev. page to input elements
    try {

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
        $_SESSION['lName'] = $_POST['last_name'];
        $_SESSION['fName'] = $_POST['first_name'];
        $_SESSION['dob'] = $_POST['DOB'];
        $_SESSION['email'] = $_POST['student_email'];
        $_SESSION['prog'] = $_POST['Program'];

        try {
            $checkEmail = "SELECT student_id, student_email FROM users_info WHERE student_email=?";
            $toDB = $conn->prepare($checkEmail);
            $toDB->execute([$_SESSION['email']]);
            $result = $toDB->get_result()->fetch_assoc();
            if ($result) {
                // Email in use, try again
                if ($_SESSION['id'] != $result['student_id']) {
                    $_SESSION['bad_email'] = true;
                    return;
                }
            }
            else{
                unset($_SESSION['bad_email']);
            }

            $toDB = $conn->prepare($addrQuery);
            $toDB->bind_param("issssi", ...[$street_number, $street_name, $city, $province, $postal_code, $_SESSION['id']]);
            $toDB->execute();

            $toDB = $conn->prepare($avatarQuery);
            $toDB->bind_param("ii", ...[$avatar, $_SESSION['id']]);
            $toDB->execute();

            $toDB = $conn->prepare($infoQuery);
            $toDB->bind_param("ssssi", ...[$_SESSION['email'], $_SESSION['fName'], $_SESSION['lName'], $_SESSION['dob'], $_SESSION['id']]);
            $toDB->execute();

            $toDB = $conn->prepare($progQuery);
            $toDB->bind_param("si", $_SESSION['prog'], $_SESSION['id']);
            $toDB->execute();
        } catch (\Throwable $th) {
            echo ("<br>ERROR: {$th}");
            die(1);
        }

        $toDB->close();
        $conn->close();

        header("Location: index.php");
    }
}

function showPosts()
{
    if (isset($_SESSION['id'])) {
        $conn = connect();
        $postQuery = "SELECT * FROM users_posts ORDER BY post_id DESC LIMIT 10";
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
    else{
        header("Location: login.php");
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
            $date = date('Y-m-d h:i:s');

            $toDB->bind_param("iss", ...[$_SESSION['id'], $postContent, $date]);
            $toDB->execute();
        } catch (\Throwable $th) {
            echo ("<br>ERROR: {$th}");
            die(1);
        }

        $toDB->close();
        $conn->close();
    }
}

function processLogin(){
    // If already logged in, log out and come back here
    if (isset($_SESSION['id'])) {
        header('Location: logout.php');
    }

    // If attempting to log in, gather info
    if (isset($_POST['login-email'])){
        
        $loginQ = "SELECT pass FROM users_passwords WHERE student_id=?";
        $idQ = "SELECT student_id from users_info WHERE student_email=?";
        
        try {
            $conn = connect();
            $id = $conn->prepare($idQ);
            $id->bind_param('s', ...[$_POST['login-email']]);
            $id->execute();

            $idRes = $id->get_result()->fetch_assoc();
            if (!isset($idRes)) {
                // Write to JS to display error, don't submit form
                echo("<p class='error-message center'>No account registered with that email</p>");

                return;
            }

            $pass = $conn->prepare($loginQ);
            $pass->execute([$idRes['student_id']]);
            $passHash = $pass->get_result()->fetch_assoc()['pass'];

            if (password_verify($_POST['password-box'], $passHash)) {
                $_SESSION['id'] = $idRes['student_id'];
            }
            else {
                echo("<p class='error-message'>Email/password does not match</p>");
                unset($_SESSION['id']);

                return;
            }

            header('Location: index.php');
        } catch (\Throwable $th) {
            echo($th);
            try {
                $id->close();
                $conn->close();
            } catch (\Throwable $th) {
                die(1);
            }
            die(1);
        }

    }
}