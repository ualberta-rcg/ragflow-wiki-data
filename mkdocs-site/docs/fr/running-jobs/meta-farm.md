---
title: "META-Farm/fr"
slug: "meta-farm"
lang: "fr"

source_wiki_title: "META-Farm/fr"
source_hash: "f4dce0a4c2c7c47b37b62155d3c8930f"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T08:40:47.029369+00:00"

tags:
  []

keywords:
  - "temps CPU"
  - "#SBATCH -t"
  - "option -f"
  - "assistance supplémentaire"
  - "GLOST"
  - "métatâches"
  - "job_script.sh"
  - "sortie du code"
  - "dépannage"
  - "traitement"
  - "post-traitement"
  - "GPU NVidia"
  - "Status.run"
  - "resubmit.run"
  - "file d'attente"
  - "table.dat"
  - "groupe de cas"
  - "métatâche"
  - "fichiers de sortie"
  - "programme"
  - "équilibrage dynamique de la charge de travail"
  - "équilibrage dynamique"
  - "numéro de cas"
  - "mécanisme de protection"
  - "single_case.sh"
  - "META"
  - "cas échouent"
  - "META-Farm"
  - "resoumettre automatiquement"
  - "argument $ID"
  - "mode META"
  - "outil META"
  - "Commandes"
  - "meta-farm"
  - "cas qui ont échoué"
  - "cas individuel"
  - "automatisation de calculs"
  - "cœurs CPU"
  - "état de la sortie"
  - "farm_init.run"
  - "ordonnanceur"
  - "tâche MPI"
  - "resoumettre les cas"
  - "ordonnanceur Slurm"
  - "option -auto"
  - "mode SIMPLE"
  - "optimisation"
  - "submit.run"
  - "équipe de soutien technique"
  - "Mode META"
  - "fonctions avancées"
  - "temps d'exécution"
  - "nœud"
  - "STATUS"
  - "script de tâche"
  - "méthode Monte-Carlo"
  - "soumission de tâches"
  - "temps en file d'attente"

