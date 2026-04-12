---
title: "Technical glossary for the resource allocation competitions/fr"
slug: "technical_glossary_for_the_resource_allocation_competitions"
lang: "fr"

source_wiki_title: "Technical glossary for the resource allocation competitions/fr"
source_hash: "31b44a5039b9beac771db7e6c182bd83"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T11:51:38.433535+00:00"

tags:
  []

keywords:
  - "ressources de calcul"
  - "plusieurs cœurs"
  - "traitement multifil"
  - "Infonuagique"
  - "service infonuagique de l'Alliance"
  - "nœuds de la grappe"
  - "copies de sauvegarde"
  - "stockage objet"
  - "vCPU-année"
  - "instantané de volume"
  - "Ressources de calcul"
  - "machine virtuelle"
  - "équivalent-cœur"
  - "vGPU-année"
  - "protocoles S3 et Swift"
  - "mémoire distribuée"
  - "tâche séquentielle"
  - "nœud de calcul"
  - "GPU-année"
  - "IaaS"
  - "cœur CPU"
  - "instance persistante"
  - "grappe"
  - "exécution des tâches"
  - "pilote Fuse"
  - "stockage infonuagique"
  - "OpenStack"
  - "allocation de ressources"
  - "Allocation de ressources"
  - "nœuds de calcul"
  - "GPU"
  - "nœud de connexion"
  - "cœur-année"
  - "CPU"
  - "répertoire personnel"
  - "espace de stockage"
  - "allocation"
  - "zone de travail /scratch"
  - "adresse IP flottante"
  - "partager les données"
  - "système de fichiers /home"
  - "tâche"
  - "CephFS"
  - "stockage persistant"
  - "stockage dans un système de fichiers partagé"
  - "Nœud de calcul"
  - "instance de calcul"
  - "infonuagique"
  - "tâche en parallèle"
  - "mémoire vive"
  - "juste part des ressources"
  - "système de fichiers"
  - "multitraitement symétrique"

questions:
  - "Quelles sont les définitions et les différences entre les diverses ressources de calcul physiques et virtuelles (CPU, GPU, vCPU, vGPU) mentionnées dans le texte ?"
  - "De quelle manière l'allocation des ressources de calcul (CPU, GPU) diffère-t-elle de l'allocation des ressources de stockage et infonuagiques ?"
  - "Que signifient les termes liés au traitement par lots, tels que « grappe », « nœud de calcul » et « cœur-année » ?"
  - "Quel est le rôle d'un nœud de connexion (ou nœud d'accès) lors de l'utilisation d'une grappe de calcul ?"
  - "Comment le principe de la « juste part des ressources » influence-t-il la priorité d'exécution des tâches d'un utilisateur ?"
  - "Qu'est-ce qui définit une tâche dans un système de traitement par lots et quelles sont les deux principales catégories de tâches en parallèle ?"
  - "Qu'est-ce qu'un « cœur-année » dans le contexte des ressources informatiques ?"
  - "Comment l'utilisation de plusieurs cœurs sur de courtes périodes peut-elle équivaloir à un cœur-année ?"
  - "Sur quelle unité de mesure se base l'allocation des ressources de calcul ?"
  - "Comment définit-on une tâche en parallèle selon le texte ?"
  - "Quelles sont les deux grandes catégories de tâches en parallèle mentionnées ?"
  - "Quelle est la différence principale entre les tâches de traitement multifil et les tâches à mémoire distribuée en termes d'utilisation des nœuds et de la mémoire ?"
  - "Comment un utilisateur doit-il procéder s'il prévoit une utilisation irrégulière ou intensive de ses ressources de calcul ?"
  - "Quelle est la différence entre la mémoire par cœur et la mémoire par nœud sur un nœud de calcul ?"
  - "Quelles sont les principales différences de fonction et de persistance entre les systèmes de fichiers /scratch et /home ?"
  - "Quelles sont les caractéristiques et les cas d'utilisation idéaux pour les espaces de stockage /project, /nearline et le stockage local ?"
  - "À quel type de projets s'adresse principalement le système de stockage dCache et comment faut-il procéder pour pouvoir l'utiliser ?"
  - "Comment le texte définit-il le service infonuagique de l'Alliance et quelles sont les unités de mesure associées à ses ressources virtuelles ?"
  - "Quels types de fichiers et de données sont généralement stockés dans le répertoire personnel d'un utilisateur ?"
  - "Quelles sont les caractéristiques du répertoire personnel en termes de taille, de persistance et de sauvegarde par rapport à la zone de travail /scratch ?"
  - "Quelle est la visibilité du répertoire personnel à travers les différents nœuds de la grappe ?"
  - "Comment le texte définit-il le « service infonuagique de l'Alliance » et sur quel modèle de virtualisation repose-t-il ?"
  - "Que représente l'unité de mesure « vCPU-année » dans le contexte de l'infonuagique ?"
  - "Quelle est la particularité de la mesure « vGPU-année » par rapport au « GPU-année » standard ?"
  - "Quelles sont les principales différences entre une instance de calcul et une instance persistante en matière de durée de vie et d'allocation de processeurs ?"
  - "Comment se distinguent les différentes solutions de stockage proposées, telles que le disque local éphémère, le stockage infonuagique et le stockage objet ?"
  - "Quel est le rôle d'une adresse IP flottante dans la gestion des machines virtuelles et l'hébergement d'un portail de service ?"
  - "Qu'est-ce qu'un instantané de volume et à quelles fins est-il principalement utilisé dans un environnement OpenStack ?"
  - "Quelles sont les caractéristiques principales du stockage objet et par quels protocoles peut-on y accéder ?"
  - "Quelles sont les unités de mesure utilisées pour quantifier respectivement les volumes ou instantanés et le stockage objet ?"
  - "Qu'est-ce que le stockage dans un système de fichiers partagé et quel est son objectif principal ?"
  - "Quelles sont les technologies et les pilotes requis pour faire fonctionner ce service sous Windows ou Linux ?"
  - "Dans quelle unité de mesure cet espace de stockage persistant est-il quantifié ?"
  - "Qu'est-ce que le stockage dans un système de fichiers partagé et quel est son objectif principal ?"
  - "Quelles sont les technologies et les pilotes requis pour faire fonctionner ce service sous Windows ou Linux ?"
  - "Dans quelle unité de mesure cet espace de stockage persistant est-il quantifié ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

