#!/usr/bin/env python3
"""Sklada list motywacyjny do PDF w tej samej identyfikacji co CV.

Uzycie:  python3 cv/letter.py
Wynik:   cv/build/Motivation_Letter_Heritage_in_Video_Games.pdf
"""

import html
import subprocess
from pathlib import Path

from generate import CHROME_CANDIDATES, CONTACT, BUILD

ROOT = Path(__file__).resolve().parent

PROGRAMME = "Heritage in Video Games"
INSTITUTION = "Bragança Polytechnic University, Mirandela Campus"
ADDRESSEE = "Prof. Bárbara Barroso and Prof. Rita Costa"
DATE = "3 August 2026"

PARAGRAPHS = [
    "I am applying for the <b>Heritage in Video Games</b> programme at the Mirandela Campus. I am a "
    "Computer Science student at Lodz University of Technology and a software developer working on web "
    "and mobile applications, and I would like to spend these weeks turning a piece of local heritage "
    "into something people can actually play.",

    "My interest is not theoretical. At Fintech Łódź_Hack my team took first place with <b>Moje Osiedle</b>, "
    "a gamified extension of the Łódź city card that rewards residents for taking part in neighbourhood "
    "life and supporting local businesses. Building it showed me how quickly a game layer changes the way "
    "people relate to the place they live in, and how much of that place's story never gets told. I come "
    "from Łódź, a city built on the 19th century textile industry, where factory districts such as Księży "
    "Młyn survive as architecture while the memory attached to them fades. That is the kind of intangible "
    "heritage I would like to prototype around.",

    "What I bring is the ability to ship. I have released a mobile application built in React Native to "
    "the App Store and Google Play, I build interactive interfaces in React and TypeScript, and five "
    "hackathons have taught me to get from a concept to a working prototype in days rather than months. "
    "On a team I am usually the person who makes sure the demo runs.",

    "What I want from the programme is the other half of that equation: a structured understanding of what "
    "heritage is, including the UNESCO framing and the distinction between its tangible and intangible "
    "forms, so that my design decisions rest on method rather than intuition. I am equally drawn to working "
    "with students from Sweden, France, Finland and Spain. Heritage is precisely the subject where my Polish "
    "assumptions will not survive contact with four other cultures, and that friction is the point.",

    "I am available for the full virtual component from 9 October to 27 November and for the physical week "
    "in Mirandela from 16 to 20 November. My English is at B2 level, which is sufficient for teamwork, "
    "documentation and presentations.",

    "Thank you for considering my application. I would be glad to share my portfolio or discuss project "
    "ideas in more detail.",
]

CSS = """
@page { size: A4; margin: 20mm 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body {
  font-family: "Liberation Sans", "DejaVu Sans", Arial, sans-serif;
  font-size: 10.2pt; line-height: 1.55; color: #23211d; background: #fff;
}
.page { width: 170mm; margin: 0 auto; }
.mono { font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; }

.head { border-bottom: 1.6px solid #a8b87a; padding-bottom: 9px; margin-bottom: 16px; }
.name { font-size: 19pt; font-weight: 700; letter-spacing: -0.02em; color: #1a1916; }
.role { font-size: 8.4pt; letter-spacing: 0.1em; text-transform: uppercase; color: #5f6e38; margin: 2px 0 7px; }
.contacts { display: flex; flex-wrap: wrap; gap: 2px 14px; font-size: 8pt; color: #6a6660; }

.meta { font-size: 9pt; color: #6a6660; margin-bottom: 14px; }
.meta b { color: #23211d; font-weight: 700; }
.subject { font-size: 10.5pt; font-weight: 700; color: #1a1916; margin-bottom: 12px; }
p.body { margin-bottom: 9px; text-align: justify; }
.sign { margin-top: 18px; font-size: 10pt; }
.sign .who { font-weight: 700; color: #1a1916; margin-top: 2px; }
"""


def esc(v):
    return html.escape(str(v))


def render():
    contacts = "".join(
        f"<span>{esc(c)}</span>"
        for c in (CONTACT["location"]["en"], CONTACT["phone"], CONTACT["email"],
                  CONTACT["github"], CONTACT["site"])
    )
    body = "".join(f'<p class="body">{p}</p>' for p in PARAGRAPHS)
    return f'''<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>Motivation letter, {esc(PROGRAMME)}</title><style>{CSS}</style></head>
<body><div class="page">
  <div class="head">
    <div class="name">Kacper Kleczaj</div>
    <div class="role mono">Software Developer, web and mobile</div>
    <div class="contacts mono">{contacts}</div>
  </div>

  <div class="meta">
    <b>{esc(ADDRESSEE)}</b><br>{esc(INSTITUTION)}<br>Łódź, {esc(DATE)}
  </div>

  <div class="subject">Application for {esc(PROGRAMME)}, autumn 2026</div>

  <p class="body">Dear Professors,</p>
  {body}

  <div class="sign">Yours sincerely,<div class="who">Kacper Kleczaj</div></div>
</div></body>
</html>'''


def main():
    BUILD.mkdir(parents=True, exist_ok=True)
    html_path = BUILD / "Motivation_Letter_Heritage_in_Video_Games.html"
    pdf_path = html_path.with_suffix(".pdf")
    html_path.write_text(render(), encoding="utf-8")

    chrome = next((c for c in CHROME_CANDIDATES if c and Path(c).exists()), None)
    if chrome is None:
        raise SystemExit("nie znaleziono Chromium")
    subprocess.run(
        [chrome, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", html_path.as_uri()],
        check=True, capture_output=True,
    )
    print(f"  {pdf_path.name} ({pdf_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
