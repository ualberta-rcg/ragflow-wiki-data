---
title: "Visual Studio Code/fr"
slug: "visual_studio_code"
lang: "fr"

source_wiki_title: "Visual Studio Code/fr"
source_hash: "d1afcad478df676fbe7b894883f3f76c"
last_synced: "2026-04-10T15:28:10.183781+00:00"
last_processed: "2026-04-11T12:45:39.159435+00:00"

tags:
  []

keywords:
  - "extensions.autoUpdate"
  - "settings.json"
  - "VS Code"
  - "internet access"
  - "telemetry"
  - "code-server"
  - "interactive job"
  - "Visual Studio Code"
  - "update.mode"
  - "développement local"
  - "Remote SSH"
  - "nœud de connexion"
  - "débogage"
  - "remote.extensionKind"
  - "Remote-SSH"
  - "configuration SSH"
  - "SLURM"
  - "github.copilot"
  - "VS Code launcher"
  - "JupyterLab"

questions:
  - "Pourquoi est-il fortement déconseillé d'utiliser Visual Studio Code directement sur les nœuds de connexion d'un système distant ?"
  - "Quelle est la procédure recommandée pour synchroniser et tester sur les systèmes distants un code développé localement avec VS Code ?"
  - "Quelles alternatives sécuritaires sont proposées pour éditer des fichiers ou déboguer du code directement sur les systèmes distants ?"
  - "Comment configurer son fichier SSH local pour préparer la connexion à distance avec VS Code ?"
  - "Quelles modifications spécifiques faut-il apporter aux paramètres locaux de VS Code via la palette de commandes ?"
  - "Quelles sont les étapes pour créer et paramétrer le fichier de configuration (settings.json) directement sur le serveur distant ?"
  - "What are the steps required to launch VS Code from within JupyterLab?"
  - "What level of resources should be selected when starting the interactive JupyterLab job?"
  - "What network limitation applies to the code-server instance running in the compute job?"
  - "How does this configuration manage automatic updates and telemetry data collection?"
  - "What specific behaviors are defined for extensions running in a remote environment?"
  - "How are AI-powered features like GitHub Copilot and chat agents handled in these settings?"
  - "Comment établir et fermer correctement une connexion à distance avec VS Code via SSH ?"
  - "Quelles sont les restrictions et les avertissements à respecter lors de l'utilisation de VS Code sur un nœud de connexion ?"
  - "Quelle est la procédure détaillée pour configurer et se connecter à un nœud de calcul interactif avec SLURM ?"
  - "Comment établir et fermer correctement une connexion à distance avec VS Code via SSH ?"
  - "Quelles sont les restrictions et les avertissements à respecter lors de l'utilisation de VS Code sur un nœud de connexion ?"
  - "Quelle est la procédure détaillée pour configurer et se connecter à un nœud de calcul interactif avec SLURM ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