## Ressources de calcul
**CPU** (pour *central processing unit*) : Unité centrale de traitement; cerveau de l’ordinateur où s’effectuent la plupart des calculs. On l'appelle aussi **processeur** ou **processeur central**.

**GPU** (pour *graphics processing unit*) : Processeur utilisé pour accélérer les applications d’apprentissage profond, d’analytique et de génie, par exemple. Des accélérateurs de processeurs graphiques font fonctionner des centres de données écoénergétiques dans des laboratoires universitaires, des universités, de grandes entreprises ainsi que des petites et moyennes entreprises partout dans le monde. Ils jouent un rôle important dans l’accélération des applications, que ce soit sur des plateformes en intelligence artificielle, dans les domaines de l’automobile, des drones ou de la robotique.

**vCPU** (pour *virtual central processing unit*) : Unité centrale de traitement virtuelle. Dans un environnement infonuagique, un ou plusieurs CPU virtuels sont assignés à chaque machine virtuelle. Le système d’exploitation de la machine virtuelle considère chaque CPU virtuel comme un cœur de processeur physique simple.

**vGPU** (pour *virtual graphics processing unit*) : Processeur graphique virtuel. Un ou plusieurs vGPU peuvent être assignés à une instance dans un environnement infonuagique. Le système d'exploitation de l'instance voit chaque vGPU comme étant une carte GPU physique distincte.

**Unité GPU de référence (UGR)** : Unité de mesure de l’utilisation relative d’une ressource GPU. La valeur est employée pour déterminer le coût d'utilisation d’un modèle particulier de GPU puisque la performance de chacun est différente. Par exemple,
* 1 GPU A100-40GB = 4.0 UGR
* 1 GPU V100-16GB = 2.2 UGR
* 1 GPU P100-12GB = 1.0 UGR

## Allocation de ressources
Les ressources infonuagiques et les ressources de stockage sont allouées différemment des ressources de calcul CPU et GPU.

