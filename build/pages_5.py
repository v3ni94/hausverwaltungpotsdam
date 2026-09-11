# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,"/home/user/hausverwaltungpotsdam/build")
from gen_site import *
from pages_1 import CTA_WEG, RECHT

# ---------------------------------------------------------------- zertifizierter Verwalter
faq_z = [
 ("Ist der zertifizierte Verwalter dasselbe wie die Erlaubnis nach § 34c GewO?",
  "Nein. Die Erlaubnis nach § 34c GewO ist die gewerberechtliche Voraussetzung für die "
  "Tätigkeit als Wohnimmobilienverwalter. Der zertifizierte Verwalter nach § 26a WEG ist "
  "eine zusätzliche Qualifikation, die auf einem Nachweis rechtlicher, kaufmännischer "
  "und technischer Kenntnisse beruht."),
 ("Können Eigentümer einen zertifizierten Verwalter verlangen?",
  "Wohnungseigentümer können im Rahmen ordnungsmäßiger Verwaltung grundsätzlich die "
  "Bestellung eines zertifizierten Verwalters verlangen. Das WEG enthält eine Ausnahme "
  "für bestimmte kleine Gemeinschaften, die von einem Wohnungseigentümer verwaltet "
  "werden."),
 ("Gilt die Zertifizierung auch für juristische Personen?",
  "Bei einer Gesellschaft kommt es darauf an, dass die maßgeblich tätigen Personen die "
  "Anforderungen erfüllen. Die Einzelheiten ergeben sich aus § 26a WEG und der "
  "Zertifizierter-Verwalter-Prüfungsverordnung."),
 ("Gibt es eine Weiterbildungspflicht?",
  "Für erlaubnispflichtige Wohnimmobilienverwalter besteht eine gewerberechtliche "
  "Weiterbildungspflicht von 20 Stunden innerhalb von drei Kalenderjahren. Nachweise "
  "können auf Verlangen vorzulegen sein."),
]
page("/ratgeber/zertifizierter-verwalter/",
 "Zertifizierter Verwalter: Was Eigentümer prüfen sollten",
 "Was bedeutet zertifizierter Verwalter nach § 26a WEG, wie unterscheidet er sich "
 "von der Erlaubnis nach § 34c GewO und was können Eigentümer verlangen?",
 "Zertifizierter Verwalter: Was die Bezeichnung bedeutet",
 "Gewerbeerlaubnis, Zertifizierung und Weiterbildung sind drei verschiedene "
 "Nachweise. Für die Auswahl einer Verwaltung lohnt es, sie auseinanderzuhalten.",
 f"""
<h2>Drei Nachweise, die oft verwechselt werden</h2>
<div class="scroll"><table>
<tr><th>Nachweis</th><th>Grundlage</th><th>Bedeutung</th></tr>
<tr><td>Erlaubnis als Wohnimmobilienverwalter</td><td>§ 34c GewO</td>
<td>Gewerberechtliche Voraussetzung für die Tätigkeit. Geprüft werden unter anderem
Zuverlässigkeit, geordnete Vermögensverhältnisse und der Nachweis einer
Vermögensschadenhaftpflichtversicherung.</td></tr>
<tr><td>Zertifizierter Verwalter</td><td>§ 26a WEG, ZertVerwV</td>
<td>Nachweis rechtlicher, kaufmännischer und technischer Kenntnisse, grundsätzlich
über eine Prüfung bei der Industrie- und Handelskammer. Die Verordnung regelt
zusätzlich Gleichstellungen für bestimmte Qualifikationen.</td></tr>
<tr><td>Weiterbildung</td><td>Gewerberecht</td>
<td>Weiterbildungspflicht von 20 Stunden innerhalb von drei Kalenderjahren für
erlaubnispflichtige Wohnimmobilienverwalter.</td></tr>
</table></div>
<p>Die Erlaubnis ist die Zugangsvoraussetzung, die Zertifizierung eine zusätzliche
Qualifikation. Eine Verwaltung ohne Zertifizierung ist deshalb nicht automatisch
unzulässig tätig, umgekehrt ersetzt die Zertifizierung nicht die Erlaubnis.</p>

<h2>Was Eigentümer verlangen können</h2>
<p>Wohnungseigentümer können im Rahmen ordnungsmäßiger Verwaltung grundsätzlich die
Bestellung eines zertifizierten Verwalters verlangen. Für bestimmte kleine
Gemeinschaften, die von einem Wohnungseigentümer verwaltet werden, sieht das Gesetz
eine Ausnahme vor.</p>

<h2>Worauf es in der Praxis zusätzlich ankommt</h2>
<p>Ein Zertifikat sagt etwas über geprüftes Wissen aus, nicht über die Qualität der
täglichen Arbeit. Bei der Auswahl einer Verwaltung lohnt daher der Blick auf:</p>
<ul>
<li>nachvollziehbare Zuständigkeiten und benannte Ansprechpartner,</li>
<li>transparente Vergütung mit klarer Abgrenzung von Zusatzleistungen,</li>
<li>saubere Dokumentation von Beschlüssen, Verträgen und Maßnahmen,</li>
<li>definierte Kommunikations- und Eskalationswege,</li>
<li>technisches Verständnis und strukturierte Dienstleistersteuerung,</li>
<li>nachvollziehbare Finanzprozesse bei Abrechnung, Wirtschaftsplan und Rücklagen,</li>
<li>geordnete Übergabeprozesse zu Beginn und am Ende der Verwaltung.</li>
</ul>

<h2>Nachweise anfordern</h2>
<p>Fragen Sie im Auswahlverfahren konkret nach den vorliegenden Nachweisen und lassen
Sie sich diese vorlegen. Das ist der zuverlässigste Weg, Angaben zu prüfen, und in der
Vorbereitung eines Beschlusses ohnehin sinnvoll.</p>
{CTA_WEG}

<h2>Häufige Fragen</h2>
{faq_html(faq_z)}
{RECHT}
""",
 breadcrumb=[("/","Start"),("/ratgeber/","Ratgeber"),
             ("/ratgeber/zertifizierter-verwalter/","Zertifizierter Verwalter")],
 faq=faq_z, eyebrow="Ratgeber WEG-Recht",
 schluss=("Verwaltung auswählen",
  "Wir stellen Ihnen die Angaben zusammen, die Sie für den Vergleich mehrerer "
  "Angebote in der Eigentümerversammlung benötigen.",
  "Angebot anfragen","/kontakt/?anliegen=weg"))

