# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,"/home/user/hausverwaltungpotsdam/build")
from gen_site import *

CTA_WEG = '<p><a class="cta" href="/kontakt/?anliegen=weg">Angebot für Ihre WEG-Verwaltung anfragen</a></p>'
CTA_MIET = '<p><a class="cta" href="/kontakt/?anliegen=miete">Angebot für Ihre Mietverwaltung anfragen</a></p>'
CTA_SEV = '<p><a class="cta" href="/kontakt/?anliegen=sev">Angebot für Ihre Einheit anfragen</a></p>'
RECHT = ('<div class="hinweis"><strong>Hinweis:</strong> Die Angaben auf dieser Seite '
 'sind eine allgemeine Information und keine Rechtsberatung. Der Stand der genannten '
 'Vorschriften ist vor einer Entscheidung zu prüfen. Bei streitigen oder '
 'haftungsrelevanten Fragen empfehlen wir die Einschaltung eines Rechtsanwalts oder '
 'Fachanwalts für Wohnungseigentumsrecht.</div>')

# ---------------------------------------------------------------- Startseite
page("/", "Hausverwaltung Potsdam: WEG- und Mietverwaltung | Müller",
 "Hausverwaltung Müller GmbH: WEG-Verwaltung, Mietverwaltung und "
 "Sondereigentumsverwaltung für Eigentümergemeinschaften und Vermieter in Potsdam.",
 "Hausverwaltung in Potsdam für Eigentümer und Vermieter",
 "Die Hausverwaltung Müller GmbH verwaltet Wohnungseigentum und Mietobjekte in "
 "Potsdam und Brandenburg. Klare Zuständigkeiten, nachvollziehbare Finanzprozesse "
 "und geordnete Kommunikation.",
 f"""
<p>Ob Eigentümergemeinschaft, Kapitalanleger oder Vermieter einer einzelnen Einheit:
Verwaltung ist vor allem eine Frage geordneter Abläufe. Beschlüsse, Abrechnungen,
Dienstleister, Schadensfälle und Fristen müssen zusammenpassen und jederzeit
nachvollziehbar sein.</p>

<p>Wir prüfen mit Ihnen zuerst die Ausgangslage und benennen, welche Informationen
für ein belastbares Angebot erforderlich sind. Erst danach sprechen wir über
Leistungsumfang und Vergütung.</p>

<h2>Unsere Leistungsbereiche</h2>
<div class="cards">
<div class="card"><h3>WEG-Verwaltung</h3>
<p>Verwaltung von Eigentümergemeinschaften: Versammlungen, Beschlussumsetzung,
Wirtschaftsplan, Jahresabrechnung, technische Koordination.</p>
<a href="/weg-verwaltung-potsdam/">WEG-Verwaltung ansehen</a></div>
<div class="card"><h3>Mietverwaltung</h3>
<p>Verwaltung vermieteter Objekte: Mieterkommunikation, Zahlungsverkehr,
Nebenkostenabrechnung, Instandhaltung und Dienstleistersteuerung.</p>
<a href="/mietverwaltung-potsdam/">Mietverwaltung ansehen</a></div>
<div class="card"><h3>Sondereigentumsverwaltung</h3>
<p>Verwaltung der einzelnen vermieteten Einheit innerhalb einer bestehenden
Eigentümergemeinschaft, abgegrenzt zur WEG-Verwaltung.</p>
<a href="/sondereigentumsverwaltung-potsdam/">SEV ansehen</a></div>
</div>

<h2>Sie denken über einen Verwalterwechsel nach?</h2>
<p>Ein Wechsel gelingt, wenn Abberufung, Bestellung, Vertrag und Übergabe
aufeinander abgestimmt sind. Diese vier Punkte werden in der Praxis häufig
vermischt, was vermeidbare Verzögerungen verursacht.</p>
<ul>
<li>Die <strong>Abberufung</strong> betrifft das Amt des Verwalters.</li>
<li>Der <strong>Verwaltervertrag</strong> ist davon rechtlich zu trennen.</li>
<li>Die <strong>Bestellung</strong> der neuen Verwaltung erfolgt durch Beschluss.</li>
<li>Die <strong>Übergabe</strong> entscheidet, ob die neue Verwaltung arbeitsfähig ist.</li>
</ul>
<p><a class="cta ghost" href="/ratgeber/verwalterwechsel-weg/">Ablauf eines Verwalterwechsels
Schritt für Schritt</a></p>

<h2>Ratgeber und Arbeitsvorlagen</h2>
<p>Für Eigentümer und Verwaltungsbeiräte stellen wir die häufigsten Fragen
strukturiert dar und bieten Mustervorlagen zum Herunterladen an.</p>
<div class="cards">
<div class="card"><h3>Hausverwaltung kündigen</h3>
<p>Abberufung, Vertrag, Zuständigkeit und Ablauf in der Eigentümerversammlung.</p>
<a href="/ratgeber/hausverwaltung-weg-kuendigen/">Zum Beitrag</a></div>
<div class="card"><h3>Was darf eine Hausverwaltung?</h3>
<p>Interne Befugnisse, Vertretung nach außen und beschlusspflichtige Vorgänge.</p>
<a href="/ratgeber/was-darf-eine-hausverwaltung/">Zum Beitrag</a></div>
<div class="card"><h3>Mustervorlagen</h3>
<p>Beschlussprotokoll, Verwaltervertrag und Vollmacht als PDF.</p>
<a href="/vorlagen/">Zu den Vorlagen</a></div>
</div>
{RECHT}
""",
 eyebrow="Potsdam und Brandenburg",
 aktionen=[("Angebot anfragen","/kontakt/",False),
           ("Leistungen ansehen","/weg-verwaltung-potsdam/",True)],
 schluss=("Sie möchten ein Angebot?",
  "Nennen Sie uns Objekt, Einheitenzahl und Ihren gewünschten Übernahmezeitpunkt. "
  "Wir sagen Ihnen, welche Unterlagen wir für ein belastbares Angebot benötigen.",
  "Angebot anfragen","/kontakt/"))

