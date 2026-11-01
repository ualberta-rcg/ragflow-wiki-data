---
title: "Cloud shared security responsibility model/fr"
slug: "cloud_shared_security_responsibility_model"
lang: "fr"

source_wiki_title: "Cloud shared security responsibility model/fr"
source_hash: "b90a81a8dc276a32c727c94d3b1236f0"
last_synced: "2026-11-01T01:58:40.824100+00:00"
last_processed: "2026-11-01T02:31:00.239298+00:00"

tags:
  - cloud

keywords:
  - "plateformes infonuagiques"
  - "équipe de soutien technique"
  - "sécurité des données"
  - "groupes de recherche"
  - "responsabilité partagée"

questions:
  - "Quelles sont les responsabilités principales des groupes de recherche lorsqu’ils utilisent les environnements infonuagiques de la Fédération de l'Alliance ?"
  - "Quels rôles et quelles limites l’équipe de soutien technique assume‑t‑elle dans la gestion et la protection des plateformes infonuagiques ?"
  - "Quels engagements de conformité et quelles bonnes pratiques doivent être respectés par tous les intervenants pour assurer la sécurité et la disponibilité des services infonuagiques ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Plusieurs plateformes infonuagiques font partie de l’infrastructure de calcul de pointe de la Fédération de l'Alliance. Nous décrivons ici les responsabilités qui incombent spécifiquement aux groupes de recherche qui utilisent les environnements infonuagiques et celles qui reviennent spécifiquement à l’équipe de soutien qui gère ces environnements. D’autres aspects relatifs à la sécurité sont la responsabilité de tous les intervenants.

## Les groupes de recherche qui utilisent les environnements infonuagiques

Les responsabilités des groupes de recherche sont :
* la mise en place de mesures de contrôle adéquates pour la protection de la confidentialité, de l’intégrité et de la disponibilité de leurs données de recherche;
* l’installation et la configuration de leurs instances, y compris les systèmes d’exploitation, les services et les logiciels;
* la maintenance et les [mises à jour](security_considerations_when_running_a_vm.md) périodiques de leurs instances;
* la mise en application de règles pour les groupes de sécurité afin de limiter les services exposés à l’Internet;
* l'implémentation et les tests de procédures de sauvegarde et de restauration;
* le chiffrement des données en transit ou au repos;
* l'application du [principe de moindre privilège](https://fr.wikipedia.org/wiki/Principe_de_moindre_privil%C3%A8ge) pour allouer l’accès à leurs instances par d’autres utilisateurs.

## L’équipe de soutien technique qui gère les environnements infonuagiques

Les responsabilités de cette équipe sont :
* la protection des plateformes infonuagiques;
* la configuration et la gestion des ressources de calcul et de stockage ainsi que des bases de données et de la réseautique;
* la sécurité physique de l’infrastructure et des locaux où elle est installée.  

!!! attention "Important"
    L’équipe nationale des services infonuagiques ne gère pas les instances des utilisateurs et ne fournit aucune assistance technique relativement à ces instances. Toutefois, si une instance s’avère nuisible, l’équipe peut choisir de la fermer et de la verrouiller afin de protéger celles des autres utilisateurs. Dans de tels cas, l'équipe de recherche pourrait être invitée à fournir des plans de correction avant que l'accès à l’instance ne soit restauré, et ce, pour la protection des autres.

## Responsabilité de tous

Tous doivent se conformer aux lois, règlements, politiques, procédures et ententes contractuelles qui s’appliquent.  
L’adhésion aux politiques de la Fédération de l'Alliance et des établissements membres est requise, particulièrement en ce qui a trait à une utilisation acceptable, tel que décrit [sur notre site web](https://www.alliancecan.ca/fr/politiques). L’adoption par tous de pratiques de bonne conduite sur l’Internet préservera la réputation de nos réseaux et l’intégrité et la disponibilité de nos services infonuagiques.

!!! note "Contact"
    Pour toute autre information, écrivez à cloud@tech.alliancecan.ca.

## Références
* [Page wiki sur le service infonuagique de la Fédération de l'Alliance](cloud.md)
* [Page wiki sur la sécurité des instances](security_considerations_when_running_a_vm.md)
* [Politiques de l'Alliance](https://www.alliancecan.ca/fr/politiques)