/**
 *
 *  @Title client.js
 *
 *  @Brief JavaScript For holding functions that handle the client
 *
 *  @Author Ty, Declan, Jack, Mphatso
 *
 */

/**
  * //////////////////////////////////////
 __      __         
 \ \    / /         
  \ \  / /   _  ___ 
   \ \/ / | | |/ _ \
    \  /| |_| |  __/
     \/  \__,_|\___|
                    
  * //////////////////////////////////////
  */

/* Feed Component */

Vue.component("feed-item", {
  props: ["feed"],
  template:
    '<a :href="feed.url">' +
    '<div class="card newsItem">' +
    '<img :src="feed.image">' +
    '<div class="articleWords">' +
    "<h4>{{feed.title}}</h4>" +
    '<p>"{{feed.description}}..."</p>' +
    '<img class="teamImage" src="https://cdn.glitch.com/8db8a81a-3c21-4049-a279-408bafb3a783%2Fnfl-1-logo-png-transparent.png?v=1612974806169">' +
    "</div>" +
    "</div>" +
    "</a>",
});

/* General News Component */

Vue.component("news-item", {
  props: ["news"],
  template:
    '<a :href="news.url">' +
    '<div class="card newsItem">' +
    '<img :src="news.image">' +
    '<div class="articleWords">' +
    "<h4>{{news.title}}</h4>" +
    '<p>"{{news.description}}..."</p>' +
    "</div>" +
    "</div>" +
    "</a>",
});

/* Team Selection Component */

Vue.component("team-option", {
  props: ["option"],
  methods: {
    /**
     * @name teamOptions
     * @brief Function to get current teams, leagues or conferences from a dictionary and populate a display grid or firebase with selected user teams
     * @param option the current team, league or conference selected
     * @param record the record of the selection
     */
    teamOption: function (option, record) {
      if (record == "") {
        $.post(
          "http://127.0.0.1:5000/conferences?" + $.param({ option: option }),
          (option_data) => {
            app.teamOptions = option_data;

            var docTeams = [];
            var docRef = db.collection("users").doc(user);
            docRef.get().then((doc) => {
              if (doc.exists) {
                docTeams = doc.data().teams; 
                for (i = 0; i < app.teamOptions.length; i++) {
                  console.log("checking")
                  if (docTeams.includes(app.teamOptions[i].id) ){
                      console.log("removing item")
                      console.log("option: ",option,"\n index: ",i,"\n teamId:", app.teamOptions[i].id)
                      app.teamOptions.splice(i, 1);
                    }
                  }
              } else {
                // doc.data() will be undefined in this case
                console.log("No such document!");
              }
            });
          }
        );
      } else {
        //Insert Data to user teams
        var docTeams = [];
        var docRef = db.collection("users").doc(user);

        docRef.get().then((doc) => {
          if (doc.exists) {
            // console.log("Document data:", doc.data().teams);
            docTeams = doc.data().teams;
            // console.log("After Concat:", docTeams);
            if (!docTeams.includes(option)) {
              
              for (i = 0; i < app.teamOptions.length; i++) {
                if (option == app.teamOptions[i].id){
                  // console.log("option: ",option,"\n index: ",i,"\n teamId:", app.teamOptions[i].id)
                  app.teamOptions.splice(i, 1);
                }
              }

              docTeams.push(option);
              // console.log("After Push:", docTeams);
            }

            return db
              .collection("users")
              .doc(user)
              .update({
                teams: docTeams,
              })
              .then(() => {
                console.log("User Teams Updated");
              });
          } else {
            // doc.data() will be undefined in this case
            console.log("No such document!");
          }
        });
      }
    },
  },
  template:
    '<div v-on:click="teamOption(option.id,option.record)" >' +
    "<h4>{{option.title}}</h4>" +
    '<img :src="option.image">' +
    "</div>",
});

/* Team Remove Component */

Vue.component("remove-item", {
  props: ["item"],
  methods: {
    /**
     * @name removeItem
     * @brief Function to remove a selected team from a user's preferences
     * @param option the current team selected
     */
    removeItem: function (option) {
      //Insert Data to user teams
      var docTeams = [];
      var docRef = db.collection("users").doc(user);

      docRef.get().then((doc) => {
        if (doc.exists) {
          docTeams = doc.data().teams;
          if (docTeams.includes(option)) {
            var index = docTeams.indexOf(option);
            // console.log("Splice started for:", option);
            docTeams.splice(index, 1);
            // console.log("After Deletion:", docTeams);
            app.loadUserTeams();
          }

          return db
            .collection("users")
            .doc(user)
            .update({
              teams: docTeams,
            })
            .then(() => {
              console.log("Team Deleted From User Data");
            });
        } else {
          // doc.data() will be undefined in this case
          console.log("No such document!");
        }
      });
    },
  },
  template:
    "<div>" +
    '<h4 v-on:click="removeItem(item.id)">&#x2716;</h4>' +
    "<h4>{{item.title}}</h4>" +
    '<img :src="item.image">' +
    "</div>",
});