* Un groupe de recherche obtient un maximum de ressources de stockage pour sa consommation exclusive pendant la durée de la période d’allocation. Pour l'allocation de ressources infonuagiques, la quantité de vCPU et d'espace de stockage alloués ne peut être dépassée au cours de la période d'allocation.
* Les CPU et les GPU alloués ne le sont pas en quantités maximales, mais plutôt en quantités cibles dont la disponibilité est soumise à la priorisation par l’ordonnanceur. Une allocation de *n* cœurs CPU signifie que le groupe de recherche peut s’attendre à pouvoir accéder à ce nombre de cœurs CPU tout au long de la durée de la période d’allocation. Il demeure possible d’utiliser plus de ressources pourvu qu’elles ne soient pas utilisées par d’autres groupes. Les périodes de sous-utilisation, par exemple lorsque les activités de recherche sont ralenties ou que le matériel est en panne ou en maintenance, ne sont pas compensées. Pour en savoir plus sur les allocations de calcul, voyez [Allocations et ordonnancement](allocations-et-ordonnancement.md).

## Traitement par lots
**grappe** (en anglais, *cluster*) : Groupe de nœuds de calcul interconnectés qui est géré par un programme d'ordonnancement.

**nœud de calcul** (en anglais, *compute node*) : Unité de calcul d’une grappe. Un nœud de calcul possède sa propre image du système d’exploitation, un ou plusieurs cœurs de processeur (CPU) et de la mémoire vive (RAM). Il peut être assigné à une tâche seul ou en groupe et les tâches l'utilisent de manière exclusive ou partagée, selon la grappe.

**cœur-année** (en anglais, *core year*) : Mesure qui équivaut à utiliser un cœur CPU de façon continue pendant une année complète. L’utilisation de 12 cœurs pendant un mois et celle de 365 cœurs pendant une seule journée équivalent toutes deux à l’utilisation d’un cœur-année. Les ressources de calcul sont allouées sur la base de cœurs-années.

**équivalent-cœur** (en anglais, *core-equivalent*) : Un équivalent-cœur se compose d’un cœur simple et d’une certaine quantité de mémoire; pour le nommer, nous utilisons souvent le terme *bundle*. En plus du cœur, le *bundle* contient aussi la mémoire considérée comme étant associée à ce cœur. Pour en savoir plus, voyez [Allocations et ordonnancement des tâches de calcul](allocations-et-ordonnancement-des-taches-de-calcul.md).

**GPU-année** : Mesure qui équivaut à l'utilisation continue de 1 GPU pour une année complète ou de 12 GPU pour un mois.

**UGR-année** : Valeur résultant de la multiplication de GPU-années avec le nombre d'UGR d'un modèle particulier de GPU. Par exemple, 10 GPU-années avec un GPU de modèle A100-40GB (qui vaut 4 UGR) est égal à 40 UGR-années.

**nœud de connexion ou d'accès** (en anglais, *login node* ou *head node*) : L’accès à une grappe se fait habituellement par le nœud d’accès, point d’entrée ou nœud de connexion à la grappe. La configuration du nœud d’accès en fait le point de départ des tâches à exécuter sur la grappe. Quand vous accédez ou vous connectez à une grappe, vous êtes automatiquement connecté au nœud d’accès; il s’agit souvent d’un nœud configuré comme point de liaison entre la grappe et le réseau.

**juste part des ressources, allocation basée sur la …** (en anglais, *fair-share allocation*) : De façon générale, un algorithme de juste part (*fair share algorithm*) est utilisé pour établir la priorité des traitements par lots. Une portion de l’ensemble des ressources du système est allouée à chaque utilisateur, ce qui détermine sa priorité d’accès. Si vous avez récemment utilisé une large portion des ressources du système (c’est-à-dire plus que votre juste part), vous serez rétrogradé dans l’ordre de priorité. Le logiciel d’ordonnancement utilise toutefois une fenêtre limitée pour calculer la priorité. Après une certaine période de temps (par exemple, des semaines), le système « oublie » graduellement que vous avez surutilisé les ressources dans le passé. La grappe est ainsi utilisée dans sa pleine mesure et les utilisateurs qui se prévalent des ressources inutilisées ne sont pas pénalisés. Ceci fait en sorte que le total des ressources qui vous sont allouées ne limite en aucune façon les ressources de calcul que vous pouvez utiliser. Ce total représente plutôt la quantité de ressources que vous devriez pouvoir utiliser au cours de l’année si vous faites exécuter des tâches de façon continue et que le système fonctionne à capacité maximale. Autrement dit, continuez à travailler même si le total de vos ressources est atteint.

