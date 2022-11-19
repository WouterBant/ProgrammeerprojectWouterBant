// This script make it possible to toggle between light- and darkmode

var icon = document.getElementById("icon");

// changes the icon
icon.onclick = function() {
    document.body.classList.toggle("dark-theme");
    if(document.body.classList.contains("dark-theme")){
        localStorage.setItem('dark-theme',"yes");
        icon.src = moon;
    }else{
        localStorage.setItem('dark-theme',"no");
        icon.src = sun;
    }
}

// sets the theme
function load1(){
    if(localStorage.getItem('dark-theme')) {
        const back = localStorage.getItem('dark-theme');
        if (back === "yes"){
            document.body.classList.toggle("dark-theme");
            icon.src = moon;
        }
    }
}