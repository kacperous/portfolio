"use client";

import { useRef, useState, useCallback, useEffect } from "react";
import Image from "next/image";
import { useLang } from "./LanguageSwitcher";
import { i18n } from "@/lib/i18n";

type Project = {
  title: string;
  year: string;
  description: string;
  tags: string[];
  images: string[];
  imgFit?: "cover" | "contain";
  imgPos?: string;
  portrait?: boolean;
  hackathon?: string;
  links?: { label: string; href: string }[];
};

const projects: Project[] = [
  {
    title: "DosFit",
    year: "2025",
    description: 'Aplikacja do zmiany nawyków żywieniowych — zasada "12 miesięcy, 12 nawyków". AI licznik kalorii z analizą zdjęć. Grywalizacja i moduł rodzic-dziecko.',
    tags: ["React Native", "Python", "AI", "Expo"],
    images: ["/portfolio/dosfit/1.PNG", "/portfolio/dosfit/2.PNG", "/portfolio/dosfit/3.PNG", "/portfolio/dosfit/4.PNG", "/portfolio/dosfit/5.PNG"],
    imgFit: "contain",
    portrait: true,
    links: [
      { label: "App Store", href: "https://apps.apple.com/us/app/dosfit/id6753219160" },
      { label: "Google Play", href: "https://play.google.com/store/apps/details?id=com.dosfit.dosfitexpo" },
      { label: "dosfit.pl", href: "https://dosfit.pl" },
    ],
  },
  {
    title: "Splitly",
    year: "2025",
    description: "Mobilna aplikacja do zarządzania wspólnymi wydatkami. Automatyczne rozliczanie długów, raporty wydatków i synchronizacja w czasie rzeczywistym.",
    tags: ["React Native", "TypeScript", "Firebase"],
    images: ["/portfolio/splitly/1.PNG", "/portfolio/splitly/2.PNG", "/portfolio/splitly/3.PNG", "/portfolio/splitly/4.PNG", "/portfolio/splitly/5.PNG", "/portfolio/splitly/6.PNG", "/portfolio/splitly/7.PNG"],
    imgFit: "contain",
    portrait: true,
    links: [],
  },
  {
    title: "PotrzebnaLista",
    year: "2024–2025",
    description: "Platforma do współdzielenia list zakupów via WebSockety. Google Login, SMS weryfikacja, Stripe subskrypcje.",
    tags: ["Django", "React", "WebSockets", "Stripe"],
    images: ["/portfolio/potrzebnalista/1.jpg"],
    imgFit: "cover",
    imgPos: "center",
    links: [],
  },
  {
    title: "DPF Hunter",
    year: "2025",
    hackathon: "🥈 II miejsce — BestHackingLeague",
    description: "AI system do wykrywania pojazdów bez filtra DPF z kamer miejskich. Integracja z CEPiK do automatycznego raportowania naruszeń.",
    tags: ["Python", "Computer Vision", "FastAPI", "CEPiK API"],
    images: ["/portfolio/dpf/1.png", "/portfolio/dpf/2.png", "/portfolio/dpf/3.png", "/portfolio/dpf/4.JPG", "/portfolio/dpf/5.JPG", "/portfolio/dpf/6.JPG"],
    imgFit: "cover",
    imgPos: "center",
    links: [],
  },
  {
    title: "PharmaRadar",
    year: "2025",
    hackathon: "🥈 II miejsce — Hack&Play (PLAY)",
    description: "Aplikacja agregująca dane o lekach, alerty prawne i dane rynkowe — dedykowana farmaceutom i menedżerom aptecznym.",
    tags: ["React", "TypeScript", "Django", "REST API"],
    images: ["/portfolio/pharmaradar/1.png", "/portfolio/pharmaradar/2.png", "/portfolio/pharmaradar/3.png", "/portfolio/pharmaradar/4.png", "/portfolio/pharmaradar/5.png", "/portfolio/pharmaradar/6.jpg"],
    imgFit: "cover",
    imgPos: "top center",
    links: [],
  },
  {
    title: "Moje Osiedle",
    year: "2025",
    hackathon: "🥇 I miejsce — Fintech Łódź_Hack",
    description: "Rozszerzenie karty Łodzianina o grywalizację dzielnic. Nagradza mieszkańców za aktywność w lokalnej społeczności i wsparcie lokalnych firm.",
    tags: ["React", "TypeScript", "FinTech"],
    images: ["/portfolio/mojeosiedle/1.png", "/portfolio/mojeosiedle/2.png", "/portfolio/mojeosiedle/3.png", "/portfolio/mojeosiedle/4.png", "/portfolio/mojeosiedle/5.JPEG"],
    imgFit: "contain",
    portrait: true,
    links: [],
  },
];

