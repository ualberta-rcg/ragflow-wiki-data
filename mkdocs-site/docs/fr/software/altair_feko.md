---
title: "Altair FEKO/fr"
tags:
  - software

keywords:
  []
---

= Introduction = 
[Altair FEKO](https://altairhyperworks.com/product/FEKO) est un logiciel d’électromagnétique computationnelle (CEM)  fréquemment utilisé dans les domaines des télécommunications, de l’automobile, de l’aérospatiale et de la défense.

= Licence = 
Nous sommes fournisseur d'hébergement pour FEKO; le logiciel est installé sur nos grappes, mais nous n'avons pas une licence générique fournissant l'accès à tous nos utilisateurs. Cependant, votre groupe de recherche a peut-être accès à un serveur de licence. 

== Configuration de votre fichier de licence == 
Le module FEKO cherche l'information en rapport avec la licence à différents endroits, dont votre répertoire personnel (*home*). Si vous avez votre propre serveur de licence, vous pouvez y accéder ainsi 

**`feko.lic`**
```lua
setenv("ALTAIR_LICENSE_PATH", "<port>@<hostname>")
```

Enregistrez ce fichier dans le répertoire <tt>$HOME/.licenses/</tt>. Les pare-feu des deux parties doivent être configurés; contactez le [soutien technique](technical-support-fr.md) à ce sujet.