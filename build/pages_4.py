# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,"/home/user/hausverwaltungpotsdam/build")
from gen_site import *
from pages_1 import CTA_WEG, RECHT

# ---------------------------------------------------------------- Verwalterwechsel
faq_w = [
 ("Wie lange dauert ein Verwalterwechsel?",
  "Dafür gibt es keine einheitliche gesetzliche Gesamtdauer. Zu berücksichtigen sind "
  "die Versammlungsplanung, die aktuelle Bestellung, der Verwaltervertrag und die "
  "Übergabe. Die Einberufungsfrist für die Eigentümerversammlung soll grundsätzlich "
  "mindestens drei Wochen betragen."),
 ("Wer schließt den Vertrag mit dem neuen Verwalter?",
  "Gegenüber einem Verwalter vertritt nach § 9b Abs. 2 WEG grundsätzlich der "
  "Vorsitzende des Verwaltungsbeirats oder ein durch Beschluss ermächtigter "
  "Wohnungseigentümer die Gemeinschaft."),
 ("Muss die Bestellung im Protokoll stehen?",
  "Gefasste Beschlüsse sind unverzüglich in einer Niederschrift festzuhalten. "
  "§ 24 Abs. 6 WEG regelt außerdem die erforderlichen Unterschriften der Niederschrift."),
 ("Was passiert, wenn die alte Verwaltung Unterlagen nicht herausgibt?",
  "Die der Gemeinschaft zuzuordnenden Unterlagen und Daten sind nach Beendigung der "
  "Verwaltung geordnet zu übergeben. Bleibt die Übergabe aus, sollte der Umfang "
  "schriftlich und mit Fristsetzung angefordert und der Vorgang dokumentiert werden. "
  "Bei anhaltender Weigerung ist rechtlicher Rat zu empfehlen."),
]
page("/ratgeber/verwalterwechsel-weg/",
 "Verwalterwechsel in der WEG: Ablauf Schritt für Schritt",
 "Vom ersten Beschluss bis zur Übergabe: So lässt sich der Wechsel einer "
 "WEG-Verwaltung strukturiert vorbereiten und durchführen.",
 "Verwalterwechsel in der WEG: So läuft er ab",
 "Ein Wechsel besteht aus vier Bausteinen: Ausgangslage, Beschlüsse, Vertrag "
 "und Übergabe. Erst der letzte entscheidet, ob die neue Verwaltung arbeiten kann.",
 f"""
<h2>1. Ausgangslage prüfen</h2>
<p>Zunächst werden der aktuelle Bestellungsbeschluss, der Verwaltervertrag und die
geplante zeitliche Abfolge geprüft. Ziel ist ein klarer Stichtag, zu dem die
bisherige Verwaltung endet und die neue Verwaltung handlungsfähig übernimmt. Sinnvoll
ist eine Abstimmung auf das Wirtschaftsjahr, damit Abrechnungszeiträume nicht
zerschnitten werden.</p>

<h2>2. Anforderungen festlegen</h2>
<p>Bevor Angebote eingeholt werden, sollte die Gemeinschaft definieren, was ihr
wichtig ist: Objektgröße, Sanierungsbedarf, technische Besonderheiten, Zahl der
Eigentümer, laufende Streit- oder Versicherungsfälle, gewünschte digitale Prozesse
sowie Art und Umfang der Kommunikation.</p>

<h2>3. Angebote vergleichen</h2>
<p>Nicht nur die Grundvergütung ist entscheidend, sondern der genaue Leistungsumfang
und die möglichen Zusatzvergütungen. Professionelle Verwaltung umfasst rechtliche,
kaufmännische, technische und organisatorische Aufgaben. Prüfen Sie, welche
Leistungen in der Grundvergütung enthalten sind und welche gesondert berechnet
werden.</p>

<h2>4. Beschlüsse vorbereiten</h2>
<p>Der Gegenstand eines Beschlusses muss bereits bei der Einberufung bezeichnet
werden. Die Einberufungsfrist soll nach § 24 Abs. 4 WEG mindestens drei Wochen
betragen, sofern keine besondere Dringlichkeit vorliegt. Vorzubereiten sind
Abberufung, Neubestellung und die Ermächtigung zum Abschluss des Verwaltervertrags.</p>

<h2>5. Neue Verwaltung bestellen</h2>
<p>Eine Verwalterbestellung kann grundsätzlich für höchstens fünf Jahre erfolgen, bei
der ersten Bestellung nach Begründung von Wohnungseigentum beträgt die gesetzliche
Höchstgrenze drei Jahre. Der Beschluss sollte eindeutig festhalten, welche Verwaltung
bestellt wird, ab wann die Bestellung beginnt und bis zu welchem Zeitpunkt sie gilt.
Die Bestellung sollte nicht unnötig mit allen Einzelheiten des Dienstleistungsvertrags
vermischt werden.</p>

<h2>6. Vertretung beim Vertragsschluss klären</h2>
<p>Gegenüber dem Verwalter selbst vertritt nach § 9b Abs. 2 WEG der Vorsitzende des
Verwaltungsbeirats oder ein durch Beschluss ermächtigter Wohnungseigentümer die
Gemeinschaft. Eine mögliche Beschlussfassung lautet dem Sinn nach:</p>
<div class="box"><p>Der Vorsitzende des Verwaltungsbeirats [Name], ersatzweise der
durch diesen Beschluss ermächtigte Wohnungseigentümer [Name], wird ermächtigt, den
der Eigentümerversammlung vorliegenden Verwaltervertrag im Namen der Gemeinschaft der
Wohnungseigentümer abzuschließen.</p></div>
<p>Die konkrete Formulierung muss auf den Einzelfall und den vorgelegten
Vertragsentwurf abgestimmt werden.</p>

<h2>7. Übergabe organisieren</h2>
<p>Ein guter Wechsel endet nicht mit der Abstimmung. Erst die strukturierte Übergabe
sorgt dafür, dass die neue Verwaltung tatsächlich arbeiten kann. Zu prüfen sind
insbesondere:</p>
<ul>
<li>Beschlusssammlung und Versammlungsunterlagen,</li>
<li>Teilungserklärung und Gemeinschaftsordnung,</li>
<li>Verträge und Versicherungspolicen,</li>
<li>aktuelle Buchhaltungsdaten,</li>
<li>Wirtschaftsplan und Abrechnungsunterlagen,</li>
<li>Konten und Zahlungsprozesse,</li>
<li>offene Forderungen,</li>
<li>laufende Schäden und Versicherungsfälle,</li>
<li>Gewährleistungsfälle,</li>
<li>Wartungs- und Dienstleistungsverträge,</li>
<li>Schlüssel und technische Unterlagen,</li>
<li>Eigentümer- und Kontaktdaten,</li>
<li>laufende gerichtliche oder außergerichtliche Vorgänge.</li>
</ul>
<p>Die Beschlusssammlung ist gesetzlich vorgesehen und grundsätzlich vom Verwalter zu
führen. Für größere Gemeinschaften empfiehlt sich ein schriftliches Übergabeprotokoll
mit Dokumentenliste und eindeutig gekennzeichneten offenen Punkten.</p>

<h2>Zeitliche Orientierung</h2>
<p>Die folgenden Werte sind Planungswerte aus der Praxis, keine gesetzlichen Fristen.
Gesetzlich geregelt ist die Einberufungsfrist von grundsätzlich mindestens drei
Wochen.</p>
<div class="scroll"><table>
<tr><th>Zeitraum</th><th>Schritte</th></tr>
<tr><td>T-10 bis T-8 Wochen</td><td>Bestellungsbeschluss und Vertrag prüfen,
Anforderungen definieren</td></tr>
<tr><td>T-8 bis T-6 Wochen</td><td>Angebote einholen, Kandidaten vergleichen</td></tr>
<tr><td>T-6 bis T-4 Wochen</td><td>Beschlussvorschläge vorbereiten, Vertragsentwurf
abstimmen</td></tr>
<tr><td>mindestens T-3 Wochen</td><td>Einladung zur Eigentümerversammlung,
Tagesordnung eindeutig bezeichnen</td></tr>
<tr><td>T-0</td><td>Beschlüsse über Abberufung, Neubestellung und Ermächtigung</td></tr>
<tr><td>danach</td><td>Verwaltervertrag abschließen, Übergabe terminieren</td></tr>
<tr><td>Wechselstichtag</td><td>Konten und Zugänge, Unterlagen und Daten, offene
Vorgänge</td></tr>
<tr><td>Nachlauf</td><td>Übergabeprotokoll vervollständigen, fehlende Unterlagen
nachfordern</td></tr>
</table></div>
<p>Vorlagen für Protokoll, Vertrag und Vollmacht finden Sie im Bereich
<a href="/vorlagen/">Vorlagen</a>.</p>
{CTA_WEG}

<h2>Häufige Fragen</h2>
{faq_html(faq_w)}
{RECHT}
""",
 breadcrumb=[("/","Start"),("/ratgeber/","Ratgeber"),
             ("/ratgeber/verwalterwechsel-weg/","Verwalterwechsel")],
 faq=faq_w, eyebrow="Ratgeber WEG-Recht",
 aktionen=[("Wechsel besprechen","/kontakt/?anliegen=weg",False),
           ("Vorlagen herunterladen","/vorlagen/",True)],
 schluss=("Übergabe sauber aufsetzen",
  "Den größten Zeitverlust verursacht eine unvollständige Übergabe. Wir stimmen die "
  "Dokumentenliste und den Stichtag mit Ihnen ab.",
  "Wechsel besprechen","/kontakt/?anliegen=weg"))

