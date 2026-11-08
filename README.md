# Fonte & Fourneaux

Application web de musculation et de nutrition, en un seul fichier (`index.html`).

## Onglets

- **Programme** : programmes en 3, 4 ou 5 jours, séance à saisir série par série (kg, reps, valeurs précédentes), minuteur de repos, bibliothèque de 95 exercices avec muscles travaillés, fiche et historique.
- **Recettes** : menu de saison planifié par repas et par jour, batch cooking (nombre de plats et de portions, conservation), portions calculées selon la cible de calories et de protéines.
- **Courses** : liste agrégée par rayon, à cocher, avec suppression et restauration, et assistant IA pour modifier le menu.
- **Suivi** : séances enregistrées automatiquement, objectif hebdomadaire, présence sur 12 semaines, progression par exercice (1RM estimé), poids de corps, séances modifiables.

## Installer sur un téléphone (hors ligne)

Ouvre https://maarbis-web.github.io/fonte-fourneaux/ dans Chrome, puis menu ⋮ → « Installer l'application » (ou bouton « Installer l'application » dans « Mes infos »).
L'appli s'ouvre en plein écran avec son icône et fonctionne sans réseau.

Dans cette version, toutes les données restent sur le téléphone (rien n'est envoyé en ligne). Pense à utiliser « Exporter mes données » dans « Mes infos » pour en garder une copie.
L'assistant IA et la synchronisation entre appareils n'existent que dans la version claude.ai.

## Fichiers

- `app-claude.html` : la source, publiée telle quelle sur claude.ai (sauvegarde dans le compte Claude, assistant IA, images).
- `index.html` : version installable hors ligne, générée par `python3 build.py` à partir de `app-claude.html`.
- `manifest.webmanifest`, `sw.js`, `icon-*.png` : installation et fonctionnement hors ligne.
