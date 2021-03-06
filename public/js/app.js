/**
 *
 *  @Title app.js
 *
 *  @Brief The login, logout, and signup functions using firebase
 *
 *  @Author Ty, Declan, Jack, Mphatso
 *
 */

//Initialize Firebase
const config = {
  apiKey: "AIzaSyDM0YYvGQFSc9qy6jh2hpxZy_87B8eNc3o",
  authDomain: "webapp-43db3.firebaseapp.com",
  databaseURL: "https://webapp-43db3-default-rtdb.firebaseio.com",
  projectId: "webapp-43db3",
  storageBucket: "webapp-43db3.appspot.com",
  messagingSenderId: "967819702334",
  appId: "1:967819702334:web:516489547c9f45733a616f",
  measurementId: "G-B4T0X396WR",
};
firebase.initializeApp(config);

const auth = firebase.auth();
const db = firebase.firestore();

//update firestore settings
db.settings({ timestampsInSnapshots: true });

//Get elements
const loginForm = document.getElementById("loginToAccount");
const signUpForm = document.getElementById("createAccount");

const txtEmail = document.getElementById("loginEmail");
const txtPassword = document.getElementById("loginPassword");

const signupEmail = document.getElementById("signupEmail");
const signupPassword = document.getElementById("signupPassword");
const confirmPassword = document.getElementById("confirmPassword");

const btnLogin = document.getElementById("submitLogin");
const btnSignUp = document.getElementById("submitSignUp");
const btnLogout = document.getElementById("submitLogout");

var user = "";

//sign up
btnSignUp.addEventListener("click", (ev) => {
  ev.preventDefault();

  if (signupPassword.value != confirmPassword.value){
    swal("Sign Up Failed", "Passwords are not matching", "error");
    return 0;
  }

  //get user info
  const email = signupEmail.value;
  const password = signupPassword.value;

  //sign up user
  auth
    .createUserWithEmailAndPassword(email, password)
    .then((cred) => {
      newUser = cred.user.uid;
      user = newUser;
      console.log(user)
      console.log("Signed Up")
      return db.collection("users").doc(cred.user.uid).set({
        teams: [],
        darkMode: "off",
      }); 
    })
    .then(() => {
        toggleLogin("hideLogin");
        app.resetTeams();
        welcomeScreens = document.getElementsByClassName("welcomeScreen");
        welcomeScreens[1].style.display = "grid";
        welcomeScreens[0].style.display = "grid";
        document.getElementById("addTeamsButton").click();
        signUpForm.reset();
      })
    .catch((error) => {
      swal("Sign Up Failed", '"' + error + '"', "error");
    })

});

//log out
btnLogout.addEventListener("click", (ev) => {
  ev.preventDefault();
  auth.signOut().then(() => {
    user = "";
    toggleLogin("showLogin");
  });
});

//sign in
btnLogin.addEventListener("click", (ev) => {
  ev.preventDefault();

  //get user info
  const email = txtEmail.value;
  const password = txtPassword.value;

  //log in user
  auth
    .signInWithEmailAndPassword(email, password)
    .then((cred) => {
      console.log(cred.user);
      user = cred.user.uid;
      toggleLogin("hideLogin");
      app.resetTeams();
      app.loadUserTeams();
      loginForm.reset();
    })
    .catch((error) => {
      swal("Login Failed", '"' + error + '"', "error");
    });
});
