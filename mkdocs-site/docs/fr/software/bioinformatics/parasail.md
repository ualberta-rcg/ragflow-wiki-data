---
title: "Parasail/fr"
tags:
  []

keywords:
  []
---

[parasail](https://github.com/jeffdaily/parasail) est une bibliothèque  SIMD C (C99) qui contient des implémentations d'algorithmes d'alignement de séquences par paires Smith-Waterman (alignement local), Needleman-Wunsch (alignement global) et autres alignements semi-globaux.

= Utilisation = 

Pour connaître la version disponible, utilisez

```bash
module spider parasail
```

Chargez la bibliothèque avec

```bash
module load parasail/2.6.2
```

## Avec le binaire <tt>parasail_aligner</tt>  
Il est important de définir le nombre de fils selon le nombre de cœurs alloués à votre tâche, par exemple 
<syntaxhighlight lang="bash">
parasail_aligner -t ${SLURM_CPUS_PER_TASK:-1} ...}}
</syntaxhighlight>

## Extension Python 
Le module contient des liaisons pour plusieurs versions de Python. 
Pour connaître les versions compatibles de Python, lancez

```bash
module spider parasail/1.3.4
```

### Utiliser l'extension 
1. Chargez les modules requis.

```bash
module load parasail/2.6.2 python/3.11 scipy-stack/2023b
```

2. Importez parasail 1.3.4.

```bash
python -c "import parasail"
```

L'importation est réussie quand la commande ne retourne rien.

### Exemple 
Comparez les résultats d'un alignement local avec BioPython et parasail.

1. Préparez le script Python.

**`parasail-sw.py`**
```python
import parasail
from Bio.Align import PairwiseAligner

A = "ACGT" * 1000

# parasail
matrix = parasail.matrix_create("ACGT", 1, 0)
parasail_score = parasail.sw(A, A, 1, 1, matrix).score

# biopython
bio_score = PairwiseAligner().align(A, A)[0].score

print('parasail:', parasail_score)
print('biopython:', bio_score)
```

2. Préparez le script de soumission selon votre environnement.
<tabs>
<tab name="StdEnv par défaut">

**`submit-parasail.sh`**
```sh
#!/bin/bash
#SBATCH --account=def-someuser  # replace with your PI account
#SBATCH --cpus-per-task=1 
#SBATCH --mem-per-cpu=3G      # increase as needed
#SBATCH --time=1:00:00

module load parasail/2.6.2 python/3.11 scipy-stack/2023b

# Install any other requirements, such as Biopython
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip
pip install --no-index biopython==1.83

python parasail-sw.py
```

</tab>
<tab name="StdEnv/2020">
2.1. Identify available wheels first :

```bash
avail_wheel parasail
```

```
name      version    python    arch
--------  ---------  --------  -------
parasail  1.2.4      py2,py3   generic
```

Installez maintenant la version choisie dans votre environnement virtuel.

**`submit-parasail.sh`**
```sh
#!/bin/bash
#SBATCH --account=def-someuser  # replace with your PI account
#SBATCH --cpus-per-task=1 
#SBATCH --mem-per-cpu=3G      # increase as needed
#SBATCH --time=1:00:00

module load StdEnv/2020 gcc parasail/2.5 python/3.10

# Install any other requirements, such as Biopython
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate
pip install --no-index --upgrade pip
pip install --no-index parasail==1.2.4 biopython==1.83

python parasail-sw.py
```

</tab>
</tabs>

3. Soumettez la tâche avec

```bash
sbatch submit-parasail.sh
```

4. Une fois la tâche terminée, vérifiez le résultat dans le fichier de sortie de l'ordonnanceur Slurm.

```bash
less slurm-*.out
```

```
parasail: 4000
biopython: 4000.0
```

#### Paquets Python disponibles 
Les exigences des paquets Python qui dépendent de parasail seront satisfaites en chargeant le module parasail.

```bash

```
 grep parasail
|result=
parasail                           1.3.4
}}