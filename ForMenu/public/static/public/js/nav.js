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
    // cerrar menú de crear menu
    $('#activeCrearMenu').on('click', function () {
        $('#crearMenuDiv, .overlay2').addClass('active');
        $('html').css('overflow-y', 'hidden');
    });
    $('#closeCrearMenu, .overlay2').on('click', function () {
        $('#crearMenuDiv, .overlay2').removeClass('active');
        $('html').css('overflow-y', 'scroll');
    });
 });





/*
función que lee la url de un input type file y la coloca
como fondo de un div para poder ser previsualizada 
y mejorar la experiencia de usuario
*/
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#bluh').css("background", "linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.3) 50%, rgba(0, 0, 0, 0.7) 100%), url('" + e.target.result + "') no-repeat");
            $('#bluh').css("background-size", "cover");
            $('#bluh').css("background-position", "center");
        }
        reader.readAsDataURL(input.files[0]);
    }
}





/*
esto activa la función de arriba cuando detecta que el input 
ha sido modificado
*/
$("#id_imagen").change(function () {
    readURL(this);
});



$('#id_imagen').click(function () {
    $('.botonNuevaImagen, .alertaImagen').addClass('show');
});




$('#paso2, #paso2_2, #paso2_3').click(function () {
    $('.paso1, .paso3, .paso4').removeClass('active');
    $('.paso2').addClass('active');
});

$('#paso3, #paso3_2').click(function () {
    $('.paso1, .paso2, .paso4').removeClass('active');
    $('.paso3').addClass('active');
});

