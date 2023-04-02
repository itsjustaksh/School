<!DOCTYPE html>
<html lang="en">

<head>
    <?php
    session_start();

    if (!isset($_SESSION['start'])) {
        $_SESSION['start'] = time();
    }
    ?>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/css/reset.css" />
    <link rel="stylesheet" href="assets/css/style.css" />
    <title>SyscBook Login</title>
    <?php
    include("connection.php");
    ?>
</head>

<body>
    <header>
        <h1>SYSCBOOK</h1>
        <p>Social media for SYSC students in Carleton University</p>
    </header>
    <nav>
        <ul class="navbar">
            <li class="no-show" id="home-nav-link">
                <a href="index.php"><strong>Home</strong></a>
            </li>
            <li class="no-show" id="profile-nav-link">
                <a href="profile.php"><strong>Profile</strong></a>
            </li>
            <li id="register-nav-link">
                <a href="register.php"><strong>Register</strong></a>
            </li>
            <li class="no-show" id="logout-nav-link">
                <a href="login.php"><strong>Logout</strong></a>
            </li>
            <li>
                <a href="login.php"><strong>Login</strong></a>
            </li>
        </ul>
    </nav>

    <main>
        <div id="login-container">
            <h1 id="login-heading" class="center">Login</h1>
            <div>
                <?php
                processLogin();
                ?>
            </div>
            <form action="" method="POST" id="login-form">
                <fieldset>
                    <div class="center" id="login-form-container">
                        <label for="login-email">
                            <p>Email: </p>
                        </label>
                        <input type="email" name="login-email" id="login-email" placeholder="email@domain.ca">
                        <label for="password-box">
                            <p>Password: </p>
                        </label>
                        <input type="password" name="password-box" id="password-box" placeholder="********">
                        <input id="submit-login" type="submit" value="Login" name="login">
                    </div>
                </fieldset>
            </form>
        </div>
    </main>
</body>

</html>