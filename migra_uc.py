import os
from django.core.files import File
from portfolio.models import UnidadeCurricular

for obj in UnidadeCurricular.objects.all():
    if obj.imagem and obj.imagem.name:

        try:
            local_path = obj.imagem.path
        except:
            continue

        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )
            print(f"Migrado: {obj.nome}")