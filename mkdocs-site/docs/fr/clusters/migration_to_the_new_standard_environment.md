---
title: "Migration to the new standard environment/fr"
slug: "migration_to_the_new_standard_environment"
lang: "fr"

source_wiki_title: "Migration to the new standard environment/fr"
source_hash: "ca7c3ba31589384b360a25e168e4265e"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T08:34:06.090831+00:00"

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

## Quelles sont les différences entre `StdEnv/2023` et les autres environnements standards?
Référez-vous à la page [Environnements logiciels standards](standard-software-environments.md).

## Puis-je changer mon environnement standard par défaut?
Après le 1er avril 2024, **`StdEnv/2023` sera l'environnement par défaut pour toutes nos grappes**. Il reste toutefois possible de modifier le fichier `$HOME/.modulerc`. Par exemple, la commande suivante fera en sorte que votre environnement par défaut sera `StdEnv/2020`:

```bash
echo "module-version StdEnv/2020 default" >> $HOME/.modulerc
```

!!! note
    Pour que ceci prenne effet, vous devez vous déconnecter et vous reconnecter à nouveau.

## Faut-il réinstaller/recompiler le code quand l'environnement standard est modifié?
Oui. Si vous compilez votre propre code ou que vous avez installé des paquets R ou Python, vous devez recompiler ou réinstaller les paquets avec le nouvel environnement.

## Comment puis-je utiliser un environnement moins récent?
Si vous avez des travaux en cours et que vous ne voulez pas changer les versions des logiciels que vous utilisez présentement, ajoutez à vos scripts de tâche la commande

```bash
module load StdEnv/2020
```
avant de charger d’autres modules.

## Les versions moins récentes seront-elles effacées?
Les environnements moins récents resteront disponibles ainsi que les logiciels qui en dépendent.

!!! warning
    Par contre, les versions **2016.4 et 2018.3 ne sont plus supportées** et nous vous recommandons de ne pas les utiliser. Notre équipe n'installera des logiciels que dans le nouvel environnement 2023.

## Est-il possible d'utiliser ensemble des modules qui proviennent de différents environnements?

!!! warning
    Non, vous obtiendrez des résultats imprévisibles et sans doute des erreurs. Dans chaque tâche, vous pouvez explicitement charger l’un ou l’autre des environnements, mais seulement un environnement par tâche.

## Quel environnement devrais-je utiliser?
Nous vous recommandons d'utiliser `StdEnv/2023` pour vos nouveaux projets ou si vous voulez utiliser une version plus récente d'un logiciel. Pour ce faire, ajoutez à vos scripts de tâches la commande

```bash
module load StdEnv/2023
```
Il n’est pas nécessaire de supprimer cette commande pour utiliser `StdEnv/2023` après le 1er avril.

## Puis-je conserver mon environnement actuel en chargeant des modules dans mon `.bashrc`?

!!! warning
    Il n’est pas recommandé de charger des modules dans votre `.bashrc`. Chargez plutôt les modules via les scripts pour vos tâches.

## J'utilise uniquement des ressources infonuagiques; est-ce que le changement d'environnement me concerne?
Non, ce changement ne touche que l'utilisation des [logiciels disponibles](available-software.md) qui sont [chargés via les modules](utiliser-des-modules.md).

## Je ne peux plus charger un module que j’utilisais avant le changement
Le nouvel environnement contient des versions plus récentes de la plupart des applications. Pour connaître ces versions, lancez la commande `module avail`. Par exemple,

```bash
module avail gcc
```
montre plusieurs versions des compilateurs GCC, qui sont peut-être différentes de celles des environnements moins récents.