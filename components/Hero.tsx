"use client";

import { useEffect, useState } from "react";
import { useLang } from "./LanguageSwitcher";
import { i18n } from "@/lib/i18n";

export default function Hero() {
  const { lang } = useLang();
  const t = i18n[lang].hero;

  const [roleIndex, setRoleIndex] = useState(0);
  const [displayed, setDisplayed] = useState("");
  const [deleting, setDeleting] = useState(false);

  const roles = t.typewriter;

  useEffect(() => {
    setDisplayed("");
    setDeleting(false);
  }, [lang]);

  useEffect(() => {
    const cur = roles[roleIndex % roles.length];
    let timer: ReturnType<typeof setTimeout>;
    if (!deleting && displayed.length < cur.length) {
      timer = setTimeout(() => setDisplayed(cur.slice(0, displayed.length + 1)), 55);
    } else if (!deleting && displayed.length === cur.length) {
      timer = setTimeout(() => setDeleting(true), 2600);
    } else if (deleting && displayed.length > 0) {
      timer = setTimeout(() => setDisplayed(cur.slice(0, displayed.length - 1)), 28);
    } else {
      setDeleting(false);
      setRoleIndex(i => (i + 1) % roles.length);
    }
    return () => clearTimeout(timer);
  }, [displayed, deleting, roleIndex, roles]);

  return (
    <section id="hero" className="min-h-screen flex flex-col justify-center px-6 pt-14">
      <div className="max-w-5xl mx-auto w-full py-12">

        {/* Badge */}
        <div className="flex items-center gap-2.5 mb-12">
          <span className="dot-live" />
          <span style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.72rem", letterSpacing: "0.1em", color: "var(--accent)" }}>
            {t.badge}
          </span>
        </div>

        {/* Name */}
        <h1 className="font-bold leading-[0.92] mb-8"
          style={{ fontSize: "clamp(3.8rem, 11vw, 7.5rem)", color: "var(--fg)", letterSpacing: "-0.02em" }}>
          Kacper<br />Kleczaj
        </h1>

        {/* Typewriter */}
        <div className="mb-8 h-8 flex items-center">
          <span style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "clamp(0.82rem, 2vw, 1rem)", color: "var(--fg-3)", letterSpacing: "0.01em" }}>
            {displayed}
            <span style={{ display: "inline-block", width: 2, height: "1em", background: "var(--accent)", marginLeft: 2, verticalAlign: "text-bottom", animation: "blink 1s step-end infinite" }} />
          </span>
        </div>

        {/* Mono attributes */}
        <div className="mb-5 flex flex-wrap gap-4">
          {t.attrs.map(item => (
            <span key={item.key} style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.7rem", color: "var(--fg-3)" }}>
              <span style={{ color: "var(--fg-3)" }}>{item.key}=</span>
              <span style={{ color: "var(--fg-2)" }}>&quot;{item.val}&quot;</span>
            </span>
          ))}
        </div>

        {/* Bio */}
        <p className="mb-12 max-w-lg" style={{ color: "var(--fg-2)", fontSize: "1rem", lineHeight: 1.75 }}>
          {t.bio}
        </p>

        {/* CTAs */}
        <div className="flex flex-wrap gap-3">
          <a href="#projects"
            className="inline-flex items-center px-5 py-2.5 rounded-lg text-sm font-semibold transition-colors duration-150"
            style={{ background: "var(--accent)", color: "#fff" }}
            onMouseEnter={e => (e.currentTarget.style.background = "#8fa064")}
            onMouseLeave={e => (e.currentTarget.style.background = "var(--accent)")}
          >
            {t.cta}
          </a>
          {[
            { label: "GitHub", href: "https://github.com/kacperous", external: true },
            { label: "LinkedIn", href: "https://www.linkedin.com/in/kacper-kleczaj-819622337/", external: true },
            { label: "kleczaj.kacper@gmail.com", href: "mailto:kleczaj.kacper@gmail.com", external: false },
          ].map(b => (
            <a key={b.label} href={b.href}
              target={b.external ? "_blank" : undefined}
              rel={b.external ? "noopener noreferrer" : undefined}
              className="inline-flex items-center px-5 py-2.5 rounded-lg transition-colors duration-150"
              style={{ border: "1px solid var(--border-2)", color: "var(--fg-3)", fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.76rem" }}
              onMouseEnter={e => { (e.currentTarget as HTMLElement).style.color = "var(--fg)"; (e.currentTarget as HTMLElement).style.borderColor = "rgba(255,255,255,0.2)"; }}
              onMouseLeave={e => { (e.currentTarget as HTMLElement).style.color = "var(--fg-3)"; (e.currentTarget as HTMLElement).style.borderColor = "var(--border-2)"; }}
            >
              {b.label}
            </a>
          ))}
        </div>

        {/* Stats */}
        <div className="mt-20 pt-8 flex flex-wrap gap-12" style={{ borderTop: "1px solid var(--border)" }}>
          {t.stats.map(s => (
            <div key={s.label}>
              <div className="font-bold mb-1" style={{ fontSize: "1.6rem", color: "var(--fg)", letterSpacing: "-0.02em" }}>{s.value}</div>
              <div className="mono-label">{s.label}</div>
            </div>
          ))}
        </div>
      </div>
      <style jsx>{`@keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }`}</style>
    </section>
  );
}
