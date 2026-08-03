#!/usr/bin/env python3
"""Generuje CV (PL + EN) na podstawie tresci portfolio.

Uzycie:  python3 cv/generate.py
Wynik:   cv/build/CV_Kacper_Kleczaj_PL.pdf  +  CV_Kacper_Kleczaj_EN.pdf
         cv/build/CV_Kacper_Kleczaj_PL.docs.html  (wersja pod Google Docs)

Zdjecie: wrzuc plik do cv/assets/photo.jpg (albo .png/.jpeg) i odpal skrypt.
Bez pliku w naglowku pojawiaja sie inicjaly.
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
    "location": {"pl": "Łódź", "en": "Łódź, Poland"},
    "phone": "+48 690 827 655",
    "email": "kleczaj.kacper@gmail.com",
    "github": "github.com/kacperous",
    "linkedin": "linkedin.com/in/kacper-kleczaj-819622337",
    "site": "kacperous.github.io/portfolio",
}

PROFILE = {
    "pl": "Software Developer z 1,5 roku doświadczenia komercyjnego. Buduję aplikacje webowe i mobilne "
          "w Pythonie (FastAPI, Django) oraz TypeScripcie (React, React Native, Next.js). Odpowiadam za "
          "architekturę systemu eCMR na AWS. Laureat 5 hackathonów, w tym 3 pierwsze miejsca.",
    "en": "Software Developer with 1.5 years of commercial experience. I build web and mobile applications "
          "in Python (FastAPI, Django) and TypeScript (React, React Native, Next.js). I own the architecture "
          "of an AWS hosted eCMR system. Winner of 5 hackathons, including 3 first places.",
}

EXPERIENCE = [
    {
        "role": "Software Developer",
        "company": "Digitay",
        "site": "digitay.pl",
        "period": {"pl": "od 07.2026", "en": "since 07.2026"},
        "desc": {
            "pl": "Aplikacje webowe i mobilne dla klientów Digitay, od architektury po wdrożenie produkcyjne. "
                  "Główny produkt: Fluo, system do rejestracji czasu pracy i zarządzania zespołem.",
            "en": "Web and mobile applications for Digitay clients, from architecture to production rollout. "
                  "Flagship product: Fluo, a time tracking and team management platform.",
        },
        "points": {
            "pl": [
                "Fluo: rejestracja czasu pracy, grafiki, urlopy i raporty kosztów projektów",
                "Aplikacja mobilna w React Native/Expo z trybem offline, panel webowy w Next.js i API na Node.js",
            ],
            "en": [
                "Fluo: time tracking, schedules, leave requests and project cost reports",
                "React Native/Expo mobile app with offline mode, Next.js web panel and a Node.js API",
            ],
        },
    },
    {
        "role": "Software Developer",
        "company": "Norsys sp. z o.o.",
        "site": "greentransit.pl",
        "period": {"pl": "od 12.2025", "en": "since 12.2025"},
        "desc": {
            "pl": "Architektura i rozwój GreenTransit, systemu eCMR do elektronicznego obiegu dokumentów "
                  "transportowych. Platforma PWA na AWS eliminująca papier w branży TSL.",
            "en": "Architecture and development of GreenTransit, an eCMR system for digital transport document "
                  "flow. An AWS hosted PWA that removes paperwork from the TSL industry.",
        },
        "points": {
            "pl": [
                "Backend w FastAPI z Alembic i PyTest, frontend w React i TypeScript",
                "Infrastruktura AWS, tryb offline PWA, integracje z systemami TMS, WMS i ERP",
            ],
            "en": [
                "FastAPI backend with Alembic and PyTest, React and TypeScript frontend",
                "AWS infrastructure, offline PWA mode, integrations with TMS, WMS and ERP systems",
            ],
        },
    },
    {
        "role": "Junior Python Developer",
        "company": "Gaius-Lex",
        "site": "gaius-lex.pl",
        "period": {"pl": "09.2025 do 05.2026", "en": "09.2025 to 05.2026"},
        "desc": {
            "pl": "Systemy do automatycznego zbierania i przetwarzania danych z serwisów publicznych.",
            "en": "Systems for automated collection and processing of data from public online sources.",
        },
        "points": {
            "pl": [
                "Narzędzia web scrapingowe, walidacja i standaryzacja pozyskanych dokumentów",
                "Optymalizacja przetwarzania dużych wolumenów danych",
            ],
            "en": [
                "Web scraping tools, validation and standardization of retrieved documents",
                "Optimization of large volume data processing",
            ],
        },
    },
]

PROJECTS = [
    {
        "title": "DosFit",
        "meta": {"pl": "App Store, Google Play", "en": "App Store, Google Play"},
        "desc": {
            "pl": "Aplikacja mobilna do zmiany nawyków żywieniowych. Licznik kalorii AI z analizą zdjęć, "
                  "grywalizacja i moduł rodzic-dziecko.",
            "en": "Mobile app for changing eating habits. AI calorie counter with photo analysis, gamification "
                  "and a parent-child module.",
        },
    },
    {
        "title": "HRK CRM",
        "meta": {"pl": "HRK Payroll Consulting", "en": "HRK Payroll Consulting"},
        "desc": {
            "pl": "CRM automatyzujący cykl życia umów i waloryzację stawek. Zbudowałem architekturę AI/RAG "
                  "(Bielik 4.5B, pgvector) do analizy treści umów.",
            "en": "CRM automating contract lifecycles and rate indexation. I built the AI/RAG architecture "
                  "(Bielik 4.5B, pgvector) for contract analysis.",
        },
    },
    {
        "title": "AI Content Agent",
        "meta": {"pl": "I miejsce, Blazity Hackathon", "en": "1st place, Blazity Hackathon"},
        "desc": {
            "pl": "Agent generujący spersonalizowane posty i wideo, montuje materiał i publikuje na Facebooku "
                  "oraz Instagramie przez Meta API.",
            "en": "Agent generating personalized posts and videos, editing the material and publishing to "
                  "Facebook and Instagram through the Meta API.",
        },
    },
    {
        "title": "Fin-Insight",
        "meta": {"pl": "projekt zespołowy", "en": "team project"},
        "desc": {
            "pl": "Zarządzanie portfelem inwestycyjnym z analizą rynkową, modułem AI Advisor opartym na LLM "
                  "i logowaniem OAuth2/OIDC w Keycloak.",
            "en": "Investment portfolio management with market analysis, an LLM based AI Advisor module and "
                  "OAuth2/OIDC login through Keycloak.",
        },
    },
]

HACKATHONS = [
    {"place": {"pl": "I miejsce", "en": "1st place"}, "first": True, "event": "Blazity Hackathon: AI for Content",
     "date": "06.2026", "project": "AI Content Agent"},
    {"place": {"pl": "I miejsce", "en": "1st place"}, "first": True, "event": "Fintech Łódź_Hack",
     "date": "12.2025", "project": "Moje Osiedle"},
    {"place": {"pl": "I miejsce", "en": "1st place"}, "first": True, "event": "Hack na Zdrowie 4, UMED Łódź",
     "date": "05.2025", "project": "Kids Health App"},
    {"place": {"pl": "II miejsce", "en": "2nd place"}, "first": False, "event": "BestHackingLeague, BEST",
     "date": "11.2025", "project": "DPF Hunter"},
    {"place": {"pl": "II miejsce", "en": "2nd place"}, "first": False, "event": "Hack&Play, PLAY",
     "date": "10.2025", "project": "PharmaRadar"},
]

SKILLS = [
    {"label": {"pl": "Frontend", "en": "Frontend"},
     "items": ["React", "React Native", "TypeScript", "Next.js", "Tailwind CSS", "PWA"]},
    {"label": {"pl": "Backend", "en": "Backend"},
     "items": ["Python", "FastAPI", "Django", "Node.js", "Java", "Spring Boot", "REST API"]},
    {"label": {"pl": "Dane i infrastruktura", "en": "Data and infrastructure"},
     "items": ["PostgreSQL", "MySQL", "MongoDB", "Redis", "Docker", "AWS", "CI/CD", "Git"]},
    {"label": {"pl": "Testy, AI i narzędzia", "en": "Testing, AI and tools"},
     "items": ["PyTest", "RAG", "pgvector", "GitHub Copilot", "Cursor"]},
]

EDUCATION = [
    {"degree": {"pl": "Informatyka Stosowana, studia inżynierskie",
                "en": "Applied Computer Science, engineering degree"},
     "school": {"pl": "Politechnika Łódzka", "en": "Lodz University of Technology"},
     "period": {"pl": "od 2023", "en": "since 2023"}},
    {"degree": {"pl": "Technik Informatyk", "en": "IT Technician"},
     "school": {"pl": "ZST im. Armii Krajowej", "en": "ZST im. Armii Krajowej"},
     "period": {"pl": "2019 do 2023", "en": "2019 to 2023"}},
]

CERTS = [
    {"title": "Eskadra Bielika", "year": "2026",
     "sub": {"pl": "Bielik w architekturach RAG, SpeakLeash i Google for Developers",
             "en": "Bielik in RAG architectures, SpeakLeash and Google for Developers"}},
    {"title": {"pl": "INF.02 i INF.03", "en": "INF.02 and INF.03"}, "year": "2023",
     "sub": {"pl": "Aplikacje internetowe, bazy danych i sieci komputerowe",
             "en": "Web applications, databases and computer networks"}},
    {"title": {"pl": "Marketing w e-commerce", "en": "E-commerce Marketing"}, "year": "2024",
     "sub": {"pl": "Santander i Politechnika Łódzka", "en": "Santander and Lodz University of Technology"}},
]

LANGUAGES = {
    "pl": "Polski ojczysty, angielski B2, niemiecki A2",
    "en": "Polish native, English B2, German A2",
}

UI = {
    "pl": {
        "subtitle": "Software Developer, web i mobile",
        "profile": "Profil",
        "experience": "Doświadczenie",
        "projects": "Projekty",
        "hackathons": "Hackathony",
        "skills": "Technologie",
        "education": "Wykształcenie",
        "certs": "Certyfikaty",
        "languages": "Języki",
        "rodo": "Wyrażam zgodę na przetwarzanie moich danych osobowych na potrzeby procesu rekrutacji, "
                "zgodnie z RODO (UE 2016/679).",
        "stats": [("5", "hackathonów"), ("3×", "I miejsce"), ("1,5", "roku w zawodzie")],
    },
    "en": {
        "subtitle": "Software Developer, web and mobile",
        "profile": "Profile",
        "experience": "Experience",
        "projects": "Projects",
        "hackathons": "Hackathons",
        "skills": "Technologies",
        "education": "Education",
        "certs": "Certifications",
        "languages": "Languages",
        "rodo": None,
        "stats": [("5", "hackathons"), ("3×", "1st place"), ("1.5", "years in the field")],
    },
}

# --------------------------------------------------------------------------- #
#  POMOCNICZE                                                                  #
# --------------------------------------------------------------------------- #


def esc(v):
    return html.escape(str(v))


def pick(value, lang):
    if isinstance(value, dict) and ("pl" in value or "en" in value):
        return value.get(lang, value.get("pl"))
    return value


def find_photo():
    if not ASSETS.is_dir():
        return None
    for ext in ("jpg", "jpeg", "png", "webp"):
        hit = next(iter(sorted(ASSETS.glob(f"photo.{ext}"))), None)
        if hit:
            return hit
    return None


def photo_html():
    path = find_photo()
    if path is None:
        return '<div class="monogram">KK</div>'
    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f'<img class="photo" src="data:{mime};base64,{data}" alt="Kacper Kleczaj">'


# --------------------------------------------------------------------------- #
#  WERSJA DO DRUKU (PDF)                                                       #
# --------------------------------------------------------------------------- #

CSS = """
@page { size: A4; margin: 9mm 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: "Liberation Sans", "DejaVu Sans", Arial, sans-serif;
  font-size: 8.9pt; line-height: 1.38; color: #23211d; background: #fff;
}
.page { width: 188mm; margin: 0 auto; }
.mono { font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; }

