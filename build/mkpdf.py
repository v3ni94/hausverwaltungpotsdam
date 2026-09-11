import base64, re, subprocess, io, sys, os
from pathlib import Path
import markdown
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from pypdf import PdfReader, PdfWriter

ROOT = Path("/home/user/hausverwaltungpotsdam")
B = ROOT / "build"
OUT = B / "pdf"; OUT.mkdir(exist_ok=True)

ORANGE, ANTHRAZIT, MITTELGRAU = "#E6A83C", "#87888A", "#9C9D9F"
HELLGRAU, UMRISS, SCHWARZ = "#D7D8DA", "#ECECEC", "#1A1A1A"
LOGO = B / "assets" / "Logo_HVM.jpg"
FOOT1 = "Hausverwaltung Müller GmbH | Rheinpromenade 13 | 40789 Monheim am Rhein"
FOOT2 = "Amtsgericht Düsseldorf, HRB 104762 | Geschäftsführer: Timo Müller | www.muellerhv.de"

CSS = """
@page { size: A4; margin: 26mm 20mm 34mm 25mm; }
body { font-family: Helvetica, Arial, sans-serif; font-size: 10pt; line-height: 1.3;
       color: %(sch)s; margin:0; }
h1 { font-size: 17pt; color: %(sch)s; margin: 0 0 2mm 0; page-break-after: avoid; }
h2 { font-size: 13pt; color: %(sch)s; margin: 8mm 0 2mm 0; padding-top: 2mm;
     border-top: 0.6pt solid %(hell)s; page-break-after: avoid; }
h3 { font-size: 11pt; color: %(ant)s; margin: 5mm 0 1.5mm 0; page-break-after: avoid; }
h4 { font-size: 10pt; margin: 4mm 0 1mm 0; page-break-after: avoid; }
p { margin: 0 0 2.2mm 0; }
ul, ol { margin: 0 0 2.5mm 0; padding-left: 6mm; }
li { margin-bottom: 0.8mm; }
table { border-collapse: collapse; width: 100%%; font-size: 8pt; margin: 2mm 0 4mm 0;
        page-break-inside: avoid; }
th { background: %(orange)s; color: #fff; text-align: left; padding: 1.4mm 1.6mm;
     font-weight: bold; font-size: 8pt; }
td { padding: 1.3mm 1.6mm; border-bottom: 0.4pt solid %(hell)s; vertical-align: top; }
tr:nth-child(even) td { background: #FAFAFA; }
code { font-family: "Courier New", monospace; font-size: 8.5pt; }
pre { font-family: "Courier New", monospace; font-size: 7.6pt; line-height: 1.25;
      background: #FAFAFA; border-left: 1.6pt solid %(orange)s; padding: 2.5mm 3mm;
      white-space: pre-wrap; margin: 2mm 0 4mm 0; }
blockquote { margin: 2mm 0 3mm 0; padding: 1mm 0 1mm 4mm;
             border-left: 1.6pt solid %(orange)s; color: %(ant)s; }
strong { color: %(sch)s; }
.cover { page-break-after: always; padding-top: 45mm; }
.cover .kicker { font-size: 9pt; color: %(ant)s; letter-spacing: 0.6pt;
                 text-transform: uppercase; margin-bottom: 4mm; }
.cover h1 { font-size: 26pt; line-height: 1.15; margin-bottom: 5mm; }
.cover .bar { width: 28mm; height: 1.6mm; background: %(orange)s; margin: 0 0 8mm 0; }
.cover .sub { font-size: 11.5pt; color: %(ant)s; line-height: 1.45; margin-bottom: 14mm; }
.cover .meta { font-size: 9pt; color: %(ant)s; line-height: 1.7; }
.cover .meta b { color: %(sch)s; }
.toc { font-size: 9.5pt; }
.toc ol { list-style: none; padding-left: 0; }
.toc li { margin-bottom: 1.5mm; }
.note { font-size: 8.5pt; color: %(ant)s; border: 0.4pt solid %(hell)s;
        padding: 2.5mm 3mm; margin: 3mm 0; }
h2, h3 { -webkit-region-break-inside: avoid; }
""" % dict(sch=SCHWARZ, ant=ANTHRAZIT, hell=HELLGRAU, orange=ORANGE)

