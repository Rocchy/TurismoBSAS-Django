from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    imagenes = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Sitio web", null=True, blank=True)
    created = models. DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    def __str__(self) :
        return self.title
    
    class Meta:
        verbose_name = "pueblo"
        verbose_name_plural = "pueblos"
