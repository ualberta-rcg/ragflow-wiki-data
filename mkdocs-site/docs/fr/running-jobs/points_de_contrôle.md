---
title: "Points de contrôle/fr"
tags:
  []

keywords:
  []
---

L’exécution d’un programme est parfois trop longue pour la durée permise par les systèmes de soumissions qui sont sur les grappes. L’exécution d’un long programme est également tributaire des aléas des systèmes. Un programme ayant une courte durée d’exécution peut aisément être redémarré. Par contre, lorsque l’exécution du programme devient très longue, il est préférable de faire des points de contrôle pour minimiser les chances de perdre plusieurs semaines de calcul. Ceux-ci permettront par la suite le redémarrage du programme.

## Création et chargement d'un point de contrôle 
La création et le chargement d'un point de contrôle peuvent déjà être implémentés dans une application que vous utilisez. Il suffit alors d'utiliser cette fonctionnalité et de consulter la documentation à cet effet au besoin.

Cependant, si vous avez accès au code source de l'application et/ou que vous en êtes l'auteur, vous pouvez implémenter la création et le chargement de points de contrôle. À la base:

* La création d'un fichier de point de contrôle se fait de façon périodique. On suggère des périodes de 2 à 24 heures
* Pendant l'écriture du fichier, il faut garder en tête que la tâche de calcul peut être interrompue à tout moment, et ce, pour toute sorte de raison technique. Par conséquent:
** Il est préférable de ne pas écraser le précédent point de contrôle en créant le nouveau
** On peut rendre l'écriture *atomique* en effectuant une opération qui vient confirmer la fin de l'écriture du point de contrôle. Par exemple, on peut initialement nommer le fichier en fonction de la date et l'heure et, finalement, créer un lien symbolique "derniere-version" vers le nouveau fichier de point de contrôle ayant un nom unique. Autre méthode plus avancée : on peut créer un second fichier contenant une somme de hachage du point de contrôle, permettant ainsi de valider l'intégrité du point de contrôle à son éventuel chargement
** Une fois l'écriture atomique complétée, on peut décider de supprimer ou non des vieux points de contrôle

<!--
Afin de ne pas réinventer la roue, surtout si la modification du code source n'est pas une option, nous suggérons l'utilisation de [DMTCP](http://dmtcp.sourceforge.net/).

=== DMTCP === 

Le logiciel [DMTCP](http://dmtcp.sourceforge.net/) (Distributed Multithreaded CheckPointing) permet de faire des points de contrôles de programmes sans avoir à les recompiler.  La première exécution est effectuée avec le programme <tt>dmtcp_launch</tt> en spécifiant le temps entre les intervalles de sauvegarde. Le redémarrage se fait en exécutant le script <tt>dmtcp_restart_script.sh</tt>. Par défaut, ce script et les fichiers de redémarrage du programme sont écrits à l'endroit où le programme a été lancé. On peut changer l’emplacement des fichiers de sauvegarde  avec l’option <tt>--ckptdir <répertoire pour les sauvegardes></tt>. Vous pouvez faire <tt>dmtcp_launch --help</tt> pour obtenir toutes les options. Notez que DMTCP ne marche pas pour le moment avec les logiciels parallélisés par MPI. 

Un exemple de script:
-->
<!--

-->
## Resoumettre une tâche pour un calcul de longue durée 
Si on prévoit qu'un long calcul sera morcelé en plusieurs tâches Slurm, les [deux méthodes recommandées](running-jobs-fr#resoumettre_une_t.c3.a2che_pour_un_calcul_de_longue_dur.c3.a9e.md) sont:
* [l'utilisation de vecteurs de tâches (*job arrays*) Slurm](running_jobs-fr#red.c3.a9marrage_avec_des_vecteurs_de_t.c3.a2ches.md);
* [la resoumission à partir de la fin du script](running_jobs-fr#resoumettre_.c3.a0_partir_d.27un_script.md).