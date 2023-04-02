<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="assets/css/reset.css">
    <link rel="stylesheet" href="assets/css/style.css">
    <title>SyscBook Users</title>
    <?php include('connection.php'); ?>
</head>

<body>
    <header>
        <h1>SYSCBOOK</h1>
        <p>Social media for SYSC students in Carleton University</p>
    </header>
    <nav>
        <ul class="navbar">
            <li>
                <a href="index.php" id="home-nav-link"><strong>Home</strong></a>
            </li>
            <li>
                <a href="profile.php" id="profile-nav-link"><strong>Profile</strong></a>
            </li>
            <li>
                <a href="logout.php" id="logout-nav-link"><strong>Logout</strong></a>
            </li>
            <li style="display: none;">
                <a href="user_list.php" id="user-list-link"><strong>User List</strong></a>
            </li>
        </ul>
    </nav>

    <main>
        <section>
            <table>
                <tbody>
                    <tr>
                        <th>Student ID</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>Program</th>
                    </tr>
                    <?php displayUsers(); ?>
                </tbody>
            </table>
        </section>
    </main>
</body>

</html>