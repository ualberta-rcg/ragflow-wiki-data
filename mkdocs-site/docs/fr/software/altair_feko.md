---
title: "Altair FEKO/fr"
slug: "altair_feko"
lang: "fr"

source_wiki_title: "Altair FEKO/fr"
source_hash: "aa6b9b3605d25c803188cefd2d17a339"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:13:07.246235+00:00"

tags:
  - software

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

# Introduction
[Altair FEKO](https://altairhyperworks.com/product/FEKO) est un logiciel d'électromagnétique computationnelle (CEM) fréquemment utilisé dans les domaines des télécommunications, de l'automobile, de l'aérospatiale et de la défense.

# Licence
Nous sommes fournisseur d'hébergement pour FEKO; le logiciel est installé sur nos grappes, mais nous n'avons pas une licence générique fournissant l'accès à tous nos utilisateurs. Cependant, votre groupe de recherche a peut-être accès à un serveur de licence.

## Configuration de votre fichier de licence
Le module FEKO cherche l'information en rapport avec la licence à différents endroits, dont votre répertoire personnel (*home*). Si vous avez votre propre serveur de licence, vous pouvez y accéder ainsi :

```lua title="feko.lic"
setenv("ALTAIR_LICENSE_PATH", "<port>@<hostname>")
```

Enregistrez ce fichier dans le répertoire `$HOME/.licenses/`. Les pare-feu des deux parties doivent être configurés; contactez le [soutien technique](technical-support-fr.md) à ce sujet.