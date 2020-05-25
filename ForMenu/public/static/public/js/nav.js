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
    $('#activeAjustes').on('click', function () {
        $('#ajustesDiv, .overlay2').addClass('active');
        $('html').css('overflow-y', 'hidden');
    });
    $('#closeAjustes, .overlay2').on('click', function () {
        $('#ajustesDiv, .overlay2').removeClass('active');
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


setTimeout(function () {
    $(".desaparecer5").addClass('active');
}, 3000);

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

$('#paso3, #paso3_2, #paso3_3').click(function () {
    $('.paso1, .paso2, .paso4').removeClass('active');
    $('.paso3').addClass('active');
});

$('#paso4, #paso4_2, #paso4_3').click(function () {
    $('.paso1, .paso2, .paso3').removeClass('active');
    $('.paso4').addClass('active');
});





/*
lunes 
*/
if ($('#no_lunes').is(':checked')) {
    $('.lunes').addClass('active');
} else {
    $('.lunes').removeClass('active');
}
$('#si_lunes, #no_lunes').click(function () {
    if ($('#no_lunes').is(':checked')) {
        $('.lunes').addClass('active');
    } else {
        $('.lunes').removeClass('active');
    }
});
if ($('#no_turno_lunes').is(':checked')) {
    $('.lunes').addClass('active2');
} else {
    $('.lunes').removeClass('active2');
}
$('#si_turno_lunes, #no_turno_lunes').click(function () {
    if ($('#no_turno_lunes').is(':checked')) {
        $('.lunes').removeClass('active2');
    } else {
        $('.lunes').addClass('active2');
    }
});
if ($('#no_turno_lunes').is(':checked')) {
    $('.lunes').removeClass('active2');
} else {
    $('.lunes').addClass('active2');
}



/*
martes 
*/
if ($('#no_martes').is(':checked')) {
    $('.martes').addClass('active');
} else {
    $('.martes').removeClass('active');
}
$('#si_martes, #no_martes').click(function () {
    if ($('#no_martes').is(':checked')) {
        $('.martes').addClass('active');
    } else {
        $('.martes').removeClass('active');
    }
});
if ($('#no_turno_martes').is(':checked')) {
    $('.martes').addClass('active2');
} else {
    $('.martes').removeClass('active2');
}
$('#si_turno_martes, #no_turno_martes').click(function () {
    if ($('#no_turno_martes').is(':checked')) {
        $('.martes').removeClass('active2');
    } else {
        $('.martes').addClass('active2');
    }
});
if ($('#no_turno_martes').is(':checked')) {
    $('.martes').removeClass('active2');
} else {
    $('.martes').addClass('active2');
}

/*
miercoles 
*/
if ($('#no_miercoles').is(':checked')) {
    $('.miercoles').addClass('active');
} else {
    $('.miercoles').removeClass('active');
}
$('#si_miercoles, #no_miercoles').click(function () {
    if ($('#no_miercoles').is(':checked')) {
        $('.miercoles').addClass('active');
    } else {
        $('.miercoles').removeClass('active');
    }
});
if ($('#no_turno_miercoles').is(':checked')) {
    $('.miercoles').addClass('active2');
} else {
    $('.miercoles').removeClass('active2');
}
$('#si_turno_miercoles, #no_turno_miercoles').click(function () {
    if ($('#no_turno_miercoles').is(':checked')) {
        $('.miercoles').removeClass('active2');
    } else {
        $('.miercoles').addClass('active2');
    }
});
if ($('#no_turno_miercoles').is(':checked')) {
    $('.miercoles').removeClass('active2');
} else {
    $('.miercoles').addClass('active2');
}


/*
jueves 
*/
if ($('#no_jueves').is(':checked')) {
    $('.jueves').addClass('active');
} else {
    $('.jueves').removeClass('active');
}
$('#si_jueves, #no_jueves').click(function () {
    if ($('#no_jueves').is(':checked')) {
        $('.jueves').addClass('active');
    } else {
        $('.jueves').removeClass('active');
    }
});
if ($('#no_turno_jueves').is(':checked')) {
    $('.jueves').addClass('active2');
} else {
    $('.jueves').removeClass('active2');
}
$('#si_turno_jueves, #no_turno_jueves').click(function () {
    if ($('#no_turno_jueves').is(':checked')) {
        $('.jueves').removeClass('active2');
    } else {
        $('.jueves').addClass('active2');
    }
});
if ($('#no_turno_jueves').is(':checked')) {
    $('.jueves').removeClass('active2');
} else {
    $('.jueves').addClass('active2');
}




/*
viernes 
*/
if ($('#no_viernes').is(':checked')) {
    $('.viernes').addClass('active');
} else {
    $('.viernes').removeClass('active');
}
$('#si_viernes, #no_viernes').click(function () {
    if ($('#no_viernes').is(':checked')) {
        $('.viernes').addClass('active');
    } else {
        $('.viernes').removeClass('active');
    }
});
if ($('#no_turno_viernes').is(':checked')) {
    $('.viernes').addClass('active2');
} else {
    $('.viernes').removeClass('active2');
}
$('#si_turno_viernes, #no_turno_viernes').click(function () {
    if ($('#no_turno_viernes').is(':checked')) {
        $('.viernes').removeClass('active2');
    } else {
        $('.viernes').addClass('active2');
    }
});
if ($('#no_turno_viernes').is(':checked')) {
    $('.viernes').removeClass('active2');
} else {
    $('.viernes').addClass('active2');
}



/*
sabado 
*/
if ($('#no_sabado').is(':checked')) {
    $('.sabado').addClass('active');
} else {
    $('.sabado').removeClass('active');
}
$('#si_sabado, #no_sabado').click(function () {
    if ($('#no_sabado').is(':checked')) {
        $('.sabado').addClass('active');
    } else {
        $('.sabado').removeClass('active');
    }
});
if ($('#no_turno_sabado').is(':checked')) {
    $('.sabado').addClass('active2');
} else {
    $('.sabado').removeClass('active2');
}
$('#si_turno_sabado, #no_turno_sabado').click(function () {
    if ($('#no_turno_sabado').is(':checked')) {
        $('.sabado').removeClass('active2');
    } else {
        $('.sabado').addClass('active2');
    }
});
if ($('#no_turno_sabado').is(':checked')) {
    $('.sabado').removeClass('active2');
} else {
    $('.sabado').addClass('active2');
}



/*
domingo 
*/
if ($('#no_domingo').is(':checked')) {
    $('.domingo').addClass('active');
} else {
    $('.domingo').removeClass('active');
}
$('#si_domingo, #no_domingo').click(function () {
    if ($('#no_domingo').is(':checked')) {
        $('.domingo').addClass('active');
    } else {
        $('.domingo').removeClass('active');
    }
});
if ($('#no_turno_domingo').is(':checked')) {
    $('.domingo').addClass('active2');
} else {
    $('.domingo').removeClass('active2');
}
$('#si_turno_domingo, #no_turno_domingo').click(function () {
    if ($('#no_turno_domingo').is(':checked')) {
        $('.domingo').removeClass('active2');
    } else {
        $('.domingo').addClass('active2');
    }
});
if ($('#no_turno_domingo').is(':checked')) {
    $('.domingo').removeClass('active2');
} else {
    $('.domingo').addClass('active2');
}
