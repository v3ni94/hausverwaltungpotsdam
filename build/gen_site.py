# -*- coding: utf-8 -*-
"""Generator der statischen Website hausverwaltungpotsdam.de."""
from pathlib import Path
import json, html as H

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
DOMAIN = "https://hausverwaltungpotsdam.de"

FIRMA = "Hausverwaltung Müller GmbH"
STRASSE, PLZORT = "Rheinpromenade 13", "40789 Monheim am Rhein"
TEL = "030 439733333"
TEL_LINK = "+4930439733333"
MAIL = "potsdam@muellerhv.de"
LEADMAIL = "lead@muellerhv.de"

NAV = [("/", "Start"), ("/weg-verwaltung-potsdam/", "WEG-Verwaltung"),
       ("/mietverwaltung-potsdam/", "Mietverwaltung"),
       ("/sondereigentumsverwaltung-potsdam/", "Sondereigentum"),
       ("/ratgeber/", "Ratgeber"), ("/vorlagen/", "Vorlagen")]

ORG = {"@context":"https://schema.org","@type":"Organization",
  "@id":DOMAIN+"/#organization","name":FIRMA,"legalName":FIRMA,"url":DOMAIN+"/",
  "logo":DOMAIN+"/assets/logo-hvm.jpg",
  "address":{"@type":"PostalAddress","streetAddress":STRASSE,"postalCode":"40789",
             "addressLocality":"Monheim am Rhein","addressCountry":"DE"},
  "telephone":"+49 30 439733333","email":"potsdam@muellerhv.de",
  "areaServed":[{"@type":"City","name":"Potsdam"},{"@type":"State","name":"Brandenburg"}],
  "contactPoint":[{"@type":"ContactPoint","contactType":"customer service",
    "telephone":"+49 30 439733333","email":"potsdam@muellerhv.de",
    "areaServed":"DE","availableLanguage":"German"}]}

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


import re as _re
def sektionen(body):
    """Zerlegt den Fließtext an den H2-Überschriften in Abschnitte und legt
    abwechselnd ein Flächenband darunter."""
    def _slug(t):
        t = _re.sub(r"<[^>]+>", "", t).lower()
        for a, b in (("ä","ae"),("ö","oe"),("ü","ue"),("ß","ss")):
            t = t.replace(a, b)
        t = _re.sub(r"[^a-z0-9]+", "-", t).strip("-")
        return t

    body = _re.sub(r"<h2>(.*?)</h2>",
                   lambda m: '<h2 id="%s">%s</h2>' % (_slug(m.group(1)), m.group(1)),
                   body)
    teile = _re.split(r"(?=\n<h2)", body.strip())
    out, band = [], False
    for i, t in enumerate(teile):
        t = t.strip()
        if not t:
            continue
        cls = ' class="band"' if band else ""
        out.append('<section%s><div class="wrap">%s</div></section>' % (cls, t))
        band = not band
    return "\n".join(out)

def page(path, title, desc, h1, lead, body, breadcrumb=None, faq=None,
         extra_ld=None, eyebrow=None, aktionen=None, schluss=None, formular=False,
         noindex=False):
    url = DOMAIN + path
    cur = ' aria-current="page"'
    nav = "\n".join(
        '<li><a href="%s"%s>%s</a></li>' % (u, cur if u == path else "", n)
        for u, n in NAV)
    crumb = ""
    if breadcrumb:
        parts = " &rsaquo; ".join(
            ('<a href="%s">%s</a>' % (u, n)) if u != path else ("<span>%s</span>" % n)
            for u, n in breadcrumb)
        crumb = '<div class="wrap crumb">%s</div>' % parts
    lds = [ORG]
    if breadcrumb: lds.append(crumbs(breadcrumb))
    if faq: lds.append(faq_ld(faq))
    if extra_ld: lds.append(extra_ld)
    ldtags = "\n".join('<script type="application/ld+json">%s</script>'
                       % json.dumps(l, ensure_ascii=False) for l in lds)

    robots = '<meta name="robots" content="noindex, follow">' if noindex else ""
    formular_js = '<script src="/assets/formular.js" defer></script>' if formular else ""
    eb = '<p class="eyebrow">%s</p>' % eyebrow if eyebrow else ""
    ld_html = '<p class="lead">%s</p>' % lead if lead else ""
    akt = ""
    if aktionen:
        akt = '<div class="aktionen">%s</div>' % "".join(
            '<a class="cta%s" href="%s">%s</a>' % (" ghost" if g else "", u, t)
            for t, u, g in aktionen)
    schluss_html = ""
    if schluss:
        st, sp, sb, su = schluss
        schluss_html = f'''<section class="schluss"><div class="wrap inner">
<div><h2>{st}</h2><p>{sp}</p></div>
<div><a class="cta ghost" href="{su}">{sb}</a></div>
</div></section>'''

    doc = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
{robots}
<link rel="icon" href="/assets/favicon.png" type="image/png">
<link rel="stylesheet" href="/assets/style.css">
<meta name="theme-color" content="#E6A83C">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/logo-hvm.jpg">
<meta property="og:locale" content="de_DE">
{ldtags}
</head>
<body>
<div class="kennlinie"><i></i><i></i><i></i><i></i></div>
<header class="site"><div class="wrap head">
<a class="marke" href="/"><img src="/assets/logo-hvm.png" alt="{FIRMA}" width="132" height="114"></a>
<button class="navtoggle" type="button" aria-expanded="false" aria-controls="hauptmenue"
  aria-label="Menü öffnen"><span></span></button>
