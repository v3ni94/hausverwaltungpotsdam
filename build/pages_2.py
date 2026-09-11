# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,"/home/user/hausverwaltungpotsdam/build")
from gen_site import *
from pages_1 import CTA_WEG, CTA_MIET, CTA_SEV, RECHT

# ---------------------------------------------------------------- Mietverwaltung
faq_miet = [
 ("Was unterscheidet Mietverwaltung von WEG-Verwaltung?",
  "Die WEG-Verwaltung verwaltet das gemeinschaftliche Eigentum einer "
  "Eigentümergemeinschaft und ist deren Organ. Die Mietverwaltung handelt im Auftrag "
  "eines Eigentümers und betreut das Mietverhältnis, also Mieterkommunikation, "
  "Zahlungen, Abrechnungen und Instandhaltung des jeweiligen Objekts."),
 ("Wie wird die Mietverwaltung vergütet?",
  "Die Vergütung richtet sich nach Objekt, Einheitenzahl, Zustand und vereinbartem "
  "Leistungsumfang. Sie wird im Verwaltervertrag festgelegt. Leistungen außerhalb der "
  "Grundverwaltung werden gesondert vereinbart."),
 ("Bis wann muss die Nebenkostenabrechnung vorliegen?",
  "Für die Abrechnung von Betriebskosten gelten gesetzliche Fristen, die sich nach dem "
  "Abrechnungszeitraum bemessen. Die konkrete Frist ist im Einzelfall zu prüfen. Wir "
  "planen die Abrechnung so, dass die Unterlagen rechtzeitig vor Fristablauf vorliegen."),
]
page("/mietverwaltung-potsdam/",
 "Mietverwaltung Potsdam für Vermieter | Hausverwaltung Müller",
 "Mietverwaltung in Potsdam: Mieterkommunikation, Zahlungsverkehr, "
 "Nebenkostenabrechnung und Instandhaltung. Angebot für Ihr Objekt anfragen.",
 "Mietverwaltung in Potsdam",
 "Verwaltung vermieteter Objekte für Eigentümer und Kapitalanleger: "
 "laufender Betrieb, Abrechnung und Instandhaltung aus einer Hand.",
 f"""
<p>Vermietung ist ein laufender Betrieb. Mieteingänge, Rückstände, Schäden,
Wartungstermine, Abrechnungsfristen und Mieterwechsel müssen ohne Lücken
zusammenlaufen. Fehlt die Struktur, entstehen Ausfälle, verspätete Abrechnungen und
vermeidbare Konflikte.</p>

<h2>Leistungsbereiche in der Mietverwaltung</h2>
<ul>
<li>Ansprechpartner für Mieter und Abstimmung mit dem Eigentümer,</li>
<li>Überwachung der Mieteingänge und Mahnwesen im vereinbarten Umfang,</li>
<li>Betriebs- und Nebenkostenabrechnung,</li>
<li>Abwicklung von Schäden und Versicherungsfällen im vereinbarten Umfang,</li>
<li>Beauftragung und Kontrolle von Handwerkern und Dienstleistern,</li>
<li>Überwachung von Wartungs- und Versorgungsverträgen,</li>
<li>Vorbereitung von Mieterwechseln, Übergaben und Abnahmen,</li>
<li>Dokumentation und Auskunft gegenüber dem Eigentümer.</li>
</ul>

<h2>Aktuelle Pflichten, die Vermieter betreffen</h2>
<p>Zwei Themen sind derzeit besonders relevant und sollten frühzeitig geprüft werden:</p>
<div class="scroll"><table>
<tr><th>Thema</th><th>Kern</th><th>Zeitbezug</th></tr>
<tr><td>Fernablesbare Verbrauchserfassung</td>
<td>Nicht fernablesbare Ausstattungen sind nach § 5 HeizkostenV grundsätzlich
nachzurüsten oder auszutauschen. Für technisch unmögliche oder unzumutbare Fälle
sind Ausnahmen geregelt.</td>
<td>grundsätzlich bis 31.12.2026</td></tr>
<tr><td>Prüfung älterer Heizungsanlagen</td>
<td>Für bestimmte wassergeführte Heizungsanlagen in Gebäuden mit mindestens sechs
Wohnungen oder Nutzungseinheiten ist eine Prüfung und Optimierung vorgesehen.</td>
<td>für Anlagen von vor Oktober 2009 grundsätzlich bis 30.09.2027</td></tr>
</table></div>
<p>Beide Punkte sind vor einer Maßnahme am aktuellen Verordnungs- und Gesetzestext
zu prüfen. Wir stimmen die Umsetzung mit Ihnen und den Dienstleistern ab.</p>

<h2>Angebot für Ihr Objekt</h2>
<p>Für ein Angebot benötigen wir Angaben zur Lage und Größe des Objekts, zur Anzahl
der Einheiten, zum Zustand, zu bestehenden Verträgen sowie zu laufenden
Rückständen oder Streitfällen.</p>
{CTA_MIET}

<h2>Häufige Fragen zur Mietverwaltung</h2>
{faq_html(faq_miet)}
{RECHT}
""",
 breadcrumb=[("/","Start"),("/mietverwaltung-potsdam/","Mietverwaltung Potsdam")],
 faq=faq_miet, eyebrow="Leistung",
 aktionen=[("Angebot anfragen","/kontakt/?anliegen=miete",False),
           ("Leistungen ansehen","#leistungsbereiche-in-der-mietverwaltung",True)],
 schluss=("Mietverwaltung für Ihr Objekt",
  "Nennen Sie uns Lage, Größe, Einheitenzahl und bestehende Verträge. Auf dieser "
  "Grundlage stimmen wir den Leistungsumfang mit Ihnen ab.",
  "Angebot anfragen","/kontakt/?anliegen=miete"))

