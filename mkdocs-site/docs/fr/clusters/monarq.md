---
title: "MonarQ/fr"
slug: "monarq"
lang: "fr"

source_wiki_title: "MonarQ/fr"
source_hash: "116bd5e05dd85abbdcca86a37a295bf6"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T09:29:02.379486+00:00"

tags:
  []

keywords:
  - "PennyLane"
  - "dictionnaire"
  - "algorithmes quantiques"
  - "programmation quantique"
  - "Narval"
  - "SBATCH"
  - "MonarQ"
  - "résultat du circuit"
  - "fichier slurm"
  - "Informatique quantique"
  - "python my_circuit.py"
  - "circuit quantique"
  - "Snowflurry"
  - "Julia"
  - "Calcul Québec"
  - "ordinateur quantique"
  - "qubits"

questions:
  - "Qu'est-ce que l'ordinateur quantique MonarQ et quand sera-t-il de nouveau opérationnel ?"
  - "Quelles sont les étapes à suivre pour demander et obtenir l'accès à MonarQ ?"
  - "Quelles sont les caractéristiques techniques du processeur et quelles bibliothèques logicielles permettent de l'utiliser ?"
  - "Quels sont les prérequis et la méthode de connexion nécessaires pour accéder à l'infrastructure quantique MonarQ ?"
  - "Comment préparer son environnement virtuel Python et configurer ses identifiants pour utiliser MonarQ comme machine avec PennyLane ?"
  - "De quelle manière doit-on soumettre l'exécution d'un circuit quantique via l'ordonnanceur Slurm et où peut-on consulter les résultats obtenus ?"
  - "Quelle est la relation de compatibilité entre MonarQ et Snowflurry, et dans quel langage ce dernier est-il programmé ?"
  - "Quel est l'objectif principal du plugiciel PennyLane-CalculQuébec développé par Calcul Québec ?"
  - "Quels avantages l'environnement PennyLane offre-t-il aux utilisateurs souhaitant exécuter des circuits quantiques sur MonarQ ?"
  - "Comment la mémoire par processeur est-elle configurée pour l'exécution du script Python ?"
  - "Quelle est la convention de nommage du fichier de sortie généré par la tâche ?"
  - "Sous quel format de données les résultats du circuit sont-ils enregistrés dans le fichier de sortie ?"
  - "Quelles sont les principales applications et les types de calculs pour lesquels MonarQ est le mieux adapté ?"
  - "Comment peut-on obtenir du soutien technique ou s'inscrire à des sessions de formation sur l'informatique quantique ?"
  - "Où doit-on se diriger pour trouver des instructions sur la soumission de tâches sur Narval et accéder aux autres outils disponibles ?"
  - "Quelles sont les principales applications et les types de calculs pour lesquels MonarQ est le mieux adapté ?"
  - "Comment peut-on obtenir du soutien technique ou s'inscrire à des sessions de formation sur l'informatique quantique ?"
  - "Où doit-on se diriger pour trouver des instructions sur la soumission de tâches sur Narval et accéder aux autres outils disponibles ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

| Nœud de connexion | **https://monarq.calculquebec.ca** |

!!! attention "Avis important"
    **MonarQ est actuellement en cours de maintenance et devrait être opérationnel en février 2026. En attendant, Calcul Québec peut offrir l'accès à une machine similaire mais plus petite, avec 6 qubits.**

