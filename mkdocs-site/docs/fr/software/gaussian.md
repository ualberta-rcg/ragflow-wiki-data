---
title: "Gaussian/fr"
slug: "gaussian"
lang: "fr"

source_wiki_title: "Gaussian/fr"
source_hash: "e1ddad42a307606a959fdde216d90767"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T07:34:10.801772+00:00"

tags:
  - software
  - computationalchemistry

keywords:
  - "chimie computationnelle"
  - "répertoire"
  - "fréquence analytique"
  - "redémarrer les calculs"
  - "fichier .rwf"
  - "nœud de calcul"
  - "script G16"
  - "messages d'erreur"
  - "mémoire partagée"
  - "fichier rwf"
  - "redémarrer une tâche"
  - "ordonnanceur Slurm"
  - "optimisation géométrique"
  - "tâches interactives"
  - "G16"
  - "fichier chk"
  - "redémarrer la tâche"
  - "NBO"
  - "Gaussian"
  - "fichiers d'exécution"

questions:
  - "Quelles sont les restrictions techniques liées à l'exécution en parallèle de Gaussian sur les grappes Nibi et Fir ?"
  - "Quelles sont les conditions de licence qu'un utilisateur doit accepter par courriel pour obtenir l'accès à l'application ?"
  - "Quelles sont les recommandations concernant l'allocation des ressources (comme le nombre de CPU) et la gestion des fichiers d'exécution lors de la soumission d'une tâche ?"
  - "Quelles sont les différences entre l'utilisation des commandes G16 et g16 concernant la gestion et le stockage des fichiers temporaires d'exécution ?"
  - "Quelle est la procédure recommandée pour lancer une tâche Gaussian interactive à des fins de test sans utiliser le nœud de connexion ?"
  - "Quels fichiers spécifiques (tels que .rwf ou .chk) sont nécessaires pour redémarrer une tâche Gaussian interrompue, et à quels types de calculs s'appliquent-ils ?"
  - "Quels types de fichiers d'exécution par défaut sont créés avec l'option G16 et dans quel répertoire sont-ils sauvegardés ?"
  - "Dans quelles circonstances les fichiers d'exécution demeurent-ils dans le répertoire de travail ?"
  - "Quel fichier spécifique permet de récupérer et de redémarrer une tâche ultérieurement ?"
  - "À partir de quel fichier est-il possible de redémarrer une optimisation géométrique ?"
  - "Quelle caractéristique commune partagent les calculs pouvant être redémarrés avec le fichier rwf ?"
  - "Quels exemples précis de calculs de fréquences, de propriétés ou d'énergies sont mentionnés comme compatibles avec une reprise via le fichier rwf ?"
  - "Comment doit-on configurer le fichier d'entrée pour redémarrer une tâche à partir d'un fichier rwf ?"
  - "Où peut-on trouver des exemples de fichiers d'entrée et de scripts pour les différentes versions du logiciel ?"
  - "Dans quelles versions spécifiques du logiciel les outils NBO6 et NBO7 sont-ils respectivement inclus ?"
  - "Comment doit-on configurer le fichier d'entrée pour redémarrer une tâche à partir d'un fichier rwf ?"
  - "Où peut-on trouver des exemples de fichiers d'entrée et de scripts pour les différentes versions du logiciel ?"
  - "Dans quelles versions spécifiques du logiciel les outils NBO6 et NBO7 sont-ils respectivement inclus ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Voir aussi la [page sur les messages d'erreur de Gaussian](chemistry/gaussian_error_messages.md).*

