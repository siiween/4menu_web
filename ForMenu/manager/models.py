# django
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# utils
from PIL import Image
import uuid


class Restaurante(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)


    nombre = models.CharField(
        'restaurant name',
        max_length=200,
    )


    telefono = models.CharField(
        max_length=17,
        blank=True,
    )

    ciudad = models.CharField(
        'Ciudad',
        max_length=50,
        default='Alicante'
    )

    pais = models.CharField(
        'País',
        max_length=50,
        default='España'
    )

    provincia = models.CharField(
        'Provincia',
        max_length=50,
        default='Alicante'
    )

    direccion = models.CharField(
        'Dirección',
        max_length=200,
        default='Calle España'
    )

    imagen = models.ImageField(upload_to='perfil', blank=True, null=True)
    

    is_active = models.BooleanField(
        'active',
        default=True
    )

    is_complete = models.BooleanField(
        'complete restaurant',
        default=False
    )

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created'
    )

    modified = models.DateTimeField(
        'Modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified'
    )


    def save(self, force_insert=False, force_update=False, using=None):
            # cuando se guarde una nueva entrada del model le
            # reducimos el tamaño a la imagen
        super().save()
        if self.imagen:
            img = Image.open(self.imagen.path)
            if img.height > 1500 or img.width > 1500:
                output_size = (1500, 1500)
                img.thumbnail((output_size), Image.ANTIALIAS)
                img.save(self.imagen.path)

    def __str__(self):
        return self.nombre




class Horario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    lunes = models.BooleanField(default=True)
    lunesTurno = models.BooleanField(default=False)
    lunesOpen = models.CharField(max_length=5, default="08:00")
    lunesClose = models.CharField(max_length=5, default="13:00")
    lunesOpen2 = models.CharField(max_length=5, default="15:00")
    lunesClose2 = models.CharField(max_length=5, default="20:00")

    martes = models.BooleanField(default=True)
    martesTurno = models.BooleanField(default=False)
    martesOpen = models.CharField(max_length=5, default="08:00")
    martesClose = models.CharField(max_length=5, default="13:00")
    martesOpen2 = models.CharField(max_length=5, default="15:00")
    martesClose2 = models.CharField(max_length=5, default="20:00")

    miercoles = models.BooleanField(default=True)
    miercolesTurno = models.BooleanField(default=False)
    miercolesOpen = models.CharField(max_length=5, default="08:00")
    miercolesClose = models.CharField(max_length=5, default="13:00")
    miercolesOpen2 = models.CharField(max_length=5, default="15:00")
    miercolesClose2 = models.CharField(max_length=5, default="20:00")

    jueves = models.BooleanField(default=True)
    juevesTurno = models.BooleanField(default=False)
    juevesOpen = models.CharField(max_length=5, default="08:00")
    juevesClose = models.CharField(max_length=5, default="13:00")
    juevesOpen2 = models.CharField(max_length=5, default="15:00")
    juevesClose2 = models.CharField(max_length=5, default="20:00")

    viernes = models.BooleanField(default=True)
    viernesTurno = models.BooleanField(default=False)
    viernesOpen = models.CharField(max_length=5, default="08:00")
    viernesClose = models.CharField(max_length=5, default="13:00")
    viernesOpen2 = models.CharField(max_length=5, default="15:00")
    viernesClose2 = models.CharField(max_length=5, default="20:00")

    sabado = models.BooleanField(default=True)
    sabadoTurno = models.BooleanField(default=False)
    sabadoOpen = models.CharField(max_length=5, default="08:00")
    sabadoClose = models.CharField(max_length=5, default="13:00")
    sabadoOpen2 = models.CharField(max_length=5, default="15:00")
    sabadoClose2 = models.CharField(max_length=5, default="20:00")

    domingo = models.BooleanField(default=True)
    domingoTurno = models.BooleanField(default=False)
    domingoOpen = models.CharField(max_length=5, default="08:00")
    domingoClose = models.CharField(max_length=5, default="13:00")
    domingoOpen2 = models.CharField(max_length=5, default="15:00")
    domingoClose2 = models.CharField(max_length=5, default="20:00")


    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created'
    )

    modified = models.DateTimeField(
        'Modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified'
    )

    def __str__(self):
        return self.user.username





class Menu(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    qr = models.ImageField(upload_to='QR')
    pdf = models.FileField(upload_to='PDF')
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created'
    )

    modified = models.DateTimeField(
        'Modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified'
    )

    def __str__(self):
        return self.nombre
