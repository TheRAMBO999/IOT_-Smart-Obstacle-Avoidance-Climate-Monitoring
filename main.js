const firebaseConfig = {
  apiKey: "AIzaSyB-gEMXlAFw-NhhVUol6aJdXWuC0hrCjIA",
  authDomain: "loginapp-47b52.firebaseapp.com",
  databaseURL: "https://loginapp-47b52-default-rtdb.firebaseio.com",
  projectId: "loginapp-47b52",
  storageBucket: "loginapp-47b52.appspot.com",
  messagingSenderId: "928039063965",
  appId: "1:928039063965:web:0dfc0a87e3d803f5255f74",
  measurementId: "G-ZJLZDN19H1"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

var firebaseRef = firebase.database().ref().child('login');

firebaseRef.once("value").then(function(snapshot){
  var loginInfo = snapshot.val();
  document.getElementById("login").addEventListener("click", function(){
    var username = document.getElementById("username");
    var password = document.getElementById("pass");
    if (username.value == loginInfo.username && password.value == loginInfo.password){
      location.replace("home.html");
    } else if (username.value != loginInfo.username){
      username.style.borderColor = "red";
    } else if (password.value != loginInfo.password){
      password.style.borderColor = "red";
    }
  });
});

document.getElementById('pass').addEventListener("input", function(){
  document.getElementById("pass").style.borderColor = "#ccc";
});
document.getElementById('username').addEventListener("input", function(){
  document.getElementById("username").style.borderColor = "#ccc";
});

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

document.addEventListener('DOMContentLoaded', function() {
  var sensorRef = firebase.database().ref().child('sensorData');

  sensorRef.on("value", function(snapshot) {
    var sensorData = snapshot.val();
    var tableBody = document.getElementById('sensorDataBody');
    tableBody.innerHTML = ''; // Clear previous data

    for (var key in sensorData) {
      if (sensorData.hasOwnProperty(key)) {
        var data = sensorData[key];
        var row = tableBody.insertRow();
        row.insertCell().innerText = data.humidity + '%';
        row.insertCell().innerText = data.temperature + '°C';
        row.insertCell().innerText = data.heatIndex + '°C';
        row.insertCell().innerText = new Date(data.timestamp).toLocaleString();
        var pirCell = row.insertCell();
        pirCell.innerText = data.pir ? 'Motion detected' : 'No motion';
        pirCell.classList.add(data.pir ? 'true' : 'false');
      }
    }
  });
});
