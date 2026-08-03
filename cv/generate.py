#!/usr/bin/env python3
"""Generuje CV (PL + EN) w HTML i PDF na podstawie treści portfolio.

Uzycie:  python3 cv/generate.py
Wynik:   cv/build/CV_Kacper_Kleczaj_PL.pdf  +  CV_Kacper_Kleczaj_EN.pdf

Zdjecie: wrzuc plik do cv/assets/photo.jpg (albo .png/.jpeg).
Jesli go nie ma, w naglowku pojawia sie inicjaly.
"""

import base64
import html
import mimetypes
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / "build"
ASSETS = ROOT / "assets"

CHROME_CANDIDATES = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
    shutil.which("chromium") or "",
    shutil.which("chromium-browser") or "",
    shutil.which("google-chrome") or "",
]

# --------------------------------------------------------------------------- #
#  DANE                                                                        #
# --------------------------------------------------------------------------- #

CONTACT = {
    "location": {"pl": "Łódź, Polska", "en": "Łódź, Poland"},
    "phone": "+48 690 827 655",
    "email": "kleczaj.kacper@gmail.com",
    "github": "github.com/kacperous",
    "linkedin": "linkedin.com/in/kacper-kleczaj-819622337",
    "site": "kacperous.github.io/portfolio",
}

PROFILE = {
    "pl": "Software Developer z 1,5-rocznym doświadczeniem komercyjnym w budowaniu aplikacji webowych "
          "i mobilnych — od architektury, przez implementację, po wdrożenie produkcyjne. Na co dzień pracuję "
          "w Pythonie (FastAPI, Django) oraz TypeScripcie (React, React Native, Next.js). Odpowiadałem za "
          "całościową architekturę systemu eCMR na AWS oraz wdrażałem architekturę AI/RAG w produkcyjnym CRM. "
          "Laureat 5 hackathonów (3× I miejsce, 2× II miejsce). Student Informatyki Stosowanej na Politechnice Łódzkiej.",
    "en": "Software Developer with 1.5 years of commercial experience building web and mobile applications — "
          "from architecture through implementation to production rollout. I work daily with Python (FastAPI, Django) "
          "and TypeScript (React, React Native, Next.js). I owned the end-to-end architecture of an AWS-hosted eCMR "
          "system and delivered an AI/RAG architecture inside a production CRM. Winner of 5 hackathons "
          "(3× 1st place, 2× 2nd place). Applied Computer Science student at Lodz University of Technology.",
}

