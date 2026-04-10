---
title: "Visual Studio Code/fr"
tags:
  []

keywords:
  []
---

<b>TRADUCTION EN COURS</B> <BR>[Visual Studio Code](https://code.visualstudio.com/) est un environnement de développement local intégré (IDE) personnalisable de [Microsoft](https://www.microsoft.com) qui offre plusieurs extensions.

* Utilisez VS Code en mode local et évitez de le connecter aux systèmes. Enregistrez vos modifications dans les fichiers de /project avec Git, puis appliquez-les sur les systèmes pour faire les tests.
* Utilisez nano ou vim pour modifier les fichiers directement sur les systèmes.
* Pour le débogage et les tests rapides, vous pouvez charger le module <tt>code-server</tt>.
* Si aucune de ces solutions n'est possible, vous pouvez configurer VS Code pour les connexions à distance.

__FORCETOC__

=Utiliser VS Code localement=

Les avantages sont les suivants :

* vitesse et stabilité : l'exécution locale de VS Code réduit les interruptions réseau et améliore la performance, ce qui est idéal pour le développement itératif;
* accès direct : vous pouvez interagir avec les fichiers, les extensions et le terminal directement sur votre ordinateur, sans latence;
* possibilité de travailler hors ligne : aucune contrainte de connexion Internet ou de serveur distant, ce qui vous permet de coder n'importe où et n'importe quand.

Il est recommandé de développer localement avec VS Code. Vous pouvez ainsi personnaliser et ajouoter vos extensions et langages préférés avec VS Code.

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
git pull
```

<div lang="en" dir="ltr" class="mw-content-ltr">
Then test your changes in a short [interactive job](running_jobs#interactive_jobs.md) using minimal resources.
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">
= Editing files on the systems=
While VS Code is great for local development, sometimes you need direct access to files on a remote system. In such cases, terminal-based editors like <tt>nano</tt> or <tt>vim</tt> offer a lightweight and efficient way to edit files directly from the command line.
</div>

Si vous préférez une interface graphique, l'éditeur de texte [JupyterLab](jupyterlab-fr.md) est une option commode; les scripts au formats Markdown, Python et autres sont pris en charge.

<div lang="en" dir="ltr" class="mw-content-ltr">
= Debugging and testing =
If you need to debug or test your code on the systems, you can start a [<tt>code-server</tt> instance from Jupyter Lab](jupyterlab#vs_code.md).
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">
# Access one of the [options to launch JupyterLab](jupyterlab#launching_jupyterlab.md).
# Select minimal resources and start an interactive JupyterLab job.
# On the Launcher tab, click on the VS Code launcher button.
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">

The <tt>code-server</tt> module has several common extensions already available, but we can add more upon request.
</div>

## Installation personnalisée des extensions 
[en préparation ]

<div lang="en" dir="ltr" class="mw-content-ltr">
= Configuration of VS Code for remote connection =
If none of the above works for your case, one can configure VS Code to connect to a remote host with the Remote SSH extension.
</div>

<div lang="en" dir="ltr" class="mw-content-ltr">
## SSH configuration 
If not done already, [generate your SSH key](ssh_keys#generating_an_ssh_key.md) and [add your <i>public</i> SSH key on the CCDB](ssh_keys#installing_your_key.md).
</div>

Ensuite, créez ou ajoutez un fichier de configuration SSH sur votre ordinateur local.

**`~/.ssh/config`**
```text
Host *
  ServerAliveInterval 30
  User your_username

Host rorqual narval nibi fir
  HostName %h.alliancecan.ca
```

## Configuration locale 
1. Dans VS Code, ouvrez la palette <i>Command Palette</i> et appuyez <b>Ctrl+Shift+P</b> (Windows/Linux) ou <b>Cmd+Shift+P</b> (macOS).

2. Dans les paramètres d'utilisation, sélectionnez (<b>Preferences: Open User Settings (JSON)</b>) et collez ou intégrez la configuration suivante&nbsp;:
{{File
  |name=local-settings.json
  |contents=
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
}}

3. Enregistrez et relancez VS Code.

<div lang="en" dir="ltr" class="mw-content-ltr">
## Remote configuration 
1. Log in to the system via an external terminal.

```bash
ssh <username>@<host>.alliancecan.ca
```

</div>

2. Créez le répertoire.

```bash
mkdir -p ~/.vscode-server/data/Machine/
```

3. Créez la configuration <tt>settings.json</tt>.

```bash
nano ~/.vscode-server/data/Machine/settings.json
```

4. Copiez la configuration ci-dessous. Vous pourriez avoir besoin de fusionner manuellement les paramètres avec les vôtres, s'il y a lieu.
{{File
  |name=system-settings.json
  |contents=
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
}}

<div lang="en" dir="ltr" class="mw-content-ltr">
## Connecting 
# Open the Command Palette in VS Code: Press <tt>Ctrl+Shift+P</tt> (Windows/Linux) or <tt>Cmd+Shift+P</tt> (macOS).
# Type <tt>remote</tt> and then select <tt>Connect to Host...</tt>
# Choose the host (remote system) and confirm.
</div>

La connexion se fait avec un nœud de connexion.

<div lang="en" dir="ltr" class="mw-content-ltr">
## Closing your connection 
# Open the Command Palette in VS Code: Press <tt>Ctrl+Shift+P</tt> (Windows/Linux) or <tt>Cmd+Shift+P</tt> (macOS).
# Type <tt>remote</tt> and then select <tt>Remote-SSH: Kill VS Code Server on Host...</tt>
# Choose the host (remote system) and confirm.
# Open the File menu, and select <tt>Close Remote Connection</tt>.
</div>

## Fonction avancée : Se connecter à un nœud de calcul interactif 

Mettez à jour votre configuration en ajoutant les lignes suivantes&nbsp;:
<tabs>
<tab name="Narval">

**`~/.ssh/config`**
```text
Host nc* ng* nl*
  ProxyJump narval
  User your_username
```

</tab>
<tab name="Rorqual">

**`~/.ssh/config`**
```text
Host rc* rg* rl*
  ProxyJump rorqual
  User your_username
```

</tab>
</tabs>

<div lang="en" dir="ltr" class="mw-content-ltr">
# In an external terminal, connected to the system via an ssh connection, start a new <b>[interactive job](running_jobs#interactive_jobs.md)</b> (with `salloc`) with at least 2000M of memory.
## Note the allocated compute node name.
## If you need to work with `SLURM_*` environment variables in VS Code, save them all in a *source* file: 
```bash

```
 grep SLURM_  sed -e 's/^\(.*\)\(.*\)$/export \1"\2"/g' > slurm_var.sh}}
# In VS Code, start a new remote session with the name of the allocated compute node.
## Press `F1` or `Ctrl+Shift+P` to start the command prompt `&gt;` in the Command Palette.
## Start typing <i>Remote</i> and select <i>Remote-SSH: Connect to Host... <b>&gt; Remote-SSH: Connect to Host...</i></b>
## Enter the noted compute node name.
### If you get prompted for the type of operating system, select <b>Linux</b>.
# If you need to work with `SLURM_*` environment variables, navigate to the working directory in a VS Code terminal and *source* the `slurm_var.sh` file. 
```bash
source slurm_var.sh
```

</div>

<div class="mw-translate-fuzzy">
= Remarques importantes = 
* VS Code ne peut pas être utilisé sur les nœuds de connexion de tamIA.
</div>