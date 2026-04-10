---
title: "Parabricks/fr"
tags:
  []

keywords:
  []
---

Parabricks est une suite logicielle qui sert à l'analyse de l'ADN par séquençage haut débit (NGS pour *next-generation sequencing*). Le traitement se fait très rapidement; dans la documentation du produit, il est dit que Parabricks peut analyser le séquençage entier du génome humain (WGS pour *whole genome sequencing*) d'une résolution  de 30x en quelques heures, contrairement à quelques jours avec les autres techniques.

Pour plus d'information, allez à [www.nvidia.com/parabricks](http://www.nvidia.com/parabricks).

=Utilisation sur les grappes de Calcul Canada =

'''NVidia offrait le logiciel gratuitement jusqu'au 17 mai 2020 pour soutenir la recherche sur la COVID-19.'''
Vous devez maintenant vous entendre avec NVIDIA pour obtenir votre licence.

## Trouver et charger Parabricks 

Vous pouvez trouver Parabricks avec la commande <tt>spider</tt>.

```bash
module spider parabricks
```

Vous pouvez aussi le charger avec les modules Lmod.

```bash
module load parabricks/2.5.0
```

## Exemple d'utilisation 

Avant d'utiliser Parabricks, prenez connaissance de la [documentation](https://www.nvidia.com/en-us/docs/parabricks/), incluant les pipelines et les outils autonomes. Pour savoir comment demander des GPU, lisez  [Ordonnancement Slurm avec des tâches exécutées avec GPU](using-gpus-with-slurm-fr.md). Quand vous aurez compris cette information, vous pourrez soumettre une tâche comme celle-ci&nbsp;:

<pre>
#!/bin/bash
#SBATCH --account=def-someuser
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=0
#SBATCH --time=5:00:00

module load parabricks/2.5.0

DATA_DIR=/path/to/data
OUT_DIR=/path/to/output
pbrun germline \
      --ref ${DATA_DIR}/Homo_sapiens_assembly38.fa \
      --in-fq ${DATA_DIR}/some_1.fastq ${DATA_DIR}/some_2.fastq \
      --knownSites ${DATA_DIR}/dbsnp_146.hg38.vcf.gz \
      --tmp-dir ${SLURM_TMPDIR}/ \
      --out-bam ${OUT_DIR}/output.bam \
      --out-variants ${OUT_DIR}/output.vcf \
      --out-recal-file ${OUT_DIR}/report.txt
</pre>

## Problèmes fréquents 

### Échec à court terme 

Si un échec se produit à votre premier test, ce peut être en raison d'un module manquant ou d'un conflit avec une variable d'environnement. Pour résoudre le problème, essayez

```bash
module --force purge
```

```bash
module load StdEnv/2016.4 nixpkgs/16.09 parabricks/2.5.0
```

### Échec à plus long terme 

Parabricks ne fournit pas toujours une trace claire des échecs. Ceci signifie habituellement que vous n'avez pas demandé assez de mémoire. Si vous avez réservé un nœud complet avec `--nodes=1`, nous vous suggérons d'utiliser toute la mémoire avec `--mem=0`. Autrement, assurez-vous que votre pipeline a suffisamment de mémoire pour traiter vos données.

## Utilisation hybride 

Parabricks peut utiliser les CPU et les GPU. Nos tests ont été effectués avec un minimum de 10 CPU; nous vous recommandons de demander au moins cette quantité avec `--cpus-per-task=10`.

=Références =
[Site web Parabricks](http://www.nvidia.com/parabricks)

[Catégorie :Bioinformatics](catégorie-:bioinformatics.md)
[Catégorie :Software](catégorie-:software.md)
[Catégorie :COVID19_related_requests](catégorie-:covid19_related_requests.md)