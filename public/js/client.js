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

/** 
* @name feed-item
* @brief Component For News Items That exist in the Feed Page 
*/

Vue.component("feed-item", {
  props: ["feed"],
  template:
    '<a :href="feed.url" target="_blank" rel="noopener noreferrer">' +
    '<transition name="fade">' +
    '<div class="newsItem card">' +
    '<div class="newsImageHolder">' +
    '<img :src="feed.image" >' +
    "</div>" +
    '<div class="articleWords">' +
    "<h4>{{feed.title}}</h4>" +
    '<p>"{{feed.description}}..."</p>' +
    "<h6>{{feed.author}}</h6>" +
    "</div>" +
    '<img class="teamImage" :src="feed.teamLogo">' +
    "</div>" +
    "</transition>" +
    "</a>",
});

/** 
* @name news-item
* @brief Component For News Items That exist in the Search Page
*/

Vue.component("news-item", {
  props: ["news"],
  template:
    '<a :href="news.url" target="_blank" rel="noopener noreferrer">' +
    '<transition name="fade">' +
    '<div class=" newsItem card">' +
    '<div class="newsImageHolder">' +
    '<img :src="news.image">' +
    "</div>" +
    '<div class="articleWords">' +
    "<h4>{{news.title}}</h4>" +
    '<p>"{{news.description}}..."</p>' +
    "<h6>{{news.author}}</h6>" +
    "</div>" +
    '<div class="teamImage"></div>' +
    "</div>" +
    "</transition>" +
    "</a>",
});

/** 
* @name team-option
* @brief  Component for the selection options for adding teams in the 
*         'Add Teams' section of the 'Teams' page
*/

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
        var childrenIds = app.teamsJson[option]["children"];
        var childrenData = [];
        for (i = 0; i < childrenIds.length; i++) {
          childrenData.push(app.teamsJson[childrenIds[i]]);
        }

        app.teamOptions = childrenData;

        var docTeams = [];
        var docRef = db.collection("users").doc(user);
        docRef.get().then((doc) => {
          if (doc.exists) {
            docTeams = doc.data().teams;
            for (i = 0; i < app.teamOptions.length; i++) {
              if (docTeams.includes(app.teamOptions[i].id)) {
                app.teamOptions.splice(i, 1);
              }
            }
          } else {
            // doc.data() will be undefined in this case
            console.log("No such document!");
          }
        });
      } else {
        //Insert Data to user teams
        var docTeams = [];
        var docRef = db.collection("users").doc(user);

        docRef.get().then((doc) => {
          if (doc.exists) {
            docTeams = doc.data().teams;
            if (!docTeams.includes(option)) {
              for (i = 0; i < app.teamOptions.length; i++) {
                if (option == app.teamOptions[i].id) {
                  swal(
                    "Team Added!",
                    "This team's articles have been added to your feed!",
                    "success"
                  );
                }
              }

              docTeams.push(option);
              app.loadUserTeams();
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
      app.toggleResetButton("on");
    },
  },
  template:
    '<div class="card" v-on:click="teamOption(option.id,option.record);" >' +
    "<h4>{{option.title}}</h4>" +
    '<img :src="option.image">' +
    "</div>",
});

/** 
* @name remove-item
* @brief  Component for the team removal options in the 'My Teams'
*         section of the 'Teams' page
*/
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
            swal(
              "Team Removed!",
              "This team's articles have been removed from your feed!"
            );
            docTeams.splice(index, 1);
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
    '<div class="card">' +
    '<h4 v-on:click="removeItem(item.id)">&#x2716;</h4>' +
    "<h4>{{item.title}}</h4>" +
    '<img :src="item.image">' +
    "</div>",
});

/* Initialize Vue */

