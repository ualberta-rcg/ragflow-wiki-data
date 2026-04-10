---
title: "Uv/fr"
tags:
  []

keywords:
  []
---

uv est un gestionnaire de paquets et de projets Python extrêmement rapide, écrit en Rust. Son utilisation pourrait fonctionner, mais vous risquez de rencontrer des problèmes.

Voici quelques difficultés que vous pourriez rencontrer&nbsp;:
* certains paquets sont distribués dans un format incompatible avec nos grappes, mais uv tente quand même de les installer;
* uv est incapable de trouver les paquets Python fournis par les modules chargés;
* uv peut rapidement saturer le quota de votre répertoire /home, car il stocke un très grand nombre de fichiers dans la cache.

=Installation de paquets Python=
Pour installer des paquets sur nos grappes, utilisez `pip`; voir [Python](python-fr.md).

Assurez-vous d'avoir au moins la version `pip>=25.0`.

```bash
pip install --no-index --upgrade pip
```

<span id="Troubleshooting"></span>
=Dépannage=

## Vider la cache
Pour vider la cache, la commande est

```bash
uv cache clean
```

Par la suite, pour ne pas utiliser la cache, la commande est `uv --no-cache`.