# ---------------------------------------------------------------- was darf
faq_d = [
 ("Darf die Hausverwaltung ohne Beschluss Handwerker beauftragen?",
  "Für Maßnahmen ordnungsmäßiger Verwaltung von untergeordneter Bedeutung, die nicht "
  "zu erheblichen Verpflichtungen führen, sieht § 27 WEG eine eigene Befugnis vor, "
  "ebenso für Maßnahmen zur Fristwahrung oder zur Abwendung eines Nachteils. Wo die "
  "Grenze liegt, hängt vom Einzelfall und von der Beschlusslage der Gemeinschaft ab."),
 ("Kann die Gemeinschaft die Befugnisse der Verwaltung begrenzen?",
  "Im Innenverhältnis ja. Die Wohnungseigentümer können die Rechte und Pflichten des "
  "Verwalters nach § 27 Abs. 2 WEG durch Beschluss einschränken oder erweitern, etwa "
  "über Betragsgrenzen. Gegenüber Dritten wirkt eine Beschränkung der Vertretungsmacht "
  "nach § 9b WEG grundsätzlich nicht."),
 ("Darf die Verwaltung ein Darlehen für die Gemeinschaft aufnehmen?",
  "Für den Abschluss eines Darlehensvertrags verlangt das Gesetz einen Beschluss der "
  "Wohnungseigentümer. Dasselbe gilt für Grundstückskaufverträge."),
 ("Wer vertritt die Gemeinschaft gegenüber der Verwaltung selbst?",
  "Nach § 9b Abs. 2 WEG der Vorsitzende des Verwaltungsbeirats oder ein durch Beschluss "
  "ermächtigter Wohnungseigentümer."),
]
page("/ratgeber/was-darf-eine-hausverwaltung/",
 "Was darf eine Hausverwaltung und was nicht?",
 "Aufgaben, Befugnisse und Grenzen einer WEG-Verwaltung: Was der Verwalter selbst "
 "entscheiden kann und wann die Eigentümer beschließen müssen.",
 "Was darf eine Hausverwaltung und was darf sie nicht?",
 "Die Antwort hängt an einer Unterscheidung, die in der Praxis oft untergeht: "
 "Dürfen im Innenverhältnis und Vertretenkönnen im Außenverhältnis sind nicht dasselbe.",
 f"""
<h2>Zwei Ebenen, die auseinandergehalten werden müssen</h2>
<p>Wer fragt, was eine Hausverwaltung darf, meint meist zwei verschiedene Dinge:
was sie gegenüber der Gemeinschaft entscheiden darf und was sie gegenüber Dritten
wirksam erklären kann. Das Gesetz behandelt beides getrennt.</p>
<div class="scroll"><table>
<tr><th>Ebene</th><th>Regelung</th><th>Kern</th></tr>
<tr><td>Interne Aufgaben und Befugnisse</td><td>§ 27 WEG</td>
<td>Maßnahmen ordnungsmäßiger Verwaltung von untergeordneter Bedeutung ohne
erhebliche Verpflichtungen, sowie Maßnahmen zur Fristwahrung oder
Nachteilsabwendung. Durch Beschluss erweiterbar und einschränkbar.</td></tr>
<tr><td>Vertretung nach außen</td><td>§ 9b WEG</td>
<td>Der Verwalter vertritt die Gemeinschaft grundsätzlich gerichtlich und
außergerichtlich. Beschränkungen dieser Vertretungsmacht wirken gegenüber Dritten
grundsätzlich nicht.</td></tr>
</table></div>
<p>Daraus folgt eine für Eigentümer wichtige Konsequenz: Eine intern überschrittene
Befugnis macht ein Geschäft mit einem Dritten nicht automatisch unwirksam. Der
Verstoß gegen die interne Kompetenzordnung ist dann eine Frage des Verhältnisses
zwischen Gemeinschaft und Verwalter.</p>

<h2>Was die Verwaltung typischerweise selbst entscheiden kann</h2>
<ul>
<li>laufende Betriebs- und Verwaltungsvorgänge geringen Umfangs,</li>
<li>Kleinreparaturen im Rahmen der Beschlusslage,</li>
<li>Maßnahmen zur Abwendung eines drohenden Nachteils, etwa bei einem Wasserschaden,</li>
<li>fristwahrende Erklärungen, wenn keine Zeit für eine Beschlussfassung bleibt,</li>
<li>Umsetzung bereits gefasster Beschlüsse.</li>
</ul>

<h2>Was einen Beschluss der Eigentümer voraussetzt</h2>
<ul>
<li>Grundstückskaufverträge und Darlehensverträge,</li>
<li>bauliche Veränderungen und größere Instandsetzungsmaßnahmen,</li>
<li>Wirtschaftsplan, Jahresabrechnung und Vermögensbericht in der Beschlussfassung,</li>
<li>Erweiterung oder Einschränkung der Verwalterbefugnisse,</li>
<li>Bestellung und Abberufung des Verwalters selbst.</li>
</ul>

<h2>Eine saubere Kompetenzordnung schützt beide Seiten</h2>
<p>Sinnvoll ist ein Beschluss, der Betragsgrenzen, Zustimmungserfordernisse und
Informationspflichten festlegt. Die Verwaltung weiß dann, wo ihre Entscheidung endet,
und die Gemeinschaft muss nicht jeden Einzelfall in der Versammlung behandeln. Für
abgegrenzte Einzelprojekte empfiehlt sich eine schriftliche Vollmacht mit klarer
Angabe von Gegenstand, Betrag und Dauer. Ein
<a href="/vorlagen/">Vollmachtsmuster</a> steht zum Download bereit.</p>
{CTA_WEG}

<h2>Häufige Fragen</h2>
{faq_html(faq_d)}
{RECHT}
""",
 breadcrumb=[("/","Start"),("/ratgeber/","Ratgeber"),
             ("/ratgeber/was-darf-eine-hausverwaltung/","Was darf eine Hausverwaltung?")],
 faq=faq_d, eyebrow="Ratgeber WEG-Recht",
 schluss=("Kompetenzordnung festlegen",
  "Eine klare Beschlusslage zu Betragsgrenzen und Zustimmungserfordernissen entlastet "
  "Gemeinschaft und Verwaltung gleichermaßen.",
  "Beratung anfragen","/kontakt/?anliegen=weg"))
print("teil 4 ok")
