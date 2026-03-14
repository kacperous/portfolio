"use client";

import { useLang } from "./LanguageSwitcher";
import { i18n } from "@/lib/i18n";

const certifications = [
  {
    title: "INF.02",
    sub: { pl: "Projektowanie stron oraz aplikacji internetowych", en: "Web & Application Design" },
    year: "2022–2023",
    issuer: "ZST im. Armii Krajowej",
  },
  {
    title: "INF.03",
    sub: { pl: "Zarządzanie i integracja baz danych, sieci komputerowe", en: "Database Management & Computer Networks" },
    year: "2022–2023",
    issuer: "ZST im. Armii Krajowej",
  },
  {
    title: { pl: "Marketing w e-commerce", en: "E-commerce Marketing" },
    sub: { pl: "Strategie, budowanie marki, kampanie. Paweł Tkaczyk", en: "Strategy, brand building, campaigns. Paweł Tkaczyk" },
    year: "2024",
    issuer: "Santander / Politechnika Łódzka",
  },
  {
    title: "Foreign Internship",
    sub: { pl: "Uruchamianie sklepu internetowego, podstawy robotyki", en: "E-commerce store setup, robotics basics" },
    year: "2021",
    issuer: "ENSO GROUP LTD, Athens",
  },
];

const schools = [
  {
    pl: { degree: "Informatyka Stosowana", type: "Studia inżynierskie", period: "2023 — obecnie" },
    en: { degree: "Applied Computer Science", type: "Engineering degree", period: "2023 — present" },
    school: "Politechnika Łódzka / Lodz University of Technology",
    current: true,
  },
  {
    pl: { degree: "Technik Informatyk", type: "Technikum", period: "2019 — 2023" },
    en: { degree: "IT Technician", type: "Technical high school", period: "2019 — 2023" },
    school: "ZST im. Armii Krajowej",
    current: false,
    note: { pl: "Biało-czerwony pasek", en: "Honors distinction" },
  },
];

export default function Education() {
  const { lang } = useLang();
  const t = i18n[lang].education;

  return (
    <section id="education" className="px-6 py-20">
      <div className="max-w-5xl mx-auto">

        <div className="mb-14">
          <div className="mono-label mb-3">{t.label}</div>
          <h2 className="font-bold" style={{ fontSize: "clamp(1.6rem, 4vw, 2.2rem)", color: "var(--fg)", letterSpacing: "-0.02em" }}>
            {t.title}
          </h2>
        </div>

        <div className="space-y-0 mb-12">
          {schools.map((e, i) => {
            const s = e[lang];
            return (
              <div key={i} className="py-6 flex flex-wrap gap-4 items-start"
                style={{ borderBottom: "1px solid var(--border)" }}>
                <div className="flex-1 min-w-48">
                  <div className="flex flex-wrap items-center gap-2.5 mb-0.5">
                    <span className="font-semibold" style={{ color: "var(--fg)", fontSize: "0.95rem" }}>{s.degree}</span>
                    {e.current && (
                      <span className="flex items-center gap-1.5 px-2 py-0.5 rounded"
                        style={{ background: "var(--accent-dim)", border: "1px solid rgba(168,184,122,0.2)" }}>
                        <span className="dot-live" style={{ width: 5, height: 5 }} />
                        <span style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.63rem", letterSpacing: "0.1em", color: "var(--accent)" }}>NOW</span>
                      </span>
                    )}
                  </div>
                  <div style={{ fontSize: "0.85rem", color: "var(--fg-3)" }}>{s.type} · {e.school}</div>
                  {e.note && (
                    <div style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.7rem", color: "var(--fg-3)", marginTop: 4 }}>
                      {e.note[lang]}
                    </div>
                  )}
                </div>
                <span style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.72rem", color: "var(--fg-3)", flexShrink: 0, paddingTop: 2 }}>
                  {s.period}
                </span>
              </div>
            );
          })}
        </div>

        <div className="mono-label mb-6">{t.certsLabel}</div>
        <div className="space-y-0">
          {certifications.map((c, i) => {
            const title = typeof c.title === "string" ? c.title : c.title[lang];
            const sub = c.sub[lang];
            return (
              <div key={i} className="py-4 flex flex-wrap gap-4 items-start"
                style={{ borderBottom: i < certifications.length - 1 ? "1px solid var(--border)" : "none" }}>
                <div className="flex-1 min-w-48">
                  <div className="font-medium mb-0.5" style={{ color: "var(--fg)", fontSize: "0.88rem" }}>{title}</div>
                  <div style={{ fontSize: "0.81rem", color: "var(--fg-3)" }}>{sub}</div>
                  <div style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.68rem", color: "var(--fg-3)", marginTop: 3 }}>{c.issuer}</div>
                </div>
                <span style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.7rem", color: "var(--fg-3)", flexShrink: 0, paddingTop: 2 }}>{c.year}</span>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