EXPERIENCE = [
    {
        "role": "Software Developer",
        "company": "Digitay",
        "product": "digitay.pl",
        "period": {"pl": "Lipiec 2026 — obecnie", "en": "July 2026 — present"},
        "desc": {
            "pl": "Rozwój aplikacji webowych i mobilnych dla klientów Digitay — od discovery i architektury, "
                  "przez implementację, po wdrożenie produkcyjne. Główny produkt: Fluo — system do rejestracji "
                  "czasu pracy i zarządzania zespołem.",
            "en": "Building web and mobile applications for Digitay clients — from discovery and architecture "
                  "through implementation to production rollout. Flagship product: Fluo — a time tracking and "
                  "team management platform.",
        },
        "points": {
            "pl": [
                "Fluo: rejestracja czasu pracy, grafiki, urlopy i raportowanie kosztów projektów",
                "Aplikacja mobilna (React Native/Expo) z trybem offline i synchronizacją danych",
                "Panel webowy w Next.js + TypeScript oraz REST API na Node.js",
                "Integracje z systemami kadrowo-płacowymi, CI/CD i automatyczne wdrożenia",
            ],
            "en": [
                "Fluo: time tracking, schedules, leave requests and project cost reporting",
                "Mobile app (React Native/Expo) with offline mode and data synchronization",
                "Web panel in Next.js + TypeScript and a Node.js REST API",
                "Integrations with HR/payroll systems, CI/CD and automated deployments",
            ],
        },
        "tags": ["React Native", "Expo", "TypeScript", "Next.js", "Node.js", "REST API", "PostgreSQL", "CI/CD"],
    },
    {
        "role": "Software Developer",
        "company": "Norsys sp. z o.o.",
        "product": "greentransit.pl",
        "period": {"pl": "Grudzień 2025 — obecnie", "en": "December 2025 — present"},
        "desc": {
            "pl": "Pełna odpowiedzialność za architekturę i rozwój GreenTransit — systemu eCMR do elektronicznego "
                  "obiegu dokumentów transportowych. Platforma PWA na AWS, eliminuje papier w branży TSL.",
            "en": "Full ownership of GreenTransit architecture — an eCMR system for digital transport document flow. "
                  "AWS-hosted PWA eliminating paperwork in the TSL industry.",
        },
        "points": {
            "pl": [
                "Całościowa odpowiedzialność za architekturę i kod aplikacji",
                "Backend: FastAPI + Alembic (migracje) + PyTest (testy)",
                "Frontend: React + TypeScript",
                "Infrastruktura: AWS, offline PWA, integracje z TMS/WMS/ERP",
            ],
            "en": [
                "End-to-end ownership of application architecture and code",
                "Backend: FastAPI + Alembic (migrations) + PyTest (testing)",
                "Frontend: React + TypeScript",
                "Infrastructure: AWS, offline PWA, TMS/WMS/ERP integrations",
            ],
        },
        "tags": ["FastAPI", "Python", "Alembic", "PyTest", "React", "TypeScript", "PostgreSQL", "AWS", "PWA"],
    },
    {
        "role": {"pl": "Junior Python Developer", "en": "Junior Python Developer"},
        "company": "Gaius-Lex",
        "product": "gaius-lex.pl",
        "period": {"pl": "Wrzesień 2025 — Maj 2026", "en": "September 2025 — May 2026"},
        "desc": {
            "pl": "Projektowanie systemów do automatycznego zbierania i przetwarzania danych z różnych źródeł internetowych.",
            "en": "Designing systems for automated collection and processing of data from various online sources.",
        },
        "points": {
            "pl": [
                "Narzędzia web scrapingowe do pozyskiwania dokumentów publicznych",
                "Walidacja i standaryzacja danych",
                "Optymalizacja przetwarzania dużych wolumenów",
            ],
            "en": [
                "Web scraping tools for public document retrieval",
                "Data validation and standardization",
                "Optimization for large-volume data processing",
            ],
        },
        "tags": ["Python", "FastAPI", "Web Scraping", "PostgreSQL", "Docker"],
    },
    {
        "role": {"pl": "Fullstack Developer", "en": "Fullstack Developer"},
        "company": "QuickPick",
        "product": "quickpick.pl",
        "period": {"pl": "Maj 2025 — Marzec 2026", "en": "May 2025 — March 2026"},
        "desc": {
            "pl": "Tworzenie aplikacji webowych i sklepów internetowych. Pełna odpowiedzialność za wdrożenie "
                  "od analizy po utrzymanie.",
            "en": "Building web applications and e-commerce stores. Full ownership from analysis to maintenance.",
        },
        "points": {
            "pl": [
                "Aplikacje webowe: Django + React/TypeScript",
                "Sklepy: WordPress/WooCommerce",
            ],
            "en": [
                "Web apps: Django + React/TypeScript",
                "Stores: WordPress/WooCommerce",
            ],
        },
        "tags": ["Django", "React", "TypeScript", "WordPress", "WooCommerce"],
    },
    {
        "role": {"pl": "Junior Fullstack Developer", "en": "Junior Fullstack Developer"},
        "company": "GD SOFT",
        "product": "gdsoft.info",
        "period": {"pl": "Luty — Maj 2025", "en": "February — May 2025"},
        "desc": {
            "pl": "Aplikacje webowe w Spring Boot + React. Praca zespołowa w metodyce Agile/Scrum.",
            "en": "Web applications with Spring Boot + React. Team collaboration in Agile/Scrum.",
        },
        "points": {
            "pl": ["Projektowanie backendu i frontendu", "Optymalizacja kodu i baz danych"],
            "en": ["Backend and frontend design", "Code and database optimization"],
        },
        "tags": ["Spring Boot", "Java", "React", "Hibernate", "MySQL"],
    },
]

