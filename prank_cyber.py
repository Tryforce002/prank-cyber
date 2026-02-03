# -*- coding: utf-8 -*-
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>System</title>
<style>
body {
    margin: 0;
    background: black;
    color: lime;
    font-family: Consolas, monospace;
    font-size: 16px;
}
#terminal {
    padding: 20px;
    white-space: pre-line;
}
#bar-container {
    width: 90%;
    height: 20px;
    border: 1px solid lime;
    margin: 20px;
}
#bar {
    height: 100%;
    width: 0%;
    background: lime;
}
.final {
    color: white;
}
</style>
</head>

<body>
<div id="terminal">Initialisation...</div>
<div id="bar-container"><div id="bar"></div></div>

<script>
const terminal = document.getElementById("terminal");
const bar = document.getElementById("bar");
const barContainer = document.getElementById("bar-container");

const lines = [
    "Connexion au périphérique USB...",
    "Lecture du fichier : Exercice math.jpg",
    "Élévation des privilèges...",
    "Analyse mémoire...",
    "Collecte des données utilisateur...",
    "Compression des fichiers...",
    "Préparation du transfert...",
    "Connexion au serveur distant..."
];

function addLine(text) {
    terminal.textContent += "\n" + text;
    window.scrollTo(0, document.body.scrollHeight);
}

setTimeout(() => {
    let i = 0;
    const interval = setInterval(() => {
        addLine(lines[Math.floor(Math.random() * lines.length)]);
        i++;
        if (i > 20) {
            clearInterval(interval);
            startProgress();
        }
    }, 150);
}, 2000);

function startProgress() {
    let p = 0;
    const progress = setInterval(() => {
        p++;
        bar.style.width = p + "%";
        addLine("Extraction des données... " + p + "%");
        if (p >= 100) {
            clearInterval(progress);
            showFinal();
        }
    }, 50);
}

function showFinal() {
    terminal.textContent = "";
    barContainer.style.display = "none";
    terminal.classList.add("final");
    terminal.textContent =
`⚠️ DEMONSTRATION DE CYBERSECURITE ⚠️

Vous venez d’ouvrir le fichier : Exercice math.jpg

Dans un scénario réel, cette action aurait pu permettre :
- Exécution de code malveillant
- Vol de mots de passe
- Accès distant à l'ordinateur
- Propagation sur le réseau

Aucun dommage n’a été causé.

Le problème n’est pas le fichier.
Le problème est d’avoir branché la clé USB.

La faille, ce n’est pas le système.
La faille, c’est toi.`;
}

// Plein écran automatique
document.documentElement.requestFullscreen?.();
</script>
</body>
</html>
