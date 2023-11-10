from django.db import models

class Waste(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to="sasvar_app/images")
    img_name = models.CharField(max_length=50)
    # waste_type -> {'plastico','carton','mixto','papel','organico','aluminio','pet','vidrio','tetrapak'}
    waste_type = models.CharField(max_length=50)
    # container_id -> 0:Papel y cartón limpios,1:Empaques y envoltorios,2:Residuos no aprovechables,3:Orgánicos
    container_id = models.CharField(max_length=50)
    model_version = models.CharField(max_length=50, default='app_model_V0-T23')

    def __str__(self):
        return self.img_name