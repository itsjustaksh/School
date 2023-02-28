document.addEventListener("DOMContentLoaded", function () {
    
    const slider1 = document.getElementById("image1Control");
    const slider2 = document.getElementById("image2Control");
    
    function changeOp1() {
        const image1 = document.getElementById("first-image");
        const box1 = document.getElementById("image1Opacity");

        box1.value = slider1.value;
        image1.style.opacity = box1.value;
    }

    function changeOp2() {
        const image2 = document.getElementById("second-image");
        const box2 = document.getElementById("image2Opacity");

        box2.value = slider2.value;
        image2.style.opacity = box2.value;
    }

    slider1.addEventListener('change',  changeOp1);
    slider2.addEventListener('change',  changeOp2);
})