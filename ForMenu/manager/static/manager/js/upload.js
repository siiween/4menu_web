
$(document).ready(function () {
    // progress bar para crear menus
    $('#crearMenu').on('submit', function (event) {
        //event.preventDefault();
        var formData = new FormData($('#crearMenu')[0]);
        $.ajax({
            xhr: function () {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress', function (e) {
                    if (e.lengthComputable) {
                        console.log('Bytes Loaded : ' + e.loaded);
                        console.log('Total Size: ' + e.total);
                        console.log('Percentage Uploaded: ' + (e.loaded / e.total));
                        var percent = Math.round((e.loaded / e.total) * 100);
                        $('#progressBarCrearMenu').attr('aria-valuenow', percent).css('width', percent + '%')
                    }
                });
                return xhr;
            },
            type: 'POST',
            url: '/manager/',
            data: formData,
            processData: false,
            contentType: false,
            success: function () {}
        });
    });

    

    // progress bar para modificar menus
    $('#modificarMenu').on('submit', function (event) {
        //event.preventDefault();
        var formData = new FormData($('#modificarMenu')[0]);
        $.ajax({
            xhr: function () {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress', function (e) {
                    if (e.lengthComputable) {
                        console.log('Bytes Loaded : ' + e.loaded);
                        console.log('Total Size: ' + e.total);
                        console.log('Percentage Uploaded: ' + (e.loaded / e.total));
                        var percent = Math.round((e.loaded / e.total) * 100);
                        $('#progressBarModificarMenu').attr('aria-valuenow', percent).css('width', percent + '%')
                    }
                });
                return xhr;
            },
            type: 'POST',
            url: '/manager/',
            data: formData,
            processData: false,
            contentType: false,
            success: function () {}
        });
    });

    




    // progress bar para la foto
   $('#cambiarFoto').on('submit', function (event) {
       //event.preventDefault();
       var formData = new FormData($('#cambiarFoto')[0]);
       $.ajax({
           xhr: function () {
               var xhr = new window.XMLHttpRequest();
               xhr.upload.addEventListener('progress', function (e) {
                   if (e.lengthComputable) {
                       console.log('Bytes Loaded : ' + e.loaded);
                       console.log('Total Size: ' + e.total);
                       console.log('Percentage Uploaded: ' + (e.loaded / e.total));
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
           success: function () {}
       });
   });



});



