'use strict';
$(document).ready(function () {
    var pages = 6,
        scrolling = false,
        hei = this.activeElement.offsetHeight,
        currentPage = 1;

    /*****************************
    ***** NAVIGATE FUNCTIONS *****
    *****************************/
    function manageClasses() {
        scrolling = true;
        setTimeout(function () {
            scrolling = false;
        }, 1000);
    }
    function navigateUp() {
        if (currentPage > 1) {
            currentPage--;
            manageClasses();
            var t = $("#group" + currentPage).offset().top
            $('.parallax').animate({
                scrollTop: hei * (currentPage - 1)
            }, 1000);
        }
    }

    function navigateDown() {
        if (currentPage < pages) {
            manageClasses();
            var t = $("#group" + currentPage).offset().top
            $('.parallax').animate({
                scrollTop: hei * currentPage
            }, 1000);
            currentPage++;
        }
    }

    /*********************
    ***** MOUSEWHEEL *****
    *********************/
    $(document).on("mousewheel DOMMouseScroll", function (e) {
        if (!scrolling) {
            if (e.originalEvent.wheelDelta > 0 || e.originalEvent.detail < 0) {
                navigateUp();
            } else {
                navigateDown();
            }
        }
    });
    
});