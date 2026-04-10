---
title: "Automating VM creation/fr"
slug: "automating_vm_creation"
lang: "fr"

source_wiki_title: "Automating VM creation/fr"
source_hash: "9eefadcf2e640ac2b5d300d2dad6aedf"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T04:43:44.556143+00:00"

tags:
  - cloud

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

*Page enfant de [Cloud](cloud.md)*

Pour automatiser la création d'instances infonuagiques, de volumes, etc., vous pouvez utiliser [CLI OpenStack](openstack-command-line-clients.md), [Heat](#utilisation-de-gabarits-heat), [Terraform](terraform.md) ou l'API Python pour OpenStack. CLI OpenStack et Terraform sont des outils en ligne de commande, tandis que Heat s'utilise via le tableau de bord web OpenStack Horizon. Pour installer et configurer les paramètres et les logiciels dans l'instance, on utilise [cloud-init](#utilisation-de-cloud-init).

En plus de ces outils, vous pouvez aussi avoir accès à la pile logicielle de Calcul Canada (CVMFS) qui est disponible sur nos grappes d'usage général; voyez [*Utilisation de CVMFS*](#utilisation-de-cvmfs) ci-dessous.

## Utilisation de CVMFS
CVMFS est un système de fichiers HTTP qui offre un service évolutif et fiable pour la distribution de logiciels de recherche. Du côté du client, les utilisateurs n'ont qu'à monter CVMFS et utiliser les logiciels et les bibliothèques directement, sans se soucier de compiler ou d'adapter le code. Les logiciels sont précompilés pour les systèmes d’exploitation fréquemment utilisés et peuvent être chargés via des modules (voir [Utiliser des modules](utiliser-des-modules.md)).

CVMFS est installé sur les grappes Cedar, Graham et Béluga; l'installation sur un nuage se fait en suivant [ces directives](https://github.com/ComputeCanada/CVMFS/tree/main/cvmfs-cloud-scripts) (en anglais).

Pour plus d'information, consultez [notre page wiki Accès à CVMFS](accessing-cvmfs.md) et la [documentation du CERN](https://cvmfs.readthedocs.io/en/stable/).

## Utilisation de cloud-init
Les fichiers cloud-init sont utilisés pour initialiser une instance en particulier et pour être exécutés à l'intérieur de cette même instance. C'est en quelque sorte un moyen d'automatiser des tâches que vous feriez en ligne de commande lorsque connecté à votre instance. Ces fichiers peuvent servir par exemple à mettre à jour le système d'exploitation, installer et configurer des applications, créer des fichiers, exécuter des commandes et créer des utilisateurs et des groupes. Cloud-init peut aussi configurer d'autres outils comme [Ansible](https://docs.ansible.com/) ou [Puppet](https://puppet.com/).

La configuration de cloud-init est spécifiée en texte brut en format [YAML](https://fr.wikipedia.org/wiki/YAML). Pour savoir comment créer des fichiers, voyez la [documentation cloud-init](https://cloudinit.readthedocs.io/en/latest/). Ces fichiers peuvent être utilisés avec Terraform, le CLI, l'API Python et le tableau de bord Horizon, l'interface web d'OpenStack. Nous décrivons ici l'utilisation de cloud-init avec Horizon.

### Spécifier le fichier cloud-init
1. Démarrez une instance de manière habituelle par *Projet > Calcul > Instances*, en cliquant sur *Lancer une instance*. Configurez l'instance tel que décrit dans la section [Lancer une instance](cloud-quick-start.md#lancer-une-instance).
2. **Avant** de cliquer sur *Lancer*, sélectionnez l'onglet *Post-création* et entrez un fichier YAML cloud-init dans le champ *Source du script de personnalisation*, soit en faisant un copier-coller du fichier (méthode *Entrée directe*), soit en téléversant le fichier à partir de votre ordinateur (méthode *Fichier*). Dans des versions antérieures d'OpenStack, et en particulier IceHouse, le fichier cloud-init est copié dans une zone de texte. Retournez à l'onglet *Détails*.
3. Une fois que tous les champs sont remplis, cliquez sur *Lancer* pour créer l'instance.
La durée de l'opération peut être longue puisqu'elle dépend du contenu du fichier YAML.

### Suivi de CloudInit
Pour suivre la progression, examinez le journal de la console de l'instance.

1. Dans la colonne *Nom de l'instance*, cliquez sur l'instance pour obtenir l'information sur cette instance.
2. Sous l'onglet *Journal*, les lignes qui contiennent `cloud-init` décrivent les phases.
3. Quand Cloud-init s'arrête, la ligne suivante se trouve vers la fin du journal :

```text
Cloud-init v. 0.7.5 finished at Wed, 22 Jun 2016 17:52:29 +0000. Datasource DataSourceOpenStack [net,ver=2].  Up 44.33 seconds
```

Le rafraîchissement du journal se fait en cliquant sur le bouton *Actualiser*, en haut de la page.

## Utilisation de gabarits Heat
Les gabarits Heat sont encore plus puissants : ils peuvent être utilisés pour automatiser des tâches faites dans le tableau de bord OpenStack, par exemple créer simultanément plusieurs instances, configurer des groupes de sécurité, créer et configurer des réseaux ou créer des volumes et les attacher à des instances. Les gabarits Heat peuvent être utilisés avec des fichiers cloud-init; une fois que Heat a créé une instance, il peut passer un fichier cloud-init à cette instance pour exécuter des tâches de configuration ou même inclure dynamiquement de l'information sur d'autres ressources dans le fichier cloud-init (par exemple des IP flottantes d'autres instances).

Nous ne discutons pas ici de la création des fichiers HOT (*Heat Orchestration Template*); pour ce, consultez la [documentation officielle](http://docs.openstack.org/developer/heat/template_guide/hot_guide.html). Heat peut automatiser les tâches exécutées du tableau de bord OpenStack (Horizon) et passer aux fichiers CloudInit inclus des renseignements sur les adresses IP d'autres serveurs. L'utilisation d'un gabarit Heat ne nécessite habituellement pas la création préalable de ressources. Il est de bonne pratique de supprimer les ressources qui ne sont pas utilisées puisque les gabarits Heat consomment des ressources et qu'ils vont s'arrêter si le quota est dépassé.

Pour créer une pile avec un fichier HOT :

1. Sélectionnez *Projet > Orchestration > Piles* et cliquez sur *Lancer la pile* pour créer une nouvelle pile.
2. Dans la fenêtre *Sélectionner un modèle*, vous pouvez entrer une URL, un nom de fichier ou faire une entrée directe. Nous utiliserons un fichier HOT parmi ceux listés dans la section *Configurations disponibles* ci-après.
3. Pour *Source du modèle*, sélectionnez *URL*.
4. Collez l'adresse URL dans le champ *URL du modèle*.
5. Cliquez sur *Suivant* pour configurer les paramètres; ces derniers peuvent varier selon le gabarit utilisé, mais par défaut, toutes les piles ont :
    *   *Nom de la pile* : entrez le nom choisi.
    *   *Délai d'attente de création (minutes)* : nombre de minutes allouées à la création de la pile; habituellement, la valeur par défaut suffit.
    *   *Mot de passe pour utilisateur [nom]* : ce mot de passe est requis pour des modifications ultérieures à la pile; il est rarement utilisé puisque les piles de la section suivante ne sont pas conçues pour être modifiées.
6. Cliquez sur *Lancer* pour créer la pile.

Pour une image de la progression, cliquez sur le nom de la pile et sélectionnez l'onglet *Topologie*. Les nœuds gris indiquent que la création est en cours; les nœuds verts indiquent que la pile est créée; les nœuds rouges indiquent que la création a échoué. Une fois la pile créée, cliquez sur l'onglet *Vue d'ensemble* pour l'information sur la pile, c'est-à-dire l'URL pour accéder à un site ou à un service.