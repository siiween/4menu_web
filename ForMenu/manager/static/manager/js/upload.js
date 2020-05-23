
$(document).ready(function () {
    // progress bar para los menus
    $('#crearMenu, #modificarMenu').on('submit', function (event) {
        var formData = new FormData($('form')[0]);
        // event.preventDefault();
        $.ajax({
            xhr: function () {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress', function (e) {
                    if (e.lengthComputable) {
                        console.log('Bytes Loaded : ' + e.loaded);
                        console.log('Total Size: ' + e.total);
                        console.log('Percentage Uploaded: ' + (e.loaded / e.total));
                        var percent = Math.round((e.total / e.loaded) * 100);
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
            success: function () { }
        });
    });


    // progress bar para la foto
    $('#cambiarFoto').on('submit', function (event) {
        var formData = new FormData($('form')[0]);
        // event.preventDefault();
        $.ajax({
            xhr: function () {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress', function (e) {
                    if (e.lengthComputable) {
                        var percent = Math.round((e.total / e.loaded) * 100);
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
            success: function () { }
        });
    });


});



