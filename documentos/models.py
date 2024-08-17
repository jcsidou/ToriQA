from django.db import models

class DocumentoPDF(models.Model):
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField(upload_to='pdfs/')
    texto_extraido = models.TextField()

    def __str__(self):
        return self.titulo