[Visual Studio Code](https://code.visualstudio.com/) est un environnement de développement intégré (EDI) local personnalisable de [Microsoft](https://www.microsoft.com/) qui offre plusieurs extensions.

!!! warning "Consommation importante de ressources"
    **VS Code pose beaucoup de problèmes sur les nœuds de connexion. Autant que possible, *utilisez-le localement* ou configurez-le comme décrit ci-dessous.**

!!! warning "Exécution et débogage de code"
    **Si Visual Studio Code est connecté à un système distant, l'exécution ou le débogage du code peut entraîner des problèmes de performance ou des interruptions de système. Utilisez plutôt l'environnement `code-server` plus sécuritaire qui est plus approprié pour le débogage.**

*   Utilisez VS Code en mode local et évitez de le connecter aux systèmes. Enregistrez vos modifications dans les fichiers de `/project` avec Git, puis appliquez-les sur les systèmes pour faire les tests.
*   Utilisez `nano` ou `vim` pour modifier les fichiers directement sur les systèmes.
*   Pour le débogage et les tests rapides, vous pouvez charger le module `code-server`.
*   Si aucune de ces solutions n'est possible, vous pouvez configurer VS Code pour les connexions à distance.

## Utiliser VS Code localement

Les avantages sont les suivants :

*   vitesse et stabilité : l'exécution locale de VS Code réduit les interruptions réseau et améliore la performance, ce qui est idéal pour le développement itératif;
*   accès direct : vous pouvez interagir avec les fichiers, les extensions et le terminal directement sur votre ordinateur, sans latence;
*   possibilité de travailler hors ligne : aucune contrainte de connexion Internet ou de serveur distant, ce qui vous permet de coder n'importe où et n'importe quand.

Il est recommandé de développer localement avec VS Code. Vous pouvez ainsi personnaliser et ajouter vos extensions et langages préférés avec VS Code.

Une fois votre projet prêt à être testé sur les systèmes, vous pouvez enregistrer vos modifications dans un dépôt Git, les envoyer vers un hébergeur distant comme GitHub ou GitLab, puis vous connecter au système et récupérer vos modifications pour effectuer le test.

Pour plus d'information sur la gestion de versions, voir [VS Code Source Control](https://code.visualstudio.com/docs/sourcecontrol/overview).

Après avoir enregistré et envoyé vos modifications vers le dépôt distant, connectez-vous au système via le terminal.

```bash
ssh <username>@<hostname>.alliancecan.ca
```

Clonez le dépôt (s'il n'existe pas)

```bash
git clone git@github.com:username/reponame.git
```

ou changez le répertoire pour votre dépôt et incorporez les modifications avec

```bash
cd myrepo
git pull
```

Ensuite, testez vos modifications dans une [tâche interactive](running-jobs.md#taches-interactives) de courte durée en utilisant des ressources minimales.

## Modifier des fichiers sur les systèmes

Bien que VS Code soit excellent pour le développement local, il est parfois nécessaire d'accéder directement aux fichiers sur un système distant. Dans de tels cas, les éditeurs basés sur le terminal comme `nano` ou `vim` offrent un moyen léger et efficace de modifier les fichiers directement depuis la ligne de commande.

Si vous préférez une interface graphique, l'éditeur de texte [JupyterLab](jupyterlab.md) est une option commode; les scripts aux formats Markdown, Python et autres sont pris en charge.

## Débogage et tests

Si vous devez déboguer ou tester votre code sur les systèmes, vous pouvez démarrer une instance de `code-server` depuis [JupyterLab](jupyterlab.md#vs-code).

1.  Accédez à l'une des [options de lancement de JupyterLab](jupyterlab.md#lancer-jupyterlab).
2.  Sélectionnez des ressources minimales et démarrez une tâche interactive JupyterLab.
3.  Dans l'onglet *Lanceur*, cliquez sur le bouton de lancement de VS Code.

!!! note
    L'instance de `code-server` à laquelle vous accédez s'exécute dans une tâche de calcul qui **n'a pas** d'accès à Internet.
    Le module `code-server` dispose déjà de plusieurs extensions courantes, mais nous pouvons en ajouter d'autres sur demande.

## Installation personnalisée des extensions

(en préparation)

## Configuration de VS Code pour la connexion à distance

Si aucune des solutions ci-dessus ne convient à votre cas, vous pouvez configurer VS Code pour vous connecter à un hôte distant avec l'extension Remote SSH.

### Configuration SSH

Si ce n'est pas déjà fait, [générez votre clé SSH](ssh-keys.md#generer-une-cle-ssh) et [ajoutez votre clé SSH *publique* sur la base de données RCG](ssh-keys.md#installer-votre-cle).

Ensuite, créez ou ajoutez un fichier de configuration SSH sur votre ordinateur local.

```text title="~/.ssh/config"
Host *
  ServerAliveInterval 30
  User your_username

Host rorqual narval nibi fir
  HostName %h.alliancecan.ca
```

### Configuration locale

1.  Dans VS Code, ouvrez la *Palette de commandes* et appuyez sur **Ctrl+Shift+P** (Windows/Linux) ou **Cmd+Shift+P** (macOS).
2.  Dans les paramètres utilisateur, sélectionnez (**Préférences: Ouvrir les paramètres utilisateur (JSON)**) et collez ou intégrez la configuration suivante :

```json title="local-settings.json"
{
  // file-watch + search
  "files.watcherExclude": {
    "**/.git/**": true,
    "**/node_modules/**": true,
    "**/dist/**": true,
    "**/build/**": true
  },
  "search.exclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/node_modules/**": true
  },
  "search.maxThreads": 2,
  "search.ripgrep.maxThreads": 2,
  "search.useIgnoreFiles": true,

  // extensions & updates
  "remote.extensionKind": {
    "*": ["ui"],
    "ms-python.python": ["ui"]
  },
  "remote.defaultExtensionsIfInstalledLocally": ["GitHub.vscode-pull-request-github"],

  // remote-ssh
  "remote.SSH.showLoginTerminal": false,
  "remote.SSH.enableDynamicForwarding": false,
  "remote.SSH.enableServerAutoShutdown": 30,

  "workbench.startupEditor": "none"
}
```

3.  Enregistrez et relancez VS Code.

### Configuration distante

1.  Connectez-vous au système via un terminal externe.
    ```bash
    ssh <username>@<host>.alliancecan.ca
    ```

2.  Créez le répertoire.
    ```bash
    mkdir -p ~/.vscode-server/data/Machine/
    ```

3.  Créez le fichier de configuration `settings.json`.
    ```bash
    nano ~/.vscode-server/data/Machine/settings.json
    ```

4.  Copiez la configuration ci-dessous. Vous pourriez avoir besoin de fusionner manuellement les paramètres avec les vôtres, s'il y a lieu.

```json title="system-settings.json"
{
  // file-watch + search
  "files.watcherExclude": {
    "**/.git/**": true,
    "**/node_modules/**": true,
    "**/dist/**": true,
    "**/build/**": true,
    "/**": true
  },
  "search.exclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/node_modules/**": true,
    "/**": true
  },
  "search.followSymlinks": false,
  "search.maxThreads": 2,
  "search.ripgrep.maxThreads": 2,
  "search.useIgnoreFiles": true,
  "search.searchOnType": false,

  // extensions & updates
  "extensions.autoCheckUpdates": false,
  "extensions.autoUpdate": false,
  "update.mode": "none",
  "remote.extensionKind": {
    "*": ["ui"],
    "ms-python.python": ["ui"]
  },

  // Copilot
  "chat.agent.enabled": false,
  "github.copilot.enable": {
    "*": false
  },
  "remote.defaultExtensionsIfInstalledLocally": ["GitHub.vscode-pull-request-github"],

  // telemetry & git
  "telemetry.enableTelemetry": false,
  "telemetry.enableCrashReporter": false,
  "telemetry.telemetryLevel": "off",
  "telemetry.feedback.enabled": false,
  "git.autofetch": false,
  "git.enableStatusBarSync": false,

  // remote-ssh
  "remote.SSH.showLoginTerminal": false,
  "remote.SSH.enableDynamicForwarding": false,
  "remote.SSH.enableServerAutoShutdown": 30,

  "workbench.startupEditor": "none"
}
```

### Connexion

1.  Ouvrez la *Palette de commandes* dans VS Code : appuyez sur `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (macOS).
2.  Tapez `remote` et sélectionnez ensuite **Remote-SSH : Se connecter à l'hôte...**.
3.  Choisissez l'hôte (système distant) et confirmez.

La connexion se fait avec un nœud de connexion.

!!! warning "Sur un nœud de connexion..."
    ... ne faites pas de tests, ne faites aucun débogage et n'exécutez pas votre code.

### Fermeture de votre connexion

1.  Ouvrez la *Palette de commandes* dans VS Code : appuyez sur `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (macOS).
2.  Tapez `remote` et sélectionnez ensuite **Remote-SSH : Arrêter le serveur VS Code sur l'hôte...**.
3.  Choisissez l'hôte (système distant) et confirmez.
4.  Ouvrez le menu *Fichier* et sélectionnez **Fermer la connexion à distance**.

## Fonction avancée : Se connecter à un nœud de calcul interactif

Mettez à jour votre configuration en ajoutant les lignes suivantes :

=== "Narval"
    ```text title="~/.ssh/config"
    Host nc* ng* nl*
      ProxyJump narval
      User your_username
    ```

=== "Rorqual"
    ```text title="~/.ssh/config"
    Host rc* rg* rl*
      ProxyJump rorqual
      User your_username
    ```

1.  Dans un terminal externe, connecté au système via SSH, démarrez une nouvelle [tâche interactive](running-jobs.md#taches-interactives) (avec `salloc`) avec au moins 2000M de mémoire.
    *   Notez le nom du nœud de calcul alloué.
    *   Si vous devez travailler avec des variables d'environnement `SLURM_*` dans VS Code, enregistrez-les toutes dans un fichier *source* :
        ```bash
        env | grep SLURM_ | sed -e 's/^\(.*\)=\(.*\)$/export \1="\2"/g' > slurm_var.sh
        ```

2.  Dans VS Code, démarrez une nouvelle session à distance avec le nom du nœud de calcul alloué.
    *   Appuyez sur `F1` ou `Ctrl+Shift+P` pour lancer la *Palette de commandes*.
    *   Commencez à taper *Remote* et sélectionnez **Remote-SSH : Se connecter à l'hôte...**.
    *   Entrez le nom du nœud de calcul noté.
        *   Si vous êtes invité à choisir le type de système d'exploitation, sélectionnez **Linux**.

3.  Si vous devez travailler avec des variables d'environnement `SLURM_*`, naviguez jusqu'au répertoire de travail dans un terminal VS Code et *sourcez* le fichier `slurm_var.sh`.
    ```bash
    source slurm_var.sh
    ```

## Remarques importantes

*   VS Code ne peut pas être utilisé sur les nœuds de connexion de tamIA.