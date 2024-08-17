from django.http import JsonResponse
from .models import DocumentoPDF
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
import torch

# Carregue o modelo para perguntas e respostas
model = SentenceTransformer('sentence-transformers/paraphrase-MiniLM-L6-v2')

def responder_pergunta(request):
    pergunta = request.GET.get('pergunta', '')
    respostas = []

    if pergunta:
        # Extraia todas as transcrições do banco de dados
        documentos = DocumentoPDF.objects.all()

        # Construa uma lista de textos extraídos
        textos = [doc.texto_extraido for doc in documentos]
        documentos_map = {doc.texto_extraido: doc.titulo for doc in documentos}

        # Codifique a pergunta e os textos
        pergunta_embedding = model.encode(pergunta, convert_to_tensor=True)
        textos_embeddings = model.encode(textos, convert_to_tensor=True)

        # Calcule as similaridades
        similaridades = util.pytorch_cos_sim(pergunta_embedding, textos_embeddings)

        # Ordene por similaridade e obtenha as melhores respostas
        similaridade_scores = list(enumerate(similaridades[0]))
        similaridade_scores.sort(key=lambda x: x[1], reverse=True)

        for idx, score in similaridade_scores[:5]:  # Retorne as 5 respostas mais relevantes
            respostas.append({
                'titulo': documentos_map[textos[idx]],
                'resposta': textos[idx],
                'similaridade': score.item()
            })

    return JsonResponse(respostas, safe=False)
