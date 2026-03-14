"use client";

import { useLang } from "./LanguageSwitcher";
import { i18n } from "@/lib/i18n";

export default function Technologies() {
  const { lang } = useLang();
  const t = i18n[lang].tech;

  const categories = [
    { label: "Frontend", skills: ["React", "React Native", "TypeScript", "JavaScript", "Next.js", "Tailwind CSS", "Redux", "PWA"] },
    { label: "Backend", skills: ["Python", "FastAPI", "Django", "Spring Boot", "Java", "Node.js", "Express.js", "REST API", "WebSockets"] },
    { label: t.dbLabel, skills: ["PostgreSQL", "MySQL", "SQL Server", "Alembic", "Hibernate", "MongoDB", "Redis"] },
    { label: "DevOps & Infrastructure", skills: ["Docker", "AWS", "Azure", "CI/CD", "Git", "GitHub Actions", "Grafana", "Prometheus"] },
    { label: "Testing & AI Tools", skills: ["PyTest", "Unit Testing", "Integration Testing", "GitHub Copilot", "Cursor", "Claude Code"] },
    { label: "Automation & CMS", skills: ["WordPress", "WooCommerce", "N8N"] },
  ];

  const languages = lang === "pl"
    ? [
      { name: "Polski", level: "Ojczysty", pct: 100 },
      { name: "Angielski", level: "B2", pct: 70 },
      { name: "Niemiecki", level: "A2", pct: 25 },
    ]
    : [
      { name: "Polish", level: "Native", pct: 100 },
      { name: "English", level: "B2", pct: 70 },
      { name: "German", level: "A2", pct: 25 },
    ];

  return (
    <section id="technologies" className="px-6 py-20">
      <div className="max-w-5xl mx-auto">

        <div className="mb-14">
          <div className="mono-label mb-3">{t.label}</div>
          <h2 className="font-bold" style={{ fontSize: "clamp(1.6rem, 4vw, 2.2rem)", color: "var(--fg)", letterSpacing: "-0.02em" }}>
            {t.title}
          </h2>
        </div>

        <div className="space-y-0">
          {categories.map((cat, i) => (
            <div key={cat.label}
              className="py-5 flex flex-wrap gap-y-3 gap-x-8 items-start"
              style={{ borderBottom: i < categories.length - 1 ? "1px solid var(--border)" : "none" }}
            >
              <div className="w-32 flex-shrink-0 pt-0.5">
                <span style={{
                  fontFamily: "var(--font-jetbrains), Consolas, monospace",
                  fontSize: "0.7rem", letterSpacing: "0.1em",
                  textTransform: "uppercase", color: "var(--fg-3)",
                }}>
                  {cat.label}
                </span>
              </div>
              <div className="flex flex-wrap gap-1.5">
                {cat.skills.map(skill => (
                  <span key={skill} className="chip">{skill}</span>
                ))}
              </div>
            </div>
          ))}
        </div>

        <div className="mt-10 pt-10" style={{ borderTop: "1px solid var(--border)" }}>
          <div className="mono-label mb-6">{lang === "pl" ? "Języki" : "Languages"}</div>
          <div className="flex flex-wrap gap-8">
            {languages.map(l => (
              <div key={l.name} style={{ minWidth: 140 }}>
                <div className="flex justify-between items-baseline mb-2">
                  <span style={{ fontSize: "0.88rem", color: "var(--fg)", fontWeight: 500 }}>{l.name}</span>
                  <span style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.68rem", color: "var(--fg-3)" }}>{l.level}</span>
                </div>
                <div className="h-px" style={{ background: "var(--border)", position: "relative" }}>
                  <div style={{ position: "absolute", top: 0, left: 0, height: "100%", width: `${l.pct}%`, background: "var(--accent)", opacity: 0.6 }} />
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
