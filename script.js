document.addEventListener("DOMContentLoaded", function () {

    const mobileMenu = document.getElementById("mobileMenu");
    const navMenu = document.querySelector(".nav-menu");

    if (mobileMenu) {

        mobileMenu.addEventListener("click", function () {

            navMenu.classList.toggle("show");

        });

    }


    /*
       Close mobile navigation after
       selecting a navigation link
    */

    const navLinks = document.querySelectorAll(".nav-menu a");

    navLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            navMenu.classList.remove("show");

        });

    });

});