# ---------------------------------------------------------------- Vorlagen
DL = """
<div class="dl"><div class="ico">PDF</div><div>
<h3>{t}</h3><p>{d}</p>
<a class="cta ghost" href="/vorlagen/{f}" download>Vorlage herunterladen</a>
</div></div>"""
page("/vorlagen/", "Muster und Vorlagen für Eigentümergemeinschaften | Müller",
 "Kostenlose Muster für Eigentümergemeinschaften: Beschlussprotokoll zur "
 "Verwalterbestellung, Verwaltervertrag und Vollmacht als PDF.",
 "Muster und Vorlagen für Eigentümergemeinschaften",
 "Arbeitsvorlagen für die Vorbereitung von Beschlüssen und Verträgen. "
 "Alle Muster sind auf die konkrete Gemeinschaft anzupassen.",
 f"""
<div class="hinweis"><strong>Wichtig:</strong> Die Muster dienen ausschließlich als
allgemeine Arbeits- und Orientierungshilfe und stellen keine Rechtsberatung dar.
WEG-Beschlüsse, Verträge und Vollmachten müssen auf die konkrete Gemeinschaft, die
Teilungserklärung, die Gemeinschaftsordnung, die bestehende Vertragslage und den
jeweiligen Sachverhalt abgestimmt werden. Vor Verwendung sollte insbesondere bei
einem Verwalterwechsel, einer streitigen Abberufung oder einer weitreichenden
Vollmacht eine Prüfung durch einen im Wohnungseigentumsrecht erfahrenen Rechtsanwalt
oder Fachanwalt erfolgen.</div>

{DL.format(t="Beschlussprotokoll zur Verwalterbestellung",
 d="Niederschrift mit den Beschlussanträgen zur Abberufung, zur Neubestellung und zur "
   "Ermächtigung zum Abschluss des Verwaltervertrags, jeweils mit Abstimmungsfeldern "
   "und den Unterschriftsfeldern nach § 24 Abs. 6 WEG.",
 f="HVM_Muster-Beschlussprotokoll-Verwalterbestellung.pdf")}

{DL.format(t="Verwaltervertrag WEG",
 d="Vertragsmuster mit Vertragsgegenstand, Grund- und Sonderleistungen, Befugnissen, "
   "Eigentümerversammlung, Rechnungswesen, Vergütung, Laufzeit, Versicherung, "
   "Datenschutz und Übergabe.",
 f="HVM_Muster-Verwaltervertrag-WEG.pdf")}

{DL.format(t="Vollmacht",
 d="Vollmacht mit ausdrücklicher Begrenzung nach Vertragsgegenstand, Betrag und Dauer "
   "sowie einer Auflistung der nicht umfassten Vorgänge.",
 f="HVM_Muster-Vollmacht.pdf")}

<h2>Welche Vorlage wofür?</h2>
<div class="scroll"><table>
<tr><th>Vorlage</th><th>Zweck</th><th>Kritischer Punkt</th></tr>
<tr><td>Beschlussprotokoll</td><td>Bestellung und Abberufung dokumentieren</td>
<td>eindeutige Beschlussformulierung und Bestellungszeitraum</td></tr>
<tr><td>Verwaltervertrag</td><td>Leistungen und Vergütung regeln</td>
<td>Bestellung und Vertrag sind zwei verschiedene Vorgänge</td></tr>
<tr><td>Vollmacht</td><td>konkrete Vertretungsbefugnis dokumentieren</td>
<td>Vertretung gegenüber dem Verwalter nach § 9b Abs. 2 WEG beachten</td></tr>
</table></div>

<h2>Hintergrund zu den Vorlagen</h2>
<p>Wie die Muster in einen vollständigen Wechsel eingebettet sind, zeigt der Beitrag
<a href="/ratgeber/verwalterwechsel-weg/">Verwalterwechsel Schritt für Schritt</a>.
Die Unterscheidung von Abberufung und Vertrag erläutert der Beitrag
<a href="/ratgeber/hausverwaltung-weg-kuendigen/">Hausverwaltung einer WEG
kündigen</a>.</p>
{CTA_WEG}
""",
 breadcrumb=[("/","Start"),("/vorlagen/","Vorlagen")],
 eyebrow="Kostenlose Downloads",
 schluss=("Muster auf Ihre Gemeinschaft anpassen",
  "Die Vorlagen sind Ausgangspunkte. Für die konkrete Beschlussfassung stimmen wir "
  "Formulierung und Zeitplan mit Ihnen ab.",
  "Angebot anfragen","/kontakt/"))
print("teil 5 ok")
