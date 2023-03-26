<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SyscBook Login</title>
</head>

<body>
    <header>
        <h1>SYSCBOOK</h1>
        <p>Social media for SYSC students in Carleton University</p>
    </header>
    <nav>
        <ul class="navbar">
            <li id="home-nav-link">
                <a href="index.php"><strong>Home</strong></a>
            </li>
            <li class="no-show" id="profile-nav-link">
                <a href="profile.php"><strong>Profile</strong></a>
            </li>
            <li id="register-nav-link">
                <a href="register.php"><strong>Register</strong></a>
            </li>
            <li class="no-show" id="logout-nav-link">
                <a href="index.php"><strong>Logout</strong></a>
            </li>
        </ul>
    </nav>

    <main>
        <div class="login-container">
            <form action="" method="post">
                <fieldset>
                    <label for="login-email">
                        <p>Username/email: </p>
                    </label>
                    <input type="email" name="login-email" id="login-email" placeholder="Username">
                    <label for="password-box">
                        <p>Password: </p>
                    </label>
                    <input type="password" name="password-box" id="password-box" placeholder="Password">
                    <input type="submit" value="Login" name="login">
                </fieldset>
            </form>
        </div>
    </main>
</body>

</html>