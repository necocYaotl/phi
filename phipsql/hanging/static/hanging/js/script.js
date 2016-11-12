


// Get the modal
var modal1 = document.getElementById('welcomeOne');
var modal2 = document.getElementById('welcomeTwo');
var modal3 = document.getElementById('welcomeThree');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
window.onload = function() {
    modal1.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
modal1.onclick = function() {
    modal1.style.display = "none";
    modal2.style.display = "block";
}

modal2.onclick = function() {
    modal2.style.display = "none";
    modal3.style.display = "block";
}

modal3.onclick = function() {
    modal3.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