// ── Lightbox ──────────────────────────────────────────────────────────────────

function Lightbox({ images, startIdx, portrait, onClose }: {
  images: string[];
  startIdx: number;
  portrait?: boolean;
  onClose: () => void;
}) {
  const [idx, setIdx] = useState(startIdx);

  const prev = useCallback(() => setIdx(i => (i - 1 + images.length) % images.length), [images.length]);
  const next = useCallback(() => setIdx(i => (i + 1) % images.length), [images.length]);

  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (e.key === "Escape") onClose();
      if (e.key === "ArrowLeft") prev();
      if (e.key === "ArrowRight") next();
    };
    window.addEventListener("keydown", handler);
    document.body.style.overflow = "hidden";
    return () => {
      window.removeEventListener("keydown", handler);
      document.body.style.overflow = "";
    };
  }, [onClose, prev, next]);

  return (
    <div
      onClick={onClose}
      style={{
        position: "fixed", inset: 0, zIndex: 1000,
        background: "rgba(0,0,0,0.92)", backdropFilter: "blur(12px)",
        display: "flex", alignItems: "center", justifyContent: "center",
      }}
    >
      {/* Image */}
      <div
        onClick={e => e.stopPropagation()}
        style={{
          position: "relative",
          width: portrait ? "min(90vh * 0.46, 90vw)" : "min(90vw, 1200px)",
          height: portrait ? "min(90vh, 90vw / 0.46)" : "min(80vh, 90vw * 0.5625)",
          maxWidth: portrait ? "420px" : "1200px",
          maxHeight: portrait ? "90vh" : "80vh",
        }}
      >
        <Image
          src={images[idx]}
          alt=""
          fill
          style={{ objectFit: "contain" }}
          sizes="(max-width: 768px) 100vw, 1200px"
          priority
        />
      </div>

      {/* Close */}
      <button onClick={onClose} style={{
        position: "fixed", top: 20, right: 20,
        width: 36, height: 36, borderRadius: 9,
        background: "rgba(255,255,255,0.1)", border: "1px solid rgba(255,255,255,0.15)",
        color: "#fff", fontSize: "1rem", cursor: "pointer",
        display: "flex", alignItems: "center", justifyContent: "center",
        backdropFilter: "blur(4px)",
      }}>✕</button>

      {/* Counter */}
      <div style={{
        position: "fixed", top: 24, left: "50%", transform: "translateX(-50%)",
        fontFamily: "var(--font-jetbrains), Consolas, monospace",
        fontSize: "0.65rem", color: "rgba(255,255,255,0.6)",
        letterSpacing: "0.1em",
      }}>
        {String(idx + 1).padStart(2, "0")} / {String(images.length).padStart(2, "0")}
      </div>

      {images.length > 1 && (
        <>
          <button onClick={e => { e.stopPropagation(); prev(); }} style={{
            position: "fixed", left: 16, top: "50%", transform: "translateY(-50%)",
            width: 44, height: 44, borderRadius: 11,
            background: "rgba(255,255,255,0.08)", border: "1px solid rgba(255,255,255,0.12)",
            color: "#fff", fontSize: "1.3rem", cursor: "pointer",
            display: "flex", alignItems: "center", justifyContent: "center",
            backdropFilter: "blur(4px)", transition: "background 0.15s",
          }}
            onMouseEnter={e => (e.currentTarget.style.background = "rgba(255,255,255,0.16)")}
            onMouseLeave={e => (e.currentTarget.style.background = "rgba(255,255,255,0.08)")}
          >‹</button>
          <button onClick={e => { e.stopPropagation(); next(); }} style={{
            position: "fixed", right: 16, top: "50%", transform: "translateY(-50%)",
            width: 44, height: 44, borderRadius: 11,
            background: "rgba(255,255,255,0.08)", border: "1px solid rgba(255,255,255,0.12)",
            color: "#fff", fontSize: "1.3rem", cursor: "pointer",
            display: "flex", alignItems: "center", justifyContent: "center",
            backdropFilter: "blur(4px)", transition: "background 0.15s",
          }}
            onMouseEnter={e => (e.currentTarget.style.background = "rgba(255,255,255,0.16)")}
            onMouseLeave={e => (e.currentTarget.style.background = "rgba(255,255,255,0.08)")}
          >›</button>
        </>
      )}
    </div>
  );
}