# ---------------------------------------------------------------- WEG-Verwaltung
faq_weg = [
 ("Kann eine WEG den Verwalter jederzeit abberufen?",
  "Nach § 26 Abs. 3 WEG kann ein Verwalter jederzeit abberufen werden. Der zugehörige "
  "Verwaltervertrag muss hiervon getrennt betrachtet werden und endet nach dem Gesetz "
  "spätestens sechs Monate nach der Abberufung."),
 ("Wie lange darf eine WEG-Verwaltung bestellt werden?",
  "Grundsätzlich ist eine Bestellung für höchstens fünf Jahre möglich. Bei der ersten "
  "Bestellung nach der Begründung von Wohnungseigentum liegt die gesetzliche Höchstdauer "
  "bei drei Jahren."),
 ("Wie früh muss zur Eigentümerversammlung eingeladen werden?",
  "§ 24 Abs. 4 WEG bestimmt, dass die Einberufungsfrist grundsätzlich mindestens drei "
  "Wochen betragen soll, sofern kein Fall besonderer Dringlichkeit vorliegt."),
 ("Wer unterschreibt den Vertrag mit der neuen Hausverwaltung?",
  "Gegenüber dem Verwalter wird die Gemeinschaft der Wohnungseigentümer grundsätzlich "
  "durch den Vorsitzenden des Verwaltungsbeirats oder einen durch Beschluss ermächtigten "
  "Wohnungseigentümer vertreten. Die konkrete Vertragsvollmacht sollte im Beschluss "
  "eindeutig geregelt werden."),
 ("Muss das Protokoll der Eigentümerversammlung unterschrieben werden?",
  "Ja. Die Niederschrift ist nach § 24 Abs. 6 WEG vom Vorsitzenden und einem "
  "Wohnungseigentümer sowie, sofern ein Verwaltungsbeirat bestellt ist, zusätzlich von "
  "dessen Vorsitzenden oder Vertreter zu unterschreiben."),
]
page("/weg-verwaltung-potsdam/",
 "WEG-Verwaltung Potsdam: Eigentümergemeinschaften | Müller",
 "WEG-Verwaltung in Potsdam: Eigentümerversammlung, Beschlussumsetzung, "
 "Wirtschaftsplan und Jahresabrechnung. Angebot für Ihre Eigentümergemeinschaft anfragen.",
 "WEG-Verwaltung in Potsdam",
 "Verwaltung von Eigentümergemeinschaften mit klaren Zuständigkeiten, "
 "nachvollziehbarer Buchhaltung und geordneter Vorbereitung der Beschlüsse.",
 f"""
<p>Eine Eigentümergemeinschaft entscheidet gemeinschaftlich, arbeitet aber nur dann
zügig, wenn die Verwaltung die Entscheidungen sauber vorbereitet. Dazu gehören eine
eindeutige Tagesordnung, belastbare Zahlen, eingeholte Angebote und eine
Dokumentation, die auch Jahre später nachvollziehbar ist.</p>

<h2>Leistungsbereiche in der WEG-Verwaltung</h2>
<p>Der konkrete Umfang wird im Verwaltervertrag und in der Leistungsbeschreibung
festgelegt. Typischerweise gehören dazu:</p>
<ul>
<li>Vorbereitung, Einberufung und Durchführung der Eigentümerversammlung,</li>
<li>Umsetzung wirksamer Eigentümerbeschlüsse,</li>
<li>Führung der Beschlusssammlung und der Gemeinschaftsunterlagen,</li>
<li>Wirtschaftsplan, Jahresabrechnung und Vermögensbericht,</li>
<li>Verwaltung der gemeinschaftlichen Zahlungsvorgänge und des Hausgelds,</li>
<li>Forderungsmanagement im vereinbarten Umfang,</li>
<li>Betreuung von Dienstleistungs-, Wartungs- und Versicherungsverträgen,</li>
<li>Koordinierung laufender Instandhaltungsmaßnahmen,</li>
<li>Schadens- und Versicherungsmanagement im vereinbarten Umfang,</li>
<li>Korrespondenz mit Eigentümern, Dienstleistern und Behörden.</li>
</ul>

<h2>Was die Verwaltung selbst entscheiden darf</h2>
<p>Nicht jeder Vorgang muss in die Eigentümerversammlung. § 27 WEG erlaubt und
verpflichtet den Verwalter zu Maßnahmen ordnungsmäßiger Verwaltung, die von
untergeordneter Bedeutung sind und nicht zu erheblichen Verpflichtungen führen,
sowie zu Maßnahmen, die zur Fristwahrung oder zur Abwendung eines Nachteils
erforderlich sind. Die Eigentümer können diese Rechte und Pflichten durch Beschluss
erweitern oder einschränken.</p>
<p>Davon zu unterscheiden ist die Vertretung nach außen. Weitere Einzelheiten finden
Sie im Beitrag <a href="/ratgeber/was-darf-eine-hausverwaltung/">Was darf eine
Hausverwaltung?</a></p>

<h2>Wechsel der WEG-Verwaltung</h2>
<p>Viele Gemeinschaften sprechen uns an, weil ein Wechsel ansteht. Entscheidend ist
dabei die Trennung von Amt und Vertrag:</p>
<div class="scroll"><table>
<tr><th>Vorgang</th><th>Gegenstand</th><th>Zuständigkeit</th></tr>
<tr><td>Bestellung</td><td>Wer ist Verwalter der Gemeinschaft?</td>
<td>Beschluss der Wohnungseigentümer</td></tr>
<tr><td>Abberufung</td><td>Beendigung des Amtes</td>
<td>Beschluss, nach § 26 Abs. 3 WEG jederzeit möglich</td></tr>
<tr><td>Verwaltervertrag</td><td>Leistungen, Vergütung, Laufzeit</td>
<td>Vertretung nach § 9b Abs. 2 WEG</td></tr>
<tr><td>Übergabe</td><td>Unterlagen, Daten, Konten, offene Vorgänge</td>
<td>organisatorisch zwischen alter und neuer Verwaltung</td></tr>
</table></div>
<p><a class="cta ghost" href="/ratgeber/verwalterwechsel-weg/">Verwalterwechsel Schritt
für Schritt</a></p>

<h2>Angebot anfragen</h2>
<p>Für ein belastbares Angebot benötigen wir in der Regel Angaben zu Objektgröße und
Einheitenzahl, zum Zustand und Sanierungsbedarf, zu laufenden Streit- oder
Versicherungsfällen sowie zur bestehenden Bestellung und Vertragslage.</p>
{CTA_WEG}

<h2>Häufige Fragen zur WEG-Verwaltung</h2>
{faq_html(faq_weg)}
{RECHT}
""",
 breadcrumb=[("/","Start"),("/weg-verwaltung-potsdam/","WEG-Verwaltung Potsdam")],
 faq=faq_weg, eyebrow="Leistung",
 aktionen=[("Angebot anfragen","/kontakt/?anliegen=weg",False),
           ("Ablauf des Wechsels","/ratgeber/verwalterwechsel-weg/",True)],
 schluss=("WEG-Verwaltung in Potsdam anfragen",
  "Wir prüfen mit Ihrer Gemeinschaft die Ausgangslage und benennen, welche Angaben "
  "für ein belastbares Angebot erforderlich sind.",
  "Angebot anfragen","/kontakt/?anliegen=weg"))
print("teil 1 ok")
