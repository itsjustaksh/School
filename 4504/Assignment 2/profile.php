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
  <title>Update SYSCBOOK profile</title>
  <link rel="stylesheet" href="assets/css/reset.css" />
  <link rel="stylesheet" href="assets/css/style.css" />
  <script type="text/javascript" src="assets/js/profile.js"></script>
  <?php include("connection.php"); processProfile(); ?>
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
      <div id="dom-target-container" class="no-show">
        <?php
        writeFromRegister();
        ?>
      </div>
      <h2>Update Profile information</h2>
      <form method="POST" action="index.php">
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
                  <input name="first_name" type="text" />
                </td>
                <td class="profile-rows">
                  <label>
                    <p>Last Name:</p>
                  </label>
                  <input name="last_name" type="text" />
                </td>
                <td class="profile-rows">
                  <label>
                    <p>Date of Birth:</p>
                  </label>
                  <input name="DOB" type="date" name="DOB" id="profile_dob_input" />
                </td>
              </tr>
            </tbody>
          </table>
        </fieldset>
        <fieldset>
          <table>
            <tbody>
              <tr>
                <td colspan="3">
                  <legend>
                    <p>Address</p>
                  </legend>
                </td>
              </tr>
              <tr>
                <td class="profile-rows">
                  <label>
                    <p>Street Number:</p>
                  </label>
                  <input name="street_number" type="number" />
                </td>
                <td class="profile-rows" colspan="2">
                  <label>
                    <p>Street Name:</p>
                  </label>
                  <input name="street_name" type="text" />
                </td>
              </tr>
              <tr>
                <td class="profile-rows">
                  <label>
                    <p>City:</p>
                  </label>
                  <input name="city" type="text" />
                </td>
                <td class="profile-rows">
                  <label>
                    <p>Province:</p>
                  </label>
                  <input name="province" type="text" />
                </td>
                <td class="profile-rows">
                  <label>
                    <p>Postal Code:</p>
                  </label>
                  <input name="postal_code" type="text" />
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
                  <input name="student_email" type="email" />
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
                  <p>Choose Avatar:</p>
                </td>
              </tr>
              <tr>
                <td>
                  <p>
                    <input name="avatar" type="radio" value="avatar-1" />
                    <label>
                      <img src="images/img_avatar1.png" alt="avatar-icon" />
                    </label>
                    <input name="avatar" type="radio" value="avatar-2" />
                    <label>
                      <img src="images/img_avatar2.png" alt="avatar-icon" />
                    </label>
                    <input name="avatar" type="radio" value="avatar-3" />
                    <label>
                      <img src="images/img_avatar3.png" alt="avatar-icon" />
                    </label>
                    <input name="avatar" type="radio" value="avatar-4" />
                    <label>
                      <img src="images/img_avatar4.png" alt="avatar-icon" />
                    </label>
                    <input name="avatar" type="radio" value="avatar-5" />
                    <label>
                      <img src="images/img_avatar5.png" alt="avatar-icon" />
                    </label>
                  </p>
                </td>
              </tr>
              <tr>
                <td>
                  <input name="submit" type="submit" value="Submit" />
                  <input name="reset" type="reset" value="Reset" />
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