---
title: "Migrating between clusters/fr"
slug: "migrating_between_clusters"
lang: "fr"

source_wiki_title: "Migrating between clusters/fr"
source_hash: "5b6f05be1e01bf083108ccde43e3068e"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:32:54.050392+00:00"

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

Nos grappes sont plutôt uniformes, en particulier les grappes d'usage général. Cependant, il y a certaines différences importantes que vous devez connaître lors de la migration d'une grappe à l'autre. Vous trouverez ci-dessous les points communs entre toutes les grappes ainsi que les modifications que vous devez faire quand vous migrez vers une nouvelle grappe.

Pour déplacer des données d’une grappe à l’autre, nous vous recommandons d’utiliser [Globus](globus.md), surtout quand la quantité de données dépasse quelques centaines de mégaoctets.

## Accès à nos grappes

L'accès à nos grappes se fait par [SSH](ssh.md); il suffit d'utiliser le nom particulier de la grappe à laquelle vous voulez accéder. Votre nom d'utilisateur et votre mot de passe serviront à vous connecter à toutes nos grappes. Par contre, l'accès à Niagara nécessite une étape supplémentaire qui est [décrite dans la section *Accès* de la page pour Niagara](niagara.md#accès).

## Systèmes de fichiers

Si les systèmes de fichiers de nos grappes ont tous des [structures similaires](storage-and-file-management.md), il faut se rappeler que vos données se trouvent sur une seule grappe et que le contenu de vos espaces /home, /scratch et /project sur une grappe n'est pas répliqué sur une autre grappe.
Il faut aussi savoir que les [quotas et politiques](storage-and-file-management.md#quotas-et-politiques) varient quelque peu d'une grappe à l'autre. Si vous travaillez avec un groupe qui dispose d’une allocation de stockage spéciale sur une grappe, par exemple `$HOME/projects/rrg-jsmith`, elle ne sera habituellement disponible que sur cette grappe spécifique. De même, si votre groupe a demandé que le quota par défaut pour l’espace /project dans une grappe soit augmenté de 1 à 10 To, cette augmentation se fera uniquement sur cette grappe.

## Logiciel

Dans les grappes d’usage général, plusieurs [modules](utiliser-des-modules.md) sont disponibles à tous les utilisateurs et distribués par CVMFS. Pour cette raison, vous ne devriez pas remarquer de grandes différences entre les logiciels disponibles si vous utilisez le même [environnements logiciels standards](standard-software-environments.md). Par contre, les [environnements virtuels Python](python.md#créer-et-utiliser-un-environnement-virtuel) et les paquets [R](r.md#installation-des-paquets-r) et [Perl](perl.md#installer-des-paquets) que vous aurez installés dans un répertoire d’une grappe devront être installés de nouveau sur la nouvelle grappe en suivant les mêmes étapes que lors de l’installation sur la grappe d’origine. De même, si vous avez personnalisé votre environnement sur une grappe en modifiant le fichier `$HOME/.bashrc`, vous devrez modifier le même fichier sur la nouvelle grappe. Si vous avez installé un logiciel particulier dans vos répertoires, vous devrez aussi les installer de nouveau sur la nouvelle grappe puisque, comme mentionné ci-dessus, les systèmes de fichiers de grappes différentes ne dépendent pas les uns sur les autres.

## Pour soumettre des tâches

Toutes nos grappes utilisent l’ordonnanceur Slurm pour gérer les tâches; ainsi, une grande partie d’un script pour soumettre une tâche fonctionnera partout. Notez toutefois que les grappes n’ont pas le même nombre de cœurs CPU par nœud ou par GPU; vérifiez donc le nombre de cœurs que vous pouvez utiliser sur un autre nœud. Il est aussi possible que vous deviez adapter votre script en raison d’une différence dans la quantité de mémoire.

Sur certaines grappes, les nœuds de calcul n'ont peut-être pas accès direct à l’Internet. Pour connaître les politiques particulières à chacune, cliquez sur le nom de la grappe dans le menu de gauche de cette fenêtre.

Toutes les professeures et tous les professeurs ont accès à une allocation par défaut sur chacune des grappes, par exemple `#SBATCH --account=def-jsmith`; cependant, les allocations spéciales pour les groupes de recherche et les allocations contribuées sont associées à une grappe en particulier et ne sont pas disponibles sur les autres grappes.