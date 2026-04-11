import os
import json
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from django.conf import settings
from portfolio.models import TFC, Licenciatura

ficheiro = os.path.join(settings.BASE_DIR, "data", "tfcs_2025.json")

with open(ficheiro, encoding="utf-8") as file:
    registos = json.load(file)

novos = 0

for reg in registos:
    titulo = reg.get("titulo")

    if not titulo:
        continue

    obj, criado = TFC.objects.get_or_create(
        titulo=titulo,
        defaults={
            "autor": reg.get("autor"),
            "orientador": reg.get("orientador"),  # string direta
            "ano": 2025,
            "descricao": reg.get("resumo"),       # mapeamento correto
        },
    )

    if criado:
        novos += 1
        print(f"Adicionado: {titulo}")
    else:
        print(f"Já existia: {titulo}")

print(f"\nTotal inseridos: {novos}")