---
title: "Data protection, privacy, and confidentiality/fr"
slug: "data_protection__privacy__and_confidentiality"
lang: "fr"

source_wiki_title: "Data protection, privacy, and confidentiality/fr"
source_hash: "d419fcd0b06ce9db49f896d17040465c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:48:20.161414+00:00"

tags:
  []

keywords:
  - "élévation de privilège"
  - "sécurité des données"
  - "chiffrer"
  - "correctifs"
  - "intrusion"
  - "grappes"
  - "sauvegarde"
  - "sécurité"
  - "données sensibles"
  - "listes de diffusion CVE"
  - "mesures de sécurité"
  - "contrôle des accès"
  - "confidentialité"
  - "GNU Privacy Guard"
  - "infrastructure partagée"

questions:
  - "Comment les données personnelles ou sensibles sont-elles gérées et quelles sont les responsabilités des chercheurs à cet égard ?"
  - "Quelles mesures de duplication et de sauvegarde sont mises en place pour protéger les données contre les défaillances matérielles selon les différents systèmes de fichiers ?"
  - "Comment l'infrastructure protège-t-elle les données contre les accès non autorisés, tant au niveau physique que logiciel ?"
  - "Quelle est la nature de l'infrastructure des grappes et quel risque cela implique-t-il ?"
  - "Que doit faire un utilisateur si ses données exigent un niveau de sécurité très élevé ?"
  - "Quel outil de chiffrement est spécifiquement mis à disposition sur les grappes ?"
  - "Comment l'équipe technique utilise-t-elle les listes de diffusion CVE pour prévenir les élévations de privilèges ?"
  - "Quels types de comportements sont examinés pour détecter une potentielle intrusion dans le système ?"
  - "Pourquoi des mesures de sécurité plus strictes sont-elles imposées aux comptes du personnel disposant d'accès privilégiés ?"
  - "Quelle est la nature de l'infrastructure des grappes et quel risque cela implique-t-il ?"
  - "Que doit faire un utilisateur si ses données exigent un niveau de sécurité très élevé ?"
  - "Quel outil de chiffrement est spécifiquement mis à disposition sur les grappes ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Traitement des données personnelles, privées ou sensibles (par exemple, les données de recherche clinique sur les humains)

Aucune de nos ressources n’est présentement assignée au traitement des données sensibles.

Toutes nos ressources sont gérées selon les meilleures pratiques pour la recherche universitaire et nous déployons des efforts considérables à l’intégrité, la confidentialité et la disponibilité des données. Aucune de nos ressources n’est cependant formellement certifiée pour respecter les exigences de sécurité et de confidentialité pouvant s’appliquer à certains ensembles de données. En général, plusieurs personnes se partagent nos ressources, ce qui comprend les réseaux, les nœuds et les espaces de mémoire et les données qui y sont consignées peuvent ne pas être chiffrées. Nous offrons les fonctionnalités standards Linux pour la ségrégation des systèmes de fichiers et le contrôle des accès aux fichiers et répertoires et nos administrateurs de systèmes ont accès à tout ce matériel au besoin ou avec l’autorisation des propriétaires.

La protection de la confidentialité des données est de la responsabilité des chercheurs et chercheuses. À ce titre, nous vous invitons à [prendre connaissance de nos politiques.](https://alliancecan.ca/fr/politiques)

Vous pouvez [contacter notre équipe de soutien technique](technical-support.md) pour de l’assistance sur la gestion de vos données sensibles ainsi que pour des conseils sur le contrôle des accès, le chiffrement, le stockage et la transmission de vos données.

## Défaillance du matériel

Notre principe de base est de disposer d’un certain niveau de duplication pour la plupart des systèmes de fichiers, selon le niveau de risque que présente le matériel, par exemple
* il n’y a aucune forme de duplication des systèmes de fichiers stockés localement sur les nœuds de calcul;
* il n’y a aucune copie de sauvegarde des systèmes de fichiers /scratch, mais ils sont configurés pour être protégés contre les défaillances de plusieurs disques;
* il y a une copie de sauvegarde périodique des systèmes de fichiers /project et /home qui sont en plus protégés contre les défaillances de plusieurs disques;
* une copie est faite sur ruban des systèmes de fichiers de l’espace de stockage /nearline.

## Accès non autorisé

Les accès non autorisés pourraient se produire principalement via le matériel ou les logiciels.

Pour ce qui est du matériel, l'infrastructure physique n'est accessible que par le personnel autorisé. Tout équipement de stockage qui doit être retiré par suite d’une défaillance est soit détruit, soit chiffré ou effacé avant d'être retourné au fournisseur pour être remplacé.

L’accès par logiciel aux systèmes de fichiers de nos grappes est protégé par des permissions POSIX et ACL standards. À chaque fichier sont associés un propriétaire et un groupe. Le groupe associé à un fichier est soit un utilisateur, soit un projet de recherche. Les permissions par défaut sont telles que les nouveaux fichiers qui sont créés sont accessibles en écriture par le propriétaire et en lecture par le groupe. Le groupe par défaut associé à un fichier peut dépendre de l’endroit où se trouve le fichier dans le système de fichiers. Le propriétaire du fichier doit s’assurer que ce dernier appartient au bon groupe et que les permissions d’accès appropriées soient définies.

Si les permissions d’accès à un fichier sont correctement définies, un accès non autorisé ne peut avoir lieu que par élévation de privilège (piratage). Pour contrer ceci, notre équipe technique fait le suivi des listes de diffusion CVE (*Common Vulnerabilities and Exposures*) et applique les correctifs requis. Nous examinons aussi les comportements anormaux qui seraient susceptibles d’indiquer une intrusion, en plus d’imposer des mesures de sécurité plus strictes pour les comptes de notre personnel qui dispose d'accès privilégiés par rapport aux utilisateurs réguliers.

!!! warning "Chiffrement des données sensibles"
    Il ne faut pas oublier que nos grappes font partie d’une infrastructure partagée. Même si nous prenons toutes les précautions pour réduire le risque d’accès non autorisés, la possibilité est toujours présente. Si vos données nécessitent un haut niveau de sécurité, il serait avisé de les chiffrer à l'aide d'un outil comme [GNU Privacy Guard](https://www.gnupg.org/) qui se trouve sur nos grappes sous le nom de binaire `gpg`.