// ── Card gallery (thumbnail) ──────────────────────────────────────────────────

function CardGallery({ images, fit, pos, portrait, onOpen }: {
  images: string[];
  fit: "cover" | "contain";
  pos: string;
  portrait?: boolean;
  onOpen: (idx: number) => void;
}) {
  const [idx, setIdx] = useState(0);
  const [animating, setAnimating] = useState(false);

  const go = useCallback((next: number, e?: React.MouseEvent) => {
    e?.stopPropagation();
    if (animating) return;
    setAnimating(true);
    setTimeout(() => { setIdx(next); setAnimating(false); }, 180);
  }, [animating]);

  const prev = (e: React.MouseEvent) => go((idx - 1 + images.length) % images.length, e);
  const next = (e: React.MouseEvent) => go((idx + 1) % images.length, e);

  const bg = portrait ? "var(--bg)" : "#0a0a0a";

  return (
    <div style={{ position: "relative", width: "100%", height: "100%", overflow: "hidden", background: bg }}>
      {/* Clickable image → opens lightbox */}
      <div
        onClick={() => onOpen(idx)}
        style={{
          transition: "opacity 0.18s ease", opacity: animating ? 0 : 1,
          width: "100%", height: "100%", position: "relative", cursor: "zoom-in",
        }}
      >
        <Image
          src={images[idx]}
          alt=""
          fill
          style={{ objectFit: fit, objectPosition: portrait ? "center" : pos }}
          sizes="(max-width: 768px) 92vw, 400px"
          priority={idx === 0}
        />
      </div>

      {/* Bottom gradient (skip for contain/portrait — no overlap) */}
      {!portrait && (
        <div style={{
          position: "absolute", inset: 0,
          background: "linear-gradient(to top, rgba(0,0,0,0.45) 0%, transparent 40%)",
          pointerEvents: "none",
        }} />
      )}

      {/* Expand icon hint */}
      <div onClick={() => onOpen(idx)} style={{
        position: "absolute", top: 8, left: 8,
        width: 26, height: 26, borderRadius: 6,
        background: "rgba(0,0,0,0.5)", backdropFilter: "blur(4px)",
        border: "1px solid rgba(255,255,255,0.1)",
        display: "flex", alignItems: "center", justifyContent: "center",
        cursor: "zoom-in", opacity: 0.7,
      }}>
        <svg width="11" height="11" viewBox="0 0 11 11" fill="none">
          <path d="M1 4V1h3M7 1h3v3M10 7v3H7M4 10H1V7" stroke="white" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round"/>
        </svg>
      </div>

      {images.length > 1 && (
        <>
          <button onClick={prev} style={{
            position: "absolute", left: 8, top: "50%", transform: "translateY(-50%)",
            width: 28, height: 28, borderRadius: 7,
            background: "rgba(0,0,0,0.6)", backdropFilter: "blur(6px)",
            border: "1px solid rgba(255,255,255,0.1)",
            color: "rgba(255,255,255,0.85)", fontSize: "1rem",
            cursor: "pointer", display: "flex", alignItems: "center", justifyContent: "center",
            transition: "background 0.15s", fontFamily: "system-ui",
          }}
            onMouseEnter={e => (e.currentTarget.style.background = "rgba(0,0,0,0.82)")}
            onMouseLeave={e => (e.currentTarget.style.background = "rgba(0,0,0,0.6)")}
          >‹</button>
          <button onClick={next} style={{
            position: "absolute", right: 8, top: "50%", transform: "translateY(-50%)",
            width: 28, height: 28, borderRadius: 7,
            background: "rgba(0,0,0,0.6)", backdropFilter: "blur(6px)",
            border: "1px solid rgba(255,255,255,0.1)",
            color: "rgba(255,255,255,0.85)", fontSize: "1rem",
            cursor: "pointer", display: "flex", alignItems: "center", justifyContent: "center",
            transition: "background 0.15s", fontFamily: "system-ui",
          }}
            onMouseEnter={e => (e.currentTarget.style.background = "rgba(0,0,0,0.82)")}
            onMouseLeave={e => (e.currentTarget.style.background = "rgba(0,0,0,0.6)")}
          >›</button>

          <div style={{
            position: "absolute", bottom: 10, left: 0, right: 0,
            display: "flex", justifyContent: "center", gap: 5, pointerEvents: "none",
          }}>
            {images.map((_, i) => (
              <button key={i}
                onClick={e => { e.stopPropagation(); go(i); }}
                style={{
                  width: i === idx ? 16 : 5, height: 5, borderRadius: 3,
                  background: i === idx ? "var(--accent)" : "rgba(255,255,255,0.4)",
                  border: "none", cursor: "pointer", padding: 0,
                  transition: "width 0.2s, background 0.2s",
                  pointerEvents: "auto",
                }}
              />
            ))}
          </div>

          <div style={{
            position: "absolute", top: 8, right: 8,
            fontFamily: "var(--font-jetbrains), Consolas, monospace",
            fontSize: "0.58rem", color: "rgba(255,255,255,0.65)",
            background: "rgba(0,0,0,0.5)", backdropFilter: "blur(4px)",
            border: "1px solid rgba(255,255,255,0.08)",
            padding: "2px 6px", borderRadius: 4, letterSpacing: "0.05em",
          }}>
            {String(idx + 1).padStart(2, "0")} / {String(images.length).padStart(2, "0")}
          </div>
        </>
      )}
    </div>
  );
}

