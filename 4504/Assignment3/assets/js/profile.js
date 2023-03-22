console.log("START SCRIPT");

document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll(".no-show input");
    let valList = new Object;
    let id;
    let val;

    console.log(JSON.stringify(inputs));

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
});