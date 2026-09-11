import re, sys
sys.path.insert(0, ".")
from mkpdf import *

def clean(p):
    t = Path(p).read_text(encoding="utf-8")
    t = re.sub(r"^# .*\n", "", t, count=1)          # H1 entfaellt, Kapitelueberschrift wird gesetzt
    return t.strip()

# Mermaid-Bloecke durch Textfassungen ersetzen
proz = clean(ROOT/"docs/03-prozesse-und-redaktionsplan.md")
proz = re.sub(r"## Praxis-Timeline.*?```\n", "## Praxisplanung Verwalterwechsel\n\n"
              + (B/"diagramme_text.md").read_text(encoding="utf-8").split("\n",1)[1].strip()
              + "\n", proz, flags=re.S)
proz = re.sub(r"## Ablauf Kündigungsprozess.*?```\n", "## Ablauf Kündigungsprozess\n\n"
              + (B/"flow_text.md").read_text(encoding="utf-8").split("\n",1)[1].strip()
              + "\n", proz, flags=re.S)
proz = proz.replace("### Praxisplanung Verwalterwechsel einer WEG\n", "")
proz = proz.replace("### Ablauf Kündigungsprozess\n", "")

kapitel = [
    ("1. Strategie und Leitplanken", clean(ROOT/"docs/00-strategie.md")),
    ("2. Pflicht-Content-Bausteine und Themenpriorisierung", clean(ROOT/"docs/01-content-bausteine.md")),
    ("3. Beispiel-Landingpage Verwalterwechsel", clean(ROOT/"docs/02-landingpage-beispiel.md")),
    ("4. Prozesse, Vorlagen und Redaktionsplan", proz),
    ("5. Technisches SEO und Structured Data", clean(ROOT/"docs/04-technisches-seo.md")),
]
# Ueberschriftenebenen um eine Stufe absenken
teile = []
for titel, txt in kapitel:
    txt = re.sub(r"^### ", "#### ", txt, flags=re.M)
    txt = re.sub(r"^## ", "### ", txt, flags=re.M)
    teile.append(f"<h2>{titel}</h2>\n\n" + txt)

kw = (ROOT/"keywords/keyword-portfolio.csv").read_text(encoding="utf-8").strip().split("\n")
kwtab = "| " + " | ".join(kw[0].split(";")) + " |\n|" + "---|"*7 + "\n"
kwtab += "\n".join("| " + " | ".join(r.split(";")) + " |" for r in kw[1:])

anhang = f"""<h2>6. Keyword-Portfolio</h2>

Die Spalte volumen_band_de enthält heuristische Planungsbandbreiten für Deutschland,
keine gemessenen Suchvolumina. Live-Werte konnten nicht abgerufen werden. Vor einer
Budget- oder SEO-Entscheidung sind die Begriffe in einem Keyword-Tool zu validieren.

{kwtab}

<h2>7. Masterprompt</h2>

Der Masterprompt wird als System- oder Projektprompt gesetzt. Er zwingt das Modell zuerst
zu Quellenprüfung, Suchintention, juristischer Einordnung und Faktenprüfung, erst danach
entsteht Text.

```
{(ROOT/'prompts/masterprompt-hausverwaltung-mueller.txt').read_text(encoding='utf-8')}
```

<h2>8. JSON-LD-Vorlagen</h2>

Strukturierte Daten müssen den sichtbaren Seiteninhalt widerspiegeln. Platzhalter erst nach
Verifizierung durch tatsächliche Unternehmensdaten ersetzen.

#### Organization

```
{(ROOT/'schema/organization.json').read_text(encoding='utf-8').strip()}
```

#### LocalBusiness

```
{(ROOT/'schema/localbusiness.json').read_text(encoding='utf-8').strip()}
```

#### FAQPage

```
{(ROOT/'schema/faqpage.json').read_text(encoding='utf-8').strip()}
```
"""

cover = dict(
    kicker="Hausverwaltung Müller GmbH",
    title="SEO- und Content-System hausverwaltungpotsdam.de",
    sub="Strategie, Masterprompt, Content-Bausteine, Redaktionsplan und Vorlagen für "
        "WEG-Verwaltung, Mietverwaltung und Sondereigentumsverwaltung in Potsdam und Brandenburg.",
    meta="<b>Stand der Recherche:</b> 10.09.2026<br><b>Dokumentdatum:</b> 11.09.2026<br>"
         "<b>Status:</b> Arbeitsgrundlage, keine Rechtsberatung",
)
toc = [t for t,_ in kapitel] + ["6. Keyword-Portfolio", "7. Masterprompt", "8. JSON-LD-Vorlagen"]

html = md2html("\n\n".join(teile) + "\n\n" + anhang,
               "SEO- und Content-System Hausverwaltung Müller GmbH", cover, toc)
n = render(html, OUT/"HVM_SEO-Content-System_Gesamtdokument.pdf")
print("Gesamtdokument:", n, "Seiten")

# Vorlagen einzeln
vorlagen = [
 ("01-protokoll-bestellung-hausverwaltung.txt","Muster Beschlussprotokoll Verwalterbestellung",
  "Niederschrift zur Abberufung, Neubestellung und Ermächtigung zum Abschluss des Verwaltervertrags."),
 ("02-verwaltervertrag-weg.txt","Muster Verwaltervertrag WEG",
  "Vertragsmuster für die Verwaltung einer Gemeinschaft der Wohnungseigentümer."),
 ("03-vollmacht.txt","Muster Vollmacht",
  "Vollmacht mit Begrenzung nach Vertragsgegenstand, Betrag und Dauer."),
]
for datei, titel, sub in vorlagen:
    txt = (ROOT/"vorlagen"/datei).read_text(encoding="utf-8")
    cv = dict(kicker="Hausverwaltung Müller GmbH | Muster", title=titel,
              sub=sub, meta="<b>Dokumentdatum:</b> 11.09.2026<br><b>Status:</b> Muster, keine Rechtsberatung")
    body = "<pre>" + txt.replace("&","&amp;").replace("<","&lt;") + "</pre>"
    h = md2html("", titel, cv) .replace("</body>", body + "</body>")
    ziel = OUT/("HVM_" + titel.replace(" ","-").replace("ü","ue") + ".pdf")
    print(titel + ":", render(h, ziel), "Seiten")
