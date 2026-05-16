import os
from django.core.files import File
from artigos.models import Artigo

for obj in Artigo.objects.all():
    if obj.fotografia and obj.fotografia.name:

        try:
            local_path = obj.imagem.path
        except:
            continue

        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.fotografia.save(
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )
            print(f"Migrado: {obj.titulo}")