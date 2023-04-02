<?php
    session_start();

    if (!isset($_SESSION['start'])) {
        $_SESSION['start'] = time();
    }

    include("connection.php");
    session_destroy();
    header("Location: login.php");
?>