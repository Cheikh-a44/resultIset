// ============================================================
// credits.js — ISET Rosso
// ============================================================
// قائمة كاملة بالمواد و Crédits لكل قسم و فصل
// ⚠️ عدّل الأرقام بحرية
// ⚠️ أضف المواد الناقصة في الأقسام الفارغة
// ============================================================

window.CREDITS_DATA = {

  // ============================================================
  // TC - Tronc Commun (السنة الأولى)
  // ⚠️ لا أعرف مواد TC — الرجاء إضافتها
  // ============================================================
  TC: {
    S1: {
      // "Nom_Matiere": 3,
    },
    S2: {
      // "Nom_Matiere": 3,
    }
  },

  // ============================================================
  // PPV - Productions Végétales
  // ============================================================
  PPV: {
    S3: {
      "Francais_s3": 3,
      "Economie": 3,
      "I_Agronomie": 4,
      "I_Horticulture": 4,
      "Pesticides_agricoles": 4,
      "Entomologie_et_Nemato": 4,
      "Science_des_sols": 4,
      "Science_des_plantes": 4
    },
    S4: {
      "Vulgarisation": 3,
      "Technique_de_propagation": 4,
      "Technique_d_irrigation_et_BEC": 3,
      "Ecophysiologie_et_Biochimie": 4,
      "Fertilite_du_sol": 3,
      "Methodes_de_diagnostic": 3,
      "Malherbologie": 3
    },
    S5: {
      // ⚠️ لا أعرف مواد PPV S5 — الرجاء إضافتها
      // "Nom_Matiere": 3,
    },
    S6: {
      // ⚠️ لا أعرف مواد PPV S6 — الرجاء إضافتها
      // "Nom_Matiere": 3,
    }
  },

  // ============================================================
  // GAB - Génie Agricole et Biologique
  // ============================================================
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
    S4: {
      // ⚠️ لا أعرف مواد GAB S4 — الرجاء إضافتها
      // "Nom_Matiere": 3,
    },
    S5: {
      // ⚠️ لا أعرف مواد GAB S5
    },
    S6: {
      // ⚠️ لا أعرف مواد GAB S6
    }
  },

  // ============================================================
  // GEM - Génie Électromécanique
  // ⚠️ لا أعرف أي مادة — الرجاء إضافتها
  // ============================================================
  GEM: {
    S3: {},
    S4: {},
    S5: {},
    S6: {}
  },

  // ============================================================
  // PSA - Production et Santé Animales
  // ⚠️ لا أعرف أي مادة
  // ============================================================
  PSA: {
    S3: {},
    S4: {},
    S5: {},
    S6: {}
  },

  // ============================================================
  // STA - Sciences et Techniques Agroalimentaires
  // ⚠️ لا أعرف أي مادة
  // ============================================================
  STA: {
    S3: {},
    S4: {},
    S5: {},
    S6: {}
  }
};

// ============================================================
// المواد التي ليس لها TP
// ⚠️ عدّل هذه القائمة حسب نظامك
// ============================================================
window.NO_TP_SUBJECTS = [
  // Français
  "Francais", "Francais_2", "Francais_s3", "Francais_GAB_S3",

  // Anglais
  "Anglais", "Anglais_2",

  // Mathématiques et Statistiques
  "Math_et_Statistique",

  // Économie
  "Economie", "Economie_GAB",

  // Vulgarisation (حسب نظامك — إن كانت لها TP، احذفها من هنا)
  "Vulgarisation"
];

// ============================================================
// المواد التي تعتبر Stage
// ============================================================
window.STAGE_SUBJECTS = [
  "Stage",
  "Stage_fin_etude"
];

// ============================================================
// DEPT_SEMESTERS — الأقسام والفصول
// ============================================================
window.DEPT_SEMESTERS = {
  TC:  ["S1", "S2"],
  PPV: ["S3", "S4", "S5", "S6"],
  GAB: ["S3", "S4", "S5", "S6"],
  GEM: ["S3", "S4", "S5", "S6"],
  PSA: ["S3", "S4", "S5", "S6"],
  STA: ["S3", "S4", "S5", "S6"]
};

console.log("✅ credits.js chargé");
console.log("  Départements:", Object.keys(window.CREDITS_DATA).join(", "));
console.log("  Matières sans TP:", window.NO_TP_SUBJECTS.length);