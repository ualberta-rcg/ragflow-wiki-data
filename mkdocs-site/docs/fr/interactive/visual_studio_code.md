---
title: "Visual Studio Code/fr"
slug: "visual_studio_code"
lang: "fr"

source_wiki_title: "Visual Studio Code/fr"
source_hash: "38beaf0153da8eed14a6a1fa486069a7"
last_synced: "2026-05-24T00:00:16.123503+00:00"
last_processed: "2026-05-24T00:54:04.875439+00:00"

tags:
  []

keywords:
  - "code-server"
  - "settings.json"
  - "VS Code"
  - "Remote SSH"
  - "JupyterLab"
  - "Git"
  - "configuration SSH"
  - "remote.extensionKind"
  - "nœud de connexion"
  - "interactive job"
  - "extensions.autoUpdate"
  - "Remote-SSH"
  - "débogage"
  - "SLURM"
  - "update.mode"
  - "telemetry"
  - "Visual Studio Code"
  - "internet access"
  - "développement local"
  - "github.copilot"

questions:
  - "Pourquoi est-il fortement déconseillé de connecter Visual Studio Code directement aux nœuds de connexion des systèmes distants ?"
  - "Quelle est la méthode recommandée pour développer localement avec VS Code et transférer ses modifications vers les systèmes ?"
  - "Quelles solutions alternatives sont proposées pour éditer des fichiers ou déboguer du code directement sur les systèmes distants ?"
  - "Comment doit-on configurer son fichier SSH local pour se connecter aux serveurs distants de l'Alliance ?"
  - "Quelles modifications spécifiques faut-il apporter aux paramètres locaux de VS Code pour optimiser la recherche et la connexion SSH ?"
  - "Quelles sont les étapes à suivre sur le serveur distant pour créer et configurer le fichier settings.json de VS Code ?"
  - "What resources should be selected when starting the interactive JupyterLab job?"
  - "How do you access the VS Code application from within the JupyterLab interface?"
  - "What network restriction exists for the code-server instance running in the compute job?"
  - "How does this configuration handle automatic updates for the editor and its extensions?"
  - "What settings are applied to GitHub Copilot and chat agents in this file?"
  - "How does this configuration address data privacy regarding telemetry and crash reporting?"
  - "Quelles sont les étapes pour se connecter à un hôte distant dans VS Code et quelles sont les restrictions à respecter sur les nœuds de connexion ?"
  - "Comment configurer et établir une session VS Code sur un nœud de calcul interactif en utilisant SLURM et un ProxyJump ?"
  - "Quelle est la procédure pour fermer correctement une connexion distante et sur quels systèmes l'utilisation de VS Code est-elle interdite ?"

status:
  downloaded: true
  converted: true
  tagged: false
  keywords_generated: true
  ragflow_synced: true
  qa_generated: false
---

