
$(document).ready(function () {
    // progress bar para los menus
    $('#crearMenu, #modificarMenu').on('submit', function (event) {
        var formData = new FormData($('form')[0]);
        $.ajax({
            xhr: function () {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress', function (e) {
                    if (e.lengthComputable) {
                        var percent = Math.round((e.loaded / e.total) * 100);
                        $('#progressBarCrearMenu, #progressBarModificarMenu').attr('aria-valuenow', percent).css('width', percent + '%')
                    }
                });
                return xhr;
            },
            type: 'POST',
            url: '/manager/',
            data: formData,
            processData: false,
            contentType: false,
        });
    });


    // progress bar para la foto
    $('#cambiarFoto').on('submit', function (event) {
        var formData = new FormData($('form')[0]);
        $.ajax({
            xhr: function () {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress', function (e) {
                    if (e.lengthComputable) {
                        var percent = Math.round((e.loaded / e.total) * 100);
                        $('#progressBarFoto').attr('aria-valuenow', percent).css('width', percent + '%')
                    }
                });
                return xhr;
            },
            type: 'POST',
            url: '/manager/',
            data: formData,
            processData: false,
            contentType: false,
        });
    });


});



