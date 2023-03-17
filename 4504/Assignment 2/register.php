<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Register on SYSCBOOK</title>
    <link rel="stylesheet" href="assets/css/reset.css" />
    <link rel="stylesheet" href="assets/css/style.css" />
    <?php include("connection.php") ?>
  </head>
  <body>
    <header>
      <h1>SYSCBOOK</h1>
      <p>Social media for SYSC students in Carleton University</p>
    </header>
    <nav>
      <ul class="navbar">
        <li>
          <a href="index.php"><strong>Home</strong></a>
        </li>
        <li>
          <a href="profile.php"><strong>Profile</strong></a>
        </li>
        <li>
          <a href="register.php"><strong>Register</strong></a>
        </li>
        <li>
          <a href="index.php"><strong>Logout</strong></a>
        </li>
      </ul>
    </nav>
    <main>
      <section>
        <h2>Register a new profile</h2>
        <form method="POST" action="">
          <fieldset>
            <table>
              <tbody>
                <tr>
                  <td colspan="3">
                    <legend><p>Personal information</p></legend>
                  </td>
                </tr>
                <tr>
                  <td class="profile-rows">
                    <label><p>First Name:</p></label>
                    <input type="text" name="first_name"/>
                  </td>
                  <td class="profile-rows">
                    <label><p>Last Name:</p></label>
                    <input type="text" name="last_name"/>
                  </td>
                  <td class="profile-rows">
                    <label><p>Date of Birth:</p></label>
                    <input type="date" name="DOB" id="profile_dob_input" />
                  </td>
                </tr>
              </tbody>
            </table>
          </fieldset>
          <fieldset>
            <!-- <legend><p>Profile information</p></legend> -->
            <table>
              <tbody>
                <tr>
                  <td colspan="5">
                    <legend><p>Profile information</p></legend>
                  </td>
                </tr>
                <tr>
                  <td class="profile-rows">
                    <label><p>Email address:</p></label>
                    <input type="email" name="student_email"/>
                  </td>
                </tr>
                <tr>
                  <td class="profile-rows">
                    <label><p>Program:</p></label>
                    <select name="Program">
                      <option>Choose Program</option>
                      <option>Computer Systems Engineering</option>
                      <option>Software Engineering</option>
                      <option>Communications Engineering</option>
                      <option>Biomedical and Electrical Engineering</option>
                      <option>Electrical Engineering</option>
                      <option>Special</option>
                    </select>
                  </td>
                </tr>
                <tr>
                  <td>
                    <input type="submit" value="Register" name="submit"/>
                    <input type="reset" value="Reset" name="reset"/>
                  </td>
                </tr>
              </tbody>
            </table>
          </fieldset>
        </form>
        <?php processRegister(); ?>
      </section>
    </main>
  </body>
</html>
