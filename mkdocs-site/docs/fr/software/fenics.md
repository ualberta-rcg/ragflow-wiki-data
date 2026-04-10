---
title: "FEniCS/fr"
slug: "fenics"
lang: "fr"

source_wiki_title: "FEniCS/fr"
source_hash: "8a466c2d091340379d0b9b7aaa7eba4d"
last_synced: "2026-04-09T20:02:20.019957+00:00"
last_processed: "2026-04-10T06:16:24.821344+00:00"

tags:
  - software

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

[FEniCS](https://fenicsproject.org) est une plateforme de logiciels libres pour la résolution d'équations aux dérivées partielles.

Puisque la plateforme peut être construite avec diverses extensions, nous n'offrons pas une installation centrale unique. Vous avez le choix entre :

- l'installation dans un environnement virtuel;
- l'utilisation d'un conteneur Singularity.

## Installation dans un environnement virtuel

Les instructions suivantes installent la version 2019.1.0 dans StdEnv/2020 avec OpenMPI et GCC 9.3.0.

Vous pouvez exécuter le script ci-dessous en le copiant sur la grappe que vous utilisez et en lançant **bash fenics-install.sh**.

À l'installation, une notification vous informe qu'un nouveau répertoire sera créé pour l'application, ou que le répertoire sera remplacé si l'application s'y trouve déjà. Les directives d'utilisation seront affichées quand l'installation sera terminée. Le script peut être modifié pour spécifier un répertoire différent.

```sh title="fenics-install.sh"
#!/usr/bin/env bash
# =============================================================================
# Compile script for FEniCS 2019.1.0
# =============================================================================

set -e

FENICS_INSTALL=$HOME/fenics
FENICS_VERSION=2019.1.0
PYBIND11_VERSION=2.2.3
export PYTHONPATH=$PYTHONPATH:$FENICS_INSTALL/lib/python3.10/site-packages

module purge
module load StdEnv/2020
module load gcc/9.3.0
module load hdf5-mpi/1.10.6
module load boost/1.72.0
module load eigen
module load python/3.10.2
module load scipy-stack/2023b
module load mpi4py/3.0.3
module load petsc/3.17.1
module load slepc/3.17.2
module load scotch/6.0.9
module load fftw-mpi/3.3.8
module load ipp/2020.1.217
module load swig
module load flexiblas

main () {
    warning_install
    make_fenics_directory
    download_py_packages $FENICS_VERSION
    make_py_packages
    make_pybind11
    make_dolfin
    print_instructions
}

warning_install () {
    echo "---------------------------------------------------------------"
    echo "AVERTISSEMENT : L'INSTALLATION DE FENICS/DOLFIN EFFACERA CE RÉPERTOIRE"
    echo "     $FENICS_INSTALL "
    echo
    echo "SI VOUS NE VOULEZ PAS QUE CELA ARRIVE, APPUYEZ SUR CTRL-C POUR ANNULER"
    echo "APPUYEZ SUR N'IMPORTE QUELLE TOUCHE POUR CONTINUER"
    echo "---------------------------------------------------------------"
    read -n 1
}

print_instructions () {
    echo "---------------------------------------------------------------"
    echo "POUR UTILISER FENICS/DOLFIN, VOUS DEVEZ FAIRE :"
    echo
    echo "module load StdEnv/2020"
    echo "source $FENICS_INSTALL/bin/activate"
    echo "source $FENICS_INSTALL/share/dolfin/dolfin.conf"
    echo "---------------------------------------------------------------"
}

make_fenics_directory () {
    rm -rf $FENICS_INSTALL
    mkdir -p $FENICS_INSTALL && cd $FENICS_INSTALL
}

download_py_packages () {
    version=release
    cd $FENICS_INSTALL
    git clone --branch=$version https://bitbucket.org/fenics-project/fiat.git
    git clone --branch=$version https://bitbucket.org/fenics-project/dijitso.git
    git clone https://bitbucket.org/fenics-project/ufc-deprecated.git ufc
    git clone --branch=$version https://bitbucket.org/fenics-project/ufl.git
    git clone --branch=$version https://bitbucket.org/fenics-project/ffc.git
    git clone --branch=$version https://bitbucket.org/fenics-project/dolfin.git
    git clone --branch=$version https://bitbucket.org/fenics-project/mshr.git
    git clone --branch=v$PYBIND11_VERSION \
        https://github.com/pybind/pybind11.git

    chmod u+w ~/fenics/*/.git/objects/pack/*

    mkdir -p $FENICS_INSTALL/pybind11/build
    mkdir -p $FENICS_INSTALL/dolfin/build
    mkdir -p $FENICS_INSTALL/mshr/build
}

make_pybind11 () {
    cd $FENICS_INSTALL/pybind11/build

    source $FENICS_INSTALL/bin/activate

    cmake -DPYBIND11_TEST=off \
          -DCMAKE_INSTALL_PREFIX=$HOME/fenics \
          -DPYBIND11_CPP_STANDARD=-std=c++11 ..
    make -j8 install
}

make_py_packages () {
    cd $FENICS_INSTALL
    virtualenv --no-download $FENICS_INSTALL
    source $FENICS_INSTALL/bin/activate
    pip3 install ply
    pip3 install numpy
    cd $FENICS_INSTALL/fiat    && pip3 install .
    cd $FENICS_INSTALL/dijitso && pip3 install .
    cd $FENICS_INSTALL/ufl     && pip3 install .
    cd $FENICS_INSTALL/ffc     && pip3 install .
}

make_dolfin () {
    cd $FENICS_INSTALL/dolfin/build

    source $FENICS_INSTALL/bin/activate

    cmake .. -DDOLFIN_SKIP_BUILD_TESTS=true \
          -DCMAKE_EXE_LINKER_FLAGS="-lpthread" \
          -DEIGEN3_INCLUDE_DIR=$EBROOTEIGEN/include \
          -DCMAKE_INSTALL_PREFIX=$HOME/fenics \
          -DCMAKE_SKIP_RPATH=ON \
          -DRT_LIBRARY=$EBROOTGENTOO/lib64/librt.so \
          -DHDF5_C_LIBRARY_dl=$EBROOTGENTOO/lib64/libdl.so \
          -DHDF5_C_LIBRARY_m=$EBROOTGENTOO/lib64/libm.so \
          -DHDF5_C_LIBRARY_pthread=$EBROOTGENTOO/lib64/libpthread.so \
          -DHDF5_C_LIBRARY_z=$EBROOTGENTOO/lib64/libz.so \
          -DSCOTCH_DIR=$EBROOTSCOTCH -DSCOTCH_LIBRARIES=$EBROOTSCOTCH/lib \
          -DSCOTCH_INCLUDE_DIRS=$EBROOTSCOTCH/include \
          -DBLAS_blas_LIBRARY=$EBROOTFLEXIBLAS/lib/libflexiblas.so

    make -j 8 install
    cd $FENICS_INSTALL/dolfin/python && pip3 install .
}

main
```

## Plugiciels

!!! warning "Section obsolète"
    Cette section n'est pas à jour pour l'environnement StdEnv/2020.

Installez d'abord FEniCS en suivant les directives ci-dessus.

### mshr

```sh title="mshr_install.sh"
module load hdf5-mpi/1.8.18 boost eigen python/3.5 scipy-stack/2017b petsc/3.7.5 fftw-mpi/3.3.6

export CMAKE_PREFIX_PATH=/home/$USER/software/dolfin/share/dolfin/cmake/:$CMAKE_PREFIX_PATH

git clone https://bitbucket.org/fenics-project/mshr.git
cd mshr
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$HOME/software/mshr   -DCMAKE_BUILD_TYPE=Release -DCMAKE_SKIP_RPATH=ON -DCMAKE_PREFIX_PATH=$NIXUSER_PROFILE:$CMAKE_PREFIX_PATH -DEIGEN3_INCLUDE_DIR=$EBROOTEIGEN/include 

make
make install
```

Ensuite, exécutez

```sh title="fenics_mshr_run.sh"
module load hdf5-mpi/1.8.18 boost eigen python/3.5 scipy-stack/2017b petsc/3.7.5 fftw-mpi/3.3.6
source ~/software/dolfin/share/dolfin/dolfin.conf
source ~/fenics/bin/activate
export PYTHONPATH=$HOME/software/mshr/lib/python3.5/site-packages:$PYTHONPATH
export LD_LIBRARY_PATH=$HOME/software/mshr/lib:$LD_LIBRARY_PATH
```

## Utilisation d'un conteneur Singularity

Le pilote Singularity Recipe télécharge l'image FEniCS Docker, l'installe et télécharge des paquets additionnels comme Python, par exemple. Exécutez le pilote sur votre ordinateur où Singularity est installé sous Linux et où vous avez toutes les permissions.

Utilisez la commande

```bash
sudo singularity build FEniCS.simg FEniCS-ComputeCanada-Singularity-Recipe
```

Téléversez ensuite `FEniCS.simg` dans votre compte. L'image FEniCS Docker place plusieurs fichiers dans `/home/fenics`.

```text title="FEniCS-ComputeCanada-Singularity-Recipe"
Bootstrap: docker
From: quay.io/fenicsproject/stable:latest

%post
  sudo apt-get -qq update
  sudo apt-get -y upgrade
  sudo apt-get -y install python-bitstring python3-bitstring
  sudo apt-get -y install python-certifi python3-certifi
  sudo apt-get -y install python-cryptography python3-cryptography
  sudo apt-get -y install python-cycler python3-cycler
  sudo apt-get -y install cython cython3
  sudo apt-get -y install python-dateutil python3-dateutil
  sudo apt-get -y install python-deap python3-deap
  sudo apt-get -y install python-decorator python3-decorator
  sudo apt-get -y install python-ecdsa python3-ecdsa
  sudo apt-get -y install python-ecdsa python3-ecdsa
  sudo apt-get -y install python-enum34
  sudo apt-get -y install python-funcsigs python3-funcsigs
  sudo apt-get -y install ipython ipython3 python-ipython-genutils python3-ipython-genutils
  sudo apt-get -y install python-jinja2 python3-jinja2
  sudo apt-get -y install python-jsonschema python3-jsonschema
  sudo apt-get -y install python-lockfile python3-lockfile
  sudo apt-get -y install python-markupsafe python3-markupsafe
  sudo apt-get -y install python-matplotlib python3-matplotlib
  sudo apt-get -y install python-mistune python3-mistune
  sudo apt-get -y install python-mock python3-mock
  sudo apt-get -y install python-mpmath python3-mpmath
  sudo apt-get -y install python-netaddr python3-netaddr
  sudo apt-get -y install python-netifaces python3-netifaces
  sudo apt-get -y install python-nose python3-nose
  sudo apt-get -y install ipython-notebook ipython3-notebook
  sudo apt-get -y install python-numpy python3-numpy
  sudo apt-get -y install python-pandas python3-pandas
  sudo apt-get -y install python-paramiko python3-paramiko
  sudo apt-get -y install python-path python3-path
  sudo apt-get -y install python-pathlib
  sudo apt-get -y install python-pbr python3-pbr
  sudo apt-get -y install python-pexpect python3-pexpect
  sudo apt-get -y install python-pickleshare python3-pickleshare
  sudo apt-get -y install python-prompt-toolkit python3-prompt-toolkit
  sudo apt-get -y install python-ptyprocess python3-ptyprocess
  sudo apt-get -y install python-pycryptopp
  sudo apt-get -y install python-pygments python3-pygments
  sudo apt-get -y install python-pyparsing python3-pyparsing
  sudo apt-get -y install python-zmq python3-zmq
  sudo apt-get -y install python-requests python3-requests
  sudo apt-get -y install python-scipy python3-scipy
  sudo apt-get -y install python-setuptools python3-setuptools
  sudo apt-get -y install python-simplegeneric python3-simplegeneric
  sudo apt-get -y install python-singledispatch python3-singledispatch
  sudo apt-get -y install python-six python3-six
  sudo apt-get -y install python-sympy python3-sympy
  sudo apt-get -y install python-terminado python3-terminado
  sudo apt-get -y install python-tornado python3-tornado
  sudo apt-get -y install python-traitlets python3-traitlets
  sudo apt-get -y install automake git-core libopenmpi-dev libtool mercurial openmpi-bin 
  sudo apt-get -y install python3-pip python3-venv

  # Clean up downloaded and temporary files...
  sudo apt-get clean
  sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
```

## Installation de FEniCS Legacy (2019) sur Trillium

Dans votre répertoire `/home`, configurez et testez le conteneur pour la version FEniCS Legacy 2019 avec les instructions suivantes.

### 1. Téléchargez l'image Docker au format Apptainer SIF

```bash
apttainer pull fenics-legacy.sif docker://ghcr.io/scientificcomputing/fenics-gmsh:2024-05-30
```

### 2. Créez un bac à sable (*sandbox*) avec permission d'écriture

Créez l'arborescence *fenics-legacy.sandbox* à partir du fichier SIF afin de modifier ou installer d'autres paquets.

```bash
apptainer build --sandbox fenics-legacy.sandbox fenics-legacy.sif
```

**Remarques :**
- la commande crée le répertoire *fenics-legacy.sandbox*
- Vous pouvez modifier le nom du répertoire (par exemple *fenics-dev/* ou *my_rw_image/*)
- le suffixe *.sandbox* est optionnel

### 3. Certificat pip

À l'intérieur du bac à sable, créez un dossier de certificats et un lien symbolique vers le faisceau de CA afin que pip/SSL fasse confiance au HTTPS :

```bash
apptainer exec --writable fenics-legacy.sandbox sh -c "mkdir -p /etc/pki/tls/certs && ln -s /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt"
```

### 4. Créez un nouveau SIF à partir du bac à sable

Une fois les modifications du bac à sable terminées, utilisez-le pour créer une nouvelle image en lecture seulement. Cette image est portable et permet des calculs reproductibles.

```bash
apptainer build fenics-legacy-updated.sif fenics-legacy.sandbox
```

### 5. Effectuez ces courts tests

```bash
apptainer exec --bind $PWD:/root/shared --pwd /root/shared fenics-legacy-updated.sif python3 -c "import ufl_legacy; print('ufl_legacy ok. version:', ufl_legacy.__version__)"
```

**Remarques :**
- `--bind $PWD:/root/shared` monte le répertoire hôte actif dans le conteneur
- `--pwd` définit le répertoire de travail

## Remarques importantes

- FEniCS Legacy (2019.1.x) nécessite UFL Legacy, déjà inclus.
- Le paquet Python se nomme `ufl_legacy`, et non `ufl`.
- La version UFL compatible est 2022.3.0 (fournie par `ufl_legacy`).
- L'instruction `import ufl` devrait échouer, mais non `import ufl_legacy`.

## Créez un alias ufl

Certains logiciels (tels que Oasis) assument que le nom du module à charger est `ufl`. Plutôt que de modifier ces logiciels, vous pouvez créer un *shim* qui réexporte `ufl_legacy` sous le nom `ufl`.

Créez le fichier `/pyshims/ufl/__init__.py` qui contient

```python
import sys
import ufl_legacy as ufl

api = [k for k in ufl.__dict__.keys() if not k.startswith('__') and not k.endswith('__')]
for key in api:
    sys.modules['ufl.{}'.format(key)] = getattr(ufl, key)
del api
```

## Testez l'alias

Ajoutez le chemin de l'alias (*shim*) à PYTHONPATH lors de l'utilisation du conteneur.

```bash
APPTAINERENV_PYTHONPATH=<path_to_shim>:$PYTHONPATH apptainer exec --bind /scratch:/scratch ~/fenics-legacy-updated.sif python3 -c "from ufl.tensors import ListTensor; print('UFL tensors ok')"
```

**Remarques :**
- `--bind /scratch:/scratch` monte le répertoire hôte actif dans le conteneur