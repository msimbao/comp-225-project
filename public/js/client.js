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
  login.style.bottom="100%";
  maincontent.style.display="block"
}

 /**
  *  @name showLogin
  * 
  *  @brief Function to show the Login window when the user inserts logs out
  */
function showLogin(){
  login.style.bottom="0%";
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
// getNews()

/**
 *  @name getGeneralNews
 * 
 *  @brief get news articles for the search page when queried and submit button pressed
 */
$('#generalSearchForm').submit(function(event) {
$("ul#news").empty();
event.preventDefault();
newsItem = $('#searchBar').val();
console.log(newsItem);
$.post('http://127.0.0.1:5000/news?' + $.param({'newsItem': newsItem}), function(news) {
  
  news.forEach(function(newsItem) {
    console.log(newsItem['title'])
    $('<a href="'+newsItem.url+'"><li class="card newsItem"><img src="'+newsItem.image+'"><div class="articleWords"><h4>'+newsItem.title+'</h4><p>'+newsItem.description+'</p><h6>'+newsItem.authors+'</h6></div></li></a>').appendTo('ul#news');
  });
  //"POST /newsItem?newsItem=Hello HTTP/1.1" 
  // $('<li></li>').text(newsItem).appendTo('ul#news');
  $('#searchBar').val('');
  $('#searchBar').focus();
});

});