var app = new Vue({
  el: "#vue",
  data: {
    generalNews: [],  // Array to hold news for the Search News Page
    teamOptions: [],  // Array to hold options for the Team selecton page
    feedNews: [],     // Array to hold news for the My Feed News Page
    userTeams: [],    // Array to hold team ids for a logged in user
    teamsJson: {},    // Object showing teams in different leagues by id
    darkMode: "off",  // Variable to decide if dark mode is on or off
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
     * @brief Function to search for news data. Right now it 
     *        talks to the python server and gets news from
     *        the Bing Search API
     * @param event the submit event when a user presses enter
     */
    
    generalSearch: function (event) {
      $("ul#searchFeed").empty();
      event.preventDefault();
      newsItem = $("#searchBar").val();
      $.post(
        "/news?" + $.param({ newsItem: newsItem, number: 20, logo: "" }),
        (data) => {
          this.generalNews = data.news;
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
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
            tr[i].parentNode.parentNode.style.display = "";
          } else {
            tr[i].parentNode.parentNode.style.display = "none";
          }
        }
      }
    },
    /**
     * @name populateFeed
     * @brief Function to populate user feed with team data
     */
    populateFeed: function () {
      this.feedNews = [];
      for (i = 0; i < this.userTeams.length; i++) {
        var logo, team;
        team = this.userTeams[i].title;
        logo = this.userTeams[i].image;
        $.post(
          "/news?" + $.param({ newsItem: team, number: 10, logo: logo }),
          (data) => {
            for (j = 0; j < data.news.length; j++) {
              if (data.news[j].image == null) {
                data.news[j].image = data.logoUrl;
              }

              data.news[j].teamLogo = data.logoUrl;

              this.feedNews.push(data.news[j]);
            }
          }
        );
      }
    },
    /**
     * @name setTabs 
     * @brief presets both tabs in the 'Team' page to be hidden when the page loads
     */
    setTabs: function () {
      tabcontent = document.getElementsByClassName("selectTabs");
      tablinks = document.getElementsByClassName("tablinks");

      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
      }

      tabcontent[0].style.display = "grid";
      tablinks[0].className += " activeTab";
    },
    /**
     * @name openTab 
     * @brief switches tabs based on buttons in a list
     * @param {event} evt the tab onclick event
     * @param {string} tabName id of the tab
     *
     * @copyright https://www.w3schools.com (w3schools)
     */
    openTab: function (tabName, event) {
      var i, tabcontent, tablinks;
      tabcontent = document.getElementsByClassName("selectTabs");
      tablinks = document.getElementsByClassName("tablinks");

      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
      }
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" activeTab", "");
      }
      document.getElementById(tabName).style.display = "grid";
      event.currentTarget.className += " activeTab";
    },

    /**
     * @name resetTeams
     * @brief Function to clear the teamOptions array
     */
    resetTeams: function () {
      this.teamOptions = [
        this.teamsJson["0"],
        this.teamsJson["37"],
        this.teamsJson["70"],
        this.teamsJson["111"],
      ];
    },
    /**
     *  @name setTeamsJson 
     *  @brief  fuction to get the dictionary containing teams by the league 
     *          and conferences they belong to and save it in the teamsJson
     *          object in vue.
     */
    setTeamsJson: function () {
      $.post("/setTeamsJson?" + $.param({ option: "begin" }), (resetTeams) => {
        this.teamsJson = resetTeams;
      });
    },
    /**
     * @name toggleResetButton
     * @brief Function to toggle the reset button. The state is set to be the
     *        opposite of whatever the current state is
     * @param state on/off state of button
     */
    toggleResetButton: function (state) {
      resetTeams = document.getElementById("resetTeams");
      if (state == "off") {
        resetTeams.style.display = "none";
        console.log("remove");
      } else if (state == "on") {
        console.log("reset");
        resetTeams.style.display = "block";
      }
    },
    /**
     * @name loadUserTeams
     * @brief Function to load user selected teams when a user logs in
     */
    loadUserTeams: function () {
      var myTeamsDoc = db.collection("users").doc(user);
      myTeamsDoc.get().then((doc) => {
        if (doc.exists) {
          docTeams = doc.data().teams;
          this.userTeams = [];

          for (i = 0; i < docTeams.length; i++) {
            teamId = docTeams[i];
            currentTeam = this.teamsJson[teamId];
            this.userTeams.push(currentTeam);
          }

          return db
            .collection("users")
            .doc(user)
            .update({
              teams: docTeams,
            })
            .then(() => {
              console.log("User Teams Loaded");
              this.populateFeed();
            });
        } else {
          // doc.data() will be undefined in this case
          console.log("No such document!");
        }
      });
    },
    /**
     * @name toggleDarkMode
     * @brief a function to turn dark mode on or off based on the state needed.
     */
    toggleDarkMode: function () {
      if (this.darkMode == "off") {
        $(document).ready(function () {
          $("#searchFeed .newsItem").css("background", "#313638");
          $(".newsImageHolder").css("background", "#131516");
          $(".pp-section").css("background", "#131516");
          $(".newsItem").css("background", "#313638");
          $("#navbar").css("background", "#131516");
          $("#login").css("background", "#131516");
          $("#load").css("background", "#131516");
          $(".newsItem").css("color", "#fff");
          $(".tablinks").css("color", "#000");
          $("textarea").css("color", "#fff");
          $("html").css("color", "#fff");
          $("input").css("color", "#fff");
          $("a").css("color", "#fff");
        });
        this.darkMode = "on";
      } else {
        $(document).ready(function () {
          $("#searchFeed .newsItem").css("background", "#fff");
          $(".newsImageHolder").css("background", "#fff");
          $(".pp-section").css("background", "#fff");
          $(".newsItem").css("background", "#fff");
          $("#navbar").css("background", "#fff");
          $("#login").css("background", "#fff");
          $("#load").css("background", "#fff");
          $(".newsItem").css("color", "#000");
          $(".tablinks").css("color", "#000");
          $("textarea").css("color", "#000");
          $("html").css("color", "#000");
          $("input").css("color", "#000");
          $("a").css("color", "#000");
        });
        this.darkMode = "off";
      }
    },

    /**
     * @name sendEmail
     * @brief Function to send an email when a user types a message in the contact 
     *        page. The email is annonymous and is sent to an admin of the app
     * @param {*} event the on submit event that happens when a user presses enter
     *                  or clicks the send button
     */

    sendEmail: function (event) {
      $("#contactFormMessage").empty();
      event.preventDefault();
      var emailMessage = document.getElementById("contactFormMessage").value;
      document.getElementById("contactFormMessage").value = "";
      Email.send({
        Host: "smtp.gmail.com",
        Username: "sicblivn@gmail.com",
        Password: "*********", // For full testing, I used my personal password but removed it
        To: "msimbao@macalester.edu",
        From: "sicblivn@gmail.com",
        Subject: "Anyonymous Message From Tympdeja User",
        Body: emailMessage,
      }).then(function (message) {
        swal("Done!", "Mail Sent Successfully!", "success");
      });
    },
  },
  created: function () {
    this.setTabs();
    this.toggleResetButton("off");
    this.setTeamsJson();
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

/*  
*   Page Piling is a lightweight 
*   library to handle navigation 
*   for single page websites 
*/

$(document).ready(function () {
  $("#maincontent").pagepiling({
    menu: "#myMenu",
    direction: "horizontal",
    verticalCentered: true,
    sectionsColor: [],
    anchors: ["feed", "select", "general", "contactus"],
    scrollingSpeed: 100,
    easing: "linear",
    loopBottom: false,
    loopTop: false,
    css3: true,
    navigation: false,
    normalScrollElementTouchThreshold: 1000,
    touchSensitivity: 5,
    keyboardScrolling: false,
    sectionSelector: ".section",
    animateAnchor: false,

    //events
    onLeave: function (index, nextIndex, direction) {},
    afterLoad: function (anchorLink, index) {},
    afterRender: function () {},
  });
  $.fn.pagepiling.setAllowScrolling(false);
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

/*  
*   The Login and Signup Functions and Elements are outside the Vue app
*   This was done to make it easier to handle unique errors that were
*   Popping up and to make it easier to insert user Data into the Vue app
*
*/

/**
 *  @name toggleSignUp
 *  @brief Function to hide or show sign up panel
 *  @param {string} state can be hideSignUp or showSignUp
 */

// Variables For Controlling Menu and Signup
var login = document.getElementById("login");
var navbar = document.getElementById("navbar");

$(document).ready(function () {
  $("#login").children().eq(0).fadeOut();
});

function toggleSignUp(state) {
  if (state == "showSignUp") {
    $("#login").children().eq(1).fadeOut();
    $("#login").children().eq(0).fadeIn();
  } else {
    $("#login").children().eq(1).fadeIn();
    $("#login").children().eq(0).fadeOut();
  }
}

/**
 *  @name toggleLogin
 *  @brief Function to hide or show Login panel
 *  @param {string} state can be hideLogin or showLogin
 */

function toggleLogin(state) {
  if (state == "hideLogin") {
    login.style.top = "-200%";
    maincontent.style.display = "block";
  } else {
    login.style.top = "50%";
    maincontent.style.display = "none";
  }
}


/**
 * @name hideWelcomeScreen
 * @brief Function to hide welcomeScreens that function to orient new users
 */

 var welcomeScreenId = 0;

function hideWelcomeScreen() {
  welcomeScreens = document.getElementsByClassName("welcomeScreen");
  welcomeScreens[welcomeScreenId].style.top = "-300%";
  welcomeScreens[welcomeScreenId].style.display = "none";
  welcomeScreenId++;
}

/**
 * @name validatePassword 
 * @brief function to ask user to confirm their password in a second password entry box
 * @copyright Diego Leme https://codepen.io/diegoleme
 */

var password = document.getElementById("signupPassword"),
  confirm_password = document.getElementById("confirmPassword");

function validatePassword() {
  if (password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords Don't Match");
  } else {
    confirm_password.setCustomValidity("");
  }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;
