# SEO- und Content-System Hausverwaltung Müller GmbH

Arbeitsgrundlage für den Aufbau von hausverwaltungpotsdam.de als lokales
Fachinformationssystem für WEG-Verwaltung, Mietverwaltung und
Sondereigentumsverwaltung in Potsdam und Brandenburg.

Stand der Recherche: 10.09.2026.

## Struktur

| Pfad | Inhalt |
|---|---|
| `docs/00-strategie.md` | Positionierung, rechtliche Leitplanken, Quellenhierarchie, Content-Cluster, offene Punkte |
| `docs/01-content-bausteine.md` | Seitenmatrix der sechs Kernthemen, FAQ-Bausteine, Themenpriorisierung Herbst 2026 |
| `docs/02-landingpage-beispiel.md` | Vollständige Beispiel-Landingpage Verwalterwechsel inkl. Metadaten, FAQ, interne Links |
| `docs/03-prozesse-und-redaktionsplan.md` | Vorlagenvergleich, Timeline, Prozessdiagramme, Redaktionsplan über drei Monate |
| `docs/04-technisches-seo.md` | Technischer Prüfpfad, Core Web Vitals, Structured Data, SEO-Primärquellen |
| `prompts/masterprompt-hausverwaltung-mueller.txt` | Masterprompt als System- oder Projektprompt |
| `vorlagen/` | Muster für Beschlussprotokoll, Verwaltervertrag und Vollmacht |
| `keywords/keyword-portfolio.csv` | 30 Keywords mit Intent, Priorität und Zielseite |
| `schema/` | JSON-LD-Vorlagen für Organization, LocalBusiness und FAQPage |

## Anwendung des Masterprompts

Der Masterprompt wird als System- oder Projektprompt gesetzt. Anschließend
werden die Auftragsvariablen belegt, zum Beispiel:

```text
{{FORMAT}} = Blogartikel
{{THEMA}} = Wie kündige ich die Hausverwaltung einer WEG?
{{PRIMARY_KEYWORD}} = hausverwaltung kündigen weg
{{SECONDARY_KEYWORDS}} =
weg verwalter abberufen,
verwaltervertrag kündigen,
hausverwaltung wechseln,
verwalterwechsel weg

{{ZIELGRUPPE}} =
Wohnungseigentümer und Verwaltungsbeiräte in Potsdam/Brandenburg

{{TEXTLAENGE}} = 1.800 Wörter
{{CONVERSION_ZIEL}} = Anfrage für einen Verwalterwechsel
{{CTA}} = Verwalterwechsel unverbindlich besprechen

{{INTERNE_LINKZIELE}} =
/weg-verwaltung-potsdam/
/ratgeber/verwalterwechsel-weg/
/vorlagen/bestellung-hausverwaltung-protokoll/

{{QUELLEN_STICHTAG}} = 10.09.2026
```

Danach genügt:

```text
Führe den Masterprompt mit diesen Variablen aus.
Recherchiere zuerst den aktuellen Rechtsstand.
Erstelle anschließend den vollständigen Blogartikel einschließlich
SEO-Metadaten, FAQs, interner Links, Schema und Quellen.
```

## Vor dem Rollout zu klären

1. Technische Erreichbarkeit und Indexierbarkeit der Domain prüfen.
2. CI-Daten (Logo, Farben, Schriften), Anschrift, Telefon, E-Mail, Status der
   § 34c-Erlaubnis und der Zertifizierung nach § 26a WEG bestätigen.
3. Keyword-Bandbreiten in einem Live-Tool validieren.

## Rechtlicher Hinweis

Sämtliche Rechtsangaben in diesem Repository sind eine Einschätzung auf Basis
der zum Stichtag recherchierten Quellen und keine Rechtsberatung. Vor
Veröffentlichung oder Verwendung ist der aktuelle Stand der jeweiligen Norm zu
prüfen. Bei streitigen oder haftungsrelevanten Themen ist eine Prüfung durch
einen Rechtsanwalt oder Fachanwalt für Wohnungseigentumsrecht zu empfehlen.