PROJECTS = [
    {
        "title": "DosFit",
        "year": "2025",
        "note": {"pl": "App Store · Google Play · dosfit.pl", "en": "App Store · Google Play · dosfit.pl"},
        "desc": {
            "pl": 'Aplikacja mobilna do zmiany nawyków żywieniowych („12 miesięcy, 12 nawyków"). '
                  "Licznik kalorii AI z analizą zdjęć, grywalizacja i moduł rodzic-dziecko. Wydana w obu sklepach.",
            "en": 'Mobile habit-changing nutrition app ("12 months, 12 habits"). AI calorie counter with photo '
                  "analysis, gamification and a parent-child module. Shipped to both app stores.",
        },
        "tags": ["React Native", "Expo", "Python", "AI"],
    },
    {
        "title": "HRK CRM",
        "year": "2026",
        "note": {"pl": "HRK Payroll Consulting", "en": "HRK Payroll Consulting"},
        "desc": {
            "pl": "System CRM automatyzujący cykl życia kontraktów, waloryzację stawek i raportowanie KPI. "
                  "Wdrożyłem od podstaw architekturę AI/RAG (Bielik 4.5B v3.0, pgvector, Ollama) do semantycznej "
                  "analizy treści umów.",
            "en": "CRM automating contract lifecycles, rate indexation and KPI reporting. I built the entire "
                  "AI/RAG architecture (Bielik 4.5B v3.0, pgvector, Ollama) from scratch for semantic contract analysis.",
        },
        "tags": ["FastAPI", "React", "AI / RAG", "pgvector", "Docker"],
    },
    {
        "title": "AI Content Agent",
        "year": "2026",
        "note": {"pl": "🥇 I miejsce — Blazity Hackathon", "en": "🥇 1st place — Blazity Hackathon"},
        "desc": {
            "pl": "Agent AI generujący spersonalizowane posty i wideo na podstawie historii profilu użytkownika. "
                  "Dopasowuje treść do trendów, montuje wideo i publikuje na Facebooku oraz Instagramie (Reels) przez Meta API.",
            "en": "AI agent generating personalized posts and videos from user profile history. Adapts content to "
                  "trends, edits video and publishes to Facebook and Instagram Reels via the Meta API.",
        },
        "tags": ["Next.js", "Python", "AI Agent", "Meta API"],
    },
    {
        "title": "Fin-Insight",
        "year": "2025–2026",
        "note": None,
        "desc": {
            "pl": "Aplikacja do zarządzania portfelem inwestycyjnym z analizą rynkową i rekomendacjami AI. "
                  "Moduł AI Advisor z integracją LLM, bezpieczeństwo OAuth2/OIDC (Keycloak), architektura mikroserwisowa.",
            "en": "Investment portfolio management app with market analysis and AI recommendations. AI Advisor module "
                  "powered by LLMs, OAuth2/OIDC security (Keycloak), microservice architecture.",
        },
        "tags": ["Spring Boot", "React", "Spring Cloud", "Keycloak", "Docker"],
    },
    {
        "title": "Splitly",
        "year": "2025",
        "note": None,
        "desc": {
            "pl": "Mobilna aplikacja do zarządzania wspólnymi wydatkami — automatyczne rozliczanie długów, "
                  "raporty wydatków i synchronizacja w czasie rzeczywistym.",
            "en": "Mobile app for shared expenses — automatic debt settlement, spending reports and real-time sync.",
        },
        "tags": ["React Native", "TypeScript", "Firebase"],
    },
    {
        "title": "DPF Hunter",
        "year": "2025",
        "note": {"pl": "🥈 II miejsce — BestHackingLeague", "en": "🥈 2nd place — BestHackingLeague"},
        "desc": {
            "pl": "System AI wykrywający pojazdy z usuniętym filtrem DPF na podstawie obrazu z kamer miejskich. "
                  "Integracja z CEPiK do automatycznego raportowania naruszeń.",
            "en": "AI system detecting vehicles with removed DPF filters from city camera feeds. CEPiK integration "
                  "for automatic violation reporting.",
        },
        "tags": ["Python", "Computer Vision", "FastAPI", "CEPiK API"],
    },
]

