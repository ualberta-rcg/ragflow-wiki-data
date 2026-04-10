---
title: "Perl/fr"
tags:
  - software

keywords:
  []
---

## Description 
[Perl](http://www.perl.org) est un langage de programmation libre interprété qui possède plusieurs paquets développés au fil de plus de 25 années d'existence. Selon [cet article](http://www.cio.com/article/175450/You_Used_Perl_to_Write_WHAT_), ses forces sont la manipulation des chaînes de caractères, l'accès aux bases de données ainsi que sa portabilité. Ses faiblesses sont sa faible performance et la facilité avec laquelle on peut écrire du code illisible. En effet, par design, Perl offre plusieurs façons de réaliser la même tâche. Plusieurs programmeurs ont adopté ce langage et produisent du code très compact, mais souvent quasi illisible. 

## Charger l'interpréteur 
Perl est installé par défaut sur les serveurs de Calcul Canada. Voyez les versions disponibles avec

```bash
module spider perl
```

et chargez une version comme ceci

```bash
module load perl/5.36.1
```

## Installer les paquets
Plusieurs paquets Perl peuvent être installés via le site [Comprehensive Perl Archive Network](http://www.cpan.org/) avec l'outil <tt>cpan</tt>.
Assurez-vous d'abord que l'initialisation est correcte afin de pouvoir installer les paquets dans votre répertoire personnel (*home*). 

### Configuration initiale pour installer le module 
Lors de la première exécution de la commande <tt>cpan</tt>, vous devez décider si la configuration doit se faire de façon automatique. Répondez *yes*. 

L'utilitaire <tt>cpan</tt> demandera si vous voulez ajouter certaines variables d'environnement au fichier .bashrc; acceptez l'ajout. Entrez ensuite la commande <tt>quit</tt> via l'interface pour quitter <tt>cpan</tt>. Avant d'installer un module Perl, redémarrez l'interpréteur pour activer les nouveaux paramètres.

### Installation de paquets 
Lorsque la configuration initiale est terminée, vous pouvez installer n'importe lequel des 25&nbsp;000 paquets et plus offerts par CPAN, par exemple&nbsp;: