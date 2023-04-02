document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll(".no-show input");
    let valList = new Object;
    let id;
    let val;

    inputs.forEach(element => {
        id = element.getAttribute("id");
        val = element.getAttribute("value");

        valList[id] = val;
    });

    const fieldsToFill = document.querySelectorAll(".profile-rows>input");

    fieldsToFill.forEach(item => {
        if (valList[item.getAttribute('name')]) {
            item.setAttribute('value', valList[item.getAttribute('name')]);
        }
    });


    const selectTag = document.querySelector('.profile-rows>select');
    selectTag.value = valList[selectTag.getAttribute('name')];

    const usersA = document.getElementById('user-list-link');
    if (admin == 'True') {
        usersA.style.display = 'block';
    }

    const form = document.getElementById('register-form');

    form.addEventListener('submit', (event) => {
        let pass = validateProfile();

        if (!pass) {
            event.stopPropagation();
            event.preventDefault();
        }
    });

    function validateProfile() {
        let pass = false;

        // Check if first name exists
        if (checkLen(document.querySelector('.profile-rows>input[name="first_name"]'))) {
            document.getElementById('fname-error').classList.add('no-show');
            pass = true;
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