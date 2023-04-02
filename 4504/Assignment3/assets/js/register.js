document.addEventListener('DOMContentLoaded', function () {

    const homeA = document.getElementById('home-nav-link').parentElement;
    const logoutA = document.getElementById('logout-nav-link').parentElement;
    const loginA = document.getElementById('login-nav-link').parentElement;

    if (id == ''){
        homeA.style.display = 'none';
        logoutA.style.display = 'none';
        loginA.style.display = 'inherit';
    }
    else{
        loginA.style.display = 'none';
        homeA.style.display = 'inherit';
        logoutA.style.display = 'inherit';
    }

    const form = document.getElementById('register-form');

    form.addEventListener('submit', (event) => {
        let pass = validateRegister();

        if (!pass) {
            event.stopPropagation();
            event.preventDefault();
        }
    });



    function validateRegister() {
        const newPass = document.getElementById('password-n');
        const passConf = document.getElementById('password-c');
        const passError = document.getElementById('pass-error');
        let pass = false;

        // Check for existing same passwords
        if (newPass.value == passConf.value && checkLen(newPass)) {
            pass = true;
            passError.classList.add('no-show');
        }
        else{
            passError.classList.remove('no-show');
        }

        // Check if first name exists
        if (checkLen(document.querySelector('.profile-rows>input[name="first_name"]'))) {
            document.getElementById('fname-error').classList.add('no-show');
            pass = true && pass;
        }
        else {
            document.getElementById('fname-error').classList.remove('no-show');
        }

        // Check if last name exists
        if (checkLen(document.querySelector('.profile-rows>input[name="last_name"]'))) {
            document.getElementById('lname-error').classList.add('no-show');
            pass = true && pass;
        }
        else {
            document.getElementById('lname-error').classList.remove('no-show');
        }

        // Check if email exists
        if (checkLen(document.querySelector('.profile-rows>input[name="student_email"]'))) {
            document.getElementById('email-error').classList.remove('no-show');
            pass = true && pass;
        }
        else {
            document.getElementById('email-error').classList.add('no-show');
        }

        function checkLen(element) {
            if (element.value.length > 0) {
                return true;
            }
            return false;
        }

        return pass;
    }
});