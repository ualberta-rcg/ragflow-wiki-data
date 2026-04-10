---
title: "Diskusage Explorer/fr"
tags:
  []

keywords:
  []
---

<span id="Content_of_folders"></span>
## Contenu des répertoires

<span style="color:red">Important : Pour l'instant, cet outil est seulement disponible sur [Narval](narval.md).</span>

L'outil Diskusage Explorer vous permet d'obtenir le détail de l'utilisation de l'espace dans vos répertoires /home, /scratch et /project. Cette information est mise à jour quotidiennement et est triée selon un format [SQLite](sqlite-fr.md) pour un accès rapide. 

Dans notre exemple, nous verrons la consommation de l'espace disque du répertoire `def-professor` dans /project.

### Interface ncurse 
Sélectionnez un espace /project auquel vous avez accès et que vous voulez analyser; dans notre exemple, nous analysons <tt>def-professor</tt>.

```bash
diskusage_explorer /project/def-professor
```

Cette commande charge un navigateur qui montre les ressources consommées par tous les fichiers dans l'arborescence d'un répertoire.
[thumb|using|450px|frame|left| Naviguer avec l'outil ncurse de duc](file:ncurse-duc.png.md)
<br clear=all> <!-- This is to prevent the next section from filling to the right of the image. -->

Entrez `c` pour alterner entre l'espace disque consommé et le nombre de fichiers, `q` ou <code><esc></code> pour quitter et `h` pour l'aide.

Pour ne consulter qu'un sous-répertoire de cet espace /project sans avoir à naviguer dans toute l'arborescence, utilisez  

```bash
diskusage_explorer /project/def-professor/subdirectory/
```

La commande `man duc` affiche une page du manuel.

<span id="Graphical_user_interface"></span>
### Interface graphique 

Si le nœud de connexion est particulièrement occupé ou si vous avez un trop grand nombre de fichiers dans votre espace /project, l'affichage peut être lent et irrégulier. Pour de meilleurs résultats, voyez comment utiliser `diskusage_explorer` sur votre propre ordinateur.

Nous recommandons d'utiliser le mode texte ncurse standard sur nos nœuds de connexion, mais `diskusage_explorer` inclut aussi une belle interface graphique. 

Assurez-vous d'abord que votre connexion [SSH](ssh-fr.md) fait en sorte que l'affichage des applications d'interfaces se fait correctement. Vous pouvez alors utiliser une interface graphique avec la commande

```bash
duc gui -d /project/.duc_databases/def-professor.sqlite  /project/def-professor
```

Vous pouvez naviguer avec la souris et aussi utiliser `c` pour alterner entre la taille des fichiers et le nombre de fichiers.

[thumb|using|450px|frame|left|Naviguer avec l'outil d'interface graphique de duc](file:duc-gui-navigation.gif.md)
<br clear=all> <!-- This is to prevent the next section from filling to the right of the image. -->

<span id="Browse_faster_on_your_own_machine"></span>
### Naviguer plus rapidement sur votre ordinateur 

[Installez d'abord le logiciel diskusage_explorer](http://duc.zevv.nl/#download) sur votre ordinateur local puis, toujours sur votre ordinateur local, téléchargez le fichier SQLite de votre grappe et lancez `duc`.  

<pre>
rsync -v --progress username@beluga.calculcanada.ca:/project/.duc_databases/def-professor.sqlite  .
duc gui -d ./def-professor.sqlite  /project/def-professor
</pre>

Vous pourrez ainsi naviguer de manière plus agréable.