/* Initialize */

var app = new Vue({
  el: "#vue",
  data: {
    generalNews: [],
    teamOptions: [],
    feedNews: [],
    userTeams: [],
  },
  methods: {
    /**
     * @name talk
     * @brief Function to test if vue is handling requests
     */
    talk: function () {
      console.log("Request Sent");
    },
    /**
     * @name generalSearch
     * @brief Function to search for news data. Right now it talks to server but will hopefully
     *        grab directly from database
     */
    generalSearch: function (event) {
      $("ul#news").empty();
      event.preventDefault();
      newsItem = $("#searchBar").val();
      $.post(
        "http://127.0.0.1:5000/news?" + $.param({ newsItem: newsItem }),
        (news) => {
          this.generalNews = news;
          $("#searchBar").val("");
          $("#searchBar").focus();
        }
      );
    },

    /**
     * @name filterSearch
     * @brief Function to filter through feed content quickly. Not used right now
     * @param {event} event event for when the input of a search bar is changed
     *
     * @copyright https://www.w3schools.com/
     */
    filterSearch: function (event) {
      // console.log("Searching");
      event.preventDefault();
      var input, filter, table, tr, td, i, txtValue;
      input = document.getElementById("filterSearch");
      filter = input.value.toUpperCase();
      table = document.getElementById("newsFeed");
      tr = table.getElementsByClassName("articleWords");

      for (i = 0; i < tr.length; i++) {
        td = tr[i];
        if (td) {
          te = td.getElementsByTagName("h4")[0];
          txtValue = td.textContent || td.innerText;
          // console.log(txtValue);
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].parentNode.parentNode.style.display = "";
          } else {
            tr[i].parentNode.parentNode.style.display = "none";
          }
        }
      }
    },
    setTabs: function () {
      tabcontent = document.getElementsByClassName("selectTabs");

      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
      }
    },
    openTab: function (tabName, event) {
      var i, tabcontent, tablinks;
      tabcontent = document.getElementsByClassName("selectTabs");
      tablinks = document.getElementsByClassName("tablinks");

      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
      }
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
      }
      document.getElementById(tabName).style.display = "grid";
      event.currentTarget.className += " active";
    },
    /**
     * @name resetTeams
     * @brief Function to clear the teamOptions array
     */
    resetTeams: function () {
      $.post(
        "http://127.0.0.1:5000/resetTeams?" + $.param({ option: "begin" }),
        (resetTeams) => {
          this.teamOptions = resetTeams;
        }
      );
    },
    /**
     * @name toggleResetButton
     * @brief Function to toggle the reset button
     * @param state on/off state of button
     */
    toggleResetButton: function (state) {
      resetTeams = document.getElementById("resetTeams");
      if ((state = "0")) {
        resetTeams.style.display = "none";
        console.log("remove");
      } else if ((state = "1")) {
        console.log("reset");
        resetTeams.style.display = "block";
      }
    },
    /**
     * @name loadUserTeams
     * @brief Function to load user selected team on login
     */
    loadUserTeams: function () {
      var myTeamsDoc = db.collection("users").doc(user);
      myTeamsDoc.get().then((doc) => {
        if (doc.exists) {
          // console.log("Document data:", doc.data().teams);
          docTeams = doc.data().teams;
          // console.log("After Concat:", docTeams);
          this.userTeams = [];

          for (i = 0; i < docTeams.length; i++) {
            teamId = docTeams[i];
            $.post(
              "http://127.0.0.1:5000/grabTeam?" + $.param({ teamId: teamId }),
              (grabbedTeam) => {
                this.userTeams.push(grabbedTeam);
              }
            );
          }

          return db
            .collection("users")
            .doc(user)
            .update({
              teams: docTeams,
            })
            .then(() => {
              console.log("User Teams Loaded");
            });
        } else {
          // doc.data() will be undefined in this case
          console.log("No such document!");
        }
      });
    },
  },
  created: function () {
    this.setTabs();
    // console.log(this);
  },
});

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
    anchors: ["feed", "select", "general"],
    scrollingSpeed: 100,
    easing: "linear",
    loopBottom: false,
    loopTop: false,
    css3: true,
    navigation: false,
    // normalScrollElements: "#feed, #select, #general",
    normalScrollElementTouchThreshold: 50,
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

