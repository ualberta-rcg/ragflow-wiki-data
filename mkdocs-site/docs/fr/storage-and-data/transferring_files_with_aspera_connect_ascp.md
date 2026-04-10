---
title: "Transferring files with Aspera Connect/ascp/fr"
tags:
  []

keywords:
  []
---

ascp est un  logiciel utilisé pour transférer des données en provenance et à destination de serveurs de transfert Aspera sur lesquels vous détenez une licence, par exemple pour téléverser un jeu de données dans un dépôt de données. 

Plusieurs serveurs de transfert exigent une version à jour du logiciel, appelé maintenant Aspera Connect. En raison de certaines modifications qui y ont été apportées, vous devrez peut-être installer localement la plus récente version.

=ascp 3.5.4=
Dans les piles logicielles moins récentes, ce logiciel est disponible via un module.

Si le serveur de destination est incompatible avec cette version, vous pourriez obtenir une erreur comme

<pre>
Error with Aspera:

ascp: failed to authenticate, exiting.

Session Stop  (Error: failed to authenticate)
</pre>

=Aspera Connect/ascp 4+=

Pour utiliser Aspera Connect (auparavant nommé <i>ascp</i>), vous devez [l'installer dans un de vos répertoires locaux](installing_software_in_your_home_directory-fr.md).

1. Copiez le lien pour la plus récente version de Linux à partir du   [site web pour Aspera Connect](https://www.ibm.com/aspera/connect).

2. Positionnez-vous dans le répertoire où vous voulez installer le logiciel, par exemple votre répertoire /home.

3. Téléchargez le logiciel dans ce répertoire avec wget.

` wget link-i-copied-here `

4. Extrayez le logiciel de l'archive.

` tar -zxf ibm-aspera-connect_some_version_linux.tar.gz `

5. Lancez le script d'installation.

` bash ibm-aspera-connect_some_version_linux.sh `

5a. Rendez exécutables les fichiers de la bibliothèque.

` chmod u+x ~/.aspera/connect/plugins/*/*.so ~/.aspera/connect/lib/* `

6. Lancez le script setrpaths.
 
` setrpaths.sh --path $HOME/.aspera `

7. (Optionnel) Ajoutez les binaires ascp à votre chemin (PATH).

` export PATH=~/.aspera/connect/bin:$PATH`