<!DOCTYPE html>
<html lang="en">

<head>
  <?php
  session_start();

  if (!isset($_SESSION['start'])) {
    $_SESSION['start'] = time();
  }
  ?>
  <meta charset="utf-8" />
  <title>Register on SYSCBOOK</title>
  <link rel="stylesheet" href="assets/css/reset.css" />
  <link rel="stylesheet" href="assets/css/style.css" />
  <script>
    let id = "<?php $session_value=(isset($_SESSION['id']))?$_SESSION['id']:''; ?>";
  </script>
  <script src="assets/js/register.js"></script>
  <?php include("connection.php");
  processRegister(); ?>
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
      <li class="no-show">
        <a href="profile.php" id="profile-nav-link"><strong>Profile</strong></a>
      </li>
      <li>
        <a href="register.php" id="register-nav-link"><strong>Register</strong></a>
      </li>
      <li>
        <a href="logout.php" id="logout-nav-link"><strong>Logout</strong></a>
      </li>
      <li>
        <a href="login.php" id="login-nav-link"><strong>Login</strong></a>
      </li>
    </ul>
  </nav>
  <main>
    <section>
      <h2>Register a new profile</h2>
      <form method="POST" action="" id="register-form">
        <fieldset>
          <table>
            <tbody>
              <tr>
                <td colspan="3">
                  <legend>
                    <p>Personal information</p>
                  </legend>
                </td>
              </tr>
              <tr>
                <td class="profile-rows">
                  <label>
                    <p>First Name:</p>
                  </label>
                  <input type="text" name="first_name" />
                </td>
                <td class="profile-rows">
                  <label>
                    <p>Last Name:</p>
                  </label>
                  <input type="text" name="last_name" />
                </td>
                <td class="profile-rows">
                  <label>
                    <p>Date of Birth:</p>
                  </label>
                  <input type="date" name="DOB" id="profile_dob_input" />
                </td>
              </tr>
              <tr>
                <td colspan="3">
                  <p class="no-show error-message" id="fname-error">Registration Failed: Missing First Name</p>
                  <p class="no-show error-message" id="lname-error">Registration Failed: Missing Last Name</p>
                </td>
              </tr>
            </tbody>
          </table>
        </fieldset>
        <fieldset>
          <table>
            <tbody>
              <tr>
                <td colspan="5">
                  <legend>
                    <p>Profile information</p>
                  </legend>
                </td>
              </tr>
              <tr>
                <td class="profile-rows">
                  <label>
                    <p>Email address:</p>
                  </label>
                  <input type="email" name="student_email" />
                </td>
                <td class="profile-rows">
                  <label for="password-n">
                    <p>New Password</p>
                  </label>
                  <input type="password" name="password-n" id="password-n">
                  <label for="password-c">
                    <p>Confirm Password</p>
                  </label>
                  <input type="password" name="password-c" id="password-c">
                </td>
                <td class="profile-rows">
                  <p class="no-show error-message" id="pass-error">Registration Failed: Passwords must match</p>
                  <p class="no-show error-message" id="email-error">Registration Failed: Missing Email</p>
                  <?php
                  if (isset($_SESSION['bad_email'])) {
                    echo('<p class="error-message">Registration Failed: Email already in use</p>');
                  }
                  ?>
                </td>
              </tr>
              <tr>
                <td class="profile-rows">
                  <label>
                    <p>Program:</p>
                  </label>
                  <select name="Program">
                    <option>Choose Program</option>
                    <option value="sysc">Computer Systems Engineering</option>
                    <option value="soft">Software Engineering</option>
                    <option value="comm">Communications Engineering</option>
                    <option value="bioe">Biomedical and Electrical Engineering</option>
                    <option value="elec">Electrical Engineering</option>
                    <option value="spec">Special</option>
                  </select>
                </td>
              </tr>
              <tr>
                <td>
                  <input type="submit" value="Register" name="submit" id="submit_btn" />
                  <input type="reset" value="Reset" name="reset" />
                </td>
              </tr>
            </tbody>
          </table>
        </fieldset>
      </form>
    </section>
  </main>
</body>

</html>