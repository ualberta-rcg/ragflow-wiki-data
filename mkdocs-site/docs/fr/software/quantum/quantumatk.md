---
title: "QuantumATK/fr"
slug: "quantumatk"
lang: "fr"

source_wiki_title: "QuantumATK/fr"
source_hash: "27867a6fd220f5f31c4d3b5e23280263"
last_synced: "2026-05-02T23:50:34.269007+00:00"
last_processed: "2026-05-03T00:46:26.499505+00:00"

tags:
  []

keywords:
  - "QuantumATK"
  - "CMC"
  - "modélisation atomique"
  - "serveur de licence"
  - "licence"

questions:
  - "Qu'est-ce que le logiciel QuantumATK et quels sont ses principaux avantages pour la recherche et le développement ?"
  - "Comment les chercheurs peuvent-ils se procurer une licence valide pour utiliser QuantumATK sur les grappes de calcul ?"
  - "Quelles sont les étapes techniques requises pour configurer correctement le fichier de licence dans son répertoire personnel ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

# QuantumATK

[QuantumATK](https://www.synopsys.com/silicon/quantumatk.html) est une boîte à outils de modélisation atomique qui permet d'effectuer des simulations à grande échelle, produisant ainsi des résultats plus réalistes. Grâce à des méthodes de pointe et une plateforme conviviale, QuantumATK diminue le temps et les coûts en recherche et développement de semi-conducteurs et matériaux pour des domaines variés de haute technologie, par le perfectionnement des flux de travail dans le processus d'analyse de nouveaux matériaux.

# Licence

Nous sommes un fournisseur d'hébergement pour QuantumATK. Dans ce contexte, QuantumATK est installée sur nos grappes, mais nous n'avons pas de licence générique fournissant l'accès à tous nos utilisateurs. Cependant, plusieurs établissements, facultés et départements possèdent des licences qui peuvent être utilisées sur nos grappes.

Les chercheurs peuvent aussi acheter une licence auprès de [CMC](https://account.cmc.ca/en/WhatWeOffer/Products/CMC-00200-00368.aspx) pour une utilisation au Canada. Il est également possible d'utiliser QuantumATK sur nos grappes avec une licence achetée directement de [Synopsys](https://solvnet.synopsys.com/SmartKeys).

En ce qui a trait à l'aspect technique, nos nœuds de calcul doivent pouvoir communiquer avec votre serveur de licence. Si ce n'est déjà fait, notre équipe technique coordonnera ceci avec votre gestionnaire de licence; dans le cas de CMC, ce travail a déjà été effectué. Quand tout sera en place, vous pourrez charger le module QuantumATK qui localisera de lui-même la licence. En cas de difficulté, contactez le [soutien technique](../../support/technical_support.md).

## Configuration de votre fichier de licence

Le module QuantumATK cherche l'information en rapport avec la licence à différents endroits, dont votre répertoire personnel (`/home`). Si vous avez votre propre serveur de licence, vous pouvez y accéder avec le fichier suivant :

````bash title="quantumatk.lic"
SERVER <server> ANY <port>
USE_SERVER
````

Enregistrez ce fichier dans le répertoire `$HOME/.licenses/`, où `<server>` est votre serveur de licence et `<port>` est le numéro de port pour le serveur de licence. Les coupe-feu des deux parties doivent être configurés; pour ce faire, faites parvenir les renseignements sur le port de service et l'adresse IP de votre serveur de licence au [soutien technique](../../support/technical_support.md).

Si vous détenez une licence CMC, utilisez les valeurs suivantes dans votre fichier `quantumatk.lic` :

*   Fir : `SERVER 172.26.0.101 ANY 6053`
*   Narval : `SERVER 10.100.64.10 ANY 6053`
*   Rorqual : `SERVER 10.100.64.10 ANY 6053`
*   Trillium : `SERVER scinet-cmc ANY 6053`

Si vous ne pouvez pas obtenir la licence, faites une demande de soutien en écrivant à <cmcsupport@cmc.ca>.