.header {
  display: flex; align-items: center; gap: 15px;
  background: #1a1916; color: #f0ece6;
  padding: 10px 15px; border-radius: 6px; margin-bottom: 8px;
}
.photo, .monogram {
  width: 78px; height: 78px; border-radius: 50%; flex-shrink: 0;
  border: 2px solid #a8b87a; background: #2a2825;
}
.photo { object-fit: cover; object-position: center 20%; }
.monogram {
  color: #a8b87a; display: flex; align-items: center; justify-content: center;
  font-size: 25pt; font-weight: 700;
}
.h-main { flex: 1; min-width: 0; }
.name { font-size: 24pt; font-weight: 700; letter-spacing: -0.025em; line-height: 1; margin-bottom: 5px; }
.subtitle { font-size: 8.2pt; letter-spacing: 0.09em; text-transform: uppercase; color: #a8b87a; margin-bottom: 8px; }
.contacts { display: flex; flex-wrap: wrap; gap: 2px 12px; font-size: 7.8pt; color: #cdc7be; }
.h-stats { display: flex; gap: 15px; flex-shrink: 0; padding-left: 15px; border-left: 1px solid rgba(255,255,255,0.12); }
.h-stat { text-align: center; }
.h-stat .n { font-size: 14pt; font-weight: 700; color: #f0ece6; line-height: 1.1; }
.h-stat .l { font-size: 6.3pt; letter-spacing: 0.05em; text-transform: uppercase; color: #8a847c; }

.section { margin-bottom: 5px; }
.section-title {
  font-size: 7.6pt; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase;
  color: #5f6e38; padding-bottom: 2.5px; margin-bottom: 6px;
  border-bottom: 1.4px solid #a8b87a;
  page-break-after: avoid; break-after: avoid-page;
}

.job { margin-bottom: 5.5px; page-break-inside: avoid; }
.job:last-child { margin-bottom: 0; }
.job-head { display: flex; justify-content: space-between; align-items: baseline; gap: 12px; }
.job-role { font-size: 9.8pt; font-weight: 700; color: #1a1916; }
.job-period { font-size: 7.6pt; color: #6a6660; white-space: nowrap; }
.job-company { font-size: 8.3pt; color: #4a463f; margin-bottom: 2px; }
.job-company .site { color: #5f6e38; }
.job-desc { color: #3a3731; }
ul.points { list-style: none; margin-top: 1px; }
ul.points li { padding-left: 10px; position: relative; color: #4a463f; }
ul.points li::before {
  content: "\\25B8"; position: absolute; left: 0; top: 0; color: #a8b87a; font-size: 6.5pt; line-height: 1.95;
}

.proj-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 5px 16px; }
.proj { page-break-inside: avoid; }
.proj-head { display: flex; justify-content: space-between; align-items: baseline; gap: 8px; }
.proj-title { font-size: 9.2pt; font-weight: 700; color: #1a1916; }
.proj-meta { font-size: 7.4pt; color: #5f6e38; white-space: nowrap; }
.proj-desc { color: #4a463f; }

.hack { display: flex; align-items: baseline; gap: 9px; padding: 1.5px 0; page-break-inside: avoid; }
.hack + .hack { border-top: 1px solid #eceae4; margin-top: 2px; padding-top: 3px; }
.hack-place { width: 62px; flex-shrink: 0; font-size: 7.8pt; font-weight: 700; color: #5f6e38; }
.hack-event { flex: 1; font-size: 8.6pt; color: #23211d; }
.hack-proj { font-size: 7.8pt; color: #6a6660; }
.hack-date { flex-shrink: 0; font-size: 7.6pt; color: #6a6660; white-space: nowrap; }

.skill-row { display: flex; gap: 10px; align-items: flex-start; padding: 1.5px 0; page-break-inside: avoid; }
.skill-row + .skill-row { border-top: 1px solid #eceae4; }
.skill-label {
  width: 120px; flex-shrink: 0; font-size: 7.2pt; letter-spacing: 0.07em;
  text-transform: uppercase; color: #6a6660; padding-top: 1.5px;
}
.skill-items { flex: 1; display: flex; flex-wrap: wrap; gap: 3px; }
.tag {
  font-size: 7pt; padding: 1px 5px; border-radius: 3px;
  background: #f1f2e9; border: 1px solid #dfe2cd; color: #4a5530; white-space: nowrap;
}

.cols3 { display: grid; grid-template-columns: 1.15fr 1fr 0.6fr; gap: 16px; }
.cols3 .section { page-break-inside: avoid; margin-bottom: 0; }
.row { margin-bottom: 3px; }
.row:last-child { margin-bottom: 0; }
.row-title { font-size: 8.4pt; font-weight: 700; color: #1a1916; }
.row-sub { font-size: 7.8pt; color: #4a463f; }
.row-date { font-weight: 400; font-size: 7.4pt; color: #6a6660; white-space: nowrap; }
.langs { font-size: 8.2pt; color: #3a3731; }

.rodo {
  margin-top: 7px; padding-top: 4px; border-top: 1px solid #eceae4;
  font-size: 6.5pt; line-height: 1.3; color: #8a847c;
  page-break-inside: avoid;
}
"""


def render_print(lang):
    ui = UI[lang]
    parts = []

    stats = "".join(
        f'<div class="h-stat"><div class="n">{esc(n)}</div><div class="l">{esc(l)}</div></div>'
        for n, l in ui["stats"]
    )
    contacts = "".join(
        f"<span>{esc(c)}</span>"
        for c in (
            pick(CONTACT["location"], lang), CONTACT["phone"], CONTACT["email"],
            CONTACT["github"], CONTACT["linkedin"], CONTACT["site"],
        )
    )
    parts.append(f'''<div class="header">
  {photo_html()}
  <div class="h-main">
    <div class="name">Kacper Kleczaj</div>
    <div class="subtitle mono">{esc(ui["subtitle"])}</div>
    <div class="contacts mono">{contacts}</div>
  </div>
  <div class="h-stats">{stats}</div>
</div>''')

    parts.append(f'''<div class="section">
  <div class="section-title">{esc(ui["profile"])}</div>
  <p>{esc(PROFILE[lang])}</p>
</div>''')

    jobs = []
    for job in EXPERIENCE:
        points = "".join(f"<li>{esc(p)}</li>" for p in pick(job["points"], lang))
        jobs.append(f'''<div class="job">
  <div class="job-head">
    <div class="job-role">{esc(pick(job["role"], lang))}</div>
    <div class="job-period mono">{esc(pick(job["period"], lang))}</div>
  </div>
  <div class="job-company">{esc(job["company"])} <span class="site mono">{esc(job["site"])}</span></div>
  <div class="job-desc">{esc(pick(job["desc"], lang))}</div>
  <ul class="points">{points}</ul>
</div>''')
    parts.append(f'''<div class="section">
  <div class="section-title">{esc(ui["experience"])}</div>
  {"".join(jobs)}
</div>''')

    projs = []
    for p in PROJECTS:
        projs.append(f'''<div class="proj">
  <div class="proj-head">
    <div class="proj-title">{esc(p["title"])}</div>
    <div class="proj-meta mono">{esc(pick(p["meta"], lang))}</div>
  </div>
  <div class="proj-desc">{esc(pick(p["desc"], lang))}</div>
</div>''')
    parts.append(f'''<div class="section">
  <div class="section-title">{esc(ui["projects"])}</div>
  <div class="proj-grid">{"".join(projs)}</div>
</div>''')

    hacks = []
    for place in (True, False):
        group = [h for h in HACKATHONS if h["first"] is place]
        if not group:
            continue
        items = ", ".join(f'{h["event"]} ({h["project"]}, {h["date"]})' for h in group)
        hacks.append(f'''<div class="hack">
  <div class="hack-place">{esc(pick(group[0]["place"], lang))}</div>
  <div class="hack-event">{esc(items)}</div>
</div>''')
    parts.append(f'''<div class="section">
  <div class="section-title">{esc(ui["hackathons"])}</div>
  {"".join(hacks)}
</div>''')

    rows = []
    for cat in SKILLS:
        items = "".join(f'<span class="tag">{esc(s)}</span>' for s in cat["items"])
        rows.append(f'''<div class="skill-row">
  <div class="skill-label mono">{esc(pick(cat["label"], lang))}</div>
  <div class="skill-items">{items}</div>
</div>''')
    parts.append(f'''<div class="section">
  <div class="section-title">{esc(ui["skills"])}</div>
  {"".join(rows)}
</div>''')

    edus = "".join(f'''<div class="row">
  <div class="row-title">{esc(pick(e["degree"], lang))}</div>
  <div class="row-sub">{esc(pick(e["school"], lang))}, <span class="mono">{esc(pick(e["period"], lang))}</span></div>
</div>''' for e in EDUCATION)

    certs = "".join(f'''<div class="row">
  <div class="row-title">{esc(pick(c["title"], lang))} <span class="row-date mono">{esc(c["year"])}</span></div>
</div>''' for c in CERTS)

    parts.append(f'''<div class="cols3">
  <div class="section">
    <div class="section-title">{esc(ui["education"])}</div>
    {edus}
  </div>
  <div class="section">
    <div class="section-title">{esc(ui["certs"])}</div>
    {certs}
  </div>
  <div class="section">
    <div class="section-title">{esc(ui["languages"])}</div>
    <div class="langs">{esc(LANGUAGES[lang])}</div>
  </div>
</div>''')

    if ui["rodo"]:
        parts.append(f'<div class="rodo">{esc(ui["rodo"])}</div>')

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="utf-8"><title>CV Kacper Kleczaj</title><style>{CSS}</style></head>
<body><div class="page">{"".join(parts)}</div></body>
</html>'''


# --------------------------------------------------------------------------- #
#  WERSJA POD GOOGLE DOCS                                                      #
# --------------------------------------------------------------------------- #

DOCS_CSS = """
body { font-family: Arial, sans-serif; font-size: 10pt; color: #000; }
h1 { font-size: 20pt; margin: 0 0 2pt 0; }
h2 { font-size: 10pt; letter-spacing: 1pt; text-transform: uppercase; color: #5f6e38;
     border-bottom: 1pt solid #a8b87a; margin: 12pt 0 5pt 0; padding-bottom: 2pt; }
h3 { font-size: 11pt; margin: 8pt 0 0 0; }
p { margin: 0 0 3pt 0; }
ul { margin: 2pt 0 4pt 18pt; padding: 0; }
li { margin: 0; }
.sub { color: #5f6e38; font-size: 10pt; margin: 0 0 4pt 0; }
.meta { color: #555; font-size: 9pt; }
.small { font-size: 8pt; color: #777; }
"""


def render_docs(lang):
    """Prosty HTML, ktory Google Docs poprawnie zamienia na dokument do edycji."""
    ui = UI[lang]
    out = ["<h1>Kacper Kleczaj</h1>", f'<p class="sub">{esc(ui["subtitle"])}</p>']

    contacts = " | ".join([
        pick(CONTACT["location"], lang), CONTACT["phone"], CONTACT["email"],
        CONTACT["github"], CONTACT["linkedin"], CONTACT["site"],
    ])
    out.append(f'<p class="meta">{esc(contacts)}</p>')

    out.append(f'<h2>{esc(ui["profile"])}</h2><p>{esc(PROFILE[lang])}</p>')

    out.append(f'<h2>{esc(ui["experience"])}</h2>')
    for job in EXPERIENCE:
        out.append(f'<h3>{esc(pick(job["role"], lang))}, {esc(job["company"])}</h3>')
        out.append(f'<p class="meta">{esc(pick(job["period"], lang))} | {esc(job["site"])}</p>')
        out.append(f'<p>{esc(pick(job["desc"], lang))}</p>')
        out.append("<ul>" + "".join(f"<li>{esc(p)}</li>" for p in pick(job["points"], lang)) + "</ul>")

    out.append(f'<h2>{esc(ui["projects"])}</h2>')
    for p in PROJECTS:
        out.append(f'<h3>{esc(p["title"])}</h3>')
        out.append(f'<p class="meta">{esc(pick(p["meta"], lang))}</p>')
        out.append(f'<p>{esc(pick(p["desc"], lang))}</p>')

    out.append(f'<h2>{esc(ui["hackathons"])}</h2><ul>')
    for h in HACKATHONS:
        out.append(
            f'<li>{esc(pick(h["place"], lang))}, {esc(h["event"])} '
            f'({esc(h["project"])}), {esc(h["date"])}</li>'
        )
    out.append("</ul>")

    out.append(f'<h2>{esc(ui["skills"])}</h2><ul>')
    for cat in SKILLS:
        out.append(f'<li><b>{esc(pick(cat["label"], lang))}:</b> {esc(", ".join(cat["items"]))}</li>')
    out.append("</ul>")

    out.append(f'<h2>{esc(ui["education"])}</h2><ul>')
    for e in EDUCATION:
        out.append(
            f'<li>{esc(pick(e["degree"], lang))}, {esc(pick(e["school"], lang))} '
            f'({esc(pick(e["period"], lang))})</li>'
        )
    out.append("</ul>")

    out.append(f'<h2>{esc(ui["certs"])}</h2><ul>')
    for c in CERTS:
        out.append(f'<li>{esc(pick(c["title"], lang))}, {esc(pick(c["sub"], lang))} ({esc(c["year"])})</li>')
    out.append("</ul>")

    out.append(f'<h2>{esc(ui["languages"])}</h2><p>{esc(LANGUAGES[lang])}</p>')

    if ui["rodo"]:
        out.append(f'<p class="small">{esc(ui["rodo"])}</p>')

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="utf-8"><title>CV Kacper Kleczaj</title><style>{DOCS_CSS}</style></head>
<body>{"".join(out)}</body>
</html>'''


# --------------------------------------------------------------------------- #

def to_pdf(html_path: Path, pdf_path: Path):
    chrome = next((c for c in CHROME_CANDIDATES if c and Path(c).exists()), None)
    if chrome is None:
        print("!! nie znaleziono Chromium, pomijam PDF", file=sys.stderr)
        return False
    subprocess.run(
        [chrome, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", html_path.as_uri()],
        check=True, capture_output=True,
    )
    return pdf_path.exists()


def main():
    BUILD.mkdir(parents=True, exist_ok=True)
    photo = find_photo()
    print(f"zdjęcie: {photo.name if photo else 'BRAK, użyto inicjałów (wrzuć cv/assets/photo.jpg)'}")

    for lang, suffix in (("pl", "PL"), ("en", "EN")):
        base = BUILD / f"CV_Kacper_Kleczaj_{suffix}"
        html_path = base.with_suffix(".html")
        pdf_path = base.with_suffix(".pdf")
        docs_path = BUILD / f"CV_Kacper_Kleczaj_{suffix}.docs.html"

        html_path.write_text(render_print(lang), encoding="utf-8")
        docs_path.write_text(render_docs(lang), encoding="utf-8")
        ok = to_pdf(html_path, pdf_path)
        print(f"  {pdf_path.name} ({pdf_path.stat().st_size // 1024} KB)" if ok else "  PDF pominięty")


if __name__ == "__main__":
    main()