questions:
  - "Quelles sont les principales fonctionnalités de la suite de scripts META et comment distingue-t-elle les concepts de « cas » et de « tâche » ?"
  - "Comment le mode META utilise-t-il le fichier table.dat et le mécanisme lockfile pour assurer un équilibrage dynamique de la charge de travail ?"
  - "Quels avantages META offre-t-il par rapport à l'approche GLOST en matière de temps d'attente dans la file de l'ordonnanceur ?"
  - "Quels sont les principaux avantages de l'outil META par rapport à GLOST en termes d'efficacité et de gestion des erreurs ?"
  - "Quelles sont les étapes de configuration initiales pour créer et préparer un répertoire de groupe de cas avec META ?"
  - "Comment s'effectue la soumission des tâches et quelle est la différence entre le mode SIMPLE et le mode META avec la commande submit.run ?"
  - "Pourquoi le temps en file d'attente est-il plus court avec META qu'avec GLOST ?"
  - "Quel est l'impact de l'utilisation de GLOST sur le délai d'obtention du premier résultat pour une tâche nécessitant 10 000 cœurs CPU ?"
  - "Quelle capacité spécifique concernant le démarrage des métatâches individuelles est offerte par le système META ?"
  - "Comment doit-on configurer la commande `farm_init.run` pour initialiser un nouveau groupe de cas ?"
  - "Quels sont les fichiers qui nécessitent d'être personnalisés, créés ou copiés dans le répertoire avant de lancer le calcul ?"
  - "Quelle commande finale doit être exécutée pour soumettre le deuxième groupe de cas et dans quel répertoire ?"
  - "Quelles sont les principales commandes disponibles pour gérer ou surveiller un groupe de cas, et dans quel répertoire doivent-elles être exécutées ?"
  - "Dans quelles conditions spécifiques de quantité et de durée est-il recommandé d'utiliser le mode SIMPLE plutôt que le mode META ?"
  - "Comment la valeur attribuée à l'argument N dans la commande submit.run détermine-t-elle le mode d'exécution (SIMPLE ou META) des tâches ?"
  - "Quelle est la conséquence si une valeur non autorisée est attribuée à la variable N ?"
  - "Quel est le rôle exact de l'option \"-auto\" lors du processus de soumission ?"
  - "Quelle condition liée au fichier table.dat permet d'arrêter définitivement les resoumissions automatiques ?"
  - "Quel est le rôle du fichier final.sh et à quel moment est-il exécuté par rapport aux cas du fichier table.dat ?"
  - "Comment le script single_case.sh traite-t-il par défaut chaque ligne du fichier table.dat et dans quel répertoire exécute-t-il ces commandes ?"
  - "De quelle manière peut-on modifier single_case.sh pour éviter d'avoir à répéter la même commande sur chaque ligne du fichier table.dat ?"
  - "Quel est le rôle du fichier table.dat et comment doit-il être formaté si le code ne nécessite pas d'arguments spécifiques ?"
  - "Comment la variable STATUS permet-elle de gérer les erreurs dans single_case.sh et de quelle manière peut-on la personnaliser pour vérifier la réussite d'un cas ?"
  - "Quelles configurations doivent obligatoirement figurer dans job_script.sh et pourquoi est-il conseillé d'y ajouter des tests préalables sur les nœuds alloués ?"
  - "Quel est le rôle spécifique de l'argument `$ID` dans le script `single_case.sh` ?"
  - "Quelle méthode de traitement est appliquée lors de l'exécution du code dans cet exemple ?"
  - "Comment le script capture-t-il le statut de réussite ou d'échec de la commande principale ?"
  - "À qui doit-on signaler les problèmes rencontrés avec un nœud ?"
  - "Quel impact une seule métatâche incorrecte peut-elle avoir sur le fichier `table.dat` et le groupe de cas ?"
  - "Quelles modifications ou tests doit-on ajouter au fichier `job_script.sh` pour prévenir l'échec des cas ?"
  - "Comment fonctionne le mécanisme intégré à META pour détecter et interrompre les métatâches qui se terminent trop rapidement ?"
  - "Quels sont les principaux fichiers et répertoires de sortie générés lors de l'exécution d'une ou plusieurs métatâches ?"
  - "Quelle est la procédure pour identifier, analyser et resoumettre les cas qui ont échoué ou qui n'ont pas été exécutés ?"
  - "Que signifie le fait que certains cas échouent à plusieurs reprises lors de l'exécution ?"
  - "À quoi sert la commande `Status.run` dans le contexte du traitement des cas ?"
  - "Quel est l'effet de l'option `-f` lorsqu'elle est utilisée avec la commande `Status.run` ?"
  - "Pourquoi est-il préférable d'utiliser le mode META plutôt que le mode SIMPLE pour traiter un grand nombre de cas ?"
  - "Comment le mode META implémente-t-il l'équilibrage dynamique de la charge de travail entre les différentes métatâches ?"
  - "Quelles sont les conséquences de l'interruption d'une métatâche en cours de calcul et comment y remédier ?"
  - "Quel est l'impact du nombre de métatâches exécutées sur l'obtention des résultats finaux en mode META ?"
  - "Dans quelle situation spécifique est-il nécessaire d'utiliser la commande resubmit.run ?"
  - "Comment évaluer et définir le temps d'exécution ainsi que le nombre optimal de métatâches pour le fichier job_script.sh ?"
  - "Comment doit-on procéder pour estimer le temps d'exécution moyen d'un cas individuel ?"
  - "Quels critères faut-il respecter pour choisir la durée d'exécution optimale d'une métatâche ?"
  - "Comment calcule-t-on le nombre total de métatâches requises pour traiter l'ensemble des cas ?"
  - "Comment doit-on procéder pour soumettre un groupe de cas contenant plus de 1000 métatâches sur les systèmes Nibi et Rorqual ?"
  - "Quelle est la méthode recommandée pour tester des cas individuels avant de lancer l'exécution d'un grand groupe de cas ?"
  - "Quelles stratégies d'optimisation concernant la gestion des fichiers et des répertoires doivent être appliquées lorsque l'on traite plus de 10 000 cas ?"
  - "Quelle modification doit-être apportée au fichier `job_script.sh` pour obtenir un temps d'attente acceptable ?"
  - "Comment est calculé le nombre total de métatâches nécessaires pour traiter l'ensemble des cas ?"
  - "Quelle commande finale doit-on exécuter pour lancer le groupe de cas une fois l'estimation terminée ?"
  - "Comment le script capture-t-il l'état à la sortie du code exécuté ?"
  - "Quelle variable est utilisée pour nommer le fichier de sortie généré par le code ?"
  - "Où l'utilisateur peut-il trouver des informations sur les fonctions avancées et le dépannage de META-Farm ?"
  - "Qui doit-on mentionner lors d'une demande d'assistance au soutien technique pour l'outil META ?"
  - "Comment la terminologie définit-elle un « cas » et dans quel fichier spécifique est-il enregistré ?"
  - "Quelle est la différence fondamentale entre le mode d'opération META et le mode SIMPLE ?"
  - "Qui doit-on mentionner lors d'une demande d'assistance au soutien technique pour l'outil META ?"
  - "Comment la terminologie définit-elle un « cas » et dans quel fichier spécifique est-il enregistré ?"
  - "Quelle est la différence fondamentale entre le mode d'opération META et le mode SIMPLE ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Nouveauté

*   La version 1.0.3 publiée en mars 2025 fonctionne sur la grappe Trillium. Ceci est rendu possible avec l'ajout du nouveau mode WHOLE_NODE (inactif par défaut, mais configurable dans `config.h`) et de quelques autres ajustements. Le mode WHOLE_NODE rassemble les cas séquentiels de calcul dans des tâches qui demandent des nœuds complets. Pour plus d'information, voir [META-Farm : Fonctions avancées et dépannage](meta-farm__advanced_features_and_troubleshooting.md).

## Description

