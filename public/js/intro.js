


/*////////////////////////////////////////////////////////////////

  _____                 _____ _ _ _ _             
 |  __ \               |  __ (_) | (_)            
 | |__) |_ _  __ _  ___| |__) || | |_ _ __   __ _ 
 |  ___/ _` |/ _` |/ _ \  ___/ | | | | '_ \ / _` |
 | |  | (_| | (_| |  __/ |   | | | | | | | | (_| |
 |_|   \__,_|\__, |\___|_|   |_|_|_|_|_| |_|\__, |
              __/ |                          __/ |
             |___/                          |___/ 

///////////////////////////////////////////////////////////////////*/

/* Initialize */

$(document).ready(function () {
  $("#maincontent").pagepiling({
    menu: "#myMenu",
    direction: "vertical",
    verticalCentered: true,
    sectionsColor: ["#fff", "#fff", "#fff"],
    anchors: ["first", "second", "third"],
    scrollingSpeed: 100,
    easing: "linear",
    loopBottom: false,
    loopTop: false,
    css3: true,
    navigation: false,
    normalScrollElements: "#first, #second, #third",
    normalScrollElementTouchThreshold: 5,
    touchSensitivity: 5,
    keyboardScrolling: true,
    sectionSelector: ".section",
    animateAnchor: false,

    //events
    onLeave: function (index, nextIndex, direction) {},
    afterLoad: function (anchorLink, index) {},
    afterRender: function () {},
  });
});