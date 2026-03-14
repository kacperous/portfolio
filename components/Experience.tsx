"use client";

import { useLang } from "./LanguageSwitcher";
import { i18n } from "@/lib/i18n";

const experiences = [
  {
    period: { pl: "2025 — teraz", en: "2025 — now" },
    role: "Full Stack Developer",
    company: "Norsys sp. z o.o.",
    product: "GreenTransit",
    productUrl: "https://greentransit.pl",
    current: true,
    tags: ["FastAPI", "Python", "Alembic", "PyTest", "React", "TypeScript", "PostgreSQL", "AWS", "PWA"],
  },
  {
    period: { pl: "Wrzesień 2025 — teraz", en: "September 2025 — now" },
    role: "Junior Python Developer",
    company: "Gaius-Lex",
    product: "Gaius-Lex",
    productUrl: "https://gaius-lex.pl",
    current: true,
    tags: ["Python", "FastAPI", "Web Scraping", "PostgreSQL", "Docker"],
  },
  {
    period: { pl: "Maj 2025 — Marzec 2026", en: "May 2025 — March 2026" },
    role: "Fullstack Developer",
    company: "QuickPick",
    product: "QuickPick",
    productUrl: "https://quickpick.pl",
    current: false,
    tags: ["Django", "React", "TypeScript", "WordPress", "WooCommerce"],
  },
  {
    period: { pl: "Luty — Maj 2025", en: "February — May 2025" },
    role: "Junior Fullstack Developer",
    company: "GD SOFT",
    product: "GD SOFT",
    productUrl: "https://gdsoft.info",
    current: false,
    tags: ["Spring Boot", "Java", "React", "Hibernate", "MySQL"],
  },
];

export default function Experience() {
  const { lang } = useLang();
  const t = i18n[lang].experience;

  return (
    <section id="experience" className="px-6 py-20">
      <div className="max-w-5xl mx-auto">
        <div className="mb-14">
          <div className="mono-label mb-3">{t.label}</div>
          <h2 className="font-bold" style={{ fontSize: "clamp(1.6rem, 4vw, 2.2rem)", color: "var(--fg)", letterSpacing: "-0.02em" }}>
            {t.title}
          </h2>
        </div>

        <div className="space-y-4">
          {experiences.map((exp, i) => {
            const tx = t.items[i];
            return (
              <div key={i} className="card p-6 sm:p-7">
                <div className="flex flex-wrap items-start justify-between gap-3 mb-4">
                  <div>
                    <div className="flex flex-wrap items-center gap-2.5 mb-1">
                      <h3 className="font-semibold" style={{ fontSize: "1.05rem", color: "var(--fg)" }}>
                        {exp.role}
                      </h3>
                      {exp.current && (
                        <span className="flex items-center gap-1.5 px-2 py-0.5 rounded"
                          style={{ background: "var(--accent-dim)", border: "1px solid rgba(168,184,122,0.2)" }}>
                          <span className="dot-live" style={{ width: 5, height: 5 }} />
                          <span style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.63rem", letterSpacing: "0.1em", color: "var(--accent)" }}>{t.now}</span>
                        </span>
                      )}
                    </div>
                    <div className="flex items-center gap-2" style={{ color: "var(--fg-2)", fontSize: "0.9rem" }}>
                      <span>{exp.company}</span>
                      {exp.product && (
                        <>
                          <span style={{ color: "var(--fg-3)" }}>·</span>
                          <a href={exp.productUrl} target="_blank" rel="noopener noreferrer"
                            style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.76rem", color: "var(--accent)" }}
                            onMouseEnter={e => ((e.currentTarget as HTMLElement).style.opacity = "0.7")}
                            onMouseLeave={e => ((e.currentTarget as HTMLElement).style.opacity = "1")}
                          >
                            {exp.product} ↗
                          </a>
                        </>
                      )}
                    </div>
                  </div>
                  <span style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.72rem", color: "var(--fg-3)", whiteSpace: "nowrap" }}>
                    {exp.period[lang]}
                  </span>
                </div>

                <p className="mb-4" style={{ color: "var(--fg-2)", fontSize: "0.9rem", lineHeight: 1.65 }}>
                  {tx.description}
                </p>

                <ul className="mb-5 space-y-1.5">
                  {tx.points.map((p, j) => (
                    <li key={j} className="flex items-start gap-2.5" style={{ fontSize: "0.87rem", color: "var(--fg-3)" }}>
                      <span style={{ color: "var(--accent)", marginTop: 5, flexShrink: 0, fontSize: "0.55rem" }}>▸</span>
                      {p}
                    </li>
                  ))}
                </ul>

                <div className="flex flex-wrap gap-1.5">
                  {exp.tags.map(tag => (
                    <span key={tag} className="chip">{tag}</span>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}