META (pour META-Farm) est une suite de scripts conçus par l’équipe SHARCNET pour automatiser l’exécution d’un grand nombre de calculs connexes. En anglais, cette pratique est parfois nommée *farming*, *serial farming* ou *task farming*. META fonctionne sur tous les systèmes nationaux de l'Alliance et peut également être utilisée sur d'autres grappes qui possèdent la même configuration et qui font usage de [l’ordonnanceur Slurm](https://slurm.schedmd.com/documentation.html).

Nous employons ici le terme **cas** (*case*) pour désigner un calcul distinct; il peut être l'exécution d'un programme en série, d'un programme parallèle ou d'un programme utilisant un GPU.
Le terme **tâche** (*job*) est employé pour désigner une invocation à l’ordonnanceur de tâches; une tâche peut regrouper plusieurs cas.

META possède les fonctionnalités suivantes :

*   deux modes de fonctionnement :
    *   le mode SIMPLE avec un cas par tâche,
    *   le mode META avec plusieurs cas par tâche.
*   équilibrage dynamique de la charge de travail en mode META,
*   capture du statut de sortie pour tous les cas individuels,
*   resoumission automatique de tous les cas qui ont échoué ou n'ont jamais été exécutés,
*   exécution automatique d’une tâche de post-traitement une fois que tous les cas ont été traités avec succès.

Quelques exigences techniques :
*   Pour chaque groupe de cas, chaque cas à traiter doit être décrit sur une ligne distincte dans un fichier `table.dat`.
*   Vous pouvez exécuter plusieurs groupes de cas indépendamment, mais chacun doit avoir son propre répertoire.

En mode META, le nombre de tâches (ou *métatâches*) effectivement soumises est généralement bien inférieur au nombre de cas à traiter. Chaque métatâche peut traiter plusieurs lignes du fichier `table.dat`, donc plusieurs cas. Une collection de métatâches lira les lignes de `table.dat` séquentiellement en commençant par la première ligne et utilisera le mécanisme [lockfile](https://linux.die.net/man/1/lockfile) pour éviter une situation de concurrence. Ceci garantit un bon équilibre dynamique de la charge de travail entre les métatâches, car celles qui traitent des cas plus courts peuvent en traiter davantage.

En mode META, toutes les métatâches n'ont pas besoin d'exécuter des cas. La première métatâche commencera à traiter les lignes de `table.dat` et si la deuxième tâche démarre, elle rejoint la première, et ainsi de suite. Si le temps d'exécution d'une métatâche individuelle est suffisamment long, tous les cas peuvent être traités avec une seule métatâche.

### META vs GLOST

META possède des avantages importants par rapport à d'autres approches telles que [GLOST](glost.md) où le traitement de chaque groupe de cas est effectué dans une seule grande tâche parallèle (MPI).
*   Comme l'ordonnanceur dispose de toute la souplesse pour démarrer les métatâches individuelles quand il le souhaite, le temps en file d'attente peut être beaucoup plus court avec META qu'avec GLOST. Par exemple, dans un contexte où 10 000 cœurs CPU doivent être utilisés pendant 3 jours
    *   avec GLOST, le temps en file d'attente pour une tâche MPI avec 10 000 cœurs CPU peut être long et il faudra donc des semaines avant d’obtenir votre tout premier résultat;
    *   avec META, certaines métatâches démarrent et produisent les premiers résultats en quelques minutes.
*   À la fin du traitement d'un groupe de cas,
    *   avec GLOST, certains rangs MPI se termineront plus tôt et resteront inactifs jusqu'à la fin du tout dernier rang MPI, le plus lent;
    *   avec META, il n'y a pas de telle perte à la fin du traitement; les métatâches individuelles sortent plus tôt si elles n'ont plus de charge de travail à traiter.
*   GLOST et d'autres outils similaires ne prennent pas en charge la resoumission automatisée des cas qui ont échoué ou qui n'ont jamais été exécutés. META possède cette fonctionnalité qui de plus est très facile à utiliser.

### Webinaire META

Voyez le [webinaire enregistré le 6 octobre 2021](https://youtu.be/GcYbaPClwGE).

## Démarrage rapide

Si vous débutez avec META, suivez les étapes ci-dessous. Il est toutefois fortement recommandé de lire cette page au complet.

*   Connectez-vous à une grappe.
*   Chargez le module `meta-farm`.

    ```bash
    module load meta-farm
    ```

*   Choisissez un nom pour le répertoire du groupe de cas, par exemple `Farm_name` et créez-le avec

    ```bash
    farm_init.run  Farm_name
    ```

*   Cette commande créera également quelques fichiers importants dans le répertoire, dont certains devront être personnalisés.
*   Copiez vos fichiers exécutables et vos fichiers d'entrée dans le répertoire du groupe de cas. (Vous pouvez ignorer cette étape si vous prévoyez utiliser des chemins complets partout.)
*   Modifiez le fichier `table.dat` dans le répertoire. Il s'agit d'un fichier texte décrivant un cas (un calcul distinct) par ligne. Voyez des exemples dans les sections suivantes :
    *   [single_case.sh](#single_case.sh)
    *   [Exemple : fichiers d'entrée numérotés](meta-farm__advanced_features_and_troubleshooting.md#exemple-fichiers-dentree-numerotes) (avancé)
    *   [Exemple : fichier d'entrée doit avoir le même nom](meta-farm__advanced_features_and_troubleshooting.md#exemple-fichier-dentree-doit-avoir-le-meme-nom) (avancé)
    *   [Accéder à chaque paramètre d'un cas](meta-farm__advanced_features_and_troubleshooting.md#acceder-a-chaque-parametre-dun-cas) (avancé)
*   Modifiez le script `single_case.sh` au besoin. Souvent, aucune modification n'est requise; voir les sections suivantes :
    *   [single_case.sh](#single_case.sh)
    *   [STATUS et traitement des erreurs](#status-et-traitement-des-erreurs)
    *   [Exemple : fichier d'entrée doit avoir le même nom](meta-farm__advanced_features_and_troubleshooting.md#exemple-fichier-dentree-doit-avoir-le-meme-nom) (avancé)
    *   [Accéder à chaque paramètre d'un cas](meta-farm__advanced_features_and_troubleshooting.md#acceder-a-chaque-parametre-dun-cas) (avancé)
*   Modifiez le fichier `job_script.sh` selon vos besoins, tel que décrit dans [job_script.sh, ci-dessous](#job_script.sh). En particulier, utilisez un nom de compte de calcul valide et indiquez une durée d’exécution appropriée. Pour plus d'information sur le temps d’exécution, voir [Estimation du temps d'exécution et du nombre de métatâches](#estimation-du-temps-dexectution-et-du-nombre-de-metataches).
*   Dans le répertoire des cas, lancez

    ```bash
    submit.run -1
    ```

    pour le mode SIMPLE (un cas par tâche) ou

    ```bash
    submit.run N
    ```

    pour le mode META, où N est le nombre de métatâches à utiliser. La valeur de N doit être de beaucoup inférieure au nombre total de cas.

Pour faire exécuter un autre groupe de cas en même temps que le premier, lancez de nouveau `farm_init.run` avec un nom de groupe différent et personnalisez les fichiers `single_case.sh` et `job_script.sh` à l’intérieur du répertoire; créez ensuite un nouveau fichier `table.dat` au même endroit. Copiez l’exécutable et tous les fichiers d’entrée nécessaires. Vous pouvez maintenant lancer la commande `submit.run` dans le deuxième répertoire de cas pour soumettre le deuxième groupe de cas.

## Liste des commandes
*   **farm_init.run** : initialise un groupe de cas; voir [Démarrage rapide, ci-dessus](#demarrage-rapide).
*   **submit.run** : soumet le groupe de cas à l’ordonnanceur; voir [submit.run, ci-dessous](#submit.run).
*   **resubmit.run** : soumettre comme nouveau groupe de cas tous les traitements qui ont échoué ou qui n’ont jamais été exécutés; voir [Resoumettre les cas qui ont échoué, ci-dessous](#resoumettre-les-cas-qui-ont-echoue).
*   **list.run** : liste toutes les tâches et leur état actuel.
*   **query.run** : fournit un sommaire de l’état du groupe de cas avec le nombre de tâches dans la file d'attente, en cours d’exécution et terminées. Cette commande est plus pratique que `list.run` quand il y a un grand nombre de tâches. La commande fournit aussi de l’information sur la progression générale et celle de l’exécution en cours, c’est-à-dire le nombre de cas traités par rapport au nombre total de cas.
*   **kill.run** : interrompt toutes les tâches en cours et annule celles dans la file d’attente.
*   **prune.run** : annule uniquement les tâches dans la file d’attente.
*   **Status.run (le S au début est en majuscule)** : liste les états de tous les cas traités. L’option `-f`, fait afficher à la toute fin les lignes d’état non nulles, le cas échéant.
*   **clean.run** : supprime tous les fichiers dans le répertoire du groupe de cas ainsi que les sous-répertoires s’il y a lieu, à l’exception des fichiers `job_script.sh`, `single_case.sh`, `final.sh`, `resubmit_script.sh`, `config.h` et `table.dat`. Tous les fichiers dans le répertoire `/home/$USER/tmp` qui sont associés au groupe de cas sont aussi supprimés. Utilisez ce script avec beaucoup de prudence.

Toutes ces commandes (à l'exception de `farm_init.run` elle-même) doivent être exécutées dans un répertoire de groupe de cas créé par `farm_init.run`.

## Mode SIMPLE pour un petit nombre de cas

Rappelons qu'une seule exécution de votre code est un **cas** et qu’une invocation de l'ordonnanceur est une **tâche**. Si:
*   le nombre total de cas est assez bas, disons moins de 500 et que
*   chaque cas prend au moins 20 minutes,
il est raisonnable de dédier une tâche distincte à chacun des cas en utilisant le mode SIMPLE. Sinon, vous devriez utiliser le mode META pour gérer de nombreux cas par tâche; voir [Mode META pour un grand nombre de cas, ci-dessous](#mode-meta-pour-un-grand-nombre-de-cas).

Les trois scripts essentiels sont la commande `submit.run` et deux scripts personnalisables `single_case.sh` et `job_script.sh`.

### submit.run

!!! note "Remarque"
    La présente section est valide pour les deux modes.

Un argument de cette commande doit être spécifié, soit *N* qui représente le nombre de tâches à soumettre.

```bash
submit.run N [-auto] [optional_sbatch_arguments]
```

Avec *N*=-1, vous demandez le mode SIMPLE (pour soumettre autant de tâches qu'il y a de lignes dans le fichier `table.dat`). Si *N* est un entier positif, vous demandez le mode META (pour soumettre une tâche avec plusieurs cas), *N* étant le nombre de métatâches demandées. Toute autre valeur de *N* est une erreur.

Si l’option `-auto` est présente, la soumission se refera automatiquement à la fin, plus d'une fois si nécessaire, jusqu'à ce que tous les cas dans `table.dat` aient été traités. Cette fonction est décrite dans [Resoumettre automatiquement les cas qui ont échoué](meta-farm__advanced_features_and_troubleshooting.md#resoumettre-automatiquement-les-cas-qui-ont-echoue).

Si un fichier nommé `final.sh` est présent dans le répertoire du groupe de cas, `submit.run` le traitera comme un script de tâche pour le post-traitement et il sera lancé automatiquement une fois que tous les cas de `table.dat` auront été traités avec succès; voir [Exécuter automatiquement une tâche de post-traitement](meta-farm__advanced_features_and_troubleshooting.md#executer-automatiquement-une-tache-de-post-traitement).

Si vous fournissez d'autres arguments, ils seront transmis à la commande `sbatch` de l’ordonnanceur pour le lancement de toutes les métatâches pour ce groupe de cas.

### single_case.sh

!!! note "Remarque"
    La présente section est valide pour les deux modes.

Le script `single_case.sh` lit une ligne du fichier `table.dat`, l’analyse, puis utilise le contenu de la ligne pour lancer votre code pour un des cas. Vous pouvez adapter `single_case.sh` à vos besoins.

La version de `single_case.sh` fournie par `farm_init.run` traite chaque ligne de `table.dat` comme étant une commande littérale et l’exécute dans son propre répertoire `RUNyyy` où *yyy* représente le numéro du cas. Voici la partie pertinente de `single_case.sh` :

```bash
...
# ++++++++++++++++++++++  Modifiez le code selon vos besoins.  ++++++++++++++++++++++++
#  Dans cet exemple,
#  $ID est l'identifiant du cas dans la table d'origine (peut fournir une source unique pour le code, etc.),
#  $COMM est la ligne qui correspond à l'$ID du cas dans la table d'origine, sans le champ ID,
#  $METAJOB_ID est l'identifiant de la tâche pour la métatâche en cours (utile pour créer des fichiers par tâche).

mkdir -p RUN$ID
cd RUN$ID

echo "Case $ID:"

# Exécute la commande (une ligne dans table.dat).
# Peut utiliser plus qu'une commande pour l'interpréteur (séparées par le deux-points) sur une même ligne.
eval "$COMM"

# État à la sortie du code
STATUS=$?

cd ..
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
...
```

Par conséquent, si `single_case.sh` n’est pas modifié, chaque ligne de `table.dat` doit contenir une commande complète; il peut s'agir d'une commande composée, c'est-à-dire plusieurs commandes séparées par des points-virgules (;).

En règle générale, le fichier `table.dat` contiendra une liste de commandes identiques différenciées uniquement par leurs arguments, mais ce n'est pas obligatoire. Tout énoncé exécutable peut se trouver dans `table.dat` qui pourrait ressembler à ceci

```
  /home/user/bin/code1  1.0  10  2.1
  cp -f ~/input_dir/input1 .; ~/code_dir/code 
  ./code2 < IC.2
```

Si vous voulez exécuter la même commande pour chacun des cas et ne voulez pas avoir à la répéter à chacune des lignes de `table.dat`, vous pouvez modifier `single_case.sh` pour inclure la commande commune, puis modifier `table.dat` pour qu’il contienne uniquement les arguments ou/et des redirections pour chaque cas.

Dans l’exemple suivant, `single_case.sh` a été modifié. La commande `/path/to/your/code` est ajoutée, le contenu de `table.dat` sert d’arguments à la commande et l’argument `$ID` est ajouté pour le numéro de cas.

*   `single_case.sh`
    ```bash
    ...
    # ++++++++++++++++++++++  Modifiez le code selon vos besoins.  ++++++++++++++++++++++++
    # Dans cet exemple, $ID (numéro du cas) est utilisé comme source pour le traitement selon la méthode Monte-Carlo.
    /path/to/your/code -par $COMM  -seed $ID
    STATUS=$?
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ...
    ```
*   `table.dat`
    ```bash
     12.56
     21.35
     ...
    ```

!!! note "Remarque 1"
    Si votre code n’a pas besoin de lire d’arguments dans le fichier `table.dat`, il faut quand même générer ce fichier avec le nombre de lignes égal au nombre de cas à traiter. Tout ce qui importe dans le contenu de `table.dat` est le nombre total de lignes. Dans notre exemple, la commande simplifiée serait alors

    ```
     /path/to/your/code -seed $ID
    ```

!!! note "Remarque 2"
    Il n’est pas nécessaire d’inclure les numéros de ligne au début de chaque ligne de `table.dat`. Si le script `submit.run` ne les trouve pas, il modifiera `table.dat` pour y ajouter les numéros de lignes.

#### STATUS et traitement des erreurs

À quoi sert `STATUS` dans `single_case.sh`? La valeur de cette variable devrait être de 0 si votre cas a été traité correctement, autrement sa valeur sera positive (plus grande que 0). Ceci est très important, car `resubmit.run` l’utilise pour identifier les cas qui ont échoué et qui doivent être traités de nouveau. Dans la version de `single_case.sh` que nous fournissons, `STATUS` est le code de sortie de votre programme. Ceci ne résout pas tous les problèmes parce que certains programmes produisent un code de sortie de 0 même si tout ne s’est pas bien déroulé. Vous pouvez changer la définition de `STATUS` en modifiant `single_case.sh`.

Par exemple, si votre code doit créer le fichier `out.dat` à la fin de chaque cas, effectuez un test pour savoir si le fichier existe et changez la valeur de `STATUS` en conséquence. Dans l’exemple suivant, la valeur de `$STATUS` sera positive si le code de sortie du programme est positif ou si `out.dat` n’existe pas ou est vide.

```bash
STATUS=$?
if test ! -s out.dat
   then
   STATUS=1
   fi
```

### job_script.sh

!!! note "Remarque"
    La présente section est valide pour les deux modes.

Ce fichier est le script qui sera soumis à l’ordonnanceur pour toutes les métatâches du groupe de cas. La version crée par défaut par `farm_init.run` est

```bash
#!/bin/bash
# Indiquez les arguments sbatch pour toutes les tâches du groupe de cas.
# Doit contenir l'option pour la durée d'exécution (soit -t ou --time).
#SBATCH -t 0-00:10
#SBATCH --mem=4G
#SBATCH -A Nom_de_votre_compte

# Ne modifiez pas la ligne suivante.
task.run
```

Vous devez configurer le nom du compte (option `-A`) et la durée d’exécution (option `-t`) de la métatâche. En mode SIMPLE, indiquez une durée d’exécution un peu plus longue que celle prévue pour le cas individuel qui est de plus longue durée.

!!! warning "Important"
    Le script `job_script.sh` doit contenir une option pour la durée d’exécution, soit `-t` ou `--time`. Ceci ne peut pas être passé à `sbatch` comme argument optionnel pour `submit.run`.

Le problème suivant peut se produire : Une métatâche peut avoir été allouée à un nœud défectueux, ce qui fait immédiatement échouer le programme. Par exemple, votre programme pourrait nécessiter un GPU, mais celui qui vous est assigné fonctionne mal ou encore le système de fichiers `/project` n’est pas disponible. Tout problème avec un nœud devrait être signalé à l’équipe de soutien technique. Si ceci se produit, une seule métatâche incorrecte peut rapidement parcourir `table.dat` et faire échouer tout le groupe de cas. Pour prévenir ce problème, ajoutez des tests à `job_script.sh` avant la ligne `task.run`. Par exemple, la modification suivante teste la présence d’un GPU NVidia et force la fin d’une métatâche avant que des cas échouent

```bash
nvidia-smi >/dev/null
retVal=$?
if [ $retVal -ne 0 ]; then
    exit 1
fi
task.run
```

L’utilitaire `gpu_test` fait un travail équivalent. Sur Nibi, copiez-le dans votre répertoire `~/bin`.

```bash
cp ~syam/bin/gpu_test ~/bin
```

Un mécanisme intégré à META tente de détecter de tels problèmes pour interrompre une métatâche qui passerait trop rapidement sur les cas. Les paramètres `N_failed_max` et `dt_failed` sont définis dans le fichier `config.h`. Le mécanisme de protection se déclenche quand les `$N_failed_max` premiers cas sont d’une durée inférieure à `$dt_failed` secondes. Les valeurs par défaut sont 5 et 5; ainsi, la métatâche s’arrête par défaut si les 5 premiers cas sont terminés en moins de 5 secondes. Si le mécanisme se déclenche parce que certains de vos cas ont une durée d’exécution inférieure à `$dt_failed`, diminuez la valeur de `dt_failed` dans `config.h`.

### Fichiers de sortie

!!! note "Remarque"
    La présente section est valide pour les deux modes.

Une fois qu'une ou plusieurs métatâches sont en cours d'exécution, les fichiers suivants sont créés dans le répertoire du groupe de cas :
*   `OUTPUT/slurm-$JOBID.out`, un fichier par métatâche contenant la sortie standard,
*   `STATUSES/status.$JOBID`, un fichier par métatâche contenant l'état de chaque cas traité.

Dans les deux cas, `$JOBID` est l’identifiant de la tâche pour la métatâche correspondante.

Le répertoire `MISC` est également créé dans le répertoire racine du groupe de cas.

De plus, chaque fois que `submit.run` est exécuté, un sous-répertoire unique est créé dans `/home/$USER/tmp`. Dans ce sous-répertoire, certains petits fichiers de travail seront créés, tels que les fichiers utilisés par `lockfile` pour protéger certaines opérations critiques à l'intérieur des tâches. Les noms de ces sous-répertoires contiennent
`$NODE.$PID` où `$NODE` est le nom du nœud actuel qui est généralement un nœud de connexion et
`$PID`, l’identifiant unique du processus pour le script.
Ce sous-répertoire peut être supprimé une fois que le traitement complet du groupe de cas est terminé. Si vous lancez `clean.run`, le sous-répertoire sera automatiquement supprimé, mais prenez garde parce que cette commande supprime aussi tous les résultats obtenus.

### Resoumettre les cas qui ont échoué

!!! note "Remarque"
    La présente section est valide pour les deux modes.

La commande `resubmit.run` utilise les mêmes arguments que `submit.run`.

```bash
resubmit.run N [-auto] [optional_sbatch_arguments]
```

La commande `resubmit.run`
*   analyse tous les fichiers `status.*` (voir [Fichiers de sortie, ci-dessus](#fichiers-de-sortie));
*   détermine les cas qui ont échoué et ceux qui n'ont jamais été exécutés pour une raison quelconque, par exemple, à cause de la limite de temps d'exécution des métatâches;
*   crée ou recrée un fichier secondaire `table.dat_` qui répertorie uniquement les cas qui doivent encore être exécutés;
*   lance un nouveau groupe de cas pour ces cas.

Vous ne pouvez pas exécuter `resubmit.run` tant que toutes les tâches de l'exécution d'origine ne sont pas terminées ou annulées.

Si certains cas échouent ou ne s'exécutent toujours pas, vous pouvez soumettre le groupe de cas à nouveau, autant de fois que nécessaire. Bien sûr, si certains cas échouent à plusieurs reprises, il doit y avoir un problème avec le programme que vous exécutez ou avec son entrée. Dans ce cas, vous pouvez utiliser la commande `Status.run` (le S est en majuscule) qui affiche l’état de tous les cas traités. Avec l'option `-f`, `Status.run` triera le résultat en fonction de l’état de la sortie en affichant les cas avec un état différent de zéro dans le bas pour mieux les repérer.

De la même manière que pour `submit.run`, si l’option `-auto` est présente, le groupe de cas sera automatiquement soumis de nouveau à la fin, plus d'une fois si nécessaire (voir [Resoumettre automatiquement les cas qui ont échoué](meta-farm__advanced_features_and_troubleshooting.md#resoumettre-automatiquement-les-cas-qui-ont-echoue)).

## Mode META pour un grand nombre de cas

Le mode SIMPLE (un cas par tâche) fonctionne bien lorsque le nombre de cas est assez petit (<500). Lorsque le nombre de cas est largement supérieur à 500, les problèmes suivants peuvent survenir :

*   Chaque grappe a une limite quant au nombre de tâches que vous pouvez avoir en même temps.
*   Avec un très grand nombre de cas, chaque traitement de cas est généralement court. Si un cas s'exécute pendant <20 min, les cycles CPU peuvent être gaspillés par de l’ordonnancement non nécessaire.

Le mode META est la solution à ces problèmes. Au lieu de soumettre une tâche distincte pour chaque cas, un plus petit nombre de métatâches sont soumises, chacune traitant plusieurs cas. Pour activer le mode META, le premier argument de `submit.run` doit être le nombre souhaité de métatâches, qui doit être un nombre assez petit, soit beaucoup plus petit que le nombre de cas à traiter, par exemple

```bash
submit.run  32
```

Étant donné que chaque cas peut prendre un temps de traitement différent, le mode META utilise un schéma d'équilibrage dynamique de la charge de travail. Voici comment le mode META est implémenté :

![](assets/images/meta1.png)

Chaque tâche exécute le même script `task.run`. À l'intérieur de ce script, il y a une boucle `while` pour les cas. Chaque itération de la boucle doit passer par une zone critique (c'est-à-dire qu'une seule tâche à la fois peut effectuer certaines opérations), où elle obtient le cas suivant à traiter dans `table.dat`. Ensuite, le script `single_case.sh` (voir [single_case.sh](#single_case.sh)) est exécuté une fois pour ce nouveau cas, ce qui appelle ensuite votre code.

Cette approche crée un équilibrage dynamique de la charge de travail réalisé par toutes les métatâches actives d’un même groupe de cas. L'algorithme est illustré par le schéma ci-dessous :

![](assets/images/DWB_META.png)

[Cette animation tirée du webinaire META](https://www.youtube.com/watch?v=GcYbaPClwGE&t=423s) en illustre le fonctionnement.

L'équilibrage dynamique de la charge de travail a pour résultat que toutes les métatâches se terminent à peu près au même moment, quelle que soit la différence des durées d'exécution pour les cas individuels, quelle que soit la vitesse des processeurs des différents nœuds et quel que soit le moment où chacune des métatâches démarre. De plus, toutes les métatâches n'ont pas besoin de commencer à s'exécuter pour que tous les cas soient traités. Enfin, si une métatâche est interrompue en plein calcul (par exemple si un nœud tombe en panne), c’est au plus un cas qui sera perdu. Ceci peut facilement être repris avec `resubmit.run` (voir [Resoumettre les cas qui ont échoué](#resoumettre-les-cas-qui-ont-echoue)).

En résumé, toutes les métatâches demandées ne s'exécuteront pas nécessairement; cela dépend de la disponibilité de la grappe. Mais comme décrit ci-dessus, vous obtiendrez éventuellement tous vos résultats en mode META, quel que soit le nombre de métatâches exécutées, même si vous devrez peut-être utiliser `resubmit.run` pour terminer un groupe de cas en particulier.

### Estimation du temps d'exécution et du nombre de métatâches

Comment peut-on déterminer le nombre optimal de métatâches et le temps d'exécution à utiliser dans `job_script.sh`?

Vous devez d'abord déterminer le temps d'exécution moyen pour un cas individuel (une seule ligne dans `table.dat`). Pour ce faire, en supposant que votre programme ne soit pas parallèle, allouez un seul cœur CPU avec [`salloc`](running_jobs.md#taches-interactives), puis exécutez `single_case.sh` pour quelques cas différents. Mesurez la durée d'exécution totale et divisez-la par le nombre de cas que vous avez exécutés pour obtenir une estimation de la durée d'exécution moyenne des cas. Cela peut être fait avec une boucle `for`.

```bash
N=10; time for ((i=1; i<=$N; i++)); do  ./single_case.sh table.dat $i  ; done
```

Divisez le temps réel obtenu par `$N` pour obtenir une estimation du temps moyen d’exécution que nous appellerons ici *dt_case*.

Estimez le temps CPU total nécessaire pour traiter le tout en multipliant *dt_case* par le nombre de cas, c'est-à-dire le nombre de lignes dans `table.dat`. Si c'est en secondes CPU, diviser cela par 3600 vous donne le nombre total d'heures CPU. Multipliez cela par quelque chose comme 1,1 ou 1,3 pour avoir une certaine marge de sécurité.

Vous pouvez maintenant faire un choix judicieux pour le temps d'exécution des métatâches et cela déterminera également le nombre de métatâches nécessaires pour traiter le groupe de cas en entier.

La durée d'exécution que vous choisissez doit être nettement supérieure à la durée d'exécution moyenne d'un cas individuel, idéalement par un facteur de 100 ou plus. Il doit certainement être supérieur à la durée d'exécution la plus longue que vous prévoyez pour un cas individuel. En revanche, il ne doit pas être trop grand, soit pas plus de 3 jours. Plus la durée d'exécution d'une tâche est longue, plus elle restera longtemps en file d’attente. Sur les grappes à usage général de l’Alliance, un bon choix serait 12 ou 24 heures en raison des [politiques d’ordonnancement des tâches](job_scheduling_policies.md#duree-maximale). Une fois le temps d'exécution choisi, divisez le nombre total d'heures CPU par le temps d'exécution que vous avez choisi (en heures) pour obtenir le nombre requis de métatâches. Arrondissez ce nombre à l'entier supérieur.

Avec ces choix, le temps dans la file d'attente devrait être acceptable, et le débit et l'efficacité devraient être assez élevés.

Prenons un exemple précis. Supposons que vous exécutez la boucle `for` ci-dessus sur un processeur dédié obtenu avec `salloc` et que le résultat indique que le temps réel était de 15m50s, soit 950 secondes. Divisez cela par le nombre de cas servant d’échantillons soit 10, pour trouver que le temps moyen pour un cas individuel est de 95 secondes. Supposons également que le nombre total de cas que vous devez traiter (le nombre de lignes dans `table.dat`) est de 1000. Le temps CPU total nécessaire pour calculer tous vos cas est alors de
95 x 1 000 = 95000 secondes CPU, soit 26,4 heures CPU.
Par mesure de sécurité, multipliez cela par un facteur de 1,2 pour obtenir 31,7 heures CPU. Une durée d'exécution de 3 heures pour vos métatâches fonctionnerait ici et devrait conduire à une période acceptable dans la file d'attente. Modifiez la valeur de `#SBATCH -t` dans `job_script.sh` pour qu'elle soit `3:00:00`. Estimez maintenant le nombre de métatâches dont vous aurez besoin pour traiter tous les cas.
N = 31,7 heures de base / 3 heures = 10,6
ce qui, arrondi au nombre entier suivant, est 11. Ensuite, vous pouvez lancer le groupe de cas en exécutant une fois `submit.run 11`.

Si le nombre de métatâches dans l'analyse est supérieur à 1000, vous disposez d'un groupe de cas de taille particulièrement grande. Le nombre maximum de tâches pouvant être soumis sur Nibi et Rorqual étant de 1000, vous ne pourrez donc pas exécuter tout le groupe de cas avec une seule soumission. La solution de contournement consiste à utiliser la séquence de commandes suivante. N'oubliez pas que chaque commande ne peut être exécutée qu'après la fin de l'exécution du groupe précédent.

```bash
submit.run 1000
resubmit.run 1000
resubmit.run 1000
...   
```

Si cela semble plutôt fastidieux, envisagez plutôt d'utiliser la fonctionnalité avancée pour [resoumettre automatiquement les cas qui ont échoué](meta-farm__advanced_features_and_troubleshooting.md#resoumettre-automatiquement-les-cas-qui-ont-echoue).

## Quelques précautions

Commencez toujours par un petit test pour vous assurer que tout fonctionne avant de soumettre un grand groupe de cas. Vous pouvez tester des cas individuels en réservant un nœud interactif avec `salloc`, en passant au répertoire du groupe de cas et en exécutant des commandes telles que `./single_case.sh table.dat 1`, `./single_case.sh table.dat 2`, etc.

Si vous avez plus de 10,000 cas, vous devez déployer des efforts supplémentaires pour vous assurer que tout fonctionne aussi efficacement que possible. En particulier, minimisez le nombre de fichiers et/ou de répertoires créés lors de l'exécution. Si possible, faites que votre code poursuive ses écritures à la suite des fichiers existants (un par métatâche; **ne mélangez pas les résultats de différentes métatâches dans un seul fichier de sortie**) plutôt que de créer un fichier séparé pour chaque cas. Évitez de créer un sous-répertoire distinct pour chaque cas. Oui, la création de sous-répertoires séparés pour chaque cas est la configuration par défaut de META, mais ce comportement par défaut a été choisi pour la sécurité et non pour l'efficacité.

L'exemple suivant est optimisé pour un très grand nombre de cas. Il suppose, pour l'exemple :
*   que votre code accepte le nom du fichier de sortie via une option en ligne de commande `-o`,
*   que l'application ouvre le fichier de sortie en mode ajout (*append*), c'est-à-dire que plusieurs exécutions continueront à s'ajouter au fichier existant,
*   que chaque ligne de `table.dat` fournit le reste des arguments en ligne de commande pour votre code,
*   que plusieurs instances de votre code peuvent s'exécuter simultanément en toute sécurité dans le même répertoire et qu’il n'est donc pas nécessaire de créer un sous-répertoire pour chaque cas,
*   que chaque exécution ne produira aucun fichier en plus du fichier de sortie.
Avec cette configuration, même les très grands groupes de cas (des centaines de milliers, voire des millions) devraient être efficacement exécutés, car relativement peu de fichiers seront créés.

```bash
...
# ++++++++++++++++++++++  Modifiez le code selon vos besoins.  ++++++++++++++++++++++++
#  Here:
#  $ID est l'identifiant du cas dans la table d'origine (peut fournir une source unique pour le code, etc.),
#  $COMM est la ligne qui correspond à l'$ID du cas dans la table d'origine, sans le champ ID,
#  $METAJOB_ID est l'identifiant de la tâche pour la métatâche en cours (utile pour créer des fichiers par tâche).

# Exécute la commande (une ligne dans table.dat).
/path/to/your/code  $COMM  -o output.$METAJOB_ID

# État à la sortie du code.
STATUS=$?
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
...
```

## Assistance supplémentaire

Pour des détails sur certaines fonctionnalités et des suggestions de dépannage, voyez la version française de la page [META-Farm : Fonctions avancées et dépannage](meta-farm__advanced_features_and_troubleshooting.md).

Si vous avez besoin de plus d’assistance, contactez le [soutien technique](../support/technical_support.md) et mentionnez le nom de l’outil META et celui de son développeur, Sergey Mashchenko.

### Terminologie
*   **cas** (*case*) : Un calcul distinct. Le fichier `table.dat` contient un cas par ligne.
*   **groupe de cas** (*farm*) : Répertoire et fichiers utilisés par une instance de META-Farm. En anglais, le *farming* est la pratique d’exécuter sur une grappe plusieurs tâches distinctes qui effectuent des calculs de même nature.
*   **métatâche** (*metajob*) : Tâche pouvant traiter séparément plusieurs cas en provenance de `table.dat`.
*   **mode META** : Mode d’opération où chaque tâche peut traiter plusieurs cas en provenance de `table.dat`.
*   **mode SIMPLE** : Mode d’opération où chaque tâche peut traiter un seul cas en provenance de `table.dat`.