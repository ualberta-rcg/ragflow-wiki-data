---
title: "Cloud resources/fr"
tags:
  - cloud

keywords:
  []
---

*Page enfant de [Ressources infonuagiques](cloud-fr.md)*
## Matériel
### Nuage Arbutus
Adresse : [arbutus.cloud.alliancecan.ca](https://arbutus.cloud.alliancecan.ca)

{| class="wikitable sortable"
|-
! Nombre de nœuds !! CPU !! Mémoire (GB) !! Stockage local (éphémère) !! Réseautique !! GPU !! Nombre de CPU !! Nombre de vCPU
|-
| 156 || 2 x [Gold 6248](https://ark.intel.com/content/www/us/en/ark/products/192446/intel-xeon-gold-6248-processor-27-5m-cache-2-50-ghz.html) || 384 ||2 x 1.92TB SSD en [RAID0](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_0)  || 1 x 25GbE || s.o. || 6,240 || 12,480
|-
| 8 || 2 x [Gold 6248](https://ark.intel.com/content/www/us/en/ark/products/192446/intel-xeon-gold-6248-processor-27-5m-cache-2-50-ghz.html) || 1024 ||2 x 1.92TB SSD en [RAID1](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_1)  || 1 x 25GbE || s.o. || 320 || 6,400
|-
| 26 || 2 x [Gold 6248](https://ark.intel.com/content/www/us/en/ark/products/192446/intel-xeon-gold-6248-processor-27-5m-cache-2-50-ghz.html) || 384 ||2 x 1.6TB SSD en [RAID0](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_0)  || 1 x 25GbE || 4 x [V100 32GB](https://www.nvidia.com/en-us/data-center/v100/) || 1,040 || 2,080
|-
| 32 || 2 x [Gold 6130](https://ark.intel.com/products/120492/Intel-Xeon-Gold-6130-Processor-22M-Cache-2_10-GHz) || 256 ||6 x 900GB 10k SAS en [RAID10](https://en.wikipedia.org/wiki/Standard_RAID_levels#Nested_RAID)  || 1 x 10GbE || s.o. || 1,024 || 2,048
|-
| 4 || 2 x [Gold 6130](https://ark.intel.com/products/120492/Intel-Xeon-Gold-6130-Processor-22M-Cache-2_10-GHz) || 768 ||6 x 900GB 10k SAS en [RAID10](https://en.wikipedia.org/wiki/Standard_RAID_levels#Nested_RAID)  || 2 x 10GbE || s.o. || 128 || 2,560
|-
| 8 || 2 x [Gold 6130](https://ark.intel.com/products/120492/Intel-Xeon-Gold-6130-Processor-22M-Cache-2_10-GHz) || 256 ||4 x 1.92TB SSD en [RAID5](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_5)  || 1 x 10GbE || s.o. || 256 || 512
|-
| 240 || 2 x [E5-2680 v4](https://ark.intel.com/products/91754/Intel-Xeon-Processor-E5-2680-v4-35M-Cache-2_40-GHz) || 256 ||4 x 900GB 10k SAS en [RAID5](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_5)  || 1 x 10GbE || s.o. || 6,720 || 13,440
|-
| 8 || 2 x E5-2680 v4 || 512 || 4 x 900GB 10k SAS en RAID5 || 2 x 10GbE || s.o. || 224 || 4,480
|-
| 2 || 2 x E5-2680 v4 || 128 || 4 x 900GB 10k SAS en RAID5 || 1 x 10GbE || 2 x [Tesla K80](https://www.nvidia.com/en-us/data-center/tesla-k80/) || 56 || 112
|}
Emplacement : Université de Victoria

Nombre total de CPU : 16,008 (484 nœuds)

Nombre total de vCPU : 44,112

Nombre total de GPU : 108 (28 nœuds)

Mémoire vive : 157,184 GB

5.3 PB de stockage [Ceph](https://en.wikipedia.org/wiki/Ceph_(software))

12 PB de stockage objet [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) sur des systèmes de fichiers partagés

### Nuage Cedar
Adresse : [cedar.cloud.alliancecan.ca](http://cedar.cloud.alliancecan.ca)

{| class="wikitable"
|-
! Nombre de nœuds !! CPU !! Mémoire (GB) !! Stockage local (éphémère) !! Réseautique !! GPU !! Nombre de CPU !! Nombre de vCPU
|-
| 28 || 2 x [E5-2683 v4](https://ark.intel.com/content/www/us/en/ark/products/91766/intel-xeon-processor-e5-2683-v4-40m-cache-2-10-ghz.html) || 256 || 2 x 480GB SSD en [RAID1](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_1)|| 1 x 10GbE || s.o. || 896 || 1,792
|-
| 4 || 2 x [E5-2683 v4](https://ark.intel.com/content/www/us/en/ark/products/91766/intel-xeon-processor-e5-2683-v4-40m-cache-2-10-ghz.html) || 256 || 2 x 480GB SSD en [RAID1](https://en.wikipedia.org/wiki/Standard_RAID_levels#RAID_1)|| 1 x 10GbE || s.o. || 128 || 256
|}
Emplacement : Université Simon-Fraser 

Nombre total de CPU : 1,024

Nombre total de vCPU : 2,048

Mémoire vive : 7,680 GB

500 TB de stockage  [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) persistant 

### Nuage Nibi
Adresse : [nibi.cloud.alliancecan.ca](https://nibi.cloud.alliancecan.ca)

{| class="wikitable"
|-
! Nombre de nœuds  !! CPU !! Mémoire (GB) !! Stockage local (éphémère) !! Réseautique !! GPU !! Nombre de CPU !! Nombre de vCPU
|-
| 18|| 2 X AMD EPYC 9474F 48-Core Processor|| 1511|| 3.5 TB|| 1 X 1GbE, 1 X 25GbE, 1 X 50GbE|| N/A|| 1728||3456
|-
|}
Emplacement : Université de Waterloo

Nombre total de CPU : 1728

Nombre total de CPU : 3456

Mémoire vive totale : 26.57v TB (27202.94 GB | 27,860,544 MB)

Stockage [Ceph](https://fr.wikipedia.org/wiki/Ceph) : 7.46 PB

### Nuage Béluga
Adresse : [beluga.cloud.alliancecan.ca](https://beluga.cloud.alliancecan.ca)

{| class="wikitable"
|-
! Nombre de nœuds !! CPU !! Mémoire (GB) !! Stockage local (éphémère) !! Réseautique !! GPU !! Nombre de CPU !! Nombre de vCPU
|-
| 96 || 2 x Intel Xeon Gold 5218 || 256 || s.o., stockage Ceph éphémère || 1 x 25GbE || s.o. || 3,072 || 6,144
|-
| 16 || 2 x Intel Xeon Gold 5218 || 768 || s.o., stockage Ceph éphémère || 1 x 25GbE || s.o. || 512 || 1,024
|-
|}
Emplacement : École de Technologie Supérieure

Nombre total de CPU : 3,584

Nombre total de vCPU : 7,168

Mémoire vive : 36,864 GiB

200 TiB de stockage répliqué  SSD [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) persistant 

1.7 PiB de stockage persistant HDD [Ceph](https://en.wikipedia.org/wiki/Ceph_(software)) HDD avec code d'effacement 

==Plateforme logicielle== 
En date du 2026-02-23, les versions de la plateforme OpenStack sont&nbsp;: 
* nuage Arbutus : Ussuri
* nuage Cedar : Train
* nuage Nibi : Flamingo
* nuage Béluga : Victoria

Consultez [OpenStack Releases](http://releases.openstack.org/).

## Images
Sur les nuages de l'Alliance, nous fournissons des images pour les distributions Alma, Debian, Fedora, Rocky et Ubuntu de Linux. D'autres images pour ces distributions seront ajoutées quand de nouvelles versions ou des mises à jour deviendront disponibles. Puisqu'il n'y a plus de support ni de mise à jour quand une version atteint sa fin de vie (<i>EOL</i> pour <i> end of life</i>), nous vous recommandons de migrer vos systèmes et plateformes à une version plus récente pour que vous puissiez recevoir les rustines et les avis de sécurité. Les images pour les distributions qui ont atteint leur fin de vie seront supprimées; même si vous ne devriez pas le faire, rien ne vous empêche d'exécuter une machine virtuelle avec une ancienne distribution Linux. Cependant, les images ne seront pas disponibles pour créer de nouvelles machines virtuelles.

Pour plus d'information, voir [Travailler avec des images](working-with-images-fr#images.md).