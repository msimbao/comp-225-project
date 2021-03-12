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
    '<a :href="feed.url" target="_blank" rel="noopener noreferrer">' +
    '<transition name="fade">'+
    '<div class="newsItem">' +
    '<div class="newsImageHolder">' +
    '<img :src="feed.image" >' +
    '</div>'+
    '<div class="articleWords">' +
    "<h4>{{feed.title}}</h4>" +
    '<p>"{{feed.description}}..."</p>' +
    '<h6>{{feed.author}}</h6>'+
    "</div>" +
    '<img class="teamImage" :src="feed.teamLogo">' +
    "</div>" +
    '</transition>'+
    "</a>",
});

/* General News Component */

Vue.component("news-item", {
  props: ["news"],
  template:
    '<a :href="news.url" target="_blank" rel="noopener noreferrer">' +
    '<transition name="fade">'+
    '<div class=" newsItem">' +
    '<div class="newsImageHolder">' +
    '<img :src="news.image" class="card">' +
    '</div>'+
    '<div class="articleWords">' +
    "<h4>{{news.title}}</h4>" +
    '<p>"{{news.description}}..."</p>' +
    '<h6>{{news.author}}</h6>'+
    "</div>" +
    '<div class="teamImage"></div>' +
    "</div>" +
    '</transition>'+
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

        var childrenIds = app.teamsJson[option]["children"]
        var childrenData = []
        for (i = 0; i < childrenIds.length; i++) {
          childrenData.push(app.teamsJson[childrenIds[i]])
        }

            app.teamOptions = childrenData;

            var docTeams = [];
            var docRef = db.collection("users").doc(user);
            docRef.get().then((doc) => {
              if (doc.exists) {
                docTeams = doc.data().teams; 
                for (i = 0; i < app.teamOptions.length; i++) {
                  if (docTeams.includes(app.teamOptions[i].id) ){
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
                if (option == app.teamOptions[i].id){
                  // app.teamOptions.splice(i, 1);
                  alert("This team's articles have been added to your feed!")
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
      app.toggleResetButton('on');
    },
  },
  template:
    '<div class="card" v-on:click="teamOption(option.id,option.record);" >' +
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
            alert("This team's articles have been removed from your feed!");
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

/* Initialize */

var app = new Vue({
  el: "#vue",
  data: {
    generalNews: [],
    teamOptions: [],
    feedNews: [],
    userTeams: [],
    teamsJson: {},
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
      $("ul#searchFeed").empty();
      event.preventDefault();
      newsItem = $("#searchBar").val();
      $.post(
        "/news?" + $.param({ newsItem: newsItem, number:20, logo:"" }),
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
      console.log("Populating Feed")
      this.feedNews = []
      for (i = 0; i < this.userTeams.length; i++) {
      var logo, team
      team = this.userTeams[i].title
      logo = this.userTeams[i].image
      $.post(
        "/news?" + $.param({ newsItem: team, number:10, logo: logo }),
        (data) => {
          for (j = 0; j < data.news.length; j++) {
            if (data.news[j].image == null){
              data.news[j].image = data.logoUrl
              // data.news[j].teamLogo = ""
            }

              data.news[j].teamLogo = data.logoUrl

            this.feedNews.push(data.news[j]);
          }
        }
      )
    }
    },
    /**
     * @name setTabs presets all tabs to display:none
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
     * @name openTab switches tabs based on buttons in a list
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
          this.teamOptions = [this.teamsJson["0"],this.teamsJson["37"],this.teamsJson["70"],this.teamsJson["111"]];
    },
    /**
     * 
     * @param {*} state 
     */
    setTeamsJson: function () {
      $.post(
        "/setTeamsJson?" + $.param({ option: "begin" }),
        (resetTeams) => {
          this.teamsJson = resetTeams;
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
      if ((state == "off")) {
        resetTeams.style.display = "none";
        console.log("remove");
      } else if ((state == "on")) {
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
          docTeams = doc.data().teams;
          this.userTeams = [];

          for (i = 0; i < docTeams.length; i++) {
            teamId = docTeams[i];
            currentTeam = this.teamsJson[teamId]
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
  },
  created: function () {
    this.setTabs();
    this.toggleResetButton('off')
    this.setTeamsJson()
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
    direction: "horizontal",
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
 * @brief Function to hide welcomeScreen
 */
function hideWelcomeScreen() {
  welcomeScreen = document.getElementById("welcomeScreen");
  welcomeScreen.style.top = "-200%";
}

/**
 * @name validatePassword function to ask user to confirm their password in a second password entry box
 * @copyright Diego Leme https://codepen.io/diegoleme
 */

var password = document.getElementById("signupPassword")
  , confirm_password = document.getElementById("confirmPassword");

function validatePassword(){
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Passwords Don't Match");
  } else {
    confirm_password.setCustomValidity('');
  }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;