// ── Project card ──────────────────────────────────────────────────────────────

function ProjectCard({ p }: { p: Project }) {
  const [hovered, setHovered] = useState(false);
  const [lightboxIdx, setLightboxIdx] = useState<number | null>(null);

  return (
    <>
      {lightboxIdx !== null && (
        <Lightbox
          images={p.images}
          startIdx={lightboxIdx}
          portrait={p.portrait}
          onClose={() => setLightboxIdx(null)}
        />
      )}

      <div
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
        style={{
          flexShrink: 0, width: 380,
          scrollSnapAlign: "start",
          background: "var(--bg-2)",
          border: `1px solid ${hovered ? "var(--border-2)" : "var(--border)"}`,
          borderRadius: 14,
          display: "flex", flexDirection: "column",
          overflow: "hidden",
          transition: "border-color 0.2s, transform 0.2s, box-shadow 0.2s",
          transform: hovered ? "translateY(-2px)" : "translateY(0)",
          boxShadow: hovered ? "0 8px 32px rgba(0,0,0,0.35)" : "0 2px 8px rgba(0,0,0,0.15)",
        }}
      >
        {/* Image area — 16:9 */}
        <div style={{ height: 214, flexShrink: 0, position: "relative" }}>
          {p.images.length > 0 ? (
            <CardGallery
              images={p.images}
              fit={p.imgFit ?? "cover"}
              pos={p.imgPos ?? "center"}
              portrait={p.portrait}
              onOpen={i => setLightboxIdx(i)}
            />
          ) : (
            <div style={{
              width: "100%", height: "100%",
              display: "flex", alignItems: "center", justifyContent: "center",
              background: "#0f0f0f",
            }}>
              <span style={{ fontSize: "2.8rem", opacity: 0.3 }}>📁</span>
            </div>
          )}
        </div>

        {/* Content */}
        <div style={{ padding: "1.1rem 1.3rem 1.3rem", display: "flex", flexDirection: "column", flex: 1 }}>
          {p.hackathon && (
            <div style={{
              fontFamily: "var(--font-jetbrains), Consolas, monospace",
              fontSize: "0.62rem", color: "var(--accent)",
              letterSpacing: "0.04em", marginBottom: 7, lineHeight: 1.3,
            }}>{p.hackathon}</div>
          )}

          <div style={{ display: "flex", alignItems: "baseline", justifyContent: "space-between", gap: 8, marginBottom: 8 }}>
            <span style={{ fontWeight: 700, color: "var(--fg)", fontSize: "1rem", letterSpacing: "-0.01em" }}>{p.title}</span>
            <span style={{
              fontFamily: "var(--font-jetbrains), Consolas, monospace",
              fontSize: "0.62rem", color: "var(--fg-3)", flexShrink: 0,
            }}>{p.year}</span>
          </div>

          <p style={{ color: "var(--fg-3)", fontSize: "0.83rem", lineHeight: 1.7, flex: 1, marginBottom: 12 }}>
            {p.description}
          </p>

          {p.links && p.links.length > 0 && (
            <div style={{ display: "flex", flexWrap: "wrap", gap: 6, marginBottom: 12 }}>
              {p.links.map(link => (
                <a key={link.label} href={link.href} target="_blank" rel="noopener noreferrer"
                  style={{
                    fontFamily: "var(--font-jetbrains), Consolas, monospace",
                    fontSize: "0.63rem", letterSpacing: "0.04em",
                    color: "var(--accent)",
                    border: "1px solid rgba(168,184,122,0.3)",
                    background: "rgba(168,184,122,0.06)",
                    padding: "3px 9px", borderRadius: 5,
                    textDecoration: "none", transition: "background 0.15s, border-color 0.15s",
                  }}
                  onMouseEnter={e => {
                    (e.currentTarget as HTMLElement).style.background = "rgba(168,184,122,0.13)";
                    (e.currentTarget as HTMLElement).style.borderColor = "rgba(168,184,122,0.55)";
                  }}
                  onMouseLeave={e => {
                    (e.currentTarget as HTMLElement).style.background = "rgba(168,184,122,0.06)";
                    (e.currentTarget as HTMLElement).style.borderColor = "rgba(168,184,122,0.3)";
                  }}
                >{link.label} ↗</a>
              ))}
            </div>
          )}

          <div style={{ display: "flex", flexWrap: "wrap", gap: 5 }}>
            {p.tags.map(tag => (
              <span key={tag} className="chip">{tag}</span>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}

// ── Section ───────────────────────────────────────────────────────────────────

export default function Projects() {
  const { lang } = useLang();
  const t = i18n[lang].projects;

  const scrollRef = useRef<HTMLDivElement>(null);
  const [canLeft, setCanLeft] = useState(false);
  const [canRight, setCanRight] = useState(true);

  const scroll = (dir: "left" | "right") => {
    const el = scrollRef.current;
    if (!el) return;
    el.scrollBy({ left: dir === "right" ? 400 : -400, behavior: "smooth" });
  };

  const onScroll = () => {
    const el = scrollRef.current;
    if (!el) return;
    setCanLeft(el.scrollLeft > 8);
    setCanRight(el.scrollLeft + el.clientWidth < el.scrollWidth - 8);
  };

  const NavBtn = ({ dir }: { dir: "left" | "right" }) => {
    const active = dir === "left" ? canLeft : canRight;
    return (
      <button
        onClick={() => scroll(dir)}
        disabled={!active}
        aria-label={dir === "left" ? "Poprzedni" : "Następny"}
        style={{
          width: 34, height: 34, borderRadius: 9,
          border: `1px solid ${active ? "var(--border-2)" : "var(--border)"}`,
          background: active ? "var(--bg-3)" : "var(--bg-2)",
          color: active ? "var(--fg-2)" : "var(--fg-3)",
          opacity: active ? 1 : 0.45,
          cursor: active ? "pointer" : "default",
          display: "flex", alignItems: "center", justifyContent: "center",
          fontSize: "0.9rem", transition: "all 0.15s",
        }}
      >{dir === "left" ? "←" : "→"}</button>
    );
  };

  // Inject i18n descriptions into project data
  const localizedProjects = projects.map((p, i) => ({
    ...p,
    description: t.descriptions[i] ?? p.description,
  }));

  return (
    <section id="projects" className="py-20">
      <div className="max-w-5xl mx-auto px-6">
        {/* Header */}
        <div className="mb-12">
          <div className="mono-label mb-3">{t.label}</div>
          <div className="flex items-end justify-between gap-4 flex-wrap">
            <h2 className="font-bold" style={{ fontSize: "clamp(1.6rem, 4vw, 2.2rem)", color: "var(--fg)", letterSpacing: "-0.02em" }}>
              {t.title}
            </h2>
            <div style={{ display: "flex", gap: 6 }}>
              <NavBtn dir="left" />
              <NavBtn dir="right" />
            </div>
          </div>
        </div>

        {/* Carousel — negative margins break out of px-6 so cards start flush with text,
            scroll container has matching padding so first/last card have correct inset */}
        <div
          ref={scrollRef}
          onScroll={onScroll}
          style={{
            display: "flex", gap: 14,
            overflowX: "auto", scrollSnapType: "x mandatory",
            marginLeft: -24, marginRight: -24,
            paddingLeft: 24, paddingRight: 24,
            paddingBottom: 12, scrollbarWidth: "none",
          }}
        >
          {localizedProjects.map((p, i) => (
            <ProjectCard key={i} p={p} />
          ))}
        </div>
      </div>
    </section>
  );
}
