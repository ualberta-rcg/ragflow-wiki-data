---
title: "Torch/fr"
slug: "torch"
lang: "fr"

source_wiki_title: "Torch/fr"
source_hash: "6ff8e7461ef74ccb74f9ee05bcf2c5df"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:59:54.311497+00:00"

tags:
  - software
  - ai-and-machine-learning

keywords:
  - "calcul scientifique"
  - "apprentissage machine"
  - "CUDA"
  - "paquets Lua"
  - "Torch"

questions:
  - "Qu'est-ce que la plateforme Torch et quelles technologies sous-jacentes assurent son efficacité ?"
  - "Quelle est la différence principale entre Torch et PyTorch selon le texte ?"
  - "Comment peut-on installer et gérer des paquets Lua supplémentaires à l'aide de luarocks dans l'environnement Torch ?"
  - "Qu'est-ce que la plateforme Torch et quelles technologies sous-jacentes assurent son efficacité ?"
  - "Quelle est la différence principale entre Torch et PyTorch selon le texte ?"
  - "Comment peut-on installer et gérer des paquets Lua supplémentaires à l'aide de luarocks dans l'environnement Torch ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Torch](http://torch.ch/) est une plateforme logicielle pour le calcul scientifique qui utilise principalement les GPU et qui permet de travailler avec plusieurs algorithmes d'apprentissage machine. Sa facilité d'utilisation et son efficacité sont dues au langage de script LuaJIT et à l'implémentation sous-jacente de C/CUDA.

Il y a une certaine ressemblance entre Torch et PyTorch. Les documents en référence discutent de leurs différences :
*   [https://stackoverflow.com/questions/44371560/what-is-the-relationship-between-pytorch-and-torch](https://stackoverflow.com/questions/44371560/what-is-the-relationship-between-pytorch-and-torch)
*   [https://www.quora.com/What-are-the-differences-between-Torch-and-Pytorch](https://www.quora.com/What-are-the-differences-between-Torch-and-Pytorch)
*   [https://discuss.pytorch.org/t/torch-autograd-vs-pytorch-autograd/1671/4](https://discuss.pytorch.org/t/torch-autograd-vs-pytorch-autograd/1671/4)

PyTorch offre une interface [Python](python.md) avec des logiciels qui possèdent des fonctionnalités similaires, mais PyTorch ne dépend pas de Torch. Voyez la page [PyTorch](pytorch.md).

Pour utiliser Torch, vous devez charger un module [CUDA](cuda.md).

```bash
module load cuda torch
```

## Installation de paquets Lua
Torch comprend [luarocks](https://luarocks.org/) pour la gestion des paquets Lua. Pour la liste des paquets installés, lancez :

```bash
luarocks list
```

Si vous avez besoin d'un paquet qui ne se trouve pas dans la liste, utilisez la commande suivante pour l'installer dans votre propre répertoire.

```bash
luarocks install --local --deps-mode=all <nom_du_paquet>
```

Si vous avez de la difficulté à trouver les paquets à l'exécution, ajoutez la commande suivante juste avant de lancer votre programme Lua ([https://github.com/luarocks/luarocks/wiki/Using-LuaRocks#Rocks_trees_and_the_Lua_libraries_path](https://github.com/luarocks/luarocks/wiki/Using-LuaRocks#Rocks_trees_and_the_Lua_libraries_path)) :

```bash
eval $(luarocks path --bin)
```

Certains paquets ne s'installent pas bien avec `luarocks`; si vous avez besoin d'assistance, contactez le [soutien technique](technical-support.md).