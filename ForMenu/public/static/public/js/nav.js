$('#activeMenu, .overlay').click(function () {
    if ($('.navigation').hasClass('active')) {
        $('.navigation, .menuPalo1, .menuPalo2, .menuPalo3, .overlay').removeClass('active');
        $('html').css('overflow-y', 'scroll');
    } else {
        $('.navigation,.menuPalo1, .menuPalo2, .menuPalo3, .overlay').addClass('active');
        $('html').css('overflow-y', 'hidden');
    }
});



$(document).ready(function () {
    // cerrar menú de login
    $('#activeLogin').on('click', function () {
        $('#loginDiv, .overlay2').addClass('active');
        $('html').css('overflow-y', 'hidden');
    });
    $('#closeLogin, .overlay2').on('click', function () {
        $('#loginDiv, .overlay2').removeClass('active');
        $('html').css('overflow-y', 'scroll');
    });
    // cerrar menú de ayuda
    $('#activeAyuda').on('click', function () {
        $('#ayudaDiv, .overlay2').addClass('active');
        $('html').css('overflow-y', 'hidden');
    });
    $('#closeAyuda, .overlay2').on('click', function () {
        $('#ayudaDiv, .overlay2').removeClass('active');
        $('html').css('overflow-y', 'scroll');
    });
    // cerrar menú de alta
    $('#activeAlta, #activeAlta2').on('click', function () {
        $('#altaDiv, .overlay2').addClass('active');
        $('html').css('overflow-y', 'hidden');
    });
    $('#closeAlta, .overlay2').on('click', function () {
        $('#altaDiv, .overlay2').removeClass('active');
        $('html').css('overflow-y', 'scroll');
    });
 });


