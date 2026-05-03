---
title: "Galaxy/fr"
slug: "galaxy"
lang: "fr"

source_wiki_title: "Galaxy/fr"
source_hash: "f9bd6061fdef116a3b8348beda0b0684"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:40:54.324543+00:00"

tags:
  []

keywords:
  - "bio-informatique"
  - "plateforme web"
  - "recherche biomédicale"
  - "Galaxy"
  - "UseGalaxy Canada"

questions:
  - "Qu'est-ce que la plateforme Galaxy et à quel type de recherche est-elle principalement destinée ?"
  - "Comment s'authentifier sur UseGalaxy Canada et quel est l'espace de stockage alloué par défaut aux utilisateurs canadiens ?"
  - "Quelles sont les caractéristiques techniques de UseGalaxy Canada en matière de gestion, de prérequis et de support utilisateur ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Introduction

Galaxy est une plateforme web *open source* pour la recherche biomédicale traitant de grandes quantités de données. La plateforme rend la biologie computationnelle plus accessible, sans exiger une grande expérience en programmation ou en administration de systèmes. Conçue au départ pour la recherche en génomique, Galaxy s’adapte aujourd'hui à la plupart des domaines et sert de système de gestion du flux de travail en bio-informatique. [Cette liste de tutoriels](https://training.galaxyproject.org/) présente une bonne vue d’ensemble des possibilités qu’offre Galaxy.

!!! tip "Recommandation"
    La plateforme UseGalaxy est fortement recommandée pour le traitement de gros fichiers ou pour des tâches qui nécessitent plusieurs CPU ou GPU.

## Accéder directement à UseGalaxy Canada

Pour accéder à UseGalaxy Canada, simplement suivre le lien du site web [https://starthere.usegalaxy.ca](https://starthere.usegalaxy.ca), puis cliquer sur le bouton de connexion CILogon et sélectionner votre établissement pour vous authentifier. La plateforme détecte si vous êtes un utilisateur canadien et vous octroie automatiquement une allocation par défaut de 500 Go de stockage.

### Caractéristiques

*   **Serveur :** Beluga Cloud et Arbutus
*   **Configuration Galaxy :** Aucune (gérée par les administrateurs de UseGalaxy Canada)
*   **Connaissances Linux requises :** Aucune
*   **Gestion / Mises à jour :** Équipe UseGalaxy Canada
*   **Configuration du serveur :** Aucune
*   **Outils préinstallés :** Synchronisés avec UseGalaxy.eu
*   **Disponibilité des génomes de référence :** Oui (via CVMFS)
*   **Quota :** 500 Go par utilisateur

Le site [https://starthere.usegalaxy.ca](https://starthere.usegalaxy.ca) fournit toute l’information nécessaire concernant UseGalaxy.ca et Galaxy en général, de même qu’un formulaire si vous avez besoin d’assistance, voulez signaler un problème, ou encore faire installer de nouveaux outils ou bases de données.