def kennlinie(c, y, h, w=A4[0]):
    segs = [(0,.40,ANTHRAZIT),(.40,.60,MITTELGRAU),(.60,.675,ORANGE),(.675,1.0,HELLGRAU)]
    sk = 0.9*h
    for a,b,col in segs:
        x0, x1 = a*w, b*w
        p = c.beginPath()
        p.moveTo(x0 if a==0 else x0-sk/2, y)
        p.lineTo(x1 if b==1.0 else x1-sk/2, y)
        p.lineTo(x1 if b==1.0 else x1+sk/2, y+h)
        p.lineTo(x0 if a==0 else x0+sk/2, y+h)
        p.close()
        c.setFillColor(HexColor(col)); c.drawPath(p, stroke=0, fill=1)

def wasserzeichen(c):
    c.saveState(); c.setStrokeColor(HexColor(UMRISS)); c.setLineWidth(9); c.setLineJoin(1)
    x, y, w, wall, roof = 135*mm, -25*mm, 115*mm, 62*mm, 42*mm
    p = c.beginPath()
    p.moveTo(x, y); p.lineTo(x, y+wall); p.lineTo(x+w/2, y+wall+roof)
    p.lineTo(x+w, y+wall); p.lineTo(x+w, y)
    c.drawPath(p, stroke=1, fill=0); c.restoreState()

def overlay(npages):
    buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=A4); W, H = A4
    for i in range(npages):
        first = (i == 0)
        kennlinie(c, H-(3*mm if first else 1.2*mm), 3*mm if first else 1.2*mm)
        if first:
            wasserzeichen(c)
            iw = 40*mm; ih = iw*1143/1320
            c.drawImage(str(LOGO), W-20*mm-iw, H-10*mm-ih, width=iw, height=ih, mask='auto')
        kennlinie(c, 26*mm, 1.2*mm)
        c.setFont("Helvetica", 7.5); c.setFillColor(HexColor(ANTHRAZIT))
        c.drawCentredString(W/2, 20.5*mm, FOOT1)
        c.drawCentredString(W/2, 17*mm, FOOT2)
        if not first:
            c.setFont("Helvetica", 8); c.drawRightString(W-20*mm, 12*mm, f"Seite {i+1}")
        c.showPage()
    c.save(); buf.seek(0); return PdfReader(buf)

def render(html, target):
    tmp = B / "tmp.html"; tmp.write_text(html, encoding="utf-8")
    raw = B / "tmp.pdf"
    if raw.exists(): raw.unlink()
    subprocess.run(["/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
        "--headless","--disable-gpu","--no-sandbox","--no-pdf-header-footer",
        f"--print-to-pdf={raw}", f"file://{tmp}"], check=True,
        capture_output=True)
    base = PdfReader(str(raw)); ov = overlay(len(base.pages))
    w = PdfWriter()
    for i, pg in enumerate(base.pages):
        o = ov.pages[i]; o.merge_page(pg); w.add_page(o)
    with open(target, "wb") as f: w.write(f)
    return len(base.pages)

def md2html(md_text, title, cover=None, toc=None):
    body = markdown.markdown(md_text, extensions=["tables","fenced_code","sane_lists"])
    pre = ""
    if cover:
        items = "".join(f"<li>{t}</li>" for t in (toc or []))
        pre = f"""<div class="cover"><div class="kicker">{cover['kicker']}</div>
<h1>{cover['title']}</h1><div class="bar"></div>
<div class="sub">{cover['sub']}</div>
<div class="meta">{cover['meta']}</div>
{'<div class="toc" style="margin-top:16mm"><b>Inhalt</b><ol>'+items+'</ol></div>' if items else ''}
</div>"""
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8">
<title>{title}</title><style>{CSS}</style></head><body>{pre}{body}</body></html>"""
