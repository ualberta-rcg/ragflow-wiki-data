---
title: "Technical support/fr"
slug: "technical_support"
lang: "fr"

source_wiki_title: "Technical support/fr"
source_hash: "5876fa91da96082830f65e8182239d59"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T11:43:07.208677+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

## Demandes de soutien

*   Avant de nous contacter, vérifiez d'abord la page sur [l'état des grappes](https://status.computecanada.ca) pour savoir si votre problème a déjà été rapporté à notre équipe technique. Consultez aussi notre site wiki qui offre souvent des solutions pratiques. Si vous avez toujours besoin de nous contacter, utilisez les adresses de courriel listées ci-dessous.
*   Assurez-vous que l'adresse courriel que vous utilisez est enregistrée sous votre [compte](https://ccdb.computecanada.ca/email). De cette façon, notre système de billets de soutien peut automatiquement vous reconnaître.
*   Énoncez précisément et clairement votre problème ou votre question (voir [l'exemple d'une requête de soutien technique](#exemple-dune-requete-de-soutien-technique)).
*   Dans la ligne d'objet de votre message, évitez les énoncés vagues comme *J'ai un problème* ou *Ça ne fonctionne pas*; le temps de résolution sera plus long, car nous devrons vous contacter pour obtenir toute l'information. Assurez-vous d'inclure tous les [renseignements à fournir avec votre requête](#renseignements-a-fournir-avec-une-requete).
*   Dans la ligne d'objet de votre message, indiquez le nom de la grappe et une courte description du problème, par exemple *Erreurs pour la tâche 123456 sur la grappe Rorqual*; nous pourrons ainsi cerner plus rapidement le problème.

!!! info "Important : Adresses courriel enregistrées"
    Si vous nous contactez à partir d'une adresse de courriel que nous connaissons, notre système de requêtes de soutien vous identifiera immédiatement comme utilisateur. Assurez-vous de fournir toutes les adresses de courriel que vous utilisez dans le profil de votre compte d'utilisateur dans notre base de données.

*   Créez une nouvelle requête pour chaque problème qui n'est pas relié à une requête antérieure.

### Adresses de courriel

Veuillez choisir l'adresse qui correspond le mieux à votre besoin :

*   [comptes@tech.alliancecan.ca](mailto:comptes@tech.alliancecan.ca) -- pour des questions sur les comptes
*   [renouvellements@tech.alliancecan.ca](mailto:renouvellements@tech.alliancecan.ca) -- pour des questions sur le renouvellement des comptes
*   [globus@tech.alliancecan.ca](mailto:globus@tech.alliancecan.ca) -- pour des questions sur les services de transfert de fichiers **[Globus](globus.md)**
*   [nuage@tech.alliancecan.ca](mailto:nuage@tech.alliancecan.ca) -- pour des questions sur comment utiliser **[nos ressources infonuagiques](cloud.md)**
*   [allocations@tech.alliancecan.ca](mailto:allocations@tech.alliancecan.ca) -- pour des questions sur le [Concours pour l’allocation de ressources](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/acces-aux-ressources/concours-pour-lallocation-de-ressources) (CAR)
*   [trillium@tech.alliancecan.ca](mailto:trillium@tech.alliancecan.ca) -- pour des questions sur la grappe [Trillium](trillium.md)
*   **[support@tech.alliancecan.ca](mailto:support@tech.alliancecan.ca)** -- pour toute autre question

## Renseignements à fournir avec une requête

Afin de nous aider à mieux vous servir, veuillez inclure les renseignements suivants dans votre demande :

*   le nom de la grappe
*   le numéro de la tâche
*   le script de soumission de la tâche : donnez le chemin complet pour le script; copiez-collez le script dans votre message; ou envoyez le script en pièce jointe
*   tous les fichiers de sortie contenant des erreurs : donnez le chemin complet pour le ou les fichiers; copiez-collez le ou les fichiers dans votre message; ou envoyez le ou les fichiers en pièce jointe
*   les commandes actives au moment où le problème est survenu
*   le nom et la version du logiciel que vous vouliez utiliser
*   la date et l'heure auxquelles le problème est survenu
*   évitez de joindre des captures d'écran ou autres fichiers graphiques si ce n'est pas nécessaire; la version en texte brut est habituellement plus utile (commandes, scripts, etc.); pour plus d'information, voir [Copier-Coller](frequently-asked-questions.md#copier-coller)
*   énoncez clairement vos attentes dans votre courriel en mentionnant si nous devons accéder à vos données, copier ou modifier vos fichiers, examiner et possiblement modifier votre compte, etc. Par exemple, plutôt que de joindre des fichiers à votre courriel, vous pouvez nous indiquer où ils se trouvent dans votre compte et nous accorder la permission d'y accéder.

!!! tip "Accès à vos fichiers"
    Si nous avons déjà accès à vos fichiers via la base de données de l'Alliance (CCDB), il n'est pas nécessaire de nous accorder à nouveau la permission d'accès.

## Points importants

!!! warning "Ne partagez jamais votre mot de passe"
    **N'envoyez jamais un mot de passe.**

*   Les fichiers joints ne doivent pas dépasser 40 Mo au total.

## Exemple d'une requête de soutien technique

```text
Dest.: support@tech.alliancecan.ca
Objet: Erreurs pour la tâche 123456 sur la grappe Rorqual

Bonjour,

Mon nom est Alice, identifiant asmith. Ce matin à 10h HAE, j'ai soumis la tâche 123456 sur la grappe Rorqual. Le script pour la tâche se trouve dans `chemin pour le script`. Le script n'a pas été modifié depuis que j'ai soumis cette tâche; comme il n'est pas très long, je l'ai copié ci-dessous :

```bash
#!/bin/bash
#SBATCH --account=def-asmith-ab
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --time=00:05:00
{ time mpiexec -n 1 ./sample1 ; } 2>out.time
```

J'avais chargé les modules suivants :

```bash
[asmith@cedar5]$ module list
Currently Loaded Modules:
  1) CCconfig   2) gentoo/2023 (S)   3) gcccore/.12.3 (H)   
  4) gcc/12.3 (t)   5) hwloc/2.9.1   6) ucx/1.14.1   
  7) libfabric/1.18.0   8) pmix/4.2.4   9) ucc/1.2.0  
  10) openmpi/4.1.5 (m)  11) flexiblas/3.3.1  12) aocl-blas/5.1  
  13) aocl-lapack/5.1  14) StdEnv/2023 (S)  15) mii/1.1.2
```

La tâche a été exécutée rapidement et les fichiers *exemple-123456.out* et *exemple-123456.err* ont été générés. Il n'y avait pas de contenu dans le fichier *exemple-123456.out*, mais il y avait un message dans *exemple-123456.err* :

```bash
[asmith@rorqual2 scheduling]$ cat myjob-123456.err
slurmstepd: error: *** JOB 123456 ON cdr692 CANCELLED AT 2018-09-06T15:19:16 DUE TO TIME LIMIT ***
```

Comment puis-je résoudre ce problème?
```

## Permettre l'accès à votre compte

Vous avez peut-être consenti à nous accorder l'accès à vos fichiers par l'entente disponible dans la base de données CCDB (section *Mon compte -> Ententes*). Si ce n'est pas le cas, veuillez spécifier dans votre requête que vous nous en accordez l'accès. Ainsi, vous pouvez indiquer où se trouvent les fichiers plutôt que de les attacher à votre courriel.