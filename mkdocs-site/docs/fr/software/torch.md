---
title: "Torch/fr"
tags:
  - software
  - ai-and-machine-learning

keywords:
  []
---

[Torch](http://torch.ch/) est une plateforme logicielle pour le calcul scientifique qui utilise principalement les GPU et qui permet de travailler avec plusieurs algorithmes d'apprentissage machine. Sa facilité d'utilisation et son efficacité sont dues au langage de script LuaJIT et à l'implémentation sous-jacente de C/CUDA. 

Il y a une certaine ressemblance entre Torch et PyTorch. Les documents en référence discutent de leurs différences.<ref>https://stackoverflow.com/questions/44371560/what-is-the-relationship-between-pytorch-and-torch, https://www.quora.com/What-are-the-differences-between-Torch-and-Pytorch, et https://discuss.pytorch.org/t/torch-autograd-vs-pytorch-autograd/1671/4.</ref> PyTorch offre une interface [Python](python-fr.md) avec des logiciels qui possèdent des fonctionnalités similaires, mais PyTorch ne dépend pas de Torch. Voyez la page [PyTorch](pytorch-fr.md).

Pour utiliser Torch vous devez charger un module [CUDA](cuda-fr.md).

```bash
module load cuda torch
```

## Installation de paquets Lua 
Torch comprend [luarocks](https://luarocks.org/) pour la gestion des paquets Lua. Pour la liste des paquets installés, lancez 
  luarocks list

Si vous avez besoin d'un paquet qui ne se trouve pas dans la liste, utilisez la commande suivante pour l'installer dans votre propre répertoire. 

```bash

```
all <package name>}}

Si vous avez de la difficulté à trouver les paquets à l'exécution, ajoutez la commande suivante  juste avant de lancer votre programme Lua<ref> https://github.com/luarocks/luarocks/wiki/Using-LuaRocks#Rocks_trees_and_the_Lua_libraries_path </ref> :

 eval $(luarocks path --bin)

Certains paquets ne s'installent pas bien avec <tt>luarocks</tt>; si vous avez besoin d'assistance, contactez le [soutien technique](technical-support-fr.md).

<references />