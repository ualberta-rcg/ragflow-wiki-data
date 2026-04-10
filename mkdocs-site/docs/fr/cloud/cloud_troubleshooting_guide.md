---
title: "Cloud troubleshooting guide/fr"
slug: "cloud_troubleshooting_guide"
lang: "fr"

source_wiki_title: "Cloud troubleshooting guide/fr"
source_hash: "88ea40163fcef44332164de3a92b1526"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T05:42:45.376743+00:00"

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

!!! note
Nous apportons ici des solutions à des problèmes qui se posent fréquemment quand vous travaillez avec une instance dans nos environnements infonuagiques. Vous pouvez essayer de résoudre par vous-même certains de ces problèmes, mais d’autres nécessitent l’intervention d’un administrateur de système. Dans ce cas, nous fournissons des conseils sur comment faire une demande d’assistance et quels renseignements y inclure.

## Problème de connexion à un nuage

1.  Pour vous connecter à un de nos nuages, vous devez avoir [demandé un nouveau projet infonuagique](cloud.md#obtenir-un-projet-dans-lenvironnement-infonuagique) ou avoir demandé l’accès à un projet infonuagique existant, sans quoi vous recevrez le message *Données d'identification non valides*. [Remplissez le formulaire de demande](https://docs.google.com/forms/d/e/1FAIpQLSdLOro7wY__sFUBjRNu_ZQ7sgjUpTn7lvNuI2e015oAsFPWbQ/viewform?hl=fr).
2.  Dans les jours suivant votre demande, vous recevrez un courriel de confirmation avec les renseignements sur comment accéder à votre projet. Si vous n’avez pas reçu ce courriel après trois jours, écrivez à nuage@tech.alliancecan.ca en indiquant votre nom d’utilisateur, le nom de votre établissement et l’adresse de courriel que vous avez utilisée pour soumettre votre demande de projet.
3.  Le courriel de confirmation contient le nom du nuage où se trouve votre projet. Pour les adresses des nuages, voyez [Utiliser les ressources infonuagiques](cloud.md#utiliser-les-ressources-infonuagiques).
4.  Si vous avez reçu un courriel de confirmation et que vous ne pouvez toujours pas vous connecter, vérifiez si un incident est rapporté sur la page [État des ressources](system-status.md).
5.  Utilisez le même nom d’utilisateur que celui associé à votre compte avec l'Alliance (le même que vous utilisez pour vous connecter à une grappe). **N’utilisez pas votre adresse de courriel**. Pour vérifier vos informations d'identification, essayez de vous [connecter à la base de données CCBD](https://ccdb.alliancecan.ca/security/login).
6.  Au besoin, [réinitialisez votre mot de passe](https://ccdb.alliancecan.ca/security/forgot).
7.  Si vous ne pouvez toujours pas accéder à votre projet, écrivez à nuage@tech.alliancecan.ca en indiquant votre nom, votre nom d’utilisateur, le nom du nuage, le nom du projet et une description des démarches que vous avez tentées.

Pour plus d’information sur comment obtenir de l’aide, consultez la page [Soutien technique](technical-support.md).

## Impossible de lancer une instance

1.  Si votre instance ne peut être lancée, vérifiez si une des ressources sollicitées n’a pas atteint le quota prescrit. Votre projet est soumis à des quotas et limité en termes d’instances, de CPU et de gigabits de mémoire pouvant être utilisés. Une instance ne démarrera pas si elle cause un dépassement d’un de ces quotas. Pour vérifier votre utilisation des ressources, connectez-vous au nuage où se trouve votre projet (voir [les liens de connexion aux nuages](cloud.md#utiliser-les-ressources-infonuagiques)). Dans le menu de gauche, cliquez sur *Compute* puis sur *Vue d’ensemble*. Si ces ressources ne sont pas suffisantes pour votre projet, soumettez un [formulaire de demande pour des ressources supplémentaires](https://docs.google.com/forms/d/e/1FAIpQLSdLOro7wY__sFUBjRNu_ZQ7sgjUpTn7lvNuI2e015oAsFPWbQ/viewform?hl=fr). Pour plus d'information sur les quotas et les allocations de plus de 10To, voyez [Ressources infonuagiques avec le service d'accès rapide](cloud-ras-allocations.md).
2.  Si vous recevez le message `N'a pas pu effectuer l'opération demandée sur l'instance "...", l'instance a un statut d'erreur: Veuillez essayer à nouveau ultérieurement [Error: No valid host was found. There are not enough hosts available.]`, vérifiez le contenu du champ *Zone de disponibilité*.
    1.  Quand une instance est lancée, l’option *Détails* vous demande d’entrer un nom, une description et aussi une zone de disponibilité. Par défaut, la sélection est *Toute zone de disponibilité*, ce qui laisse le choix à OpenStack. Si vous n’utilisez pas la valeur par défaut, mais que vous l’entrez manuellement, il se pourrait que le message d’erreur soit affiché. Entrez la valeur par défaut.
    2.  Si vous recevez toujours le message ou que vous devez sélectionner une autre valeur pour la zone de disponibilité, écrivez à nuage@tech.alliancecan.ca en indiquant votre nom d’utilisateur, le nom du nuage, le nom du projet, le UUID du volume et la description des démarches que vous avez tentées.
3.  Si vous ne parvenez toujours pas à lancer l’instance, écrivez à nuage@tech.alliancecan.ca en indiquant votre nom d’utilisateur, le nom du nuage, le nom du projet, le UUID du volume et les renseignements obtenus par les démarches que vous avez tentées.

Pour plus d’information sur comment obtenir de l’aide, consultez la page [Soutien technique](technical-support.md).

## Problème de connexion à une instance

1.  Si vous ne pouvez pas vous connecter à votre instance ou à un de ses services, vérifiez si un incident est rapporté pour le nuage sur la page [État des ressources](system-status.md). Si c’est le cas, vous devrez attendre que la situation revienne à la normale.
2.  Si aucun incident n’est rapporté pour le nuage, essayez de vous y connecter via le tableau de bord OpenStack. Par exemple, si votre projet se trouve sur Arbutus, connectez-vous avec https://arbutus.alliancecan.ca. Les liens vers les autres nuages se trouvent dans la section [Utiliser les ressources infonuagiques](cloud.md).
3.  Si vous êtes toujours incapable de vous connecter, testez votre connexion internet en essayant de rejoindre une page comme [https://www.google.com](https://www.google.com) avec votre navigateur. Si votre connexion internet n’est pas en cause, écrivez à nuage@tech.alliancecan.ca en indiquant votre nom, votre nom d’utilisateur, le nom du projet, le nom du nuage et une description des démarches que vous avez tentées. Pour plus d’information sur comment obtenir de l’aide, consultez la page [Soutien technique](technical-support.md).
4.  Si la page de connexion au nuage est affichée mais que vous ne pouvez pas vous connecter, référez-vous à la section 'Problème de connexion à un nuage' ci-dessus.
5.  Si vous pouvez vous connecter au tableau de bord OpenStack, il y a quelques façons de savoir si votre instance est en fonctionnement :
    1.  Dans le menu de gauche, sélectionnez *Compute*, puis *Instances*. La colonne *État de l’alimentation* devrait afficher *En fonctionnement*. Si ce n’est pas le cas, sélectionnez *Démarrer une instance* (ou *Redémarrer une instance*, selon votre interface) dans le menu déroulant *Actions*.
        *   Vérifiez le log des actions en cliquant sur le nom de l’instance et en sélectionnant l’onglet *Log des actions*. Le log montre toutes les actions reliées à l’instance; si vous ne reconnaissez pas l’une d’elles, écrivez à nuage@tech.alliancecan.ca en indiquant votre nom, votre nom d’utilisateur, le nom du nuage, le nom du projet et l’ID d’utilisateur.
        *   Vérifiez aussi le contenu sous l’onglet *Console* qui pourrait afficher des messages d’erreur.
    2.  Si vous ne pouvez pas redémarrer votre instance, écrivez à nuage@tech.alliancecan.ca en indiquant votre nom, votre nom d’utilisateur, le nom du nuage, le nom du projet, l’ID de l’instance et une description de votre problème et des démarches que vous avez tentées. Pour connaître l’ID de l’instance, cliquez sur le nom de l’instance et sélectionnez l'onglet *Vue d’ensemble*. Pour plus d’information sur comment obtenir de l’aide, consultez la page [Soutien technique](technical-support.md).
6.  Vérifiez si vous pouvez accéder à votre instance par SSH (protocole *Secure Shell*).
    1.  Si vous ne pouvez accéder à l’application ou au service web de votre instance, que vous avez vérifié les points 1 à 4 et que votre instance est en fonctionnement, essayez de vous connecter par SSH en suivant [ces directives](cloud-quick-start.md).
    2.  Si une invite de connexion est affichée, assurez-vous d’utiliser la bonne paire de clés et le bon nom d’utilisateur. Pour savoir quelle paire de clés utiliser, sélectionnez *Compute* puis *Instances* dans le menu OpenStack et regardez dans la colonne *Paire de clés*. Le nom d’utilisateur dépend du système d’exploitation.

        | Système d'exploitation | Nom d'utilisateur |
        | :--------------------- | :---------------- |
        | Debian                 | debian            |
        | Ubuntu                 | ubuntu            |
        | AlmaLinux              | almalinux         |
        | CentOS                 | centos            |
        | Fedora                 | fedora            |

        Ces noms ne s’appliquent pas si vous avez modifié le nom d’utilisateur avec un script CloudInit personnalisé. Dans ce cas, le nom d’utilisateur sera celui que vous avez entré.
    3.  Si une invite de connexion n’est pas affichée, vérifiez vos paramètres de sécurité.
        *   Assurez-vous que votre propre adresse IP n’a pas changé. Testez votre adresse IP en entrant [https://ipv4.icanhazip.com/](https://ipv4.icanhazip.com/) dans votre navigateur. Vos paramètres de sécurité doivent accepter votre adresse IP pour que vous puissiez vous connecter à votre instance. Si votre adresse a changé, ajoutez une nouvelle règle à votre groupe de sécurité comme expliqué ci-dessous.
        *   Assurez-vous que votre adresse IP est débloquée pour SSH. Dans le tableau de bord OpenStack, sélectionnez *Réseau*, puis *Groupes de sécurité*. À la fin de la ligne pour le groupe relié à votre instance, sélectionnez *Gérer les règles* dans le menu déroulant *Actions*. Si vous n’avez pas configuré un autre groupe, celui-ci sera le groupe par défaut. Il devrait y avoir une règle *Entrée* dans la colonne *Direction*, la valeur TCP dans la colonne *Protocole IP*, la valeur 22 (SSH) dans la colonne *Plage de ports* et your-ip-address/32 dans la colonne *Préfixe IP distante*. Si cette règle est absente, cliquez sur *+Ajouter une règle* et sélectionnez *SSH* dans le menu déroulant *Règle*, entrez your-ip-address/32 dans le champ *CIDR* et cliquez sur le bouton *Ajouter*.
7.  Si vous ne pouvez toujours pas vous connecter à l’instance, écrivez à nuage@tech.alliancecan.ca en indiquant votre nom, votre nom d’utilisateur, le nom du nuage, le nom du projet, l’UUID de l’instance et les renseignements obtenus par les démarches que vous avez tentées. Pour trouver l’UUID de l’instance, sélectionnez *Compute* puis *Instances* et cliquez sur le nom de l’instance. Sous l’onglet *Vue d’ensemble*, l’UUID est la longue chaîne de caractères (lettres, chiffres et tiret) qui se trouve sur la ligne ID.

Pour plus d’information sur comment obtenir de l’aide, consultez la page [Soutien technique](technical-support.md).

## Impossible de supprimer un volume

1.  Vous ne pouvez pas supprimer un volume qui est attaché à une instance en fonctionnement. Pour vérifier ceci, connectez-vous au nuage où se trouve votre projet. Dans le menu de gauche du tableau de bord OpenStack, sélectionnez *Volumes* puis *Volumes*. La colonne *Attaché à* est vide si le volume n’est attaché à aucune instance, autrement, vous devez détacher le volume de l’instance avant de pouvoir le supprimer (voir [Détacher un volume](working-with-volumes.md#detacher-un-volume)).
2.  Une fois que le volume est détaché, vérifiez son statut. Dans le menu de gauche, sélectionnez *Volumes* puis *Volumes*. Si la colonne *Statut* montre *disponible(s)*, passez à l’étape 3. Autrement, si la colonne montre *En cours d’utilisation*, écrivez à nuage@tech.alliancecan.ca en indiquant votre nom, votre nom d’utilisateur, le nom du nuage, le nom du projet, l’UUID de l’instance et les renseignements obtenus par les démarches que vous avez tentées.
3.  Avant de supprimer un volume, il faut supprimer les instantanés attachés à ce volume, s’il y a lieu. Pour vérifier si le volume a des instantanés, sélectionnez *Volumes* puis *Instantanés*. La colonne *Nom du volume* montre le volume auquel l’instantané est attaché s’il y a lieu. Dans le menu déroulant *Actions*, sélectionnez *Supprimer l'instantané de volume*.
4.  Si vous ne pouvez toujours pas supprimer le volume, écrivez à nuage@tech.alliancecan.ca en indiquant votre nom, votre nom d’utilisateur, le nom du nuage, le nom du projet, l’UUID du volume et les renseignements obtenus par les démarches que vous avez tentées.

Pour plus d’information sur comment obtenir de l’aide, consultez la page [Soutien technique](technical-support.md).