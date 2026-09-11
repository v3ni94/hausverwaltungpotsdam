# Technisches SEO und Structured Data

## Technischer Startpunkt

Die Domain hausverwaltungpotsdam.de war im Rahmen der Recherche nicht direkt
abrufbar. Vor dem Publizieren neuer Inhalte ist daher zuerst der technische
Unterbau zu verifizieren.

Reihenfolge:

DNS und HTTPS → HTTP-Statuscodes → robots.txt → `noindex` → Canonicals →
XML-Sitemap → Search Console → URL Inspection → interne Navigation →
Core Web Vitals → Schema.

Google empfiehlt bei fehlender Sichtbarkeit ausdrücklich, zuerst zu prüfen, ob
technische Anforderungen das Crawling oder Indexieren verhindern, und nennt die
Sitemap als zusätzliche Möglichkeit, relevante URLs bekannt zu machen.

## Core Web Vitals

| Kennzahl | Zielwert "gut" |
|---|---|
| LCP, Largest Contentful Paint | kleiner oder gleich 2,5 Sekunden |
| INP, Interaction to Next Paint | unter 200 ms |
| CLS, Cumulative Layout Shift | unter 0,1 |

Praktisch bedeutet das: keine großen unkomprimierten Hero-Bilder,
Logoabmessungen im HTML reservieren, Fonts sparsam laden, überflüssiges
JavaScript vermeiden, Bilder in passenden modernen Formaten bereitstellen und
PDFs nicht als Ersatz für die indexierbare HTML-Vorlagenseite verwenden. Die
Kerninformation sollte als HTML sichtbar bleiben.

## Structured Data

JSON-LD ist das bevorzugte Format. Strukturierte Daten müssen den sichtbaren
Inhalt der jeweiligen Seite widerspiegeln. Markup vor Veröffentlichung mit dem
Rich Results Test validieren und anschließend gegebenenfalls mit URL Inspection
prüfen.

Vorlagen:

- `schema/organization.json`
- `schema/localbusiness.json` (nur bei tatsächlich lokal tätigem oder
  besuchbarem Geschäftssitz)
- `schema/faqpage.json`

Grundsatz: Solange Anschrift, Logo, Telefonnummer, Farben, Zertifizierungsstatus
und Öffnungszeiten nicht verifiziert vorliegen, bleiben sie Platzhalter. Das ist
besser als eine vermeintlich vollständige Ausgabe mit erfundenen Firmendaten.
Keine erfundenen Ratings, Reviews, Geo-Koordinaten, Öffnungszeiten, Anschriften
oder Telefonnummern markieren.

## SEO-Primärquellen

- Google Search Essentials: people-first Content, Suchbegriffe in relevanten
  Seitenelementen, crawlbare Links.
- Google SEO Starter Guide: gut lesbare, eigenständige, aktuelle und hilfreiche
  Inhalte, logisch verständliche Seitenstruktur und interne Verlinkung.
- Google GenAI-Richtlinie: generative KI für Recherche und Strukturierung ist
  zulässig, massenhafter Content ohne zusätzlichen Nutzerwert kann gegen die
  Regeln zu scaled content abuse verstoßen.
- Für AI Overviews und AI Mode gelten laut Google weiterhin die normalen
  SEO-Grundlagen. Eine indexierbare, für normale Snippets geeignete Seite ist
  Voraussetzung, spezielles AI-Markup wird nicht benötigt.

## Gesamtbewertung

Der größte SEO-Hebel liegt nicht darin, möglichst viele generische Texte über
Immobilienverwaltung zu veröffentlichen. Er liegt in der Verbindung von lokalem
Commercial Intent ("WEG-Verwaltung Potsdam"), akutem Problem-Intent
("Hausverwaltung kündigen", "Verwalter wechseln"), hochwertigen editierbaren
Vorlagen und rechtlich sauber gepflegten Aktualitätsthemen. Gleichzeitig muss
die Domain technisch wieder zuverlässig abruf- und indexierbar sein, bevor ein
Content-Ausbau sein volles Potenzial entfalten kann.
