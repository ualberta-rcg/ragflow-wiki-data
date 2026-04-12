---
title: "VM Best Practices/fr"
slug: "vm_best_practices"
lang: "fr"

source_wiki_title: "VM Best Practices/fr"
source_hash: "5f00eaa9280fc948f3b01ef299658a19"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:34:04.834304+00:00"

tags:
  - cloud

keywords:
  - "OpenStack"
  - "Mises à jour"
  - "Copie de sauvegarde"
  - "Instances infonuagiques"
  - "Volumes de données"

questions:
  - "Quelle précaution essentielle doit être prise avant de procéder à la mise à jour du système d'exploitation d'une instance infonuagique ?"
  - "Pourquoi est-il recommandé de créer un deuxième volume de données plutôt que d'essayer d'augmenter la taille du volume central ?"
  - "Quelles sont les conséquences potentielles sur le système si l'on attache plus de trois volumes à une seule instance ?"
  - "Quelle précaution essentielle doit être prise avant de procéder à la mise à jour du système d'exploitation d'une instance infonuagique ?"
  - "Pourquoi est-il recommandé de créer un deuxième volume de données plutôt que d'essayer d'augmenter la taille du volume central ?"
  - "Quelles sont les conséquences potentielles sur le système si l'on attache plus de trois volumes à une seule instance ?"

status:
  downloaded: true
  converted: true
  tagged: true
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

*Page enfant de [Services infonuagiques](cloud.md)*

Certains utilisateurs ayant rapporté des difficultés avec des instances infonuagiques, nous offrons ici quelques conseils qui pourraient vous être utiles.

## Mises à jour
La mise à jour de paquets est recommandée pour des raisons de sécurité et elle se fait souvent sans difficulté. Si la mise à niveau d'un système d'exploitation est aussi de bonne pratique, elle peut pour sa part causer certains problèmes.

!!! warning "Sauvegarde avant mise à jour"
    Avant de procéder à la mise à jour de votre système d'exploitation (par exemple de Ubuntu 20.0 à Ubuntu 22.0), faites une [copie de sauvegarde de votre instance](backing-up-your-vm.md) que vous pourrez utiliser si nécessaire.

## Volumes

### Volumes de données

Comme il est très difficile d'augmenter la taille d'un volume central (*root volume*), il peut être indiqué de **créer un deuxième volume de données** quand une instance n'a pas d'exigences de stockage limitées. Si vous avez besoin de plus d'espace et que l'espace de stockage qui vous est alloué le permet, le volume de données peut être accru assez facilement avec OpenStack, puis d'augmenter le volume logique (s'il y a lieu) et le système de fichiers de votre instance.

### Nombre de volumes par instance

!!! warning "Limitation du nombre de volumes"
    **N'attachez jamais plus de trois volumes à une instance**. Ceci produit l'arrêt du noyau (*kernel*) et peut affecter les opérations sur les disques des volumes, causant un effet de cascade qui entrave le fonctionnement de l'instance. Dans certains cas (voir ci-dessus), il est préférable de n'utiliser qu'un seul volume que vous pouvez fractionner en plusieurs systèmes de fichiers et que vous pourrez agrandir au besoin.

Plusieurs utilisateurs ont rencontré ce problème sur Arbutus (arbutus.cloud.computecanada.ca); la cause peut cependant être reliée à la taille du volume. Dans un cas particulier, 3 volumes de 100Go reliés à une instance p4-6gb ont causé l'arrêt du *kernel* à chaque tentative d'opération sur le disque. Il était par exemple très difficile de copier plus de 500Mo de données entre deux systèmes de fichiers.

Nous avons testé un cas semblable sur le nuage East : avec 4 volumes de 100Go (incluant le volume central), le même système d'exploitation et le même gabarit (*flavor*) le problème ne s'est pas reproduit. Si cette instance disposait de plus de mémoire (15Go plutôt que 6Go), il semble que ce facteur ne soit pas en cause puisque dans le cas d'Arbutus, nous n'avons pas observé une consommation de mémoire élevée.