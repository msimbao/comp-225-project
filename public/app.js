(function () {

    //Initialize Firebase
    const config = {
        apiKey: "AIzaSyDM0YYvGQFSc9qy6jh2hpxZy_87B8eNc3o",
        authDomain: "webapp-43db3.firebaseapp.com",
        databaseURL: "https://webapp-43db3-default-rtdb.firebaseio.com",
        storageBucket: "webapp-43db3.appspot.com",
    };
    firebase.initializeApp(config);

    //Get elements
    const txtEmail = document.getElementById("email");
    const txtPassword = document.getElementById("password");
    const btnLogin = document.getElementById("submitLogin");
    const btnSignUp = document.getElementById();
    const btnLogout = document.getElementById();

    //Add login event
    btnLogin.addEventListener("click", e => {
        //Get email and password
        const email = txtEmail.value;
        const pass = txtPassword.value;
        const auth = firebase.auth();
        //Sign in
        auth.signInWithEmailAndPassword(email, pass);
        promise.catch(e => console.log(e.message));
    });

    //Add signup event
    btnSignUp.addEventListener("click", e => {
        const email = txtEmail.value;
        const pass = txtPassword.value;
        const auth = firebase.auth();
        if (auth.fetchProvidersForEmail(email).length === 0) {
            //Sign in
            auth.createUserWithEmailAndPassword(email, pass);
            promise.catch(e => console.log(e.message));
        } else {
            console.log("invalid email")
        }
    });

    btnLogout.addEventListener("click", e => {
        firebase.auth().signOut();
    });

    //Add realtime listener
    firebase.auth().onAuthStateChanged(firebaseUser => {
        if(firebaseUser) {
            console.log(firebaseUser);
            btnLogout.classList.remove("hide");
        } else {
            console.log("Not logged in");
            btnLogout.classList.add("hide");
        }
    })

});