/*//////////////////////////////////////////////////////////////
  _                 _                  _____ _                         
 | |               (_)          _     / ____(_)                        
 | |     ___   __ _ _ _ __    _| |_  | (___  _  __ _ _ __  _   _ _ __  
 | |    / _ \ / _` | | '_ \  |_   _|  \___ \| |/ _` | '_ \| | | | '_ \ 
 | |___| (_) | (_| | | | | |   |_|    ____) | | (_| | | | | |_| | |_) |
 |______\___/ \__, |_|_| |_|         |_____/|_|\__, |_| |_|\__,_| .__/ 
               __/ |                            __/ |           | |    
              |___/                            |___/            |_|    

//////////////////////////////////////////////////////////////*/

/**
 *  @name toggleSignUp
 *  @brief Function to hide or show sign up panel
 *  @param {string} state can be hideSignUp or showSignUp
 */

// Variables For Controlling Menu and Signup
var login = document.getElementById("login");
var navbar = document.getElementById("navbar");

$(document).ready(function () {
  $("#login").children().eq(1).fadeOut();
});

function toggleSignUp(state) {
  if (state == "showSignUp") {
    $("#login").children().eq(2).fadeOut();
    $("#login").children().eq(1).fadeIn();
  } else {
    $("#login").children().eq(2).fadeIn();
    $("#login").children().eq(1).fadeOut();
  }
}

/**
 *  @name toggleLogin
 *  @brief Function to hide or show Login panel
 *  @param {string} state can be hideLogin or showLogin
 */

function toggleLogin(state) {
  if (state == "hideLogin") {
    // console.log("Login Bypassed");
    login.style.top = "-200%";
    maincontent.style.display = "block";
  } else {
    login.style.top = "50%";
    maincontent.style.display = "none";
  }
}

/**
 *  @name toggleMenu
 *  @brief Function to toggle the website Menu
 */

var menu = 0;
function toggleMenu() {
  if (menu == 0) {
    navbar.style.bottom = "0%";
    menu = 1;
  } else {
    navbar.style.bottom = "100%";
    menu = 0;
  }
}

/**
 * @name hideWelcomeScreen
 * @brief Function to hide welcomeScreen
 */
function hideWelcomeScreen() {
  welcomeScreen = document.getElementById("welcomeScreen");
  welcomeScreen.style.top = "-200%";
}

/**
    * ///////////////////////////////////////////////////////////

  _______    _        _____            _             _ _           
 |__   __|  | |      / ____|          | |           | | |          
    | | __ _| |__   | |     ___  _ __ | |_ _ __ ___ | | | ___ _ __ 
    | |/ _` | '_ \  | |    / _ \| '_ \| __| '__/ _ \| | |/ _ \ '__|
    | | (_| | |_) | | |___| (_) | | | | |_| | | (_) | | |  __/ |   
    |_|\__,_|_.__/   \_____\___/|_| |_|\__|_|  \___/|_|_|\___|_|   
                                                                                                                             
                                              
    * ///////////////////////////////////////////////////////////
    */

/**
 * @name openTab switches tabs based on buttons in a list
 * @param {event} evt the tab onclick event
 * @param {string} tabName id of the tab
 *
 * @copyright https://www.w3schools.com (w3schools)
 */

var i, tabcontent, tablinks;
tabcontent = document.getElementsByClassName("selectTabs");
tablinks = document.getElementsByClassName("tablinks");

for (i = 0; i < tabcontent.length; i++) {
  tabcontent[i].style.display = "none";
}

function openTab(evt, tabName) {
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "grid";
  evt.currentTarget.className += " active";
}

/**
    * ///////////////////////////////////////////////////////////

    _____       _ _     _______        _       
  |_   _|     (_) |   |__   __|      | |      
    | |  _ __  _| |_     | | ___  ___| |_ ___ 
    | | | '_ \| | __|    | |/ _ \/ __| __/ __|
    _| |_| | | | | |_     | |  __/\__ \ |_\__ \
  |_____|_| |_|_|\__|    |_|\___||___/\__|___/
                                              
                                              
    * ///////////////////////////////////////////////////////////
    */

/**
 *  @name getTestNews
 *  @brief get test news article for general search page and display it
 */
function getNews() {
  $.get("http://127.0.0.1:5000/news", function (news) {
    // console.log(news)
    news.forEach(function (newsItem) {
      // console.log(newsItem['title'])
      // $('<li class="card newsItem"></li>').text(newsItem.title).appendTo('ul#news');
      $(
        '<a href="' +
          newsItem.url +
          '"><div class="card newsItem"><img src="' +
          newsItem.image +
          '"><div class="articleWords"><h4>' +
          newsItem.title +
          "</h4><p>" +
          newsItem.description +
          "</p><h6>" +
          newsItem.authors +
          "</h6></div></div></a>"
      ).appendTo("ul#news");
    });
  });
}

// Call get News on App start to test the response
getNews();
