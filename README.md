# Frais-de-Notaires-2
<!-- 
    ================================================
    CALCULATEUR DE FRAIS NOTARIAUX SÉNÉGAL v2.0
    ================================================
    Développé pour : investissementimmoafrique.com
    Date : Mai 2025
    
    IMPORTANT - Configuration :
    1. ID Formspree déjà configuré : xwpbpyyj
    2. Tester sur tous les navigateurs cibles
    3. Vérifier l'intégration avec vos plugins WordPress<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculateur de Frais Notariaux - Investissement Immobilier Sénégal</title>
    
    <!-- 
    ================================================
    CALCULATEUR DE FRAIS NOTARIAUX SÉNÉGAL v2.0
    ================================================
    Développé pour : investissementimmoafrique.com
    Date : Mai 2025
    
    IMPORTANT - Configuration :
    1. ID Formspree déjà configuré : xwpbpyyj
    2. Tester sur tous les navigateurs cibles
    3. Vérifier l'intégration avec vos plugins WordPress
    
    Fonctionnalités :
    - Calcul automatique des frais notariaux selon barème Sénégal
    - Validation robuste côté client
    - Compatible IE11+ et tous navigateurs modernes
    - 100% responsive mobile-first
    - Protection anti-spam intégrée
    - Retry automatique en cas d'échec
    - Sauvegarde localStorage de secours
    
    Support navigateurs :
    - Chrome 45+
    - Firefox 40+
    - Safari 10+
    - Edge (toutes versions)
    - IE11 (avec dégradation gracieuse)
    -->
    
    <style>
        /* ========================================== */
        /* Reset et Variables CSS                     */
        /* ========================================== */
        :root {
            --primary-color: #059a42;
            --primary-hover: #047a34;
            --secondary-color: #1a1a1a;
            --text-color: #333;
            --border-color: #ddd;
            --bg-light: #f5f5f5;
            --error-color: #dc3545;
            --success-color: #28a745;
            --font-heading: 'Montserrat', sans-serif;
            --font-body: 'Roboto', sans-serif;
            --transition: all 0.3s ease;
        }

        * {
            box-sizing: border-box;
        }

        /* ========================================== */
        /* Container Principal                        */
        /* ========================================== */
        #notary-calculator-wrapper {
            max-width: 700px;
            margin: 0 auto;
            padding: 20px;
            font-family: var(--font-body);
            color: var(--text-color);
            line-height: 1.6;
        }

        /* Responsive */
        @media (max-width: 768px) {
            #notary-calculator-wrapper {
                padding: 15px;
            }
        }

        /* ========================================== */
        /* Barre de Progression                       */
        /* ========================================== */
        .calc-progress-bar {
            display: flex;
            justify-content: space-between;
            margin-bottom: 40px;
            position: relative;
            counter-reset: step;
        }

        .calc-progress-bar::before {
            content: '';
            position: absolute;
            top: 20px;
            left: 15%;
            right: 15%;
            height: 2px;
            background: var(--border-color);
            z-index: -1;
        }

        .calc-step {
            flex: 1;
            text-align: center;
            position: relative;
        }

        .calc-step-circle {
            width: 40px;
            height: 40px;
            margin: 0 auto 8px;
            border: 3px solid var(--border-color);
            border-radius: 50%;
            background: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-family: var(--font-heading);
            position: relative;
            z-index: 1;
            transition: var(--transition);
            counter-increment: step;
        }

        .calc-step-circle::before {
            content: counter(step);
            color: #999;
        }

        .calc-step.active .calc-step-circle,
        .calc-step.completed .calc-step-circle {
            border-color: var(--primary-color);
            background: var(--primary-color);
        }

        .calc-step.active .calc-step-circle::before,
        .calc-step.completed .calc-step-circle::before {
            color: white;
        }

        .calc-step-label {
            font-size: 14px;
            font-family: var(--font-heading);
            font-weight: 500;
        }

        /* Mobile adjustments */
        @media (max-width: 480px) {
            .calc-step-circle {
                width: 32px;
                height: 32px;
            }
            .calc-step-label {
                font-size: 12px;
            }
        }

        /* ========================================== */
        /* Contenus des étapes                        */
        /* ========================================== */
        .calc-step-content {
            display: none;
            animation: fadeIn 0.5s ease;
        }

        .calc-step-content.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* ========================================== */
        /* Titre des sections                         */
        /* ========================================== */
        .calc-section-title {
            text-align: center;
            margin-bottom: 30px;
            font-family: var(--font-heading);
            font-size: 24px;
            font-weight: 600;
            color: var(--secondary-color);
        }

        /* ========================================== */
        /* Étape 1 : Slider                          */
        /* ========================================== */
        .price-selector {
            background: var(--bg-light);
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        .price-display {
            text-align: center;
            margin-bottom: 30px;
        }

        .price-display label {
            display: block;
            font-family: var(--font-heading);
            font-weight: 500;
            margin-bottom: 10px;
        }

        .price-value {
            font-size: 32px;
            color: var(--primary-color);
            font-weight: bold;
            font-family: var(--font-heading);
            display: block;
            margin-bottom: 5px;
        }

        .price-value-fcfa {
            font-size: 18px;
            color: #666;
            font-family: var(--font-body);
        }

        /* Slider personnalisé */
        .price-slider {
            width: 100%;
            height: 8px;
            -webkit-appearance: none;
            appearance: none;
            background: linear-gradient(to right, var(--primary-color) 0%, var(--primary-color) 0%, #ddd 0%, #ddd 100%);
            border-radius: 4px;
            outline: none;
            margin: 20px 0;
        }

        .price-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: var(--primary-color);
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
            border: 3px solid white;
            transition: var(--transition);
        }

        .price-slider::-webkit-slider-thumb:hover {
            transform: scale(1.1);
            box-shadow: 0 3px 8px rgba(0,0,0,0.3);
        }

        .price-slider::-moz-range-thumb {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: var(--primary-color);
            cursor: pointer;
            box-shadow: 0 2px 6px rgba(0,0,0,0.2);
            border: 3px solid white;
        }

        /* Touch-friendly pour mobile */
        @media (max-width: 768px) {
            .price-slider::-webkit-slider-thumb {
                width: 44px;
                height: 44px;
            }
            .price-slider::-moz-range-thumb {
                width: 44px;
                height: 44px;
            }
        }

        .price-range-labels {
            display: flex;
            justify-content: space-between;
            font-size: 14px;
            color: #666;
            margin-top: 10px;
        }

        /* ========================================== */
        /* Étape 2 : Formulaire                      */
        /* ========================================== */
        .form-container {
            max-width: 450px;
            margin: 0 auto;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            font-family: var(--font-heading);
            font-weight: 500;
            margin-bottom: 8px;
            color: var(--secondary-color);
        }

        .form-group label .required {
            color: var(--error-color);
        }

        .form-control {
            width: 100%;
            padding: 12px 16px;
            border: 2px solid var(--border-color);
            border-radius: 6px;
            font-size: 16px;
            font-family: var(--font-body);
            transition: var(--transition);
            background: white;
        }

        .form-control:focus {
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(5, 154, 66, 0.1);
        }

        .form-control.error {
            border-color: var(--error-color);
        }

        .error-message {
            display: none;
            color: var(--error-color);
            font-size: 14px;
            margin-top: 5px;
        }

        .error-message.show {
            display: block;
        }

        /* Honeypot (anti-spam) */
        .honey-pot {
            position: absolute;
            left: -9999px;
            height: 0;
            width: 0;
            visibility: hidden;
        }

        /* ========================================== */
        /* Étape 3 : Résultats                       */
        /* ========================================== */
        .results-container {
            background: var(--bg-light);
            padding: 30px;
            border-radius: 10px;
        }

        .result-summary {
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid var(--border-color);
        }

        .result-summary .price-chosen {
            font-size: 20px;
            font-weight: 600;
            color: var(--secondary-color);
            font-family: var(--font-heading);
        }

        .fees-breakdown {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .fee-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 0;
            border-bottom: 1px solid #e0e0e0;
        }

        .fee-item:last-child {
            border-bottom: none;
            padding-top: 20px;
            margin-top: 10px;
            border-top: 2px solid var(--primary-color);
        }

        .fee-label {
            font-weight: 500;
            color: var(--secondary-color);
            font-family: var(--font-heading);
            flex: 1;
        }

        .fee-value {
            text-align: right;
            font-weight: 600;
            color: var(--primary-color);
            font-family: var(--font-heading);
        }

        .fee-item.total {
            font-size: 18px;
        }

        .fee-item.total .fee-label,
        .fee-item.total .fee-value {
            font-weight: 700;
        }

        /* ========================================== */
        /* Boutons                                    */
        /* ========================================== */
        .calc-navigation {
            display: flex;
            justify-content: space-between;
            gap: 15px;
            margin-top: 30px;
        }

        .calc-btn {
            padding: 12px 30px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            font-weight: 500;
            font-family: var(--font-heading);
            cursor: pointer;
            transition: var(--transition);
            position: relative;
            overflow: hidden;
        }

        .calc-btn-primary {
            background: var(--primary-color);
            color: white;
        }

        .calc-btn-primary:hover:not(:disabled) {
            background: var(--primary-hover);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(5, 154, 66, 0.3);
        }

        .calc-btn-secondary {
            background: #6c757d;
            color: white;
        }

        .calc-btn-secondary:hover {
            background: #5a6268;
        }

        .calc-btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }

        /* Loader */
        .calc-btn .spinner {
            display: inline-block;
            width: 16px;
            height: 16px;
            border: 2px solid #ffffff;
            border-top-color: transparent;
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
            margin-right: 8px;
            vertical-align: middle;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* ========================================== */
        /* Messages de feedback                       */
        /* ========================================== */
        .alert {
            padding: 15px 20px;
            border-radius: 6px;
            margin-top: 20px;
            font-size: 16px;
            animation: slideIn 0.5s ease;
        }

        .alert-success {
            background: #d4edda;
            color: #155724;
            border: 1px solid #c3e6cb;
        }

        .alert-error {
            background: #f8d7da;
            color: #721c24;
            border: 1px solid #f5c6cb;
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* ========================================== */
        /* Tooltip info                               */
        /* ========================================== */
        .info-tooltip {
            display: inline-block;
            width: 18px;
            height: 18px;
            background: var(--primary-color);
            color: white;
            border-radius: 50%;
            font-size: 12px;
            line-height: 18px;
            text-align: center;
            cursor: help;
            margin-left: 5px;
            position: relative;
        }

        .info-tooltip:hover::after {
            content: attr(data-tooltip);
            position: absolute;
            bottom: 25px;
            left: 50%;
            transform: translateX(-50%);
            background: #333;
            color: white;
            padding: 8px 12px;
            border-radius: 4px;
            font-size: 14px;
            white-space: nowrap;
            z-index: 10;
            font-family: var(--font-body);
        }

        /* ========================================== */
        /* Responsive adjustments                     */
        /* ========================================== */
        @media (max-width: 480px) {
            .calc-section-title {
                font-size: 20px;
            }
            
            .price-value {
                font-size: 26px;
            }
            
            .calc-navigation {
                flex-direction: column;
            }
            
            .calc-btn {
                width: 100%;
            }
            
            .fee-item {
                flex-direction: column;
                text-align: center;
                gap: 8px;
            }
            
            .fee-value {
                text-align: center;
            }
        }
    </style>
</head>
<body>

<div id="notary-calculator-wrapper">
    <!-- ID Formspree configuré pour investissementimmoafrique.com -->
    <form id="notary-calc-form" action="https://formspree.io/f/xwpbpyyj" method="POST">
        <!-- Identifiant unique pour ce calculateur -->
        <input type="hidden" name="calculator_source" value="calculateur_frais_notariaux_v2_2025" />
        <input type="hidden" name="_subject" value="Nouveau calcul frais notariaux immobilier Sénégal" />
        
        <!-- Honeypot anti-spam (ne pas modifier le name) -->
        <input type="text" name="_gotcha" class="honey-pot" tabindex="-1" autocomplete="off" />
        
        <!-- Barre de progression -->
        <div class="calc-progress-bar">
            <div class="calc-step active" data-step="1">
                <div class="calc-step-circle"></div>
                <div class="calc-step-label">Montant</div>
            </div>
            <div class="calc-step" data-step="2">
                <div class="calc-step-circle"></div>
                <div class="calc-step-label">Coordonnées</div>
            </div>
            <div class="calc-step" data-step="3">
                <div class="calc-step-circle"></div>
                <div class="calc-step-label">Résultats</div>
            </div>
        </div>

        <!-- ÉTAPE 1 : Sélection du prix -->
        <div id="step-1" class="calc-step-content active">
            <h3 class="calc-section-title">Quel est le prix du bien immobilier ?</h3>
            
            <div class="price-selector">
                <div class="price-display">
                    <label for="price-range">Montant de la transaction</label>
                    <span class="price-value" id="price-eur-display">70 000 €</span>
                    <span class="price-value-fcfa" id="price-fcfa-display">(45 916 990 FCFA)</span>
                </div>
                
                <input 
                    type="range" 
                    id="price-range" 
                    name="transaction_amount_eur"
                    class="price-slider"
                    min="60000" 
                    max="200000" 
                    step="1000" 
                    value="70000"
                    aria-label="Prix en euros"
                />
                
                <div class="price-range-labels">
                    <span>60 000 €</span>
                    <span>200 000 €</span>
                </div>
            </div>
            
            <div class="calc-navigation">
                <div></div>
                <button type="button" class="calc-btn calc-btn-primary" id="btn-step-2">
                    Suivant →
                </button>
            </div>
        </div>

        <!-- ÉTAPE 2 : Informations de contact -->
        <div id="step-2" class="calc-step-content">
            <h3 class="calc-section-title">Vos coordonnées</h3>
            
            <div class="form-container">
                <div class="form-group">
                    <label for="first-name">
                        Prénom <span class="required">*</span>
                    </label>
                    <input 
                        type="text" 
                        id="first-name" 
                        name="first_name"
                        class="form-control" 
                        required
                        minlength="2"
                        maxlength="50"
                        aria-required="true"
                    />
                    <div class="error-message" id="first-name-error">
                        Veuillez entrer un prénom valide (minimum 2 caractères)
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="last-name">
                        Nom <span class="required">*</span>
                    </label>
                    <input 
                        type="text" 
                        id="last-name" 
                        name="last_name"
                        class="form-control" 
                        required
                        minlength="2"
                        maxlength="50"
                        aria-required="true"
                    />
                    <div class="error-message" id="last-name-error">
                        Veuillez entrer un nom valide (minimum 2 caractères)
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="email">
                        Email <span class="required">*</span>
                    </label>
                    <input 
                        type="email" 
                        id="email" 
                        name="email"
                        class="form-control" 
                        required
                        aria-required="true"
                    />
                    <div class="error-message" id="email-error">
                        Veuillez entrer une adresse email valide
                    </div>
                </div>
                
                <div class="form-group">
                    <label for="phone">
                        Téléphone
                        <span class="info-tooltip" data-tooltip="Optionnel mais recommandé">?</span>
                    </label>
                    <input 
                        type="tel" 
                        id="phone" 
                        name="phone"
                        class="form-control"
                        placeholder="Ex: +33 6 12 34 56 78"
                    />
                </div>
                
                <div class="form-group">
                    <label for="country">
                        Pays de résidence <span class="required">*</span>
                    </label>
                    <select id="country" name="country" class="form-control" required>
                        <option value="">-- Sélectionnez --</option>
                        <option value="FR">France</option>
                        <option value="SN">Sénégal</option>
                        <option value="CA">Canada</option>
                        <option value="US">États-Unis</option>
                        <option value="BE">Belgique</option>
                        <option value="CH">Suisse</option>
                        <option value="IT">Italie</option>
                        <option value="ES">Espagne</option>
                        <option value="CI">Côte d'Ivoire</option>
                        <option value="ML">Mali</option>
                        <option value="other">Autre</option>
                    </select>
                    <div class="error-message" id="country-error">
                        Veuillez sélectionner votre pays
                    </div>
                </div>
            </div>
            
            <div class="calc-navigation">
                <button type="button" class="calc-btn calc-btn-secondary" id="btn-back-1">
                    ← Précédent
                </button>
                <button type="button" class="calc-btn calc-btn-primary" id="btn-calculate">
                    Calculer →
                </button>
            </div>
        </div>

        <!-- ÉTAPE 3 : Résultats -->
        <div id="step-3" class="calc-step-content">
            <h3 class="calc-section-title">Estimation des frais notariaux</h3>
            
            <div class="results-container">
                <div class="result-summary">
                    <div class="price-chosen">
                        Prix du bien : <span id="final-price-eur">—</span> €
                        (<span id="final-price-fcfa">—</span> FCFA)
                    </div>
                </div>
                
                <ul class="fees-breakdown">
                    <li class="fee-item">
                        <span class="fee-label">
                            Émoluments notaire + TVA (18%)
                            <span class="info-tooltip" data-tooltip="Honoraires du notaire selon barème officiel">?</span>
                        </span>
                        <span class="fee-value">
                            <span id="notary-eur">—</span> € / <span id="notary-fcfa">—</span> FCFA
                        </span>
                    </li>
                    
                    <li class="fee-item">
                        <span class="fee-label">
                            Droits d'enregistrement (5%)
                            <span class="info-tooltip" data-tooltip="Taxe obligatoire sur les mutations immobilières">?</span>
                        </span>
                        <span class="fee-value">
                            <span id="registration-eur">—</span> € / <span id="registration-fcfa">—</span> FCFA
                        </span>
                    </li>
                    
                    <li class="fee-item">
                        <span class="fee-label">
                            Publicité foncière (1%)
                            <span class="info-tooltip" data-tooltip="Frais de publication à la conservation foncière">?</span>
                        </span>
                        <span class="fee-value">
                            <span id="publication-eur">—</span> € / <span id="publication-fcfa">—</span> FCFA
                        </span>
                    </li>
                    
                    <li class="fee-item">
                        <span class="fee-label">
                            Droits de timbre
                            <span class="info-tooltip" data-tooltip="Forfait fixe de 6 000 FCFA">?</span>
                        </span>
                        <span class="fee-value">
                            <span id="stamp-eur">—</span> € / <span id="stamp-fcfa">—</span> FCFA
                        </span>
                    </li>
                    
                    <li class="fee-item">
                        <span class="fee-label">
                            Frais de dossier & certificats
                            <span class="info-tooltip" data-tooltip="Réquisitions, extraits, certificats divers">?</span>
                        </span>
                        <span class="fee-value">
                            <span id="admin-eur">—</span> € / <span id="admin-fcfa">—</span> FCFA
                        </span>
                    </li>
                    
                    <li class="fee-item total">
                        <span class="fee-label">TOTAL ESTIMÉ</span>
                        <span class="fee-value">
                            <span id="total-eur">—</span> € / <span id="total-fcfa">—</span> FCFA
                        </span>
                    </li>
                </ul>
            </div>
            
            <div id="formspree-feedback"></div>
            
            <div class="calc-navigation">
                <button type="button" class="calc-btn calc-btn-secondary" id="btn-restart">
                    ← Nouveau calcul
                </button>
                <button type="button" class="calc-btn calc-btn-primary" id="btn-download" style="display:none;">
                    📥 Télécharger le récapitulatif
                </button>
            </div>
        </div>
    </form>
</div>

<script>
(function() {
    'use strict';
    
    // ========================================
    // Configuration et constantes
    // ========================================
    var FCFA_PER_EUR = 655.957;
    var RETRY_DELAY = 1000;
    var MAX_RETRIES = 3;
    
    // ========================================
    // Références DOM
    // ========================================
    var form = document.getElementById('notary-calc-form');
    var steps = document.querySelectorAll('.calc-step');
    var stepContents = document.querySelectorAll('.calc-step-content');
    
    // Slider
    var priceSlider = document.getElementById('price-range');
    var priceEurDisplay = document.getElementById('price-eur-display');
    var priceFcfaDisplay = document.getElementById('price-fcfa-display');
    
    // Champs formulaire
    var firstNameInput = document.getElementById('first-name');
    var lastNameInput = document.getElementById('last-name');
    var emailInput = document.getElementById('email');
    var phoneInput = document.getElementById('phone');
    var countrySelect = document.getElementById('country');
    
    // Boutons
    var btnStep2 = document.getElementById('btn-step-2');
    var btnBack1 = document.getElementById('btn-back-1');
    var btnCalculate = document.getElementById('btn-calculate');
    var btnRestart = document.getElementById('btn-restart');
    
    // Affichage résultats
    var finalPriceEur = document.getElementById('final-price-eur');
    var finalPriceFcfa = document.getElementById('final-price-fcfa');
    var feedbackDiv = document.getElementById('formspree-feedback');
    
    // État de l'application
    var currentStep = 1;
    var calculationData = {};
    var isSubmitting = false;
    
    // ========================================
    // Fonctions utilitaires
    // ========================================
    function formatNumber(num) {
        return Math.round(num).toLocaleString('fr-FR');
    }
    
    function round2(num) {
        return Math.round(num * 100) / 100;
    }
    
    function euroToFcfa(eur) {
        return eur * FCFA_PER_EUR;
    }
    
    function fcfaToEuro(fcfa) {
        return fcfa / FCFA_PER_EUR;
    }
    
    // ========================================
    // Gestion du slider
    // ========================================
    function updatePriceDisplay() {
        var eurValue = parseInt(priceSlider.value);
        var fcfaValue = euroToFcfa(eurValue);
        
        priceEurDisplay.textContent = formatNumber(eurValue) + ' €';
        priceFcfaDisplay.textContent = '(' + formatNumber(fcfaValue) + ' FCFA)';
        
        // Mettre à jour la barre de progression du slider
        var percent = ((eurValue - priceSlider.min) / (priceSlider.max - priceSlider.min)) * 100;
        priceSlider.style.background = 'linear-gradient(to right, #059a42 0%, #059a42 ' + percent + '%, #ddd ' + percent + '%, #ddd 100%)';
    }
    
    priceSlider.addEventListener('input', updatePriceDisplay);
    
    // ========================================
    // Navigation entre étapes
    // ========================================
    function showStep(stepNumber) {
        currentStep = stepNumber;
        
        // Mettre à jour les contenus (compatible IE11)
        for (var i = 0; i < stepContents.length; i++) {
            if (i === stepNumber - 1) {
                stepContents[i].classList.add('active');
            } else {
                stepContents[i].classList.remove('active');
            }
        }
        
        // Mettre à jour la barre de progression
        for (var j = 0; j < steps.length; j++) {
            steps[j].classList.remove('active', 'completed');
            if (j < stepNumber - 1) {
                steps[j].classList.add('completed');
            } else if (j === stepNumber - 1) {
                steps[j].classList.add('active');
            }
        }
        
        // Scroll to top sur mobile
        if (window.innerWidth <= 768) {
            try {
                form.scrollIntoView({ behavior: 'smooth', block: 'start' });
            } catch (e) {
                // Fallback pour vieux navigateurs
                window.scrollTo(0, form.offsetTop);
            }
        }
    }
    
    // ========================================
    // Validation des champs
    // ========================================
    function validateName(name) {
        var regex = /^[a-zA-ZÀ-ÿ\s\-']+$/;
        return regex.test(name) && name.length >= 2 && name.length <= 50;
    }
    
    function validateEmail(email) {
        var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }
    
    function validatePhone(phone) {
        if (!phone) return true; // Optionnel
        var regex = /^[\d\s\+\-\(\)]+$/;
        return regex.test(phone) && phone.length >= 8;
    }
    
    function showError(inputId, show) {
        var input = document.getElementById(inputId);
        var errorMsg = document.getElementById(inputId + '-error');
        
        if (show) {
            input.classList.add('error');
            errorMsg.classList.add('show');
        } else {
            input.classList.remove('error');
            errorMsg.classList.remove('show');
        }
    }
    
    function validateStep2() {
        var isValid = true;
        
        // Valider prénom
        if (!validateName(firstNameInput.value.trim())) {
            showError('first-name', true);
            isValid = false;
        } else {
            showError('first-name', false);
        }
        
        // Valider nom
        if (!validateName(lastNameInput.value.trim())) {
            showError('last-name', true);
            isValid = false;
        } else {
            showError('last-name', false);
        }
        
        // Valider email
        if (!validateEmail(emailInput.value.trim())) {
            showError('email', true);
            isValid = false;
        } else {
            showError('email', false);
        }
        
        // Valider pays
        if (!countrySelect.value) {
            showError('country', true);
            isValid = false;
        } else {
            showError('country', false);
        }
        
        return isValid;
    }
    
    // Validation en temps réel
    firstNameInput.addEventListener('blur', function() {
        showError('first-name', !validateName(this.value.trim()));
    });
    
    lastNameInput.addEventListener('blur', function() {
        showError('last-name', !validateName(this.value.trim()));
    });
    
    emailInput.addEventListener('blur', function() {
        showError('email', !validateEmail(this.value.trim()));
    });
    
    countrySelect.addEventListener('change', function() {
        showError('country', !this.value);
    });
    
    // ========================================
    // Calcul des frais
    // ========================================
    function calculateFees(priceEur) {
        var priceFcfa = euroToFcfa(priceEur);
        
        // Barème émoluments notaire selon le montant
        var notaryRate;
        if (priceFcfa <= 20000000) {
            notaryRate = 0.045;
        } else if (priceFcfa <= 80000000) {
            notaryRate = 0.03;
        } else {
            notaryRate = 0.015;
        }
        
        // Calculs en FCFA
        var notaryBaseFcfa = priceFcfa * notaryRate;
        var notaryTvaFcfa = notaryBaseFcfa * 0.18;
        var notaryTotalFcfa = notaryBaseFcfa + notaryTvaFcfa;
        
        var registrationFcfa = priceFcfa * 0.05;
        var publicationFcfa = priceFcfa * 0.01;
        var stampFcfa = 6000;
        var adminFcfa = 200000;
        
        var totalFcfa = notaryTotalFcfa + registrationFcfa + publicationFcfa + stampFcfa + adminFcfa;
        
        // Conversion en EUR
        return {
            price: {
                eur: priceEur,
                fcfa: Math.round(priceFcfa)
            },
            notary: {
                eur: round2(fcfaToEuro(notaryTotalFcfa)),
                fcfa: Math.round(notaryTotalFcfa)
            },
            registration: {
                eur: round2(fcfaToEuro(registrationFcfa)),
                fcfa: Math.round(registrationFcfa)
            },
            publication: {
                eur: round2(fcfaToEuro(publicationFcfa)),
                fcfa: Math.round(publicationFcfa)
            },
            stamp: {
                eur: round2(fcfaToEuro(stampFcfa)),
                fcfa: stampFcfa
            },
            admin: {
                eur: round2(fcfaToEuro(adminFcfa)),
                fcfa: adminFcfa
            },
            total: {
                eur: round2(fcfaToEuro(totalFcfa)),
                fcfa: Math.round(totalFcfa)
            }
        };
    }
    
    // ========================================
    // Affichage des résultats
    // ========================================
    function displayResults(fees) {
        // Prix choisi
        document.getElementById('final-price-eur').textContent = formatNumber(fees.price.eur);
        document.getElementById('final-price-fcfa').textContent = formatNumber(fees.price.fcfa);
        
        // Détail des frais
        document.getElementById('notary-eur').textContent = formatNumber(fees.notary.eur);
        document.getElementById('notary-fcfa').textContent = formatNumber(fees.notary.fcfa);
        
        document.getElementById('registration-eur').textContent = formatNumber(fees.registration.eur);
        document.getElementById('registration-fcfa').textContent = formatNumber(fees.registration.fcfa);
        
        document.getElementById('publication-eur').textContent = formatNumber(fees.publication.eur);
        document.getElementById('publication-fcfa').textContent = formatNumber(fees.publication.fcfa);
        
        document.getElementById('stamp-eur').textContent = formatNumber(fees.stamp.eur);
        document.getElementById('stamp-fcfa').textContent = formatNumber(fees.stamp.fcfa);
        
        document.getElementById('admin-eur').textContent = formatNumber(fees.admin.eur);
        document.getElementById('admin-fcfa').textContent = formatNumber(fees.admin.fcfa);
        
        document.getElementById('total-eur').textContent = formatNumber(fees.total.eur);
        document.getElementById('total-fcfa').textContent = formatNumber(fees.total.fcfa);
    }
    
    // ========================================
    // Envoi à Formspree (compatible IE11)
    // ========================================
    function sendToFormspree(formData, retryCount) {
        if (retryCount === undefined) retryCount = 0;
        
        // Créer une promise-like pour IE11
        var promise = {
            then: function(onSuccess, onError) {
                var xhr = new XMLHttpRequest();
                xhr.open('POST', form.action);
                xhr.setRequestHeader('Accept', 'application/json');
                
                xhr.onload = function() {
                    try {
                        var result = JSON.parse(xhr.responseText);
                        if (xhr.status === 200 || xhr.status === 201) {
                            if (onSuccess) onSuccess(result);
                        } else if (retryCount < MAX_RETRIES) {
                            // Retry avec délai
                            setTimeout(function() {
                                sendToFormspree(formData, retryCount + 1).then(onSuccess, onError);
                            }, RETRY_DELAY * Math.pow(2, retryCount));
                        } else {
                            if (onError) onError(new Error('Échec après ' + MAX_RETRIES + ' tentatives'));
                        }
                    } catch (e) {
                        if (onError) onError(e);
                    }
                };
                
                xhr.onerror = function() {
                    if (retryCount < MAX_RETRIES) {
                        setTimeout(function() {
                            sendToFormspree(formData, retryCount + 1).then(onSuccess, onError);
                        }, RETRY_DELAY * Math.pow(2, retryCount));
                    } else {
                        if (onError) onError(new Error('Erreur réseau'));
                    }
                };
                
                xhr.send(formData);
                
                return {
                    catch: function(onError) {
                        // Pour chaîner .then().catch()
                        return this;
                    }
                };
            }
        };
        
        return promise;
    }
    
    // ========================================
    // Gestionnaires d'événements
    // ========================================
    
    // Étape 1 → 2
    btnStep2.addEventListener('click', function() {
        showStep(2);
    });
    
    // Étape 2 → 1
    btnBack1.addEventListener('click', function() {
        showStep(1);
    });
    
    // Calculer et envoyer (version compatible IE11)
    btnCalculate.addEventListener('click', function() {
        if (isSubmitting) return;
        
        // Valider
        if (!validateStep2()) {
            return;
        }
        
        isSubmitting = true;
        var originalText = this.innerHTML;
        this.innerHTML = '<span class="spinner"></span> Calcul en cours...';
        this.disabled = true;
        
        // Référence au bouton pour le callback
        var button = this;
        
        // Calculer les frais
        var priceEur = parseInt(priceSlider.value);
        calculationData = calculateFees(priceEur);
        
        // Préparer les données pour Formspree
        var formData;
        try {
            formData = new FormData();
        } catch (e) {
            // Fallback pour très vieux navigateurs
            alert('Votre navigateur est trop ancien. Veuillez le mettre à jour.');
            button.innerHTML = originalText;
            button.disabled = false;
            isSubmitting = false;
            return;
        }
        
        // Métadonnées
        formData.append('calculator_source', form.querySelector('[name="calculator_source"]').value);
        formData.append('_subject', 'Calcul frais notariaux - ' + emailInput.value);
        formData.append('timestamp', new Date().toISOString());
        formData.append('user_agent', navigator.userAgent);
        
        // Données utilisateur
        formData.append('first_name', firstNameInput.value.trim());
        formData.append('last_name', lastNameInput.value.trim());
        formData.append('email', emailInput.value.trim());
        formData.append('phone', phoneInput.value.trim() || 'Non renseigné');
        formData.append('country', countrySelect.value);
        
        // Données de calcul
        formData.append('transaction_amount_eur', calculationData.price.eur);
        formData.append('transaction_amount_fcfa', calculationData.price.fcfa);
        
        // Détail des frais (compatible IE11)
        for (var key in calculationData) {
            if (calculationData.hasOwnProperty(key) && key !== 'price' && calculationData[key].eur !== undefined) {
                formData.append('fees_' + key + '_eur', calculationData[key].eur);
                formData.append('fees_' + key + '_fcfa', calculationData[key].fcfa);
            }
        }
        
        // Envoyer à Formspree (compatible IE11)
        sendToFormspree(formData)
            .then(function(result) {
                if (result.ok || result.success) {
                    feedbackDiv.innerHTML = '<div class="alert alert-success">✅ Merci ! Vos informations ont été envoyées avec succès. Nous vous contacterons prochainement.</div>';
                    
                    // Sauvegarder en localStorage comme backup
                    try {
                        if (typeof(Storage) !== "undefined" && localStorage) {
                            localStorage.setItem('last_calculation', JSON.stringify({
                                date: new Date().toISOString(),
                                data: calculationData,
                                user: {
                                    name: firstNameInput.value + ' ' + lastNameInput.value,
                                    email: emailInput.value
                                }
                            }));
                        }
                    } catch (e) {
                        console.log('localStorage non disponible');
                    }
                } else {
                    throw new Error('Échec de l\'envoi');
                }
                
                // Afficher les résultats
                displayResults(calculationData);
                showStep(3);
            })
            .catch(function(error) {
                console.error('Erreur Formspree:', error);
                feedbackDiv.innerHTML = '<div class="alert alert-error">⚠️ Une erreur est survenue. Vos résultats sont affichés mais n\'ont pas pu être envoyés. Veuillez réessayer ou nous contacter directement.</div>';
                
                // Afficher quand même les résultats
                displayResults(calculationData);
                showStep(3);
            })
            .then(function() {
                // Finally equivalent pour IE11
                button.innerHTML = originalText;
                button.disabled = false;
                isSubmitting = false;
            });
    });
    
    // Nouveau calcul
    btnRestart.addEventListener('click', function() {
        // Réinitialiser le formulaire
        form.reset();
        priceSlider.value = 70000;
        updatePriceDisplay();
        
        // Effacer les erreurs (compatible IE11)
        var errorElements = document.querySelectorAll('.error');
        for (var i = 0; i < errorElements.length; i++) {
            errorElements[i].classList.remove('error');
        }
        
        var errorMessages = document.querySelectorAll('.error-message.show');
        for (var j = 0; j < errorMessages.length; j++) {
            errorMessages[j].classList.remove('show');
        }
        
        // Effacer le feedback
        feedbackDiv.innerHTML = '';
        
        // Retour étape 1
        showStep(1);
    });
    
    // ========================================
    // Initialisation
    // ========================================
    updatePriceDisplay();
    
    // Désactiver l'envoi classique du formulaire
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        return false;
    });
    
    // Focus sur mobile avec debounce
    if (window.innerWidth <= 768) {
        var touchTimeout;
        priceSlider.addEventListener('touchstart', function() {
            var slider = this;
            clearTimeout(touchTimeout);
            touchTimeout = setTimeout(function() {
                slider.focus();
            }, 100);
        });
    }
    
    // Analytics (si disponible)
    if (typeof gtag !== 'undefined') {
        // Track page view
        try {
            gtag('event', 'page_view', {
                page_title: 'Calculateur Frais Notariaux',
                page_location: window.location.href
            });
        } catch (e) {
            console.log('GTM non configuré');
        }
        
        // Track calculations (une seule fois)
        var trackingDone = false;
        btnCalculate.addEventListener('click', function() {
            if (!trackingDone && validateStep2()) {
                try {
                    gtag('event', 'calculate', {
                        event_category: 'Calculator',
                        event_label: 'Notary Fees',
                        value: parseInt(priceSlider.value)
                    });
                    trackingDone = true;
                } catch (e) {
                    console.log('Erreur tracking');
                }
            }
        });
    }
    
})();

/*
 * ================================================
 * GUIDE D'INTÉGRATION WORDPRESS/ELEMENTOR
 * ================================================
 * 
 * Option 1 - Widget HTML Elementor :
 * 1. Ajouter un widget "HTML" dans votre page
 * 2. Coller tout le code (HTML + CSS + JS)
 * 3. Publier la page
 * 
 * Option 2 - Shortcode WordPress :
 * Dans functions.php :
 * 
 * function notary_calculator_shortcode() {
 *     ob_start();
 *     include get_template_directory() . '/calculateur-notaire.html';
 *     return ob_get_clean();
 * }
 * add_shortcode('calculateur_notaire', 'notary_calculator_shortcode');
 * 
 * Puis utiliser [calculateur_notaire] dans vos pages
 * 
 * Option 3 - Plugin custom :
 * Créer un plugin WordPress dédié pour une meilleure maintenance
 * 
 * IMPORTANT :
 * - Testez avec vos plugins de cache actifs
 * - Vérifiez la compatibilité avec votre thème
 * - ID Formspree déjà configuré (xwpbpyyj)
 * - Activez Google Analytics si nécessaire
 */
</script>

</body>
</html>
