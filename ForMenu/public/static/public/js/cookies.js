if (localStorage.cookie4Menu > 0) {
    document.getElementById('cookie1').style.display = 'none';
    $('html').css('overflow-y', 'scroll');
} else {
    $('html').css('overflow-y', 'hidden');
    document.getElementById('cookie1').style.display = 'block';
}

function controlcookies() {
    localStorage.cookie4Menu = (localStorage.cookie4Menu || 0);
    localStorage.cookie4Menu++;
    cookie1.style.display = 'none';
    $('html').css('overflow-y', 'scroll');
}