Gaussian est une application de chimie computationnelle produite par [Gaussian, Inc.](http://gaussian.com/)

## Limites

Gaussian est présentement disponible uniquement sur [Nibi](../clusters/nibi.md) et [Fir](fir.md).

Nos systèmes nationaux ne prennent pas en charge [l'exécution en parallèle grappe/réseau (*parallélisme Linda*)](https://gaussian.com/running/?tabid=4), mais uniquement
[l'exécution en parallèle avec multiprocesseur à mémoire partagée](https://gaussian.com/running/?tabid=4).
Ainsi, une tâche Gaussian ne peut pas utiliser plus d'un nœud de calcul.

## Licence

Pour utiliser l'application, vous devez accepter certaines conditions. Copiez les énoncés suivants dans un courriel et faites-le parvenir au [soutien technique](../support/technical_support.md).
1.  Je ne fais pas partie d'un groupe de recherche qui développe une application concurrente.
2.  Je ne copierai pas Gaussian ni ne rendrai l'application disponible à un tiers.
3.  Je [reconnaîtrai la collaboration de l'Alliance](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/reconnaissance-de-l'alliance) dans toute publication.
4.  J'informerai l'Alliance de tout changement concernant les précédentes conditions.
Si vous êtes un utilisateur parrainé par un chercheur principal, celui-ci doit aussi nous avoir fait parvenir une copie des mêmes énoncés.

Nous pourrons alors vous donner accès à Gaussian.

## Utiliser Gaussian sur Fir et Nibi
Le module `gaussian` est installé sur [Nibi](../clusters/nibi.md) et [Fir](fir.md). Pour connaître les versions disponibles, utiliser la commande `module spider` comme suit :

```bash
module spider gaussian
```

Pour les commandes qui s'appliquent aux modules, voir [Utiliser des modules](../programming/utiliser_des_modules.md).

### Soumettre des tâches
Les grappes nationales utilisent l'ordonnanceur Slurm; pour des renseignements sur la soumission d'une tâche, consultez [Exécuter des tâches](../running-jobs/running_jobs.md).

Puisque seule la version avec multiprocesseur à mémoire partagée de Gaussian est prise en charge, vos tâches ne peuvent utiliser qu'un seul nœud et jusqu'au maximum de cœurs par nœud. Cependant, en raison de la scalabilité de Gaussian, nous vous recommandons *de ne pas utiliser plus de 32 CPU par tâche si vous ne pouvez pas prouver qu'ils seront bien utilisés.* Nibi et Fir ont 192 CPU par nœud; nous vous demandons de ne pas utiliser des nœuds entiers puisque ce ne serait pas efficace. Si vos tâches nécessitent plus de mémoire que ce que vous pouvez obtenir sur un seul nœud, sachez que chacune des grappes offre quelques nœuds avec plus de mémoire. Pour connaître le nombre de nœuds sur une grappe et leur capacité, consultez [Fir](fir.md#caracteristiques_des_noeuds) et [Nibi](../clusters/nibi.md#caracteristiques_des_noeuds).

En plus du fichier d'entrée *name.com*, vous devez préparer un script décrivant les ressources de calcul pour la tâche; ce script doit être dans le même répertoire que le fichier d'entrée.

Il y a deux options pour les tâches Gaussian, selon la localisation des fichiers d'exécution par défaut et la taille de la tâche :

#### Option 1 : G16 (G09, G03)

Avec cette option, les fichiers d'exécution par défaut (unnamed .rwf, .inp, .d2e, .int, .skr) sont enregistrés dans /scratch/username/jobid/ et demeurent dans ce répertoire si la tâche n'est pas terminée ou si elle a échoué. Le fichier .rwf peut y être récupéré pour redémarrer la tâche plus tard.

Voici un exemple d'un script G16.

Remarquez que pour assurer la cohérence, les fichiers portent le même nom avec des extensions différentes (name.sh, name.com, name.log).
```bash title="mysub.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --mem=32G             # memory, roughly 2 times %mem defined in the input name.com file
#SBATCH --time=02-00:00       # expect run time (DD-HH:MM)
#SBATCH --cpus-per-task=32    # No. of cpus for the job as defined by %nprocs in the name.com file
module load gaussian/g16.c01
G16 name.com            # G16 command, input: name.com, output: name.log
```
Pour utiliser Gaussian 09 ou Gaussian 03, remplacez gaussian/g16.c01 par gaussian/g09.e01 ou gaussian/g03.d01 et remplacez G16 par G09 ou G03. Modifiez --mem, --time, --cpus-per-task selon vos besoins en ressources de calcul.

#### Option 2 : g16 (g09, g03)

Avec cette option, les fichiers d'exécution par défaut (unnamed .rwf, .inp, .d2e, .int, .skr) sont enregistrés temporairement dans $SLURM_TMPDIR (/localscratch/username.jobid.0/) dans le nœud de calcul où la tâche devait être exécutée. Les tâches seront exécutées plus rapidement si vous utilisez /localscratch. L'ordonnanceur supprime les fichiers quand la tâche est terminée que ce soit avec ou sans succès. Si vous voulez utiliser le fichier .rwf pour redémarrer la tâche plus tard, vous devez spécifier et nommer votre propre fichier .rwf explicitement dans le fichier d'entrée de Gaussian.

/localscratch est d'environ 3To, partagés par toutes les tâches exécutées sur le même nœud. Si la taille de vos fichiers est semblable ou plus grande, utilisez plutôt l'option G16 (G09, G03).

Voici un exemple d'un script g16.
```bash title="mysub.sh"
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --mem=32G             # memory, roughly 2 times %mem defined in the input name.com file
#SBATCH --time=02-00:00       # expect run time (DD-HH:MM)
#SBATCH --cpus-per-task=32    # No. of cpus for the job as defined by %nprocs in the name.com file
module load gaussian/g16.c01
g16 < name.com >& name.log              # g16 command, input: name.com, output: name.log
```

#### Soumettez la tâche
```bash
sbatch mysub.sh
```

### Tâches interactives
Il est possible d'exécuter une tâche Gaussian interactive à des fins de test. Il n'est cependant pas indiqué d'exécuter une tâche Gaussian interactive sur un nœud de connexion. Ouvrez plutôt une session interactive sur un nœud de calcul avec `salloc` pour une durée d'une heure, avec 8 CPUs et 10Go de mémoire.
```bash
salloc --time=1:0:0 --cpus-per-task=8 --mem=10g
```

Puis, utilisez
```bash
module load gaussian/g16.c01
G16 g16_test2.com    # G16 saves runtime file (.rwf etc.) to /scratch/yourid/93288/
```

ou
```bash
module load gaussian/g16.c01
g16 < g16_test2.com >& g16_test2.log &   # g16 saves runtime file to /localscratch/yourid/
```

### Redémarrer une tâche
Une tâche Gaussian peut être redémarrée à partir du fichier `rwf` précédent.

Comme d'habitude, l'optimisation géométrique peut être redémarrée à partir du fichier `chk`.
Avec le fichier `rwf`, vous pouvez redémarrer les calculs qui se font en une étape, par exemple les calculs de fréquence analytique incluant des propriétés comme ROA et VCD avec ONIOM; les calculs CCSD et EOM-CCSD; NMR; Polar=OptRot; et les énergies CID, CISD, CCD, QCISD et BD.

Pour redémarrer une tâche à partir du fichier `rwf`, vous devez connaître l'endroit où se situe ce fichier `rwf` de la tâche précédente.

Il suffit d'indiquer d'abord le chemin `%rwf` vers le fichier `rwf` précédent et modifier la ligne des mots-clés pour qu'elle se lise `#p restart`, puis laisser une ligne vide à la fin.

Voici un exemple :
```
%rwf=/scratch/yourid/jobid/name.rwf
%NoSave
%chk=name.chk
%mem=5000mb
%nprocs=16
#p restart

```

### Exemples

Un exemple de fichier d'entrée et de scripts `*.sh` se trouve dans
`/opt/software/gaussian/version/examples/`
où la version est g03.d10, g09.e01, g16.a03 ou g16.b01.

## Remarques
1.  NBO7 est inclus uniquement dans la version g16.c01 avec l'emploi des mots-clés nbo6 et nbo7.
2.  NBO6 est inclus dans les versions g09.e01 et g16.b01.
3.  Voir les diapositives du webinaire [Running Gaussian16 and NBO7 effectively on Nibi and Fir](Gauss_NBO_2026_2.pdf) (2026).

## Erreurs
Vous trouverez la solution à plusieurs erreurs dans [Gaussian – Messages d’erreur](chemistry/gaussian_error_messages.md).