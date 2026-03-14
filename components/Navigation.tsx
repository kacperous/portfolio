"use client";

import { useState, useEffect } from "react";
import LanguageSwitcher, { useLang } from "./LanguageSwitcher";

function NavLinks({ mobile, onClose }: { mobile?: boolean; onClose?: () => void }) {
  const { lang } = useLang();
  const items = [
    { pl: "Doświadczenie", en: "Experience", href: "#experience" },
    { pl: "Projekty", en: "Projects", href: "#projects" },
    { pl: "Hackathony", en: "Hackathons", href: "#hackathons" },
    { pl: "Stack", en: "Stack", href: "#technologies" },
    { pl: "Kontakt", en: "Contact", href: "#contact" },
  ];

  if (mobile) {
    return (
      <>
        {items.map((i) => (
          <a key={i.href} href={i.href}
            className="text-sm py-2"
            style={{ color: "var(--fg-2)", fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.78rem", letterSpacing: "0.04em" }}
            onClick={onClose}
          >
            {lang === "pl" ? i.pl : i.en}
          </a>
        ))}
      </>
    );
  }

  return (
    <ul className="hidden md:flex items-center gap-7">
      {items.map((i) => (
        <li key={i.href}>
          <a href={i.href}
            className="transition-colors duration-150 hover:text-white"
            style={{ color: "var(--fg-3)", fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "0.78rem", letterSpacing: "0.04em" }}
          >
            {lang === "pl" ? i.pl : i.en}
          </a>
        </li>
      ))}
    </ul>
  );
}

export default function Navigation() {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const fn = () => setScrolled(window.scrollY > 30);
    window.addEventListener("scroll", fn, { passive: true });
    return () => window.removeEventListener("scroll", fn);
  }, []);

  return (
    <nav
      className="fixed top-0 left-0 right-0 z-50 transition-all duration-300"
      style={{
        background: scrolled ? "rgba(26,25,22,0.55)" : "transparent",
        backdropFilter: scrolled ? "blur(20px) saturate(1.4)" : "none",
        WebkitBackdropFilter: scrolled ? "blur(20px) saturate(1.4)" : "none",
        borderBottom: scrolled ? "1px solid var(--border)" : "1px solid transparent",
      }}
    >
      <div className="max-w-5xl mx-auto px-6 h-14 flex items-center justify-between">
        <a href="#hero"
          style={{ fontFamily: "var(--font-jetbrains), Consolas, monospace", fontSize: "1.05rem", color: "var(--fg-2)", letterSpacing: "0.04em" }}
        >
          <span style={{ color: "var(--fg-3)" }}>{"<"}</span>
          <span style={{ color: "var(--fg)" }}>KK</span>
          <span style={{ color: "var(--fg-3)" }}>{"/>"}</span>
        </a>

        <NavLinks />

        <div className="hidden md:flex items-center gap-3">
          <LanguageSwitcher />
        </div>

        <button className="md:hidden p-1.5" onClick={() => setOpen(v => !v)} aria-label="Menu">
          <div style={{ width: 18, display: "flex", flexDirection: "column", gap: 4 }}>
            <span className="block h-px w-full transition-all duration-200" style={{ background: "var(--fg-2)", transform: open ? "rotate(45deg) translateY(5px)" : "" }} />
            <span className="block h-px w-full transition-all duration-200" style={{ background: "var(--fg-2)", opacity: open ? 0 : 1 }} />
            <span className="block h-px w-full transition-all duration-200" style={{ background: "var(--fg-2)", transform: open ? "rotate(-45deg) translateY(-5px)" : "" }} />
          </div>
        </button>
      </div>

      {open && (
        <div className="md:hidden px-6 pb-5 pt-3 flex flex-col gap-1"
          style={{ background: "rgba(10,10,10,0.97)", borderTop: "1px solid var(--border)" }}>
          <NavLinks mobile onClose={() => setOpen(false)} />
          <div className="pt-3 mt-1" style={{ borderTop: "1px solid var(--border)" }}>
            <LanguageSwitcher />
          </div>
        </div>
      )}
    </nav>
  );
}