HACKATHONS = [
    {"place": {"pl": "I miejsce", "en": "1st place"}, "first": True,
     "event": "Blazity Hackathon: AI for Content", "date": {"pl": "Czerwiec 2026", "en": "June 2026"},
     "project": "AI Content Agent", "team": "GitPushers"},
    {"place": {"pl": "I miejsce", "en": "1st place"}, "first": True,
     "event": "Fintech Łódź_Hack", "date": {"pl": "Grudzień 2025", "en": "December 2025"},
     "project": "Moje Osiedle", "team": "GitPushers"},
    {"place": {"pl": "I miejsce", "en": "1st place"}, "first": True,
     "event": "Hack na Zdrowie 4 — UMED Łódź", "date": {"pl": "Kwiecień–Maj 2025", "en": "April–May 2025"},
     "project": "Kids Health App", "team": "Alfiarze"},
    {"place": {"pl": "II miejsce", "en": "2nd place"}, "first": False,
     "event": "BestHackingLeague — BEST", "date": {"pl": "Listopad 2025", "en": "November 2025"},
     "project": "DPF Hunter", "team": "Alfa Guys"},
    {"place": {"pl": "II miejsce", "en": "2nd place"}, "first": False,
     "event": "Hack&Play — PLAY", "date": {"pl": "Październik 2025", "en": "October 2025"},
     "project": "PharmaRadar", "team": "GitPushers"},
]

SKILLS = [
    {"label": {"pl": "Frontend", "en": "Frontend"},
     "items": ["React", "React Native", "TypeScript", "JavaScript", "Next.js", "Tailwind CSS", "Redux", "PWA"]},
    {"label": {"pl": "Backend", "en": "Backend"},
     "items": ["Python", "FastAPI", "Django", "Spring Boot", "Java", "Node.js", "Express.js", "REST API", "WebSockets"]},
    {"label": {"pl": "Bazy danych", "en": "Databases"},
     "items": ["PostgreSQL", "MySQL", "SQL Server", "Alembic", "Hibernate", "MongoDB", "Redis"]},
    {"label": {"pl": "DevOps i infrastruktura", "en": "DevOps & Infrastructure"},
     "items": ["Docker", "AWS", "Azure", "CI/CD", "Git", "GitHub Actions", "Grafana", "Prometheus"]},
    {"label": {"pl": "Testy i narzędzia AI", "en": "Testing & AI Tools"},
     "items": ["PyTest", "Unit Testing", "Integration Testing", "GitHub Copilot", "Cursor", "Claude Code"]},
    {"label": {"pl": "Automatyzacja i CMS", "en": "Automation & CMS"},
     "items": ["WordPress", "WooCommerce", "N8N"]},
]

EDUCATION = [
    {"degree": {"pl": "Informatyka Stosowana — studia inżynierskie", "en": "Applied Computer Science — engineering degree"},
     "school": {"pl": "Politechnika Łódzka", "en": "Lodz University of Technology"},
     "period": {"pl": "2023 — obecnie", "en": "2023 — present"}, "note": None},
    {"degree": {"pl": "Technik Informatyk — technikum", "en": "IT Technician — technical high school"},
     "school": {"pl": "ZST im. Armii Krajowej", "en": "ZST im. Armii Krajowej"},
     "period": {"pl": "2019 — 2023", "en": "2019 — 2023"},
     "note": {"pl": "Biało-czerwony pasek (wyróżnienie)", "en": "Graduated with honors"}},
]

CERTS = [
    {"title": "Eskadra Bielika", "year": "2026",
     "issuer": "Bielik.ai · SpeakLeash · Google for Developers",
     "sub": {"pl": "Warsztaty: Od modelu do systemu — Bielik w architekturach RAG",
             "en": "Workshops: From model to system — Bielik in RAG architectures"}},
    {"title": "INF.02", "year": "2023", "issuer": "ZST im. Armii Krajowej",
     "sub": {"pl": "Projektowanie stron oraz aplikacji internetowych", "en": "Web & application design"}},
    {"title": "INF.03", "year": "2023", "issuer": "ZST im. Armii Krajowej",
     "sub": {"pl": "Zarządzanie i integracja baz danych, sieci komputerowe",
             "en": "Database management & integration, computer networks"}},
    {"title": {"pl": "Marketing w e-commerce", "en": "E-commerce Marketing"}, "year": "2024",
     "issuer": {"pl": "Santander / Politechnika Łódzka", "en": "Santander / Lodz University of Technology"},
     "sub": {"pl": "Strategie, budowanie marki, kampanie — Paweł Tkaczyk",
             "en": "Strategy, brand building, campaigns — Paweł Tkaczyk"}},
    {"title": {"pl": "Praktyki zagraniczne", "en": "Foreign Internship"}, "year": "2021",
     "issuer": "ENSO GROUP LTD, Ateny / Athens",
     "sub": {"pl": "Uruchamianie sklepu internetowego, podstawy robotyki",
             "en": "E-commerce store setup, robotics basics"}},
]

