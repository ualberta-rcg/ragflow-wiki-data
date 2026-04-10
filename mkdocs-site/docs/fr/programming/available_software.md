---
title: "Available software/fr"
tags:
  []

keywords:
  []
---

__FORCETOC__

Le tableau présenté ci-dessous montre la liste des logiciels disponibles sur la plateforme nationale. Cette liste est modifiée à l'ajout de tout nouveau logiciel. Pour demander l'installation ou la mise à jour d'un logiciel ou d'une bibliothèque, communiquez avec le [soutien technique](technical-support-fr.md). Pour utiliser notre environnement logiciel sur votre propre ordinateur, voyez [notre page wiki CVMFS](accessing-cvmfs-fr.md).

## Notes
Pour utiliser un logiciel qui n'est pas déjà installé par défaut, vous devez charger le module qui s'applique. Pour plus d'information sur comment utiliser le système de modules Lmod, consultez [ Utiliser des modules](-utiliser-des-modules.md). Prenez note que certains modules prérequis sont chargés par défaut. 

<b>Points à retenir à propos des logiciels disponibles</b>

* La plupart des modules Python ne sont pas installés en tant que modules (Lmod), mais en tant que [paquets binaires](available_python_wheels.md) (<i>wheels</i>) localisés sous `/cvmfs/soft.computecanada.ca/custom/python/wheelhouse/`; [TensorFlow](tensorflow-fr.md) en est un exemple. Voyez la page [Python](python-fr.md) pour des détails sur comment lister les paquets Python et les installer.
* De même, la plupart des paquets R et Perl ne sont pas installés. Nous vous recommandons de les installer dans votre environnement personnel ou dans celui de votre groupe. Voyez les pages [R](r-fr.md) et [Perl](perl-fr.md) pour des détails sur l'installation des paquets.
* Voyez la page [Algèbre symbolique](symbolic-algebra-software-fr.md) où il est question de SageMath.
* Notez que [Docker](https://www.docker.com/) n'est pas disponible sur nos grappes, mais que [Apptainer](apptainer-fr.md) peut être utilisé en chargeant le module `apptainer`. Pour convertir les contenants Docker, consultez [la documentation Apptainer](https://apptainer.org/docs/).
* Certains logiciels listés dans le tableau ci-dessous sont sous licence et donc non accessibles directement; vous pouvez en demander l'accès au besoin. En tentant de charger le module d'un tel logiciel, vous recevrez les consignes sur comment en obtenir l'accès.
* La plupart des paquets listés se trouvent sur toutes nos grappes. Certains cependant ne sont disponibles que sur un site en particulier en raison des restrictions liées à l'octroi des licences; voir [Modules disponibles uniquement sur certaines grappes](available-software-fr#modules_disponibles_uniquement_sur_certaines_grappes.md) ci-dessous.
* Les paquets listés sont disponibles dans un ou plusieurs de nos environnements logiciels standards. Dans certains cas peu fréquents, vous devrez charger un environnement logiciel différent pour avoir accès à un paquet en particulier; voyez [Environnements logiciels standards](standard-software-environments-fr.md). 
* Plusieurs paquets reliés au système d’exploitation comme [Autotools](autotools-fr.md), [Make](make-fr.md) et [Git](git.md) ne sont pas installés en tant que modules, mais font partie de l'environnement par défaut; ils ne paraissent pas dans le tableau.

## Modules disponibles sur toutes les grappes
Le tableau suivant liste les logiciels pour lesquels un module d'environnement est disponible. Certains modules peuvent être chargés avec la commande `module load` alors que d'autres nécessitent des conditions particulières.
Dans la colonne <i>Description</i>, cliquez sur <i>Expand</i> pour connaître les prérequis et lire une description sommaire du logiciel (en anglais).
Un lien dans la colonne <i>Documentation</i> conduit à la documentation spécifique sur le logiciel.
Pour lister les logiciels selon leur type, effectuez un tri en cliquant sur l'en-tête de la colonne <i>Type</i>.

Les types sont&nbsp;:
* ai (intelligence artificielle)
* bio (biologie, bio-informatique)
* chem (chimie)
* geo (sciences de la Terre)
* io (input/output)
* math (mathématiques)
* mpi ([MPI](mpi-fr.md))
* phys (physique et génie)
* tools (langages et bibliothèques)
* vis ([visualisation](visualization-fr.md)).

Les logiciels pour les architectures obsolètes se trouvent respectivement dans [AVX](modules_avx.md) et [SSE3](modules_sse3.md).

<tabs>
<tab name="AVX512 (Fir, Nibi, Rorqual, Trillium, Killarney, tamIA, Vulcan)">

</tab>
<tab name="AVX2 (Narval)">

</tab>
</tabs>

## Modules disponibles uniquement sur certaines grappes
La plupart des applications sont installées dans CVMFS, un système de fichiers qui facilite la gestion du grand nombre des paquets que nous offrons. Cependant, d'autres paquets ne sont installés que dans certains sites, principalement pour des raisons de licence.

{| class="wikitable"
|+ style="text-align: left;" |Logiciels installés localement
|-
! scope="col" |Module !! scope="col" | Type !! scope="col" | Documentation !! scope="col" | Grappe !! scope="col" | Description
|-
| adf/2016.106 ||rowspan="6"| chem ||rowspan="6"| [ADF](adf.md) ||rowspan="6"| Nibi ||rowspan="6"| Amsterdam Density Functional Modeling Suite; recherche en chimie computationnelle
|-
| adf/2017.207  
|-
| adf/2018.104  
|-
| adf/2019.305
|-
| ams/2020.102 || chem || [AMS](ams.md) || Nibi ||  Amsterdam Modeling Suite  
|-
| amber/16 || chem || [AMBER](amber.md) || Nibi || ensemble d'applications pour effectuer des simulations en dynamique moléculaire
|-
| dirac/16.0  ||rowspan="2"| phys ||rowspan="2"|  ||rowspan="2"|  Cedar ||rowspan="2"| Direct Iterative Relativistic All-electron Calculations; calcule les propriétés moléculaires avec des méthodes de chimie quantique relativiste (site web&nbsp;: http://diracprogram.org)
|-
| dirac/17.0  
|-
| galaxy/20.01 || bio || || Cedar || plateforme d'analyse, de gestion et d'archivage  des données qui rend la bio-informatique accessible aux chercheurs sans compétences en programmation ou en administration de systèmes. Sur Cedar, chaque groupe peut avoir une instance de Galaxy qui est exécutée dans un compte partagé; ce compte est créé par une ou un administrateur de système. Contactez le [soutien technique](technical-support-fr.md).  (site web&nbsp;: https://usegalaxy.org/)
|-
| gaussian/g03.d01 ||rowspan="4"| chem ||rowspan="4"| [Gaussian](gaussian.md) ||rowspan="4"| Nibi ||rowspan="4"| paquet logiciel d'usage général en chimie computationnelle  (site web&nbsp;:http://gaussian.com/)
|-
| gaussian/g09.e01   
|-
| gaussian/g16.b01  
|-
| gaussian/g16.c01  
|-
| gaussian/g03.d01 ||rowspan="6"| chem ||rowspan="6"| [Gaussian](gaussian.md) ||rowspan="6"| Fir||rowspan="6"| paquet logiciel d'usage général en chimie computationnelle  (site web&nbsp;:http://gaussian.com/)
|-
| gaussian/g09.b01  
|-
| gaussian/g09.e01  
|-
| gaussian/g16.a03  
|-
| gaussian/g16.b01  
|-
| gaussian/g16.c01  
|-
| gbrowse/2.56 || bio || [GBrowse](gbrowse.md) || Cedar || outil composé d’une base de données combinée à des pages web interactives pour manipuler et visualiser des données génomiques (site web&nbsp;:http://gmod.org/wiki/GBrowse)
|-
| sas/9.4 || math||  || Cedar || suite logicielle développée par le <i>SAS Institute for advanced analytics</i> pour l'analyse multivariée, l'intelligence d'affaires, la gestion des données et l'analyse prédictive. Sur Cedar, une licence de l'<i>Alberta School of Business</i> permet l'utilisation de SAS à quiconque est admissible. (site web&nbsp;:https://www.sas.com/en_ca/home.html0)
|-
| TPP/5.1.0 || bio ||  || Cedar || Trans-Proteomic Pipeline (TPP) est une collection d'outils intégrés développée au SPC pour l'analyse de données protéomiques MS/MS. Cedar offre aussi sur demande une interface web TPP (tpp_gui) par groupe. 
|}