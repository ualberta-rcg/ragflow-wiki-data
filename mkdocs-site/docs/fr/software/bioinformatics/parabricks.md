---
title: "Parabricks/fr"
slug: "parabricks"
lang: "fr"

source_wiki_title: "Parabricks/fr"
source_hash: "adbf67f48e78fc2754ba6f7d7e2f539a"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T09:47:30.538004+00:00"

tags:
  []

keywords:
  []

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: false
  ragflow_synced: false
  qa_generated: false
---

Parabricks est une suite logicielle servant à l'analyse de l'ADN par séquençage à haut débit (NGS pour *next-generation sequencing*). Le traitement s'effectue très rapidement; selon la documentation du produit, Parabricks peut analyser le séquençage entier du génome humain (WGS pour *whole genome sequencing*) à une résolution de 30x en quelques heures, comparativement à quelques jours avec les autres techniques.

Pour plus d'information, allez à [www.nvidia.com/parabricks](http://www.nvidia.com/parabricks).

## Utilisation sur les grappes de Calcul Canada

**NVIDIA offrait le logiciel gratuitement jusqu'au 17 mai 2020 pour soutenir la recherche sur la COVID-19.**
Vous devez maintenant vous entendre avec NVIDIA pour obtenir votre licence.

## Trouver et charger Parabricks

Vous pouvez trouver Parabricks avec la commande `spider`.

```bash
module spider parabricks
```

Vous pouvez aussi le charger avec les modules Lmod.

```bash
module load parabricks/2.5.0
```

## Exemple d'utilisation

Avant d'utiliser Parabricks, consultez la [documentation](https://www.nvidia.com/en-us/docs/parabricks/), incluant les pipelines et les outils autonomes. Pour savoir comment demander des GPU, lisez [Ordonnancement Slurm avec des tâches exécutées avec GPU](using-gpus-with-slurm.md). Une fois ces informations assimilées, vous pourrez soumettre une tâche comme celle-ci :

```bash
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
```

!!! note
    Pour que le chemin soit absolu, utilisez la commande `realpath`.

## Problèmes fréquents

### Échec à court terme

Si un échec se produit lors de votre premier test, cela pourrait être dû à un module manquant ou à un conflit avec une variable d'environnement. Pour résoudre le problème, essayez :

```bash
module --force purge
```

```bash
module load StdEnv/2016.4 nixpkgs/16.09 parabricks/2.5.0
```

### Échec à plus long terme

Parabricks ne fournit pas toujours une trace claire des échecs. Cela signifie généralement que vous n'avez pas demandé assez de mémoire vive. Si vous avez réservé un nœud complet avec `--nodes=1`, nous vous suggérons d'utiliser toute la mémoire vive disponible avec `--mem=0`. Autrement, assurez-vous que votre pipeline dispose de suffisamment de mémoire vive pour traiter vos données.

## Utilisation hybride

Parabricks peut utiliser les CPU et les GPU. Nos tests ont été effectués avec un minimum de 10 CPU; nous vous recommandons de demander au moins cette quantité avec `--cpus-per-task=10`.

## Références

[Site web Parabricks](http://www.nvidia.com/parabricks)