<nav class="main" id="hauptmenue" aria-label="Hauptnavigation"><ul>
{nav}
<li class="nav-cta"><a href="/kontakt/">Angebot anfragen</a></li>
</ul></nav>
<a class="cta klein kopf-cta" href="/kontakt/">Angebot anfragen</a>
</div></header>
{crumb}
<main>
<div class="hero"><svg class="haus" viewBox="0 0 240 170" fill="none" aria-hidden="true">
<path d="M20 165V78L120 12l100 66v87" stroke="currentColor" stroke-width="9"
 stroke-linejoin="round"/></svg>
<div class="wrap inner">
{eb}
<h1>{h1}</h1>
{ld_html}
{akt}
</div></div>
{sektionen(body)}
{schluss_html}
</main>
<footer class="site"><div class="wrap">
<div class="fgrid">
<div>
<p class="wortmarke"><span>HV</span><b>M</b></p>
<p class="marke-zeile">Hausverwaltung Müller GmbH</p>
<p class="claim">Immobilienverwaltung für Eigentümergemeinschaften und Vermieter
in Potsdam und Brandenburg.</p>
</div>
<div><h4>Leistungen</h4><ul>
<li><a href="/weg-verwaltung-potsdam/">WEG-Verwaltung</a></li>
<li><a href="/mietverwaltung-potsdam/">Mietverwaltung</a></li>
<li><a href="/sondereigentumsverwaltung-potsdam/">Sondereigentumsverwaltung</a></li>
</ul></div>
<div><h4>Ratgeber</h4><ul>
<li><a href="/ratgeber/hausverwaltung-weg-kuendigen/">Hausverwaltung kündigen</a></li>
<li><a href="/ratgeber/verwalterwechsel-weg/">Verwalterwechsel</a></li>
<li><a href="/ratgeber/was-darf-eine-hausverwaltung/">Was darf eine Hausverwaltung?</a></li>
<li><a href="/ratgeber/zertifizierter-verwalter/">Zertifizierter Verwalter</a></li>
<li><a href="/vorlagen/">Muster und Vorlagen</a></li>
</ul></div>
<div><h4>Kontakt</h4><ul>
<li>{FIRMA}</li><li>{STRASSE}</li><li>{PLZORT}</li>
<li><a href="tel:{TEL_LINK}">{TEL}</a></li>
<li><a href="mailto:{MAIL}">{MAIL}</a></li>
</ul></div>
</div>
<div class="legal">
<div>{FIRMA} | Amtsgericht Düsseldorf, HRB 104762 | Geschäftsführer: Timo Müller</div>
<div class="rechts"><a href="/impressum/">Impressum</a>
<a href="/datenschutz/">Datenschutz</a></div>
</div>
</div></footer>
{formular_js}
<script>
(function(){{
  var b=document.querySelector('.navtoggle'), n=document.getElementById('hauptmenue'),
      h=document.querySelector('header.site');
  if(b&&n){{b.addEventListener('click',function(){{
    var o=b.getAttribute('aria-expanded')==='true';
    b.setAttribute('aria-expanded',String(!o));
    b.setAttribute('aria-label',o?'Menü öffnen':'Menü schließen');
    n.classList.toggle('offen',!o);
  }});}}
  if(h){{var f=function(){{h.classList.toggle('fixiert',window.scrollY>8);}};
    f();window.addEventListener('scroll',f,{{passive:true}});}}
}})();
</script>
</body>
</html>
"""
    target = SITE / (path.lstrip("/") or "") / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(doc, encoding="utf-8")
    return path
