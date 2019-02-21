'use strict';


/**
 * Object.assign() polyfill
 */
Object.assign || Object.defineProperty(Object, "assign", { enumerable: !1, configurable: !0, writable: !0, value: function (a, b) { "use strict"; if (void 0 === a || null === a) error("Cannot convert first argument to object"); for (var c = Object(a), d = 1; d < arguments.length; d++) { var e = arguments[d]; if (void 0 !== e && null !== e) for (var f = Object.keys(Object(e)), g = 0, h = f.length; g < h; g++) { var i = f[g], j = Object.getOwnPropertyDescriptor(e, i); void 0 !== j && j.enumerable && (c[i] = e[i]) } } return c } });

/**
 * CustomEvent() polyfill
 */
!function () { if ("function" == typeof window.CustomEvent) return; function t(t, e) { e = e || { bubbles: !1, cancelable: !1, detail: void 0 }; var n = document.createEvent("CustomEvent"); return n.initCustomEvent(t, e.bubbles, e.cancelable, e.detail), n } t.prototype = window.Event.prototype, window.CustomEvent = t }();


/**
 * ������� ����������� ������� swipe �� ��������.
 * @param {Object} el - ������� DOM.
 * @param {Object} settings - ������ � ���������������� �����������.
 */
var swipe = function (e, settings) {

    // ��������� �� ���������
    var settings = Object.assign({}, {
        minDist: 60,  // ����������� ���������, ������� ������ ������ ���������, ����� ���� �������� ��� ����� (px)
        maxDist: 120, // ������������ ���������, �� �������� ������� ����� ������ ���������, ����� ���� �������� ��� ����� (px)
        maxTime: 700, // ������������ �����, �� ������� ������ ���� �������� ����� (ms)
        minTime: 50   // ����������� �����, �� ������� ������ ���� �������� ����� (ms)
    }, settings);

    // ��������� ������� ��� ��������� ���������
    if (settings.maxTime < settings.minTime) settings.maxTime = settings.minTime + 500;
    if (settings.maxTime < 100 || settings.minTime < 50) {
        settings.maxTime = 700;
        settings.minTime = 50;
    }

    var el = e,       // ������������� �������
        dir,                  // ����������� ������ (horizontal, vertical)
        swipeType,            // ��� ������ (up, down, left, right)
        dist,                 // ���������, ���������� ����������
        isMouse = false,      // ��������� ���� (�� ������������ ��� ���-�������)
        isMouseDown = false,  // �������� �� �������� ������� ���� (�� ������������ ��� ���-�������)
        startX = 0,           // ������ ��������� �� ��� X (pageX)
        distX = 0,            // ���������, ���������� ���������� �� ��� X
        startY = 0,           // ������ ��������� �� ��� Y (pageY)
        distY = 0,            // ���������, ���������� ���������� �� ��� Y
        startTime = 0,        // ����� ������ �������
        support = {           // �������������� ��������� ���� �������
            pointer: !!("PointerEvent" in window || ("msPointerEnabled" in window.navigator)),
            touch: !!(typeof window.orientation !== "undefined" || /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) || "ontouchstart" in window || navigator.msMaxTouchPoints || "maxTouchPoints" in window.navigator > 1 || "msMaxTouchPoints" in window.navigator > 1)
        };

    /**
     * ���������� ��������� � �������� �������: pointer, touch � mouse.
     * @returns {Object} - ���������� ������ � ���������� ���������.
     */
    var getSupportedEvents = function () {
        switch (true) {
            case support.pointer:
                events = {
                    type: "pointer",
                    start: "PointerDown",
                    move: "PointerMove",
                    end: "PointerUp",
                    cancel: "PointerCancel",
                    leave: "PointerLeave"
                };
                // ���������� ��������� ��� IE10
                var ie10 = (window.navigator.msPointerEnabled && Function('/*@cc_on return document.documentMode===10@*/')());
                for (var value in events) {
                    if (value === "type") continue;
                    events[value] = (ie10) ? "MS" + events[value] : events[value].toLowerCase();
                }
                break;
            case support.touch:
                events = {
                    type: "touch",
                    start: "touchstart",
                    move: "touchmove",
                    end: "touchend",
                    cancel: "touchcancel"
                };
                break;
            default:
                events = {
                    type: "mouse",
                    start: "mousedown",
                    move: "mousemove",
                    end: "mouseup",
                    leave: "mouseleave"
                };
                break;
        }
        return events;
    };


    /**
     * ����������� ������� mouse/pointer � touch.
     * @param e {Event} - ��������� � �������� ��������� �������.
     * @returns {TouchList|Event} - ���������� ���� TouchList, ���� ��������� ������� ��� ���������.
     */
    var eventsUnify = function (e) {
        return e.changedTouches ? e.changedTouches[0] : e;
    };


    /**
     * ��������� ������ ������� ����������.
     * @param e {Event} - �������� �������.
     */
    var checkStart = function (e) {
        var event = eventsUnify(e);
        if (support.touch && typeof e.touches !== "undefined" && e.touches.length !== 1) return; // ������������� ������� ����������� ��������
        dir = "none";
        swipeType = "none";
        dist = 0;
        startX = event.pageX;
        startY = event.pageY;
        startTime = new Date().getTime();
        if (isMouse) isMouseDown = true; // ��������� ����
        e.preventDefault();
    };

    /**
     * ���������� �������� ���������.
     * @param e {Event} - �������� �������.
     */
    var checkMove = function (e) {
        if (isMouse && !isMouseDown) return; // ����� �� �������, ���� ���� ��������� ���� ������� �� ����� ��������
        var event = eventsUnify(e);
        distX = event.pageX - startX;
        distY = event.pageY - startY;
        if (Math.abs(distX) > Math.abs(distY)) dir = (distX < 0) ? "left" : "right";
        else dir = (distY < 0) ? "up" : "down";
        e.preventDefault();
    };

    /**
     * ���������� ��������� ������� ����������.
     * @param e {Event} - �������� �������.
     */
    var checkEnd = function (e) {
        if (isMouse && !isMouseDown) { // ����� �� ������� � ����� �������� ������� ����
            mouseDown = false;
            return;
        }
        var endTime = new Date().getTime();
        var time = endTime - startTime;
        if (time >= settings.minTime && time <= settings.maxTime) { // �������� ������� �����
            if (Math.abs(distX) >= settings.minDist && Math.abs(distY) <= settings.maxDist) {
                swipeType = dir; // ���������� ���� ������ ��� "left" ��� "right"
            } else if (Math.abs(distY) >= settings.minDist && Math.abs(distX) <= settings.maxDist) {
                swipeType = dir; // ���������� ���� ������ ��� "top" ��� "down"
            }
        }
        dist = (dir === "left" || dir === "right") ? Math.abs(distX) : Math.abs(distY); // ���������� ���������� ���������� ���������

        // ��������� ���������� ������� swipe
        if (swipeType !== "none" && dist >= settings.minDist) {
            var swipeEvent = new CustomEvent("swipe", {
                bubbles: true,
                cancelable: true,
                detail: {
                    full: e, // ������ ������� Event
                    dir: swipeType, // ����������� ������
                    dist: dist, // ��������� ������
                    time: time // �����, ����������� �� �����
                }
            });
            el.dispatchEvent(swipeEvent);
        }
        e.preventDefault();
    };

    // ���������� �������������� �������
    var events = getSupportedEvents();

    // �������� ������� ����
    if ((support.pointer && !support.touch) || events.type === "mouse") isMouse = true;

    // ���������� ������������ �� �������
    el.addEventListener(events.start, checkStart);
    el.addEventListener(events.move, checkMove);
    el.addEventListener(events.end, checkEnd);

};

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
    //$(document).on("mousewheel DOMMouseScroll", function (e) {
    //    if (!scrolling) {
    //        if (e.originalEvent.wheelDelta > 0 || e.originalEvent.detail < 0) {
    //            navigateUp();
    //        } else {
    //            navigateDown();
    //        }
    //    }
    //});

    function MyFunc(e) {
        if (!scrolling) {
            if (e.type == 'swipe') {
                if (e.detail.dir == "up") {
                    navigateDown();
                } else if (e.detail.dir == "down") {
                    navigateUp();
                }
            } else if (e.type == 'mousewheel') {
                if (e.wheelDelta > 0 || e.detail < 0) {
                    navigateUp();
                } else {
                    navigateDown();
                }
            }
        }
    }

    //var el = document.getElementById('parallax');
    var el = document;
    swipe(el);
    el.addEventListener("swipe", function (e) {
        MyFunc(e);
    });
    el.addEventListener("mousewheel", function (e) {
        MyFunc(e);
    });
    el.addEventListener("DOMMouseScroll", function (e) {
        MyFunc(e);
    });
});
