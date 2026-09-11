# -*- coding: utf-8 -*-
"""Generator der statischen Website hausverwaltungpotsdam.de."""
from pathlib import Path
import json, html as H

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DOMAIN = "https://hausverwaltungpotsdam.de"

FIRMA = "Hausverwaltung Müller GmbH"
STRASSE, PLZORT = "Rheinpromenade 13", "40789 Monheim am Rhein"
TEL, MAIL = "[Telefonnummer ergänzen]", "[E-Mail-Adresse ergänzen]"

NAV = [("/", "Start"), ("/weg-verwaltung-potsdam/", "WEG-Verwaltung"),
       ("/mietverwaltung-potsdam/", "Mietverwaltung"),
       ("/sondereigentumsverwaltung-potsdam/", "Sondereigentum"),
       ("/ratgeber/", "Ratgeber"), ("/vorlagen/", "Vorlagen"), ("/kontakt/", "Kontakt")]

ORG = {"@context":"https://schema.org","@type":"Organization",
  "@id":DOMAIN+"/#organization","name":FIRMA,"legalName":FIRMA,"url":DOMAIN+"/",
  "logo":DOMAIN+"/assets/logo-hvm.jpg",
  "address":{"@type":"PostalAddress","streetAddress":STRASSE,"postalCode":"40789",
             "addressLocality":"Monheim am Rhein","addressCountry":"DE"},
  "areaServed":[{"@type":"City","name":"Potsdam"},{"@type":"State","name":"Brandenburg"}]}

def crumbs(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":i+1,"name":n,"item":DOMAIN+u}
        for i,(u,n) in enumerate(items)]}

def faq_ld(pairs):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}}
        for q,a in pairs]}

def faq_html(pairs):
    return "\n".join(f'<div class="faq"><h3>{q}</h3><p>{a}</p></div>' for q,a in pairs)

def page(path, title, desc, h1, lead, body, breadcrumb=None, faq=None, extra_ld=None):
    url = DOMAIN + path
    cur = ' aria-current="page"'
    nav = "\n".join(
        '<li><a href="%s"%s>%s</a></li>' % (u, cur if u == path else "", n)
        for u, n in NAV)
    crumb = ""
    if breadcrumb:
        parts = " &rsaquo; ".join(
            (f'<a href="{u}">{n}</a>' if u!=path else f"<span>{n}</span>")
            for u,n in breadcrumb)
        crumb = f'<div class="wrap crumb">{parts}</div>'
    lds = [ORG]
    if breadcrumb: lds.append(crumbs(breadcrumb))
    if faq: lds.append(faq_ld(faq))
    if extra_ld: lds.append(extra_ld)
    ldtags = "\n".join('<script type="application/ld+json">%s</script>'
                       % json.dumps(l, ensure_ascii=False) for l in lds)
    doc = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="icon" href="/assets/favicon.png" type="image/png">
<link rel="stylesheet" href="/assets/style.css">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="de_DE">
{ldtags}
</head>
<body>
<div class="kennlinie"><i></i><i></i><i></i><i></i></div>
<header class="site"><div class="wrap head">
<a href="/"><img src="/assets/logo-hvm.jpg" alt="{FIRMA}" width="150" height="130"></a>
<nav class="main" aria-label="Hauptnavigation"><ul>
{nav}
</ul></nav>
</div></header>
{crumb}
<main><div class="wrap">
<h1>{h1}</h1>
<div class="bar"></div>
{f'<p class="lead">{lead}</p>' if lead else ''}
{body}
</div></main>
<footer class="site"><div class="wrap">
<div class="fgrid">
<div><h4>Leistungen</h4><ul>
<li><a href="/weg-verwaltung-potsdam/">WEG-Verwaltung Potsdam</a></li>
<li><a href="/mietverwaltung-potsdam/">Mietverwaltung Potsdam</a></li>
<li><a href="/sondereigentumsverwaltung-potsdam/">Sondereigentumsverwaltung</a></li>
</ul></div>
<div><h4>Ratgeber</h4><ul>
<li><a href="/ratgeber/hausverwaltung-weg-kuendigen/">Hausverwaltung kündigen</a></li>
<li><a href="/ratgeber/verwalterwechsel-weg/">Verwalterwechsel</a></li>
<li><a href="/ratgeber/was-darf-eine-hausverwaltung/">Was darf eine Hausverwaltung?</a></li>
<li><a href="/ratgeber/zertifizierter-verwalter/">Zertifizierter Verwalter</a></li>
</ul></div>
<div><h4>Vorlagen</h4><ul>
<li><a href="/vorlagen/">Muster und Downloads</a></li>
</ul></div>
<div><h4>Kontakt</h4><ul>
<li>{FIRMA}</li><li>{STRASSE}</li><li>{PLZORT}</li>
<li>{TEL}</li><li>{MAIL}</li>
</ul></div>
</div>
<div class="legal">
{FIRMA} | {STRASSE} | {PLZORT}<br>
Amtsgericht Düsseldorf, HRB 104762 | Geschäftsführer: Timo Müller |
<a href="/impressum/">Impressum</a> | <a href="/datenschutz/">Datenschutz</a>
</div>
</div></footer>
</body>
</html>
"""
    target = SITE / (path.lstrip("/") or "") / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(doc, encoding="utf-8")
    return path
