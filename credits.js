// ============================================================
// credits.js — généré depuis l'espace coordinateur
// Vous pouvez modifier les crédits à la main.
// ============================================================

window.CREDITS_DATA = {
  TC: {
    S1: {
      // M11 — Module 11
      "Anglais_1": 3,
      "Français_1": 3,
      // M12 — Module 12
      "Informatique": 3,
      "Mathématiques_et_Statistiques": 5,
      // M13 — Module 13
      "Physique": 4,
      "Chimie": 4,
      // M14 — Module 14
      "Biologie_Générale": 4,
      "Microbiologie_et_Génétique": 4,
    },
    S2: {
      // M21 — Module 21
      "Anglais_2": 3,
      "Français_2": 3,
      // M22 — Module 22
      "TIC": 3,
      "PPV": 3,
      // M23 — Module 23
      "PSA": 3,
      "STA": 3,
      // M24 — Module 24
      "GAB": 3,
      "GEM": 3,
    },
  },
  PPV: {
    S3: {
      // M31 — Langue et économie
      "Francais": 3,
      "Introduction_economie_gestion": 3,
      // M32 — Principes d'agronomie
      "Principes_generaux_agronomie": 4,
      "Principes_generaux_horticulture": 4,
      // M33 — Phytoprotection 1
      "Entomologie_Nematologie_ravageurs": 4,
      "Agro_pesticides_phytopharmacie": 4,
      // M34 — Sciences du sol et des plantes
      "Introduction_science_du_sol": 4,
      "Introduction_sciences_des_plantes": 4,
    },
    S4: {
      // M41 — Vulgarisation
      "Techniques_communication_vulgarisation": 3,
      // M42 — Production végétale 1
      "Technique_propagation_production_semences": 4,
      "Besoin_en_eau_des_cultures": 3,
      // M43 — Ecophysiologie et Nutrition des plantes
      "Ecophysiologie_vegetale_Biochimie": 4,
      "Fertilite_sols_Nutrition_plantes": 3,
      // M44 — Méthodes de diagnostic
      "Methodes_diagnostic_phytoprotection": 3,
      "Malherbologie": 3,
      // M45 — Stage en milieu de travail
      "Stage": 7,
    },
    S5: {
      // M51 — Entrepreneuriat
      "Droit_Sante_Securite_environnement": 3,
      "Techniques_gestion_entreprenariat": 3,
      // M52 — Systèmes de production
      "Production_vegetale_2": 4,
      "Arboriculture": 4,
      "Conduite_calibration_equipements_agricoles": 4,
      // M53 — Phytopathologie 1
      "Phytopathologie_1": 4,
      "Projet": 4,
      // M54 — Optionnel
      "Gestion_conservation_sol_eau": 4,
      "Ennemis_cultures_lutte_integree": 4,
      "Introduction_paysage_cultures_ornementales": 4,
    },
    S6: {
      // M61 — Rédaction des rapports
      "Redaction_edition_rapports": 3,
      // M62 — Agronomie avancée
      "Amelioration_genetique_biotechnologie": 3,
      "Agroenvironnement_agriculture_precision": 3,
      // M63 — Projet de fin d'études
      "Stage_fin_etudes": 17,
      // M64 — Optionnel
      "Adaptation_changement_climatique": 4,
      "Phytopathologie_2": 4,
      "Amenagement_paysager_poste_recolte": 4,
    },
  },
  GAB: {
    S3: {
      // Autres matières (déjà dans l'ancien fichier)
      "Francais_GAB_S3": 3,
      "Economie_GAB": 3,
      "Resistance_de_materiaux": 3,
      "Energie_renouvelable": 3,
      "Environnement": 3,
      "Topographie": 4,
      "Dessin_assiste_par_ordinateur": 3,
      "Mecanique_de_fluides": 4,
      "Chimie_de_leau": 4,
    },
    S4: {
    },
    S5: {
    },
    S6: {
    },
  },
  GEM: {
    S3: {
    },
    S4: {
    },
    S5: {
    },
    S6: {
    },
  },
  PSA: {
    S3: {
    },
    S4: {
    },
    S5: {
    },
    S6: {
    },
  },
  STA: {
    S3: {
    },
    S4: {
    },
    S5: {
    },
    S6: {
    },
  },
};

window.NO_TP_SUBJECTS = [
  "Francais",
  "Francais_2",
  "Francais_s3",
  "Francais_GAB_S3",
  "Anglais",
  "Anglais_2",
  "Math_et_Statistique",
  "Economie",
  "Economie_GAB",
  "Introduction_economie_gestion",
  "Droit_Sante_Securite_environnement",
  "Techniques_gestion_entreprenariat",
  "Vulgarisation",
  "Techniques_communication_vulgarisation",
  "Redaction_edition_rapports",
  "Stage",
  "Stage_fin_etudes",
  "Anglais_1",
  "Français_1",
  "Mathématiques_et_Statistiques",
  "Français_2"
];

window.STAGE_SUBJECTS = [
  "Stage",
  "Stage_fin_etude",
  "Stage_fin_etudes",
  "Projet_fin_etudes"
];

window.DEPT_SEMESTERS = {
  "TC": [
    "S1",
    "S2"
  ],
  "PPV": [
    "S3",
    "S4",
    "S5",
    "S6"
  ],
  "GAB": [
    "S3",
    "S4",
    "S5",
    "S6"
  ],
  "GEM": [
    "S3",
    "S4",
    "S5",
    "S6"
  ],
  "PSA": [
    "S3",
    "S4",
    "S5",
    "S6"
  ],
  "STA": [
    "S3",
    "S4",
    "S5",
    "S6"
  ]
};

// Vérification (console)
(function () {
  console.log("✅ credits.js chargé");
  for (const dept in window.CREDITS_DATA) {
    for (const sem in window.CREDITS_DATA[dept]) {
      const subs = window.CREDITS_DATA[dept][sem];
      if (!Object.keys(subs).length) continue;
      const sum = Object.values(subs).reduce((x, y) => x + y, 0);
      console.log(`  ${dept} ${sem}: ${sum} crédits`);
    }
  }
})();