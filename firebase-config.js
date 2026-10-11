// firebase-config.js
// ================================================
// Configuration Firebase — ISET Rosso
// ================================================

export const firebaseConfig = {
  apiKey: "AIzaSyDnrW6WnmbEFpbWzlW9IGglxAafajt2Kyo",
  authDomain: "iset-b9974.firebaseapp.com",
  databaseURL: "https://iset-b9974-default-rtdb.firebaseio.com",
  projectId: "iset-b9974",
  storageBucket: "iset-b9974.firebasestorage.app",
  messagingSenderId: "1054170284751",
  appId: "1:1054170284751:web:8f02232478430d5ae2adba"
};

export const DEPT_SEMESTERS = {
  TC:  ["S1", "S2"],
  PPV: ["S3", "S4", "S5", "S6"],
  GAB: ["S3", "S4", "S5", "S6"],
  GEM: ["S3", "S4", "S5", "S6"],
  PSA: ["S3", "S4", "S5", "S6"],
  STA: ["S3", "S4", "S5", "S6"]
};

export const DEFAULT_NO_TP = [
  "Anglais", "Anglais_2", "Francais", "Francais_2",
  "Francais_s3", "Francais_GAB_S3", "Math_et_Statistique",
  "Economie", "Economie_GAB", "Vulgarisation"
];

export function displaySubjectName(subject) {
  if (!subject) return "";
  return subject
    .replace(/_/g, " ")
    .replace(/I_/g, "I.")
    .replace(/et_/g, "et ")
    .replace(/l eau/g, "l'eau");
}