LANGUAGES = [
    {"name": {"pl": "Polski", "en": "Polish"}, "level": {"pl": "ojczysty", "en": "native"}, "pct": 100},
    {"name": {"pl": "Angielski", "en": "English"}, "level": {"pl": "B2", "en": "B2"}, "pct": 70},
    {"name": {"pl": "Niemiecki", "en": "German"}, "level": {"pl": "A2", "en": "A2"}, "pct": 25},
]

UI = {
    "pl": {
        "title": "Software Developer · Web & Mobile",
        "profile": "Profil",
        "experience": "Doświadczenie zawodowe",
        "projects": "Wybrane projekty",
        "hackathons": "Hackathony",
        "skills": "Technologie",
        "education": "Wykształcenie",
        "certs": "Certyfikaty i kursy",
        "languages": "Języki",
        "team": "zespół",
        "rodo": "Wyrażam zgodę na przetwarzanie moich danych osobowych zawartych w niniejszym dokumencie "
                "przez potencjalnych pracodawców na potrzeby przeprowadzenia procesu rekrutacji, zgodnie z "
                "Rozporządzeniem Parlamentu Europejskiego i Rady (UE) 2016/679 (RODO).",
        "stats": [("5", "hackathonów '25–'26"), ("3×", "I miejsce"), ("1,5", "roku doświadczenia")],
    },
    "en": {
        "title": "Software Developer · Web & Mobile",
        "profile": "Profile",
        "experience": "Professional experience",
        "projects": "Selected projects",
        "hackathons": "Hackathons",
        "skills": "Technologies",
        "education": "Education",
        "certs": "Certifications & courses",
        "languages": "Languages",
        "team": "team",
        "rodo": None,
        "stats": [("5", "hackathons '25–'26"), ("3×", "1st place"), ("1.5", "years of experience")],
    },
}

# --------------------------------------------------------------------------- #
#  RENDER                                                                      #
# --------------------------------------------------------------------------- #