Visual Studio Code est un environnement de développement local intégré (IDE) personnalisable de [Microsoft](https://www.microsoft.com/) qui offre plusieurs extensions.

!!! warning "Consommation importante de ressources"
    **VS Code pose beaucoup de problèmes sur les nœuds de connexion. Autant que possible, *utilisez-le localement* ou configurez-le comme décrit ci-dessous.**

!!! warning "Exécution et débogage de code"
    **Si Visual Studio Code est connecté à un système distant, l'exécution ou le débogage du code peut entraîner des problèmes de performance ou des interruptions de système. Utilisez plutôt l'environnement `code-server` plus sécuritaire qui est plus approprié pour le débogage.**

*   Utilisez VS Code en mode local et évitez de le connecter aux systèmes. Enregistrez vos modifications dans les fichiers de `/project` avec Git, puis appliquez-les sur les systèmes pour faire les tests.
*   Utilisez `nano` ou `vim` pour modifier les fichiers directement sur les systèmes.
*   Pour le débogage et les tests rapides, vous pouvez charger le module `code-server`.
*   Si aucune de ces solutions n'est possible, vous pouvez configurer VS Code pour les connexions à distance.

## Utiliser VS Code localement

Les avantages sont les suivants :

*   vitesse et stabilité : l'exécution locale de VS Code réduit les interruptions réseau et améliore la performance, ce qui est idéal pour le développement itératif;
*   accès direct : vous pouvez interagir avec les fichiers, les extensions et le terminal directement sur votre ordinateur, sans latence;
*   possibilité de travailler hors ligne : aucune contrainte de connexion Internet ou de serveur distant, ce qui vous permet de coder n'importe où et n'importe quand.

Il est recommandé de développer localement avec VS Code. Vous pouvez ainsi personnaliser et ajouter vos extensions et langages préférés avec VS Code.

Une fois votre projet prêt à être testé sur les systèmes, vous pouvez enregistrer vos modifications dans un dépôt Git, les envoyer vers un hébergeur distant comme GitHub ou GitLab, puis vous connecter au système et récupérer vos modifications pour effectuer le test.

Pour plus d'information sur la gestion de versions, voir [Source Control de VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview).

Après avoir enregistré et envoyé vos modifications vers le dépôt distant, connectez-vous au système via le terminal.

```bash
ssh <nom_utilisateur>@<nom_hôte>.alliancecan.ca
```

Clonez le dépôt (s'il n'existe pas)

```bash
git clone git@github.com:nom_utilisateur/nom_depot.git
```

ou changez le répertoire pour votre dépôt et incorporez les modifications avec

```bash
cd mon_dépôt
git pull
```

Ensuite, testez vos modifications dans une courte [tâche interactive](../running-jobs/running_jobs.md) en utilisant des ressources minimales.

## Modifier des fichiers sur les systèmes

Bien que VS Code soit excellent pour le développement local, il arrive parfois que vous ayez besoin d'un accès direct aux fichiers sur un système distant. Dans ces cas, les éditeurs basés sur le terminal comme `nano` ou `vim` offrent un moyen léger et efficace de modifier les fichiers directement depuis la ligne de commande.

Si vous préférez une interface graphique, l'éditeur de texte [JupyterLab](jupyterlab.md) est une option commode; les scripts aux formats Markdown, Python et autres sont pris en charge.

## Débogage et tests

Si vous avez besoin de déboguer ou de tester votre code sur les systèmes, vous pouvez démarrer une instance de `code-server` à partir de [JupyterLab](jupyterlab.md#vs-code).

1.  Accédez à l'une des [options pour lancer JupyterLab](jupyterlab.md#lancer-jupyterlab).
2.  Sélectionnez des ressources minimales et démarrez une tâche interactive JupyterLab.
3.  Dans l'onglet Lanceur, cliquez sur le bouton de lancement de VS Code.

!!! note
    L'instance de `code-server` à laquelle vous accédez s'exécute dans une tâche de calcul qui **n'a pas** accès à Internet.

Le module `code-server` contient déjà plusieurs extensions courantes, mais nous pouvons en ajouter d'autres sur demande.

### Installation personnalisée des extensions
En préparation.

## Configuration de VS Code pour une connexion à distance

Si aucune des solutions ci-dessus ne vous convient, vous pouvez configurer VS Code pour vous connecter à un hôte distant avec l'extension Remote SSH.

### Configuration SSH

Si ce n'est pas déjà fait, [générez votre clé SSH](../getting-started/ssh_keys.md) et [ajoutez votre clé SSH *publique* au CCDB](../getting-started/ssh_keys.md).

Ensuite, créez ou ajoutez un fichier de configuration SSH sur votre ordinateur local.

```bash title="~/.ssh/config"
Host *
  ServerAliveInterval 30
  User votre_nom_utilisateur

Host rorqual narval nibi fir
  HostName %h.alliancecan.ca
```

### Configuration locale

1.  Dans VS Code, ouvrez la Palette de commandes et appuyez `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (macOS).

2.  Dans les paramètres d'utilisation, sélectionnez **Préférences : Ouvrir les paramètres utilisateur (JSON)** et collez ou intégrez la configuration suivante :

```json title="local-settings.json"
{
  // file-watch + search
  "files.watcherExclude": {
    "**/.git/**": true,
    "**/node_modules/**": true,
    "**/dist/**": true,
    "**/build/**": true,
  },
  "search.exclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/node_modules/**": true,
  },
  "search.maxThreads": 2,
  "search.ripgrep.maxThreads": 2,
  "search.useIgnoreFiles": true,

  // extensions & updates
  "remote.extensionKind": {
    "*": [
      "ui"
    ],
    "ms-python.python": [
      "ui"
    ]
  },
  "remote.defaultExtensionsIfInstalledLocally": [
    "GitHub.vscode-pull-request-github"
  ],

  // remote-ssh
  "remote.SSH.showLoginTerminal": false,
  "remote.SSH.enableDynamicForwarding": false,
  "remote.SSH.enableServerAutoShutdown": 30,

  "workbench.startupEditor": "none",
}
```

3.  Enregistrez et relancez VS Code.

### Configuration à distance

1.  Connectez-vous au système via un terminal externe.

```bash
ssh <nom_utilisateur>@<hôte>.alliancecan.ca
```

2.  Créez le répertoire.

```bash
mkdir -p ~/.vscode-server/data/Machine/
```

3.  Créez la configuration `settings.json`.

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
    "/**": true,
  },
  "search.exclude": {
    "**/.git/objects/**": true,
    "**/.git/subtree-cache/**": true,
    "**/node_modules/**": true,
    "/**": true,
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
    "*": [
      "ui"
    ],
    "ms-python.python": [
      "ui"
    ]
  },

  // Copilot
  "chat.agent.enabled": false,
  "github.copilot.enable": {
    "*": false,
  },
  "remote.defaultExtensionsIfInstalledLocally": [
    "GitHub.vscode-pull-request-github"
  ],

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

  "workbench.startupEditor": "none",
}
```

### Connexion

1.  Ouvrez la Palette de commandes dans VS Code : Appuyez sur `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (macOS).
2.  Tapez `remote` puis sélectionnez `Connect to Host...`
3.  Choisissez l'hôte (système distant) et confirmez.

La connexion se fait avec un nœud de connexion.

!!! warning "Sur un nœud de connexion..."
    ... ne faites pas de tests, ne faites aucun débogage et n'exécutez pas votre code.

### Fermeture de la connexion

1.  Ouvrez la Palette de commandes dans VS Code : Appuyez sur `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (macOS).
2.  Tapez `remote` puis sélectionnez `Remote-SSH: Kill VS Code Server on Host...`
3.  Choisissez l'hôte (système distant) et confirmez.
4.  Ouvrez le menu Fichier, et sélectionnez `Close Remote Connection`.

## Fonction avancée : Se connecter à un nœud de calcul interactif

Mettez à jour votre configuration en ajoutant les lignes suivantes :

=== "Narval"
    ```bash ~/.ssh/config
    Host nc* ng* nl*
      ProxyJump narval
      User votre_nom_utilisateur
    ```

=== "Rorqual"
    ```bash ~/.ssh/config
    Host rc* rg* rl*
      ProxyJump rorqual
      User votre_nom_utilisateur
    ```

1.  Dans un terminal externe, connecté au système via une connexion SSH, démarrez une nouvelle **[tâche interactive](../running-jobs/running_jobs.md)** (avec `salloc`) avec au moins 2000 Mo de mémoire.
    *   Notez le nom du nœud de calcul alloué.
    *   Si vous devez travailler avec des variables d'environnement `SLUR_*` dans VS Code, enregistrez-les toutes dans un fichier *source* :
        ```bash
        env | grep SLURM_ | sed -e 's/^\(.*\)=\(.*\)$/export \1="\2"/g' > slurm_var.sh
        ```
2.  Dans VS Code, démarrez une nouvelle session à distance avec le nom du nœud de calcul alloué.
    *   Appuyez sur `F1` ou `Ctrl+Shift+P` pour lancer l'invite de commande `>` dans la Palette de commandes.
    *   Commencez à taper *Remote* et sélectionnez *Remote-SSH: Connect to Host...* **> Remote-SSH: Connect to Host...**
    *   Entrez le nom du nœud de calcul noté.
    *   Si vous êtes invité à choisir le type de système d'exploitation, sélectionnez **Linux**.
3.  Si vous devez travailler avec des variables d'environnement `SLURM_*`, naviguez vers le répertoire de travail dans un terminal VS Code et *sourcez* le fichier `slurm_var.sh`.
    ```bash
    source slurm_var.sh
    ```

## Remarques importantes
*   VS Code ne peut pas être utilisé sur les nœuds de connexion de tamIA.
*   VS Code ne peut pas être utilisé sur les nœuds de connexion de Fir.