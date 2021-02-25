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
  * 
 __      __            _____      _               
 \ \    / /           / ____|    | |              
  \ \  / /   _  ___  | (___   ___| |_ _   _ _ __  
   \ \/ / | | |/ _ \  \___ \ / _ \ __| | | | '_ \ 
    \  /| |_| |  __/  ____) |  __/ |_| |_| | |_) |
     \/  \__,_|\___| |_____/ \___|\__|\__,_| .__/ 
                                           | |    
                                           |_|    

  * ///////////////////////////////////////////////////////////
  */

  /* News Components */

 Vue.component('news-item', {
  props: ['news'],
  template: '<a :href="news.url"><div class="card newsItem"><img :src="news.image"><div class="articleWords"><h4>{{news.title}}</h4><p>"{{news.description}}..."</p><img class="teamImage" src="https://cdn.glitch.com/8db8a81a-3c21-4049-a279-408bafb3a783%2Fnfl-1-logo-png-transparent.png?v=1612974806169"></div></div></a>'
})

  /* Team Selection Components */

Vue.component('selector-option', {
  props: ['options'],
  template: '<div><h4>{{option.title}}</h4><img :src="option.image"></div>'
})

  /* Initialize */

var app = new Vue({
  el: '#vue',
  data: {
    generalNews:[],
    selectorOptions: [],
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
    },
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
    }
  }
})

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

$(document).ready(function() {
	$('#maincontent').pagepiling({
	    menu: '#myMenu',
        direction: 'vertical',
        verticalCentered: true,
        sectionsColor: ['#f3f3f3','#f3f3f3','#f3f3f3'],
        anchors: ['feed','select','general'],
        scrollingSpeed: 100,
        easing: 'linear',
        loopBottom: false,
        loopTop: false,
        css3: true,
        navigation: false,
       	normalScrollElements: '#feed, #select, #general',
        normalScrollElementTouchThreshold: 5,
        touchSensitivity: 5,
        keyboardScrolling: true,
        sectionSelector: '.section',
        animateAnchor: false,

		//events
		onLeave: function(index, nextIndex, direction){},
		afterLoad: function(anchorLink, index){},
		afterRender: function(){},
	});
});

 /**
  * ///////////////////////////////////////////////////////////
  * ///////////////////////////////////////////////////////////
  * Set Important Variables
  * ///////////////////////////////////////////////////////////
  * ///////////////////////////////////////////////////////////
  */

// Variables For Controlling Menu
var navbar = document.getElementById('navbar')
var menuButton = document.getElementById('menuButton')

// Variables For Controlling Login Panel
 var login = document.getElementById("login")
 var loginCover = document.getElementsByClassName("loginCover")[0]


  /**
  * ///////////////////////////////////////////////////////////
  * Animate UI Functions
  * ///////////////////////////////////////////////////////////
  */

  /**
  *  @name toggleSignUp
  * 
  *  @brief Function to hide or show signup section
  */

 $(document).ready(function(){
  $('#login').children().eq(1).fadeOut();
  })
 
 function showSignUp(){
   $('#login').children().eq(2).fadeOut();
   $('#login').children().eq(1).fadeIn();
 }
 
 function hideSignUp(){
   $('#login').children().eq(2).fadeIn();
   $('#login').children().eq(1).fadeOut();
 }

 /**
  *  @name toggleLogin
  * 
  *  @brief Function to hide or show Login panel
  */

function toggleLogin(state){
  if (state == "hideLogin"){
    console.log("Login Bypassed");
    login.style.top="-200%";
    maincontent.style.display="block";
  }
  if (state == "showLogin"){
    login.style.top="50%";
    maincontent.style.display="none"
  }
}

 /**
  *  @name toggleMenu
  * 
  *  @brief Function to toggle the website Menu
  */

 var menu=0;
 function toggleMenu(){
  if (menu == 0){
    menuButton.style.color="#fff"
    navbar.style.bottom="0%"
    menu = 1;
  }
  else{
    menuButton.style.color="#000"
    navbar.style.bottom="100%"
    menu = 0;
  }
}

 /**
  * ///////////////////////////////////////////////////////////
  * ///////////////////////////////////////////////////////////
  * Functions to Test Vue Components
  * ///////////////////////////////////////////////////////////
  * ///////////////////////////////////////////////////////////
  */

/**
 *  @name getTestNews
 * 
 *  @brief get test news article for general search page and display it 
 */
function getNews(){
  $.get('http://127.0.0.1:5000/news', function(news) {
    // console.log(news)
  news.forEach(function(newsItem) {
    // console.log(newsItem['title'])
  // $('<li class="card newsItem"></li>').text(newsItem.title).appendTo('ul#news');
    $('<a href="'+newsItem.url+'"><div class="card newsItem"><img src="'+newsItem.image+'"><div class="articleWords"><h4>'+newsItem.title+'</h4><p>'+newsItem.description+'</p><h6>'+newsItem.authors+'</h6></div></div></a>').appendTo('ul#news');
});
});
}

// Call get News on App start to test the response
getNews()