CSS = """
@page { size: A4; margin: 11mm 0 11mm 0; }

* { box-sizing: border-box; margin: 0; padding: 0; }

html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }

body {
  font-family: "Liberation Sans", "DejaVu Sans", Arial, sans-serif;
  font-size: 8.6pt;
  line-height: 1.38;
  color: #23211d;
  background: #fff;
}

.page { width: 190mm; margin: 0 auto; padding: 0 2mm; }

.mono { font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; }

/* ---------- header ---------- */
.header {
  display: flex; align-items: center; gap: 14px;
  background: #1a1916; color: #f0ece6;
  padding: 11px 15px; border-radius: 6px; margin-bottom: 11px;
}
.photo {
  width: 74px; height: 74px; border-radius: 50%; flex-shrink: 0;
  object-fit: cover; object-position: center 22%;
  border: 2px solid #a8b87a; background: #2a2825;
}
.monogram {
  width: 74px; height: 74px; border-radius: 50%; flex-shrink: 0;
  border: 2px solid #a8b87a; background: #2a2825; color: #a8b87a;
  display: flex; align-items: center; justify-content: center;
  font-size: 24pt; font-weight: 700; letter-spacing: -0.02em;
}
.h-main { flex: 1; min-width: 0; }
.name { font-size: 25pt; font-weight: 700; letter-spacing: -0.025em; line-height: 1; margin-bottom: 4px; }
.role { font-size: 8.4pt; letter-spacing: 0.09em; text-transform: uppercase; color: #a8b87a; margin-bottom: 8px; }
.contacts { display: flex; flex-wrap: wrap; gap: 3px 12px; font-size: 7.8pt; color: #b9b3aa; }
.contacts span { white-space: nowrap; }
.contacts b { color: #f0ece6; font-weight: 400; }
.h-stats { display: flex; gap: 14px; flex-shrink: 0; padding-left: 14px; border-left: 1px solid rgba(255,255,255,0.12); }
.h-stat { text-align: center; }
.h-stat .n { font-size: 14pt; font-weight: 700; color: #f0ece6; line-height: 1.1; }
.h-stat .l { font-size: 6.2pt; letter-spacing: 0.05em; text-transform: uppercase; color: #8a847c; max-width: 62px; }

/* ---------- sections ---------- */
.section { margin-bottom: 8px; }
.section-title {
  font-size: 7.7pt; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase;
  color: #5f6e38; padding-bottom: 2.5px; margin-bottom: 6px;
  border-bottom: 1.4px solid #a8b87a;
  page-break-after: avoid; break-after: avoid-page;
}
.profile-text { text-align: justify; color: #3a3731; }

/* ---------- experience ---------- */
.job { margin-bottom: 7px; page-break-inside: avoid; }
.job:last-child { margin-bottom: 0; }
.job-head { display: flex; justify-content: space-between; align-items: baseline; gap: 10px; }
.job-role { font-size: 9.6pt; font-weight: 700; color: #1a1916; }
.job-period { font-size: 7.6pt; color: #6a6660; white-space: nowrap; }
.job-company { font-size: 8.2pt; color: #4a463f; margin-bottom: 2px; }
.job-company .prod { color: #5f6e38; }
.job-desc { color: #3a3731; margin-bottom: 3px; }
ul.points { list-style: none; margin-bottom: 4px; }
ul.points li { padding-left: 10px; position: relative; color: #4a463f; }
ul.points li::before {
  content: "▸"; position: absolute; left: 0; top: 0;
  color: #a8b87a; font-size: 6.5pt; line-height: 1.9;
}
.tags { display: flex; flex-wrap: wrap; gap: 3px; }
.tag {
  font-size: 6.9pt; padding: 1px 5px; border-radius: 3px;
  background: #f1f2e9; border: 1px solid #dfe2cd; color: #4a5530; white-space: nowrap;
}

/* ---------- projects ---------- */
.proj-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 6px 12px; }
.proj { page-break-inside: avoid; }
.proj-head { display: flex; justify-content: space-between; align-items: baseline; gap: 6px; }
.proj-title { font-size: 9.2pt; font-weight: 700; color: #1a1916; }
.proj-year { font-size: 7.2pt; color: #6a6660; }
.proj-note { font-size: 7.4pt; color: #5f6e38; margin-bottom: 2px; }
.proj-desc { font-size: 8.4pt; color: #4a463f; margin-bottom: 3px; }

/* ---------- hackathons ---------- */
.hack { display: flex; align-items: baseline; gap: 8px; padding: 2px 0; page-break-inside: avoid; }
.hack + .hack { border-top: 1px solid #ececE6; }
.medal { width: 13px; flex-shrink: 0; font-size: 8.5pt; }
.hack-place { width: 62px; flex-shrink: 0; font-size: 7.8pt; font-weight: 700; color: #5f6e38; }
.hack-event { flex: 1; font-size: 8.6pt; color: #23211d; }
.hack-proj { font-size: 7.8pt; color: #6a6660; }
.hack-date { width: 82px; flex-shrink: 0; text-align: right; font-size: 7.4pt; color: #6a6660; }

/* ---------- skills ---------- */
.skill-row { display: flex; gap: 9px; align-items: flex-start; padding: 2.5px 0; page-break-inside: avoid; }
.skill-row + .skill-row { border-top: 1px solid #ececE6; }
.skill-label {
  width: 108px; flex-shrink: 0; font-size: 7.2pt; letter-spacing: 0.07em;
  text-transform: uppercase; color: #6a6660; padding-top: 2px;
}
.skill-items { flex: 1; display: flex; flex-wrap: wrap; gap: 3px; }

/* ---------- bottom grid ---------- */
.cols { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; page-break-inside: avoid; }
.edu { margin-bottom: 5px; page-break-inside: avoid; }
.edu-degree { font-size: 8.8pt; font-weight: 700; color: #1a1916; }
.edu-meta { font-size: 8pt; color: #4a463f; }
.edu-period { font-size: 7.4pt; color: #6a6660; }
.edu-note { font-size: 7.4pt; color: #5f6e38; }
.cert { margin-bottom: 4px; page-break-inside: avoid; }
.cert-head { display: flex; justify-content: space-between; gap: 6px; align-items: baseline; }
.cert-title { font-size: 8.5pt; font-weight: 700; color: #1a1916; }
.cert-year { font-size: 7.2pt; color: #6a6660; }
.cert-sub { font-size: 7.6pt; color: #4a463f; line-height: 1.35; }
.cert-issuer { font-size: 7.2pt; color: #6a6660; }

/* ---------- languages ---------- */
.langs { display: flex; gap: 16px; }
.lang { flex: 1; }
.lang-head { display: flex; justify-content: space-between; align-items: baseline; font-size: 8.2pt; margin-bottom: 2px; }
.lang-name { font-weight: 700; color: #1a1916; }
.lang-level { font-size: 7.4pt; color: #6a6660; }
.bar { height: 3px; background: #ececE6; border-radius: 2px; overflow: hidden; }
.bar > i { display: block; height: 100%; background: #a8b87a; }

/* ---------- footer ---------- */
.rodo {
  margin-top: 10px; padding-top: 6px; border-top: 1px solid #ececE6;
  font-size: 6.6pt; line-height: 1.4; color: #8a847c; text-align: justify;
}
"""


