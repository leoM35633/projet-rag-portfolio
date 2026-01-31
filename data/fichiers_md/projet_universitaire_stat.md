# Projets universitaires — Statistique

---

## Présentation

Voici quelques projets réalisés dans le cadre de mon parcours en BUT Science des Données. Ils portent principalement sur des études statistiques, de la data cleaning à la modélisation et à la visualisation.

---

## BUT Science des Données — 1ère année

### Sae : Analyse de Données, Reporting et Data Visualisation — Observatoire MAVIE

- Contexte : l'observatoire MAVIE (Niort) envoie tous les 2 mois un questionnaire à une cohorte d'individus pour recenser les accidents de la vie courante. On a reçu une base Excel contenant deux tables : individus et accidents.
- Objectif : étudier les accidents de la vie courante à partir de la base fournie et produire un outil dynamique + visualisations.

#### Travail réalisé
- Nettoyage et préparation des données (consolidation des deux feuilles, gestion des valeurs manquantes).
- Analyse descriptive des types d'accidents, fréquences par tranche d'âge, localisation et contexte.
- Conception d'un outil simple pour explorer les données et création de visualisations interactives.

#### Outils
- `R` pour le nettoyage et analyses statistiques
- `Python` (Tkinter, `matplotlib`) pour un prototype d'interface et certaines visualisations
- `Power BI` pour la data visualisation interactive (dashboard)

---

### Sae : Régression sur des données réelles — Valeur foncière des logements parisiens

- Contexte : fichier CSV (>1000 logements) avec caractéristiques (arrondissement, surface, nombre de pièces, type logement...).
- Objectif : prédire la valeur foncière et sélectionner le modèle le plus adapté (puissance, linéaire, logarithmique).

#### Travail réalisé
- Pré-traitement et nettoyage des données (Excel + R).
- Analyse des corrélations et sélection des variables explicatives.
- Construction et comparaison de modèles (puissance, linéaire, logarithmique).
- Prédictions sur un jeu de test et validation des performances.

#### Outils
- `Excel` pour exploration et nettoyage initial
- `R` pour modélisation statistique et prédiction

---

### Estimation par échantillonnage

- Contexte : deux parties — estimation de la population de la Bretagne et étude de liens entre caractéristiques de véhicules et montant de la prime d'assurance.

#### Travail réalisé
- Partie 1 : tirage d'échantillons (aléatoires simples puis stratifiés) de 50 communes à partir d'un CSV ; estimation de la population bretonne et construction d'un intervalle de confiance (IC).
- Partie 2 : tests d'indépendance (khi-deux) sur variables catégorielles liées au montant de la prime, calcul du V de Cramer pour mesurer l'intensité des liaisons.

#### Outils
- `R` (sampling, tests d'hypothèse, calcul d'IC, V de Cramer)

---

### Synthèse d'un tableau de données — Étude des logements étudiants (IUT Niort)

- Contexte : enquête sur les logements des étudiants du site de Niort, saisie dans le logiciel Sphyxe.
- Objectif : étude descriptive pour mieux comprendre loyers, distance au campus et comportements de recherche.

#### Travail réalisé
- Création de tableaux et graphiques descriptifs depuis Sphyxe.
- Analyse des loyers et comportements : par exemple, corrélation entre loyers attractifs (< 400 €) et priorités de recherche.

#### Outils
- `Sphyxe` (saisie et analyses descriptives)

---

## BUT Science des Données — 2ème année

### Reporting d'une analyse multivariée — Pauvreté par département

- Contexte : base de données départementale contenant indicateurs socio-économiques.
- Objectif : identifier facteurs liés à la pauvreté, comparer départements, produire un tableau de bord interactif.

#### Travail réalisé
- Nettoyage et préparation des données.
- Construction d'un tableau de bord interactif avec `RShiny` pour explorer les départements.
- Analyses multivariées : ACP (analyse en composantes principales) et clustering (K-Means) pour repérer groupes de départements similaires.
- Comparaison des 5 départements les plus riches et des 5 les plus pauvres.

#### Outils
- `R`, `RShiny`, packages d'ACP et de clustering

#### Lien
- [Tableau de bord RShiny — placeholder](#)  <!-- Remplacer # par le lien réel -->

---

### Série temporelle — Données de lignes de bus

- Contexte : jeu de données sur les lignes de bus d'une ville — études de ponctualité et fréquentation.
- Objectif : créer des KPI, visualiser la fréquentation horaire et tester des modèles de prévision.

#### Travail réalisé
- Nettoyage et agrégation temporelle des données.
- Calcul de KPI (ponctualité, variation horaire, fréquentation moyenne).
- Tests de modèles de régression ; le modèle logarithmique a présenté le meilleur R² (~43,5 %).
- Ajout d'effets saisonniers pour estimer les tendances : prévision d'une légère hausse (~+4 %) à court terme (2025) selon le modèle.

#### Outils
- `Excel` pour traitement et analyse exploratoire

---

## Notes et suites possibles

- Si vous voulez, j'ajoute des liens GitHub, notebooks Jupyter/R ou rapports PDF pour chaque projet.
- Je peux aussi insérer des identifiants de chunking (ex. `<!-- chunk: id -->`) si vous comptez utiliser un pipeline d'ingestion automatique.