# ---------------------------------------------------------------- SEV
faq_sev = [
 ("Brauche ich eine SEV, wenn die WEG bereits eine Verwaltung hat?",
  "Die WEG-Verwaltung betreut das gemeinschaftliche Eigentum und ist nicht für Ihr "
  "Mietverhältnis zuständig. Wenn Sie Ihre Einheit vermieten, deckt die "
  "Sondereigentumsverwaltung genau diesen Bereich ab, also Mieter, Zahlungen, "
  "Abrechnung und Instandhaltung innerhalb Ihrer Wohnung."),
 ("Kann die SEV von einer anderen Firma erbracht werden als die WEG-Verwaltung?",
  "Ja. Beide Aufträge haben unterschiedliche Auftraggeber. Die WEG-Verwaltung wird von "
  "der Gemeinschaft bestellt, die Sondereigentumsverwaltung beauftragt der einzelne "
  "Eigentümer. Eine Abstimmung zwischen beiden ist in der Praxis sinnvoll."),
 ("Vertritt die SEV mich in der Eigentümerversammlung?",
  "Nur wenn Sie dies ausdrücklich vereinbaren und eine entsprechende Vollmacht "
  "erteilen. Umfang und Grenzen einer solchen Vollmacht sollten schriftlich und "
  "eindeutig festgelegt werden."),
]
page("/sondereigentumsverwaltung-potsdam/",
 "Sondereigentumsverwaltung Potsdam (SEV) | Hausverwaltung Müller",
 "Sondereigentumsverwaltung in Potsdam: Verwaltung Ihrer vermieteten Einheit "
 "innerhalb einer Eigentümergemeinschaft. Unterschied zur WEG-Verwaltung erklärt.",
 "Sondereigentumsverwaltung in Potsdam",
 "Verwaltung Ihrer vermieteten Wohnung innerhalb einer bestehenden "
 "Eigentümergemeinschaft, klar abgegrenzt zur WEG-Verwaltung.",
 f"""
<p>Wer eine Wohnung innerhalb einer Eigentümergemeinschaft vermietet, hat zwei
getrennte Ebenen: das gemeinschaftliche Eigentum, das die WEG-Verwaltung betreut,
und die eigene vermietete Einheit. Für die zweite Ebene ist die
Sondereigentumsverwaltung, kurz SEV, zuständig.</p>

<h2>SEV und WEG-Verwaltung im Vergleich</h2>
<div class="scroll"><table>
<tr><th>Merkmal</th><th>WEG-Verwaltung</th><th>Sondereigentumsverwaltung</th></tr>
<tr><td>Auftraggeber</td><td>Gemeinschaft der Wohnungseigentümer</td>
<td>einzelner Eigentümer</td></tr>
<tr><td>Grundlage</td><td>Bestellung durch Beschluss und Verwaltervertrag</td>
<td>Dienstleistungsvertrag mit dem Eigentümer</td></tr>
<tr><td>Gegenstand</td><td>gemeinschaftliches Eigentum</td>
<td>die vermietete Einheit und das Mietverhältnis</td></tr>
<tr><td>Typische Aufgaben</td>
<td>Versammlung, Wirtschaftsplan, Jahresabrechnung, Instandhaltung am Gemeinschaftseigentum</td>
<td>Mieterkommunikation, Mieteingänge, Nebenkosten, Instandhaltung in der Wohnung</td></tr>
<tr><td>Ansprechpartner des Mieters</td><td>in der Regel nicht zuständig</td>
<td>zuständig</td></tr>
</table></div>

<h2>Leistungsbereiche der SEV</h2>
<ul>
<li>Ansprechpartner für Ihren Mieter,</li>
<li>Überwachung der Mietzahlungen und Mahnwesen im vereinbarten Umfang,</li>
<li>Abrechnung der auf den Mieter umlegbaren Kosten,</li>
<li>Abstimmung mit der WEG-Verwaltung, soweit erforderlich,</li>
<li>Instandhaltung und Reparaturen innerhalb der Einheit,</li>
<li>Vorbereitung von Mieterwechsel, Übergabe und Abnahme,</li>
<li>Dokumentation und Auskunft gegenüber Ihnen als Eigentümer.</li>
</ul>

<h2>Verwaltung für Ihre Einheit anfragen</h2>
<p>Nennen Sie uns Objekt, Lage, Größe der Einheit, den aktuellen Mietstatus und ob
eine WEG-Verwaltung bereits bestellt ist. Auf dieser Grundlage nennen wir Ihnen den
möglichen Leistungsumfang.</p>
{CTA_SEV}

<h2>Häufige Fragen zur Sondereigentumsverwaltung</h2>
{faq_html(faq_sev)}
{RECHT}
""",
 breadcrumb=[("/","Start"),("/sondereigentumsverwaltung-potsdam/","Sondereigentumsverwaltung Potsdam")],
 faq=faq_sev, eyebrow="Leistung",
 aktionen=[("Angebot anfragen","/kontakt/?anliegen=sev",False),
           ("Unterschied zur WEG-Verwaltung","#sev-und-weg-verwaltung-im-vergleich",True)],
 schluss=("Verwaltung für Ihre Einheit",
  "Teilen Sie uns Objekt, Lage, Größe und den aktuellen Mietstatus mit. Wir nennen "
  "Ihnen den möglichen Leistungsumfang.",
  "Angebot anfragen","/kontakt/?anliegen=sev"))
print("teil 2 ok")
