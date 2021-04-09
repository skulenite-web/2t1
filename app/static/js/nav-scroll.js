window.onscroll = function() {navScroll()};

function navScroll() {
    if (document.body.scrollTop > 150 || document.documentElement.scrollTop > 150) {
        document.getElementById("navlogo_img").style.width = '80px';
        document.getElementById("navlogo_img").style.opacity= '1';
    } else {
        document.getElementById("navlogo_img").style.width = '0px';
        document.getElementById("navlogo_img").style.opacity= '0';
    }
}