**tâche** (en anglais, *job*) : Élément de base exécuté par le système de traitement par lots. Une tâche se compose d’un ou plusieurs processus de calcul connexes gérés comme un tout. Une tâche est décrite au moment où celle-ci est mise en file d’attente dans le système de traitement par lots. La description comprend une demande de ressources qui précise la quantité de mémoire requise, la durée de la tâche et le nombre de cœurs requis. En fonction des ressources utilisées, les tâches peuvent être exécutées en série (par un seul cœur) ou en parallèle (par plusieurs cœurs).

**tâche en parallèle** (en anglais, *parallel job*) : Tâche exécutée simultanément par plusieurs cœurs. En gros, les tâches en parallèle se divisent en deux catégories : a. les tâches de traitement multifil ou de multitraitement symétrique exécutées sur un même nœud et partageant le même espace mémoire, et b. les tâches à mémoire distribuée pouvant être exécutées sur plusieurs nœuds.

**tâche séquentielle** (en anglais, *serial job*) : Tâche exécutée par un seul cœur.

**utilisation irrégulière** (en anglais, *uneven usage*) : La plupart des systèmes de traitement par lots sont configurés pour offrir un certain nombre de cœurs-années sur une période de temps déterminée, supposant une utilisation régulière de la grappe. Cependant, les tâches peuvent être de taille inégale, avec une utilisation plus ou moins intense dans le temps. Un utilisateur pourrait avoir besoin d’une utilisation intensive (*burst*) des ressources de calcul afin de bien profiter de son allocation. Nous présumons que les ressources seront utilisées de façon régulière dans la période d’allocation. Si vous prévoyez devoir exécuter des tâches ponctuelles intensives ou utiliser vos ressources de manière variable, veuillez le mentionner sur votre formulaire de demande d’allocation de ressources. Pour les problèmes au sujet de l'exécution de vos tâches, contactez le [soutien technique](soutien-technique.md).

## Mémoire
**mémoire par cœur** (en anglais, *memory per core*) : Quantité de mémoire vive (RAM) par cœur de processeur. Si un nœud de calcul comporte 2 unités centrales ayant chacune 6 cœurs et 24Go de mémoire vive (RAM), ce nœud possède alors 2Go de mémoire par cœur.

**mémoire par nœud** (en anglais, *memory per node*) : Quantité totale de mémoire vive (RAM) installée sur un nœud de calcul.

**mémoire système de base, par cœur** (en anglais *base system memory per core*) : Capacité en Go de mémoire système demandée par une tâche, divisée par le nombre de cœurs CPU demandés.

**mémoire système de base, par GPU** (en anglais *base system memory per GPU*) : Capacité en Go de mémoire système demandée par une tâche, divisée par le nombre de GPU demandés.

## Stockage
**disque** : Support statique à semiconducteurs pour l'enregistrement, entre autres, de programmes et de données en lecture et en écriture. Contrairement à la mémoire principale de l'ordinateur ou à la mémoire vive (RAM) qui sont volatiles, le disque est un support de stockage permanent.

**système de fichiers** (en anglais, *filesystem*) : Structure de fichiers pour les systèmes d’une grappe. Un système de fichiers peut avoir des caractéristiques spécifiques en termes de performance, d’espace disponible et d’utilisation. Certains systèmes de fichiers peuvent être utilisés seulement par les nœuds d’accès d’une grappe, alors que d’autres peuvent servir de nœuds de stockage pendant l’exécution d’une tâche. Les types de systèmes de fichiers sont :

- **`/scratch`** : Système de fichier visible à partir des nœuds de calcul et qui sert de stockage haute performance utilisé lors des tâches de calcul. Il est conçu principalement pour les fichiers temporaires ou transitoires, les résultats bruts des calculs et simulations, et tout contenu pouvant aisément être recréé ou reproduit. Les données devraient être copiées dans les fichiers de travail `/scratch`, puis retirées lorsque la tâche est terminée. Ces fichiers sont purgés selon la politique du système local. Ils ne sont pas alloués par voie de concours, mais offrent des quotas élevés.

