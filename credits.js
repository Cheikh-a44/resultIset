// ============================================================
// credits.js — ISET Rosso
// Source: Emplois du département.pdf (PPV S3→S6)
// ============================================================

window.CREDITS_DATA = {
  TC: { S1: {}, S2: {} },

  PPV: {
    // ----------------------------------------------------------
    // S3 — 30 Crédits
    // ----------------------------------------------------------
    S3: {
      "Francais": 3,
      "Introduction_economie_gestion": 3,
      "Principes_generaux_agronomie": 4,
      "Principes_generaux_horticulture": 4,
      "Entomologie_Nematologie_ravageurs": 4,
      "Agro_pesticides_phytopharmacie": 4,
      "Introduction_science_du_sol": 4,
      "Introduction_sciences_des_plantes": 4
    },

    // ----------------------------------------------------------
    // S4 — 30 Crédits
    // ----------------------------------------------------------
    S4: {
      "Techniques_communication_vulgarisation": 3,
      "Technique_propagation_production_semences": 4,
      "Besoin_en_eau_des_cultures": 4,
      "Ecophysiologie_vegetale_Biochimie": 3,
      "Fertilite_sols_Nutrition_plantes": 3,
      "Methodes_diagnostic_phytoprotection": 3,
      "Malherbologie": 3,
      "Stage": 7
    },

    // ----------------------------------------------------------
    // S5 — 38 Crédits
    // ----------------------------------------------------------
    S5: {
      "Droit_Sante_Securite_environnement": 3,
      "Techniques_gestion_entreprenariat": 3,
      "Production_vegetale_2": 4,
      "Arboriculture": 4,
      "Conduite_calibration_equipements_agricoles": 4,
      "Phytopathologie_1": 4,
      "Projet": 4,
      "Gestion_conservation_sol_eau": 4,
      "Ennemis_cultures_lutte_integree": 4,
      "Introduction_paysage_cultures_ornementales": 4
    },

    // ----------------------------------------------------------
    // S6 — 38 Crédits
    // ----------------------------------------------------------
    S6: {
      "Redaction_edition_rapports": 3,
      "Amelioration_genetique_biotechnologie": 3,
      "Agroenvironnement_agriculture_precision": 3,
      "Stage_fin_etudes": 17,
      "Adaptation_changement_climatique": 4,
      "Phytopathologie_2": 4,
      "Amenagement_paysager_poste_recolte": 4
    }
  },

  GAB: {
    S3: {
      "Francais_GAB_S3": 3,
      "Economie_GAB": 3,
      "Resistance_de_materiaux": 3,
      "Energie_renouvelable": 3,
      "Environnement": 3,
      "Topographie": 4,
      "Dessin_assiste_par_ordinateur": 3,
      "Mecanique_de_fluides": 4,
      "Chimie_de_leau": 4
    },
    S4: {}, S5: {}, S6: {}
  },

  GEM: { S3: {}, S4: {}, S5: {}, S6: {} },
  PSA: { S3: {}, S4: {}, S5: {}, S6: {} },
  STA: { S3: {}, S4: {}, S5: {}, S6: {} }
};

window.NO_TP_SUBJECTS = [
  "Francais", "Francais_2", "Francais_s3", "Francais_GAB_S3",
  "Anglais", "Anglais_2",
  "Math_et_Statistique",
  "Economie", "Economie_GAB",
  "Introduction_economie_gestion",
  "Droit_Sante_Securite_environnement",
  "Techniques_gestion_entreprenariat",
  "Vulgarisation",
  "Techniques_communication_vulgarisation",
  "Redaction_edition_rapports"
];

window.STAGE_SUBJECTS = [
  "Stage", "Stage_fin_etude", "Stage_fin_etudes", "Projet_fin_etudes"
];

window.DEPT_SEMESTERS = {
  TC:  ["S1", "S2"],
  PPV: ["S3", "S4", "S5", "S6"],
  GAB: ["S3", "S4", "S5", "S6"],
  GEM: ["S3", "S4", "S5", "S6"],
  PSA: ["S3", "S4", "S5", "S6"],
  STA: ["S3", "S4", "S5", "S6"]
};

// Vérification
(function () {
  const expected = { S3: 30, S4: 30, S5: 38, S6: 38 };
  console.log("✅ credits.js chargé");
  for (const sem in expected) {
    const sum = Object.values(window.CREDITS_DATA.PPV[sem] || {}).reduce((a, b) => a + b, 0);
    console.log(`  PPV ${sem}: ${sum} / ${expected[sem]} ${sum === expected[sem] ? "✅" : "❌"}`);
  }
})();