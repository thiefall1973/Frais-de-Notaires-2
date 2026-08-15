# Frais-de-Notaires-2

## Projet
Calculateur de frais notariaux immobiliers pour le Sénégal, développé pour
investissementimmoafrique.com. Le repo est un unique fichier `README.md`
contenant tout le widget (HTML + CSS + JS inline), destiné à être intégré
dans WordPress/Elementor (widget HTML, shortcode, ou plugin custom).

## Points techniques clés
- Formulaire de capture de leads envoyé via Formspree (ID: xwpbpyyj)
- Conversion EUR/FCFA en dur (FCFA_PER_EUR = 655.957)
- Barème émoluments notaire à 3 paliers selon le montant en FCFA (4.5% / 3% / 1.5%)
- Droits d'enregistrement 5%, publicité foncière 1%, timbre 6000 FCFA fixe,
  frais de dossier 200000 FCFA fixe
- Compatible IE11+, mobile-first, sans dépendance externe (vanilla JS)
- Sauvegarde localStorage de secours du dernier calcul

## Convention de travail
- Répondre en français
- Branches de travail nommées `claude/<sujet>-<id>`
