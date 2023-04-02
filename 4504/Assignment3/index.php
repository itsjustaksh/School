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
  <title>SYSCBOOK - Main</title>
  <link rel="stylesheet" href="assets/css/reset.css" />
  <link rel="stylesheet" href="assets/css/style.css" />
  <script>
    let id = "<?php $session_value=(isset($_SESSION['id']))?$_SESSION['id']:''; ?>";
  </script>
  <script src="assets/js/home.js"></script>
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
      <li>
        <a href="index.php" id="home-nav-link"><strong>Home</strong></a>
      </li>
      <li>
        <a href="profile.php" id="profile-nav-link"><strong>Profile</strong></a>
      </li>
      <li>
        <a href="logout.php" id="logout-nav-link"><strong>Logout</strong></a>
      </li>
    </ul>
  </nav>

  <main>
    <section>
      <?php isLoggedIn(); ?>
      <form method="POST" action="">
        <fieldset>
          <table>
            <tr>
              <td>
                <legend>
                  <p>New Post</p>
                </legend>
              </td>
            </tr>
            <tr>
              <td>
                <textarea name="new_post" id="new_post_input" rows="10" cols="45" placeholder="What's on your mind? (Max 500 char)"></textarea>
              </td>
            </tr>
            <tr>
              <td class="buttons">
                <input type="submit" value="Post" />
                <input type="reset" value="Reset" />
              </td>
            </tr>
          </table>
        </fieldset>
      </form>

      <?php
      if (isset($_SESSION['id'])) {
        processNewPost();
      }
      ?>

      <?php
      if (isset($_SESSION['id'])) {
        showPosts();
      }
      ?>

    </section>
  </main>
</body>

</html>