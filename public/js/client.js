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
  * ///////////////////////////////////////////////////////////
  * ///////////////////////////////////////////////////////////
  * Set Important Variables
  * ///////////////////////////////////////////////////////////
  * ///////////////////////////////////////////////////////////
  */

// Variables For Controlling Login Panel
 var login = document.getElementById("login")
 var loginCover = document.getElementsByClassName("loginCover")[0]
 var maincontent = document.getElementById("maincontent")
   
// Variables For Controlling Team Selection
 var teams = document.getElementById("teams")
 var leagues = document.getElementById("leagues")
 var conferences = document.getElementById("conferences")
 var selectDescription = document.getElementById("selectDescription")

 // Variables For Tab Controller
 var i, tabcontent, tablinks;
 tabcontent = document.getElementsByClassName("tabcontent");
 tablinks = document.getElementsByClassName("tablinks");


  /**
  * ///////////////////////////////////////////////////////////
  * Animate UI Functions
  * ///////////////////////////////////////////////////////////
  */

/**
  *  @name showSignUp
  * 
  *  @brief Function to hide the Login panel and show the sign up panel
  */
function showSignUp(){
  loginCover.style.left="50%"
  loginCover.style.background="#003F88"
}

function hideSignUp(){
  loginCover.style.left="0%"
  loginCover.style.background="#f9c74f"
}

 /**
  *  @name hideLogin
  * 
  *  @brief Function to hide the Login window when the user inserts valid login credentials
  */
function hideLogin(){
  console.log("Login Bypassed");
  login.style.top="-200%";
  maincontent.style.display="block";
}

 /**
  *  @name showLogin
  * 
  *  @brief Function to show the Login window when the user inserts logs out
  */
function showLogin(){
  login.style.top="50%";
   maincontent.style.display="none"
}

 /**
  *  @name hideLeagues
  * 
  *  @brief Function to hide the leagues panel and show the region panel
  */
function hideLeagues(){
  selectDescription.style.left="100%";
  leagues.style.left="100%";
  $(conferences).fadeIn();
}

 /**
  *  @name hideLeagues
  * 
  *  @brief Function to hide the region panel and show the conferences panel
  */
function showLeagues(){
  selectDescription.style.left="0%";
  leagues.style.left="0%";
  $(conferences).fadeOut();
}

 /**
  *  @name hideConferences
  * 
  *  @brief Function to hide the conferences panel and show the teams panel
  */
function hideConferences(){
  conferences.style.left="200%";
  $(teams).fadeIn();
}


 /**
  *  @name hideConferences
  * 
  *  @brief Function to hide the conferences panel and show the teams panels
  */
function showConferences(){
  conferences.style.left="50%";
  $(teams).fadeOut();
}


 /**
  * ///////////////////////////////////////////////////////////
  * ///////////////////////////////////////////////////////////
  * Functions to Access Server
  * ///////////////////////////////////////////////////////////
  * ///////////////////////////////////////////////////////////
  */

/**
 *  @name getTestNews
 * 
 *  @brief get test news article for general search page
 */
function getNews(){
  $.get('http://127.0.0.1:5000/news', function(news) {
    // console.log(news)
  news.forEach(function(newsItem) {
    console.log(newsItem['title'])
  // $('<li class="card newsItem"></li>').text(newsItem.title).appendTo('ul#news');
    $('<a href="'+newsItem.url+'"><li class="card newsItem"><img src="'+newsItem.image+'"><div class="articleWords"><h4>'+newsItem.title+'</h4><p>'+newsItem.description+'</p><h6>'+newsItem.authors+'</h6></div></li></a>').appendTo('ul#news');
});
});
}

// Call get News on App start to test the response
getNews()

/**
  * ///////////////////////////////////////////////////////////
  * Functions for Tabs
  * ///////////////////////////////////////////////////////////
  */

  /**
   * @name openTab
   * @@description function to open one tab and close another based on button presses
   * @param {event} evt on click event handler
   * @param {string} tabName id string of the tab to be turned on
   */
  function openTab(evt, tabName) {
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
  }
  
  
   /**
    * ///////////////////////////////////////////////////////////
    * Set Starting Conditions
    * ///////////////////////////////////////////////////////////
    */
  
  tabcontent[0].style.display = "block";
  tablinks[3].className += " active";

 /**
  * ///////////////////////////////////////////////////////////
  * ///////////////////////////////////////////////////////////
  * Vue JS Stuff
  * ///////////////////////////////////////////////////////////
  * ///////////////////////////////////////////////////////////
  */


  /**
  * ///////////////////////////////////////////////////////////
  * ///////////////////////////////////////////////////////////
  * Set Vue Components
  * ///////////////////////////////////////////////////////////
  * ///////////////////////////////////////////////////////////
  */

Vue.component('news-item', {
  props: ['news'],
  template: '<a :href="news.url"><li class="card newsItem"><img :src="news.image"><div class="articleWords"><h4>{{news.title}}</h4><p>"{{news.description}}..."</p></div></li></a>'
})

//<a href={{news.url}}><li class="card newsItem"><img src={{news.image}}><div class="articleWords"><h4>'{{news.title}}</h4><p>'{{news.description}}...'</p></div></li></a>

/**
* ///////////////////////////////////////////////////////////
* ///////////////////////////////////////////////////////////
* Begin Vue App and Define UI Methods
* ///////////////////////////////////////////////////////////
* ///////////////////////////////////////////////////////////
*/

var app = new Vue({
  el: '#maincontent',
  data: {
    generalNews:[]
  },
  methods: {
      talk: function () {
          console.log("Request Sent")
      },
      toggleSignUp: function (state) {
        if(state == "showSignup"){
          loginCover.style.left="50%"
          loginCover.style.background="#003F88"
        }
        if(state == "showSignin"){
          loginCover.style.left="0%"
          loginCover.style.background="#f9c74f"
        }
      },
      generalSearch: function (event) {
        $("ul#news").empty();
        event.preventDefault();
        newsItem = $('#searchBar').val();
        $.post('http://127.0.0.1:5000/news?' + $.param({'newsItem': newsItem}), function(news) {
        app.generalNews = news;
        $('#searchBar').val('');
        $('#searchBar').focus();
        })
    }
  }
})