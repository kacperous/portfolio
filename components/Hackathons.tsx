"use client";

import { useLang } from "./LanguageSwitcher";
import { i18n } from "@/lib/i18n";

const hackathons = [
  {
    place: { pl: "I miejsce", en: "1st place" },
    event: "Fintech Łódź_Hack",
    date: { pl: "Grudzień 2025", en: "December 2025" },
    team: "GitPushers",
    project: "Moje Osiedle",
    isFirst: true,
  },
  {
    place: { pl: "I miejsce", en: "1st place" },
    event: "Hack na Zdrowie 4",
    organizer: "UMED Łódź",
    date: { pl: "Kwiecień–Maj 2025", en: "April–May 2025" },
    team: "Alfiarze",
    project: "Kids Health App",
    isFirst: true,
  },
  {
    place: { pl: "II miejsce", en: "2nd place" },
    event: "BestHackingLeague",
    organizer: "Best",
    date: { pl: "Listopad 2025", en: "November 2025" },
    team: "Alfa Guys",
    project: "DPF Hunter",
    isFirst: false,
  },
  {
    place: { pl: "II miejsce", en: "2nd place" },
    event: "Hack&Play",
    organizer: "PLAY",
    date: { pl: "Październik 2025", en: "October 2025" },
    team: "GitPushers",
    project: "PharmaRadar",
    isFirst: false,
  },
];

export default function Hackathons() {
  const { lang } = useLang();
  const t = i18n[lang].hackathons;

  return (
    <section id="hackathons" className="px-6 py-20">
      <div className="max-w-5xl mx-auto">

        <div className="mb-14">
          <div className="mono-label mb-3">{t.label}</div>
          <h2 className="font-bold" style={{ fontSize: "clamp(1.6rem, 4vw, 2.2rem)", color: "var(--fg)", letterSpacing: "-0.02em" }}>
            {t.title}
          </h2>
        </div>

        <div className="flex flex-wrap gap-8 mb-12 pb-10" style={{ borderBottom: "1px solid var(--border)" }}>
          {[
            { n: "4", label: t.stats[0] },
            { n: "2×", label: t.stats[1] },
            { n: "2×", label: t.stats[2] },
          ].map(s => (
            <div key={s.label}>
              <div className="font-bold mb-0.5" style={{ fontSize: "1.8rem", color: "var(--fg)", letterSpacing: "-0.02em" }}>{s.n}</div>
              <div className="mono-label">{s.label}</div>
            </div>
          ))}
        </div>

        <div className="space-y-0">
          {hackathons.map((h, i) => (
            <div key={i}
              className="group py-6 flex flex-wrap gap-4 items-start"
              style={{ borderBottom: "1px solid var(--border)" }}
            >
              <div className="w-28 flex-shrink-0">
                <span style={{
                  fontFamily: "var(--font-jetbrains), Consolas, monospace",
                  fontSize: "0.72rem",
                  color: h.isFirst ? "var(--accent)" : "var(--fg-3)",
                  letterSpacing: "0.06em",
                }}>
                  {h.place[lang]}
                </span>
              </div>

              <div className="flex-1 min-w-0">
                <div className="flex flex-wrap items-baseline gap-x-3 gap-y-1 mb-1">
                  <span className="font-semibold" style={{ color: "var(--fg)", fontSize: "0.95rem" }}>{h.event}</span>
                  {h.organizer && (
                    <span style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.7rem", color: "var(--fg-3)" }}>
                      {h.organizer}
                    </span>
                  )}
                </div>
                <div className="mb-2 flex flex-wrap gap-x-3 gap-y-0.5">
                  <span style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.75rem", color: "var(--accent)" }}>
                    {h.project}
                  </span>
                  <span style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.72rem", color: "var(--fg-3)" }}>
                    {t.team} {h.team}
                  </span>
                </div>
                <p style={{ fontSize: "0.85rem", color: "var(--fg-3)", lineHeight: 1.6 }}>{t.items[i]}</p>
              </div>

              <div className="flex-shrink-0 text-right">
                <span style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.68rem", color: "var(--fg-3)" }}>
                  {h.date[lang]}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
