document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll(".no-show input");
    let valList = new Object;

    inputs.forEach(element => {
        var id = element.getAttribute("id");
        var val = element.getAttribute("value");

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