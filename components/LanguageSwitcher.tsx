"use client";

import { createContext, useContext, useState, ReactNode } from "react";

type Lang = "pl" | "en";

interface LangContextType {
  lang: Lang;
  setLang: (l: Lang) => void;
  t: (pl: string, en: string) => string;
}

export const LangContext = createContext<LangContextType>({
  lang: "pl",
  setLang: () => {},
  t: (pl) => pl,
});

export function LangProvider({ children }: { children: ReactNode }) {
  const [lang, setLang] = useState<Lang>("pl");
  const t = (pl: string, en: string) => (lang === "pl" ? pl : en);
  return <LangContext.Provider value={{ lang, setLang, t }}>{children}</LangContext.Provider>;
}

export function useLang() {
  return useContext(LangContext);
}

export default function LanguageSwitcher() {
  const { lang, setLang } = useLang();

  return (
    <div className="flex items-center"
      style={{
        fontFamily: "var(--font-jetbrains), Consolas, monospace",
        fontSize: "0.7rem",
        letterSpacing: "0.08em",
        border: "1px solid var(--border)",
        borderRadius: 6,
        overflow: "hidden",
      }}
    >
      {(["pl", "en"] as Lang[]).map((l, i) => (
        <button key={l} onClick={() => setLang(l)}
          className="px-3 py-1.5 transition-colors duration-150"
          style={{
            background: lang === l ? "var(--bg-3)" : "transparent",
            color: lang === l ? "var(--fg)" : "var(--fg-3)",
            borderLeft: i > 0 ? "1px solid var(--border)" : "none",
            cursor: "pointer",
          }}
        >
          {l.toUpperCase()}
        </button>
      ))}
    </div>
  );
}
