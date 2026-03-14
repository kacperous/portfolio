"use client";

import { useLang } from "./LanguageSwitcher";
import { i18n } from "@/lib/i18n";

export default function Contact() {
  const { lang } = useLang();
  const t = i18n[lang].contact;

  const links = [
    { label: "email", value: "kleczaj.kacper@gmail.com", href: "mailto:kleczaj.kacper@gmail.com" },
    { label: "github", value: "github.com/kacperous", href: "https://github.com/kacperous" },
    { label: "linkedin", value: "Kacper Kleczaj", href: "https://www.linkedin.com/in/kacper-kleczaj-819622337/" },
    { label: "phone", value: "+48 690-827-655", href: "tel:+48690827655" },
  ];

  return (
    <section id="contact" className="px-6 py-20 pb-28">
      <div className="max-w-5xl mx-auto">

        <div className="mb-14">
          <div className="mono-label mb-3">{t.label}</div>
          <h2 className="font-bold" style={{ fontSize: "clamp(1.6rem, 4vw, 2.2rem)", color: "var(--fg)", letterSpacing: "-0.02em" }}>
            {t.title}
          </h2>
        </div>

        <div className="mb-14 max-w-xl">
          <p style={{ fontSize: "clamp(1rem, 2vw, 1.15rem)", color: "var(--fg-2)", lineHeight: 1.75 }}>
            {t.body}
          </p>
          <div className="mt-8">
            <a href="mailto:kleczaj.kacper@gmail.com"
              className="inline-flex items-center gap-2 px-6 py-3 rounded-lg font-semibold transition-colors duration-150"
              style={{ background: "var(--accent)", color: "#fff", fontSize: "0.9rem" }}
              onMouseEnter={e => (e.currentTarget.style.background = "#8fa064")}
              onMouseLeave={e => (e.currentTarget.style.background = "var(--accent)")}
            >
              {t.cta}
            </a>
          </div>
        </div>

        <div className="space-y-0" style={{ borderTop: "1px solid var(--border)" }}>
          {links.map(l => (
            <a key={l.label} href={l.href}
              target={l.href.startsWith("http") ? "_blank" : undefined}
              rel={l.href.startsWith("http") ? "noopener noreferrer" : undefined}
              className="flex items-center justify-between py-4 group transition-colors duration-150"
              style={{ borderBottom: "1px solid var(--border)" }}
            >
              <span style={{
                fontFamily: "var(--font-jetbrains), Consolas, monospace",
                fontSize: "0.72rem", color: "var(--fg-3)",
                letterSpacing: "0.1em", textTransform: "uppercase",
                width: 80, flexShrink: 0,
              }}>
                {l.label}
              </span>
              <span style={{ color: "var(--fg-2)", fontSize: "0.9rem" }}
                className="group-hover:text-white transition-colors">
                {l.value}
              </span>
              <span style={{ color: "var(--fg-3)", fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.8rem" }}
                className="group-hover:text-white transition-colors">
                ↗
              </span>
            </a>
          ))}
        </div>

        <div className="mt-16" style={{ borderTop: "1px solid var(--border)", paddingTop: 24 }}>
          <span style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.68rem", color: "var(--fg-3)", letterSpacing: "0.06em" }}>
            © 2026 Kacper Kleczaj · Łódź, Polska · made with <span style={{ color: "var(--accent)" }}>passion ♥</span>
          </span>
        </div>
      </div>
    </section>
  );
}
