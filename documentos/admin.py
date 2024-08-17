from django.contrib import admin
from .models import DocumentoPDF
from PyPDF2 import PdfReader

@admin.register(DocumentoPDF)
class DocumentoPDFAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if obj.arquivo:
            pdf_reader = PdfReader(obj.arquivo)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text()
            obj.texto_extraido = text
        super().save_model(request, obj, form, change)