def esc(v):
    return html.escape(str(v))


def pick(value, lang):
    """Zwraca wariant jezykowy albo wartosc wspolna."""
    if isinstance(value, dict) and ("pl" in value or "en" in value):
        return value.get(lang, value.get("pl"))
    return value


def find_photo():
    if not ASSETS.is_dir():
        return None
    for ext in ("jpg", "jpeg", "png", "webp"):
        for path in sorted(ASSETS.glob(f"photo.{ext}")):
            return path
    return None


def photo_html():
    path = find_photo()
    if path is None:
        return '<div class="monogram">KK</div>'
    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f'<img class="photo" src="data:{mime};base64,{data}" alt="Kacper Kleczaj">'


def tags_html(tags):
    return '<div class="tags">' + "".join(f'<span class="tag">{esc(t)}</span>' for t in tags) + "</div>"


def render(lang):
    ui = UI[lang]
    out = []
    a = out.append

    # header
    stats = "".join(
        f'<div class="h-stat"><div class="n">{esc(n)}</div><div class="l">{esc(l)}</div></div>'
        for n, l in ui["stats"]
    )
    contacts = [
        pick(CONTACT["location"], lang),
        CONTACT["phone"],
        CONTACT["email"],
        CONTACT["github"],
        CONTACT["linkedin"],
        CONTACT["site"],
    ]
    a(f'''<div class="header">
  {photo_html()}
  <div class="h-main">
    <div class="name">Kacper Kleczaj</div>
    <div class="role mono">{esc(ui["title"])}</div>
    <div class="contacts mono">{"".join(f"<span><b>{esc(c)}</b></span>" for c in contacts)}</div>
  </div>
  <div class="h-stats">{stats}</div>
</div>''')

    # profil
    a(f'''<div class="section">
  <div class="section-title">{esc(ui["profile"])}</div>
  <p class="profile-text">{esc(PROFILE[lang])}</p>
</div>''')

    # doswiadczenie
    jobs = []
    for job in EXPERIENCE:
        points = "".join(f"<li>{esc(p)}</li>" for p in pick(job["points"], lang))
        jobs.append(f'''<div class="job">
  <div class="job-head">
    <div class="job-role">{esc(pick(job["role"], lang))}</div>
    <div class="job-period mono">{esc(pick(job["period"], lang))}</div>
  </div>
  <div class="job-company">{esc(job["company"])} <span class="prod mono">· {esc(job["product"])}</span></div>
  <div class="job-desc">{esc(pick(job["desc"], lang))}</div>
  <ul class="points">{points}</ul>
  {tags_html(job["tags"])}
</div>''')
    a(f'''<div class="section">
  <div class="section-title">{esc(ui["experience"])}</div>
  {"".join(jobs)}
</div>''')

    # projekty
    projs = []
    for p in PROJECTS:
        note = pick(p["note"], lang)
        note_html = f'<div class="proj-note">{esc(note)}</div>' if note else ""
        projs.append(f'''<div class="proj">
  <div class="proj-head">
    <div class="proj-title">{esc(p["title"])}</div>
    <div class="proj-year mono">{esc(p["year"])}</div>
  </div>
  {note_html}
  <div class="proj-desc">{esc(pick(p["desc"], lang))}</div>
  {tags_html(p["tags"])}
</div>''')
    a(f'''<div class="section">
  <div class="section-title">{esc(ui["projects"])}</div>
  <div class="proj-grid">{"".join(projs)}</div>
</div>''')

    # hackathony
    hacks = []
    for h in HACKATHONS:
        hacks.append(f'''<div class="hack">
  <div class="medal">{"🥇" if h["first"] else "🥈"}</div>
  <div class="hack-place">{esc(pick(h["place"], lang))}</div>
  <div class="hack-event">{esc(h["event"])}
    <span class="hack-proj mono">· {esc(h["project"])} · {esc(ui["team"])}: {esc(h["team"])}</span>
  </div>
  <div class="hack-date mono">{esc(pick(h["date"], lang))}</div>
</div>''')
    a(f'''<div class="section">
  <div class="section-title">{esc(ui["hackathons"])}</div>
  {"".join(hacks)}
</div>''')

    # technologie
    rows = []
    for cat in SKILLS:
        items = "".join(f'<span class="tag">{esc(s)}</span>' for s in cat["items"])
        rows.append(f'''<div class="skill-row">
  <div class="skill-label mono">{esc(pick(cat["label"], lang))}</div>
  <div class="skill-items">{items}</div>
</div>''')
    a(f'''<div class="section">
  <div class="section-title">{esc(ui["skills"])}</div>
  {"".join(rows)}
</div>''')

    # edukacja + certyfikaty
    edus = []
    for e in EDUCATION:
        note = pick(e["note"], lang)
        note_html = f'<div class="edu-note">{esc(note)}</div>' if note else ""
        edus.append(f'''<div class="edu">
  <div class="edu-degree">{esc(pick(e["degree"], lang))}</div>
  <div class="edu-meta">{esc(pick(e["school"], lang))}</div>
  <div class="edu-period mono">{esc(pick(e["period"], lang))}</div>
  {note_html}
</div>''')

    certs = []
    for c in CERTS:
        certs.append(f'''<div class="cert">
  <div class="cert-head">
    <div class="cert-title">{esc(pick(c["title"], lang))}</div>
    <div class="cert-year mono">{esc(c["year"])}</div>
  </div>
  <div class="cert-sub">{esc(pick(c["sub"], lang))}</div>
  <div class="cert-issuer mono">{esc(pick(c["issuer"], lang))}</div>
</div>''')

    langs = []
    for l in LANGUAGES:
        langs.append(f'''<div class="lang">
  <div class="lang-head">
    <span class="lang-name">{esc(pick(l["name"], lang))}</span>
    <span class="lang-level mono">{esc(pick(l["level"], lang))}</span>
  </div>
  <div class="bar"><i style="width:{l["pct"]}%"></i></div>
</div>''')

    a(f'''<div class="cols">
  <div>
    <div class="section">
      <div class="section-title">{esc(ui["education"])}</div>
      {"".join(edus)}
    </div>
    <div class="section">
      <div class="section-title">{esc(ui["languages"])}</div>
      <div class="langs">{"".join(langs)}</div>
    </div>
  </div>
  <div class="section">
    <div class="section-title">{esc(ui["certs"])}</div>
    {"".join(certs)}
  </div>
</div>''')

    if ui["rodo"]:
        a(f'<div class="rodo">{esc(ui["rodo"])}</div>')

    title = "CV — Kacper Kleczaj"
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body><div class="page">
{"".join(out)}
</div></body>
</html>'''


def to_pdf(html_path: Path, pdf_path: Path):
    chrome = next((c for c in CHROME_CANDIDATES if c and Path(c).exists()), None)
    if chrome is None:
        print("!! nie znaleziono Chromium — pomijam PDF", file=sys.stderr)
        return False
    subprocess.run(
        [
            chrome, "--headless", "--disable-gpu", "--no-sandbox",
            "--no-pdf-header-footer", "--generate-pdf-document-outline=false",
            f"--print-to-pdf={pdf_path}", html_path.as_uri(),
        ],
        check=True,
        capture_output=True,
    )
    return pdf_path.exists()


def main():
    BUILD.mkdir(parents=True, exist_ok=True)
    photo = find_photo()
    print(f"zdjęcie: {photo.name if photo else 'BRAK (użyto inicjałów) — wrzuć cv/assets/photo.jpg'}")

    for lang, suffix in (("pl", "PL"), ("en", "EN")):
        html_path = BUILD / f"CV_Kacper_Kleczaj_{suffix}.html"
        pdf_path = BUILD / f"CV_Kacper_Kleczaj_{suffix}.pdf"
        html_path.write_text(render(lang), encoding="utf-8")
        ok = to_pdf(html_path, pdf_path)
        size = f"{pdf_path.stat().st_size // 1024} KB" if ok else "—"
        print(f"  {html_path.name}  ->  {pdf_path.name} ({size})")


if __name__ == "__main__":
    main()