- **`/home`** : Système de fichiers de base généralement utilisé pour le stockage de fichiers personnels, d’exécutables, de scripts pour l’exécution des tâches et d’ensembles de données d’entrée de relative petite taille. Chaque utilisateur possède son propre système de fichiers `/home` appelé « répertoire personnel » (*home directory*). Le répertoire personnel est persistant, plus petit que la zone de travail `/scratch` et, dans la plupart des cas, sauvegardé régulièrement. Le répertoire personnel est visible par tous les nœuds de la grappe.

- **`/project`** : Système de fichiers qui utilise des disques de performance moyenne à haute et est visible par les nœuds de calcul d’une grappe. L’espace de stockage y est plus grand que celui d’un répertoire `/home` et, dans la plupart des cas, la sauvegarde en est effectuée régulièrement. Ce type de système de fichiers est habituellement utilisé pour stocker les données fréquemment utilisées d’un projet qui ne sont toutefois pas souvent modifiées. Ils sont alloués dans le cadre des concours d’allocation de ressources.

- **`/nearline`** : Système de fichiers quasi en ligne constitué de disques et de rubans; lorsque la taille des données sur un disque atteint un certain seuil, elles sont automatiquement transférées sur ruban et retournées au disque pour les opérations de lecture. Pour utiliser cet espace de stockage, vous devez y placer les fichiers par ligne de commande Linux avec cp, mv, rsync ou autre, ou encore y transférer des fichiers en provenance d’un autre système de fichiers. Si les rubans offrent une très grande capacité, la latence est cependant augmentée lorsqu’il s’agit d’accéder à nouveau aux fichiers. Ils devraient donc être utilisés pour stocker les données rarement utilisées, mais qui doivent être conservées à long terme. Ce n’est pas à proprement parler un espace d’archivage, car les ensembles de données sont utilisés par des projets « actifs ». Ils sont soumis à des quotas et sont alloués dans le cadre des concours d’allocation de ressources.

- **`dCache`** : Système de stockage initialement conçu pour les projets en physique des hautes énergies comportant des ensembles de données de l’ordre de pétaoctets. Il est surtout utilisé pour les projets de grande envergure auxquels sont associés plusieurs chercheurs et chercheurs principaux. dCache comporte un niveau de fichiers de stockage objet superposé à des fichiers classiques. Ces deux couches intégrées supportent plusieurs protocoles d’accès et de transfert pour les données sous-jacentes. L’espace de stockage dCache est alloué dans le cadre des concours d’allocation de ressources. Pour utiliser ce type de stockage, écrivez à l’équipe nationale de physique subatomique de notre [soutien technique](soutien-technique.md).

- **stockage local** : Lecteur de disque dur ou disque statique dans un nœud de calcul, pouvant être utilisé de façon temporaire pour le stockage de programmes, de fichiers en lecture ou de leurs résultats. Les fichiers de l'espace de stockage local ne peuvent être accédés par les autres nœuds. Ce stockage pourrait ne pas être persistant, donc les fichiers qui y sont créés devraient être déplacés vers un espace de stockage autre que local afin d'éviter la perte de données.

**site** : Membre d’un partenaire de l'Alliance offrant des ressources de calcul informatique de pointe (CIP) (grappes de calcul haute performance, nuages, stockage, soutien technique).

**ruban magnétique** (en anglais, *tape*) : Technologie utilisée pour stocker à long terme des données à accès peu fréquent. Considérablement plus abordable que le stockage sur disque, elle convient à plusieurs scénarios d’utilisation.

**téraoctet (To)** (en anglais, *terabyte*) : Unité utilisée le plus souvent pour mesurer la capacité des gros appareils de stockage. Un téraoctet égale 1000 gigaoctets et précède l’unité de mesure pétaoctet.

## Infonuagique
**service infonuagique de l'Alliance** (en anglais *Alliance cloud*) : Ensemble d’équipements permettant la virtualisation sur le modèle IaaS (*Infrastructure as a Service*).

**vCPU-année** (en anglais *vCPU-year*) : Identique à CPU-année, mais dans un contexte infonuagique.

