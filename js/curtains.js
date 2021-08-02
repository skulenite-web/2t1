var curtains_active = true;

function moveVideo() {
    if (curtains_active) {
	    var height = document.getElementById('curtain-img').offsetHeight;
        //   console.log("translateY(" + height + "px);");
        document.getElementById('video').style.transform = "translateY(" + height*.23 + "px)";
    }
}

function toggleCurtains() {
    if (curtains_active) {
        document.getElementById('video').style.transform = "";
        curtains_active = false;
        document.getElementById('curtain-img').style.display = 'none';
        document.getElementById('curtain-toggle').innerHTML = 'Show Curtains';
    } else {
        curtains_active = true;
        moveVideo();
        document.getElementById('curtain-img').style.display = 'block';
        document.getElementById('curtain-toggle').innerHTML = 'Hide Curtains';
    }
}


window.onload = moveVideo;
window.onresize = moveVideo;

