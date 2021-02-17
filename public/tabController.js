/**
 * 
 *  @Title tabController.js
 * 
 *  @Brief JavaScript For holding functions that handle the switching of tabs in the front end
 * 
 *  @Author Ty, Declan, Jack, Mphatso
 * 
 */

 // Code originally from https://www.w3schools.com/

  /**
  * ///////////////////////////////////////////////////////////
  * Set Important Variables
  * ///////////////////////////////////////////////////////////
  */

var i, tabcontent, tablinks;
tabcontent = document.getElementsByClassName("tabcontent");
tablinks = document.getElementsByClassName("tablinks");


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