MonarQ est un ordinateur quantique supraconducteur à 24 qubits développé à Montréal par [Anyon Systèmes](https://anyonsys.com/) et situé à l'[École de technologie supérieure](http://www.etsmtl.ca/). Pour plus d'informations sur les spécifications et les performances de MonarQ, voir [Spécifications techniques](#spécifications-techniques) ci-dessous.

Le nom MonarQ est inspiré par la forme du circuit de qubits sur le processeur quantique qui rappelle le papillon monarque, symbole d’évolution et de migration. La majuscule Q rappelle la nature quantique de l’ordinateur et son origine québécoise. L'acquisition de MonarQ a été rendue possible grâce au soutien du [Ministère de l'Économie, de l'Innovation et de l'Énergie du Québec (MEIE)](https://www.economie.gouv.qc.ca/) et de [Développement Économique Canada (DEC)](https://dec.canada.ca/).

## Accéder à MonarQ

1.  Pour commencer le processus d'accès à MonarQ, [remplir ce formulaire](https://forms.gle/zH1a3oB4SGvSjAwh7). Il doit être complété par le chercheur principal.
2.  Vous devez [avoir un compte avec l'Alliance](https://alliancecan.ca/fr/services/calcul-informatique-de-pointe/portail-de-recherche/gestion-de-compte/demander-un-compte) pour avoir accès à MonarQ.
3.  Rencontrez notre équipe pour discuter des spécificités de votre projet, des accès et des détails de facturation.
4.  Recevez l'accès au tableau de bord MonarQ et générez votre jeton d'accès.
5.  Pour démarrer, voir [Premiers pas sur MonarQ](#premiers-pas-sur-monarq) ci-dessous.

Contactez notre équipe quantique à [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca) si vous avez des questions ou si vous souhaitez avoir une discussion plus générale avant de demander l'accès.

## Spécifications techniques

À l'instar des processeurs quantiques disponibles aujourd'hui, MonarQ fonctionne dans un environnement où le bruit reste un facteur significatif. Les métriques de performance, mises à jour à chaque calibration, sont accessibles via le portail Thunderhead. L'accès à ce portail nécessite une approbation d'accès à MonarQ.

On y retrouve, entre autres, les métriques suivantes :
*   Processeur quantique de 24 qubits
*   Porte un qubit avec fidélité de 99.8% et durée de 32ns
*   Porte deux qubits avec fidélité de 96% et durée de 90ns
*   Temps de cohérence de 4-10μs (en fonction de l'état)
*   Profondeur maximale du circuit d'environ 350 pour des portes à un qubit et 115 pour des portes à deux qubits

## Logiciels de calcul quantique

Il existe plusieurs bibliothèques logicielles spécialisées pour faire du calcul quantique et pour développer des algorithmes quantiques. Ces bibliothèques permettent de construire des circuits qui sont exécutés sur des simulateurs qui imitent la performance et les résultats obtenus sur un ordinateur quantique tel que MonarQ. Elles peuvent être utilisées sur toutes les grappes de l’Alliance.

*   [PennyLane](pennylane.md), bibliothèque de commandes en Python
*   [Snowflurry](snowflurry.md), bibliothèque de commandes en Julia
*   [Qiskit](qiskit.md), bibliothèque de commandes en Python

Les portes logiques quantiques du processeur de MonarQ sont appelées par le biais d'une bibliothèque logicielle [Snowflurry](https://github.com/SnowflurrySDK/Snowflurry.jl), écrite en [Julia](https://julialang.org/). Bien que MonarQ soit nativement compatible avec Snowflurry, il existe un plugiciel [PennyLane-CalculQuébec](https://github.com/calculquebec/pennylane-snowflurry) développé par Calcul Québec permettant d'exécuter des circuits sur MonarQ tout en bénéficiant des fonctionnalités et de l'environnement de développement offerts par [PennyLane](https://docs.alliancecan.ca/wiki/PennyLane).

## Premiers pas sur MonarQ

!!! note "Prérequis"
    Assurez-vous d’avoir un accès à MonarQ ainsi que vos identifiants de connexion (*username*, *API token*). Pour toute question, écrivez à [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca).

*   **Étape 1 : Connectez-vous à [Narval](narval.md)**
    *   MonarQ est uniquement accessible depuis Narval, une grappe de Calcul Québec. L’accès à Narval se fait à partir du nœud de connexion **narval.alliancecan.ca**.
    *   Pour de l’aide concernant la connexion à Narval, consultez la page [SSH](ssh.md).

*   **Étape 2 : Créez l’environnement**
    *   Créez un environnement virtuel Python (3.11 ou ultérieur) pour utiliser PennyLane et le plugiciel [PennyLane-CalculQuébec](https://github.com/calculquebec/pennylane-snowflurry). Ces derniers sont déjà installés sur Narval et vous aurez uniquement à importer les bibliothèques logicielles que vous souhaitez.

    ```bash
    module load python/3.11
    virtualenv --no-download --clear ~/ENV && source ~/ENV/bin/activate
    pip install --no-index --upgrade pip
    pip install --no-index --upgrade pennylane-calculquebec
    python -c "import pennylane; import pennylane_calculquebec"
    ```

*   **Étape 3 : Configurez vos identifiants sur MonarQ et définissez MonarQ comme machine (*device*)**
    *   Ouvrez un fichier Python .py et importez les dépendances nécessaires, soit PennyLane et CalculQuebecClient dans l’exemple ci-dessous.
    *   Créez un client avec vos identifiants. Votre jeton est disponible à partir du portail Thunderhead. Le *host* est **https://monarq.calculquebec.ca**.
    *   Créez un *device* PennyLane avec votre client. Vous pouvez également mentionner le nombre de qubits (*wires*) à utiliser et le nombre d'échantillons (*shots*).
    *   Pour de l’aide, consultez [pennylane_calculquebec](https://github.com/calculquebec/pennylane-calculquebec/blob/main/doc/getting_started.ipynb).

    ```python title="my_circuit.py"
    import pennylane as qml
    from pennylane_calculquebec.API.client import CalculQuebecClient

    my_client = CalculQuebecClient(host="https://monarq.calculquebec.ca", user="your username", access_token="your access token", project_id="your project_id")

    dev = qml.device("monarq.default", client = my_client, wires = 3)
    ```

*   **Étape 4 : Créez votre circuit**
    *   Dans le même fichier Python vous pouvez maintenant coder votre circuit quantique

    ```python title="my_circuit.py"
    @qml.set_shots(1000)
    @qml.qnode(dev)

    def bell_circuit():
        qml.Hadamard(wires=0)
        qml.CNOT(wires=[0, 1])
        qml.CNOT(wires=[1, 2])

        return qml.counts()

    result = bell_circuit()
    print(result)
    ```

*   **Étape 5 : Exécutez votre circuit depuis l'ordonnanceur**
    *   La commande `sbatch` est utilisée pour soumettre une tâche [sbatch](https://slurm.schedmd.com/sbatch.html).

    ```bash
    sbatch simple_job.sh
    Submitted batch job 123456
    ```

    Avec un script Slurm ressemblant à ceci:

    ```sh title="simple_job.sh"
    #!/bin/bash
    #SBATCH --time=00:15:00
    #SBATCH --account=def-someuser # Votre username
    #SBATCH --cpus-per-task=1      # Modifiez s'il y a lieu
    #SBATCH --mem-per-cpu=1G 	  # Modifiez s'il y a lieu
    python my_circuit.py
    ```

*   Le résultat du circuit est écrit dans un fichier dont le nom commence par slurm-, suivi de l'ID de la tâche et du suffixe .out, par exemple *slurm-123456.out*.
*   On retrouve dans ce fichier le résultat de notre circuit dans un dictionnaire `{'000': 496, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 504}`.
*   Pour plus d’information sur comment soumettre des tâches sur Narval, voir [Exécuter des tâches](running_jobs.md).

## Questions courantes

*   [Foire aux questions (FAQ)](https://docs.google.com/document/d/13sfHwJTo5tcmzCZQqeDmAw005v8I5iFeKp3Xc_TdT3U/edit?tab=t.0)

## Autres outils

*   [Transpileur quantique](transpileur_quantique.md)

## Applications

MonarQ est adapté aux calculs nécessitant de petites quantités de qubits de haute fidélité, ce qui en fait un outil idéal pour le développement et le test d'algorithmes quantiques. D'autres applications possibles incluent la modélisation de petits systèmes quantiques; les tests de nouvelles méthodes et techniques de programmation quantique et de correction d'erreurs; et plus généralement, la recherche fondamentale en informatique quantique.

## Soutien technique

Si vous avez des questions sur nos services quantiques, écrivez à [quantique@calculquebec.ca](mailto:quantique@calculquebec.ca).
Les sessions sur l'informatique quantique et la programmation avec MonarQ sont [listées ici.](https://www.eventbrite.com/o/calcul-quebec-8295332683)