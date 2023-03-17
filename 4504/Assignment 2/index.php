<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>SYSCBOOK - Main</title>
    <link rel="stylesheet" href="assets/css/reset.css" />
    <link rel="stylesheet" href="assets/css/style.css" />
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
        <form method="POST" action="https://ramisabouni.com/sysc4504/process_index.php">
          <fieldset>
            <table>
              <tr>
                <td>
                  <legend><p>New Post</p></legend>
                </td>
              </tr>
              <tr>
                <td>
                  <textarea
                    name="new_post"
                    id="new_post_input"
                    rows="10"
                    cols="45"
                    placeholder="What's on your mind? (Max 500 char)"
                  ></textarea>
                </td>
              </tr>
              <tr>
                <td class="buttons">
                  <input type="submit" value="Post" />
                  <input type="reset" value="Reset" />
                </td>
                <!-- <td>&nbsp;</td> -->
              </tr>
            </table>
          </fieldset>
        </form>

        <details open class="post">
          <summary>Post 1</summary>
          <br />
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla
            scelerisque faucibus accumsan. Proin in aliquet nulla. Integer
            faucibus nibh lobortis sapien eleifend vulputate. Mauris accumsan
            augue eu erat posuere ornare. Ut vestibulum aliquam lacinia.
            Pellentesque ac augue nisl. Cras laoreet faucibus efficitur. Aenean
            vitae sapien convallis, auctor magna vitae, suscipit ipsum. Nam
            maximus euismod feugiat. Suspendisse a metus metus. Donec rhoncus
            aliquam nisl, quis interdum quam dignissim euismod. Proin sed mattis
            ante, id vestibulum arcu. Aliquam ac tristique mauris. Integer et
            placerat nulla, cursus porttitor felis.
          </p>
        </details>

        <details open class="post">
          <summary>Post 2</summary>
          <br />
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla
            scelerisque faucibus accumsan. Proin in aliquet nulla. Integer
            faucibus nibh lobortis sapien eleifend vulputate. Mauris accumsan
            augue eu erat posuere ornare. Ut vestibulum aliquam lacinia.
            Pellentesque ac augue nisl. Cras laoreet faucibus efficitur. Aenean
            vitae sapien convallis, auctor magna vitae, suscipit ipsum. Nam
            maximus euismod feugiat. Suspendisse a metus metus. Donec rhoncus
            aliquam nisl, quis interdum quam dignissim euismod. Proin sed mattis
            ante, id vestibulum arcu. Aliquam ac tristique mauris. Integer et
            placerat nulla, cursus porttitor felis.
          </p>
        </details>

        <details open class="post">
          <summary>Post 3</summary>
          <br />
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla
            scelerisque faucibus accumsan. Proin in aliquet nulla. Integer
            faucibus nibh lobortis sapien eleifend vulputate. Mauris accumsan
            augue eu erat posuere ornare. Ut vestibulum aliquam lacinia.
            Pellentesque ac augue nisl. Cras laoreet faucibus efficitur. Aenean
            vitae sapien convallis, auctor magna vitae, suscipit ipsum. Nam
            maximus euismod feugiat. Suspendisse a metus metus. Donec rhoncus
            aliquam nisl, quis interdum quam dignissim euismod. Proin sed mattis
            ante, id vestibulum arcu. Aliquam ac tristique mauris. Integer et
            placerat nulla, cursus porttitor felis.
          </p>
        </details>
      </section>
    </main>
  </body>
</html>