**vGPU-année** (en anglais *vGPU-year*) : Identique à GPU-année, mais dans un contexte infonuagique.

**instance de calcul** (en anglais, *compute instance*) : Type de ressource de courte durée, avec utilisation élevée et constante du processeur. Ces ressources sont aussi connues sous l’appellation *instances batch*. Parce qu’elles sont de courte durée, elles recevront un quota plus fort de processeurs virtuels (vCPU).

**instance persistante** (en anglais, *persistent instance*) : Type de ressource de durée indéterminée (par exemple, selon la disponibilité du service), pour l’usage entre autres de serveurs web ou de serveurs de bases de données. Ces ressources sont généralement moins exigeantes en termes de processeur ou y ont recours de façon intermittente (*bursty instance*). Parce qu’elles sont de longue durée, elles recevront un quota moins fort de processeurs virtuels (vCPU).

**stockage infonuagique** (en anglais *cloud storage*) : L'espace infonuagique persistant offre aux instances virtuelles la fonctionnalité de virtualisation d'un disque. Offre une grande fiabilité et scalabilité rendues possibles par un logiciel spécialisé (Ceph).

**adresse IP flottante** (en anglais, *floating IP*) : Adresse IP publique qui est associée à une machine virtuelle; l’instance utilise la même adresse IP publique chaque fois qu’elle est lancée. Un groupe d’adresses IP flottantes est créé et elles sont ensuite assignées aux instances; l’adresse IP demeure la même et elle est toujours reliée au même nom de domaine (DNS pour *domain name system*).

**instance** (en anglais, *instance* et souvent *virtual machine*) : Machine virtuelle active ou dont l’état indique qu’elle est, par exemple, « suspendue »; elle peut être utilisée comme serveur physique.

**mémoire par cœur** (en anglais, *memory per core*) : Voir **mémoire par cœur** dans la section **Mémoire**.

**disque local éphémère** (en anglais, *ephemeral local storage*) : Espace disque souvent utilisé pour les applications cloud natives où les instances sont de courte durée et les données n’ont pas besoin d’être conservées au-delà de la durée de vie de l’instance, par exemple : quand une instance enregistre des données dans la cache pour un utilisation brève; quand une instance héberge des applications qui répliquent les données sur plusieurs instances; ou quand les données d’une instance sont enregistrées dans un volume ou dans un support de stockage externe. Contrairement aux volumes qui résident sur l’espace de stockage résilient d’une grappe, les disques locaux éphémères utilisent l’espace de stockage directement relié à l’hôte de virtualisation. Ils sont purgés et supprimés quand l’instance est supprimée par l’utilisateur ou par l’administrateur, et ne survivent pas aux bris de matériel.

**portail de service** (en anglais, *service portal*) : Notre infrastructure héberge plusieurs portails Web où se trouvent des outils et des ensembles de données. Ces portails ne nécessitent généralement pas une grande quantité de ressources de calcul ou de stockage, mais peuvent requérir l’intervention de notre équipe technique. Les groupes qui présentent un projet de portail de service utilisant souvent nos nuages, requièrent généralement une adresse IP publique et peuvent avoir (ou non) un besoin plus impérieux de temps en ligne que la plupart des projets de recherche. Sur le formulaire en ligne, cette option se nomme « Portal ».

**machine virtuelle** : Voir **instance**.

**stockage des volumes et des instantanés** : Espace de stockage persistant pour l’ensemble des volumes et des instantanés. Mesuré en Go.

**instantané de volume** (en anglais, *volume snapshot*) : Copie transactionnelle en lecture seule d’un volume OpenStack. Utilisé pour les copies de sauvegarde et l’instanciation d’autres instances.

**stockage objet** (en anglais, *object storage*) : Espace de stockage objet persistant utilisé pour de grandes quantités de données accédées principalement en mode lecture. Accessible de partout par les protocoles S3 et Swift. Mesuré en To.

**stockage dans un système de fichiers partagé** (en anglais, *shared filesystem storage*) : Espace de stockage persistant Unix pouvant être monté par plusieurs hôtes d’un même projet pour partager les données. Ce service utilise CephFS et requiert un pilote Fuse sous Windows ou Linux, ou le pilote du noyau (*kernel driver*) CephFS sous Linux. Mesuré en To.