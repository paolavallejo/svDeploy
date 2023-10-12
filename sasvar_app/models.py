from django.db import models

class Waste(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="sasvar_app/images")
    # 000000_ddmmaa.JPG número aleatorio de 6 dígitos_fecha
    img_name = models.CharField(max_length=50)
    # waste_type a futuro -> 0: Reciclable otros, 1: Reciclable papel, 2: Orgánico, 3: No aprovechable
    waste_type = models.IntegerField()
    # container_id a futuro -> 0: Orgánico, 1: No aprovechable, 2: Reciclable, 3: Papeles
    container_id = models.IntegerField()