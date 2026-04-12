---
title: "Cloud shared security responsibility model/fr"
slug: "cloud_shared_security_responsibility_model"
lang: "fr"

source_wiki_title: "Cloud shared security responsibility model/fr"
source_hash: "ca2a4abe6f83a286f8dea51f0a25d560"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T06:25:59.142516+00:00"

tags:
  - cloud

keywords:
  - "équipe de soutien"
  - "sécurité"
  - "responsabilités"
  - "plateformes infonuagiques"
  - "groupes de recherche"

questions:
  - "Quelles sont les responsabilités spécifiques des groupes de recherche concernant la configuration et la sécurité de leurs instances infonuagiques ?"
  - "Quel est le rôle de l'équipe de soutien technique et dans quelles circonstances exceptionnelles peut-elle intervenir sur l'instance d'un utilisateur ?"
  - "Quelles sont les obligations communes à tous les intervenants en matière de conformité et de politiques d'utilisation ?"
  - "Quelles sont les responsabilités spécifiques des groupes de recherche concernant la configuration et la sécurité de leurs instances infonuagiques ?"
  - "Quel est le rôle de l'équipe de soutien technique et dans quelles circonstances exceptionnelles peut-elle intervenir sur l'instance d'un utilisateur ?"
  - "Quelles sont les obligations communes à tous les intervenants en matière de conformité et de politiques d'utilisation ?"

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
* la maintenance et les [mises à jour](security_considerations_when_running_a_vm.md#mise-a-jour-d-une-instance-virtuelle) périodiques de leurs instances;
* la mise en application de règles pour les groupes de sécurité afin de limiter les services exposés à l’Internet;
* l'implémentation et les tests de procédures de sauvegarde et de restauration;
* le chiffrement des données en transit ou au repos;
* l'application du [principe de moindre privilège](https://fr.wikipedia.org/wiki/Principe_de_moindre_privil%C3%A8ge) pour allouer l’accès à leurs instances par d’autres utilisateurs.

## L’équipe de soutien technique qui gère les environnements infonuagiques
Les responsabilités de cette équipe sont :
* la protection des plateformes infonuagiques;
* la configuration et la gestion des ressources de calcul et de stockage ainsi que des bases de données et de la réseautique;
* la sécurité physique de l’infrastructure et des locaux où elle est installée.

!!! warning "Instances nuisibles"
    L’équipe nationale des services infonuagiques ne gère pas les instances des utilisateurs et ne fournit aucune assistance technique relativement à ces instances. Par contre, quand une instance s’avère nuisible, l’équipe peut choisir de la fermer et de la verrouiller afin de protéger celles des autres utilisateurs. Dans ces cas, l'équipe de recherche peut être invitée à fournir des plans de correction avant que l'accès à l’instance ne soit restauré, et ce, pour la protection des autres.

## Responsabilité de tous
Tous doivent se conformer aux lois, règlements, politiques, procédures et ententes contractuelles qui s’appliquent.
L’adhésion aux politiques de la Fédération de l'Alliance et des établissements membres est requise, particulièrement en ce qui a trait à une utilisation acceptable, tel que décrit aux [Conditions d’utilisation](https://alliancecan.ca/sites/default/files/2022-03/1-Conditions-d%E2%80%99utilisation.pdf). L’adoption par tous de pratiques de bonne conduite sur l’internet préservera la réputation de nos réseaux et l’intégrité et la disponibilité de nos services infonuagiques.

Pour toute autre information, écrivez à cloud@tech.alliancecan.ca.

## Références
* [Page wiki sur le service infonuagique de la Fédération de l'Alliance](cloud.md)
* [Page wiki sur la sécurité des instances](security_considerations_when_running_a_vm.md)
* [Conditions d'utilisation](https://alliancecan.ca/sites/default/files/2022-03/1-Conditions-d%E2%80%99utilisation.pdf)