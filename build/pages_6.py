# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,"/home/user/hausverwaltungpotsdam/build")
from gen_site import *
from pages_1 import RECHT

# ---------------------------------------------------------------- Kontakt
FORMULAR = f"""
<form id="anfrage" method="post" action="/anfrage.php" novalidate>
<input type="hidden" name="quelle" id="quelle" value="">
<p class="hp" aria-hidden="true"><label>Bitte nicht ausfüllen
<input type="text" name="website" tabindex="-1" autocomplete="off"></label></p>

<ol class="fortschritt" aria-hidden="true">
<li data-s="1">Verwaltungsart</li>
<li data-s="2">Objekt</li>
<li data-s="3">Kontakt</li>
<li data-s="4">Prüfen</li>
</ol>

<fieldset class="schritt" data-schritt="1">
<legend>Schritt 1 von 4: Welche Verwaltung benötigen Sie?</legend>
<div class="wahl">
<label><input type="radio" name="verwaltungsart" value="WEG-Verwaltung" required>
<span><b>WEG-Verwaltung</b>Verwaltung einer Eigentümergemeinschaft, auch bei
geplantem Verwalterwechsel.</span></label>
<label><input type="radio" name="verwaltungsart" value="Mietverwaltung">
<span><b>Mietverwaltung</b>Verwaltung eines vermieteten Objekts für den
Eigentümer.</span></label>
<label><input type="radio" name="verwaltungsart" value="Sondereigentumsverwaltung">
<span><b>Sondereigentumsverwaltung</b>Verwaltung einzelner vermieteter Einheiten
innerhalb einer Gemeinschaft.</span></label>
<label><input type="radio" name="verwaltungsart" value="noch offen">
<span><b>Noch offen</b>Die passende Form soll gemeinsam geklärt werden.</span></label>
</div>
</fieldset>

<fieldset class="schritt" data-schritt="2">
<legend>Schritt 2 von 4: Um welches Objekt geht es?</legend>
<label for="strasse">Straße und Hausnummer</label>
<input id="strasse" name="strasse" type="text" autocomplete="street-address" required>
<div class="zeile">
<div><label for="plz">Postleitzahl</label>
<input id="plz" name="plz" type="text" inputmode="numeric" pattern="[0-9]{{5}}"
 maxlength="5" autocomplete="postal-code" required></div>
<div><label for="ort">Ort</label>
<input id="ort" name="ort" type="text" autocomplete="address-level2" required></div>
</div>
<div class="zeile">
<div><label for="einheiten">Anzahl der Einheiten</label>
<input id="einheiten" name="einheiten" type="number" min="1" max="2000" step="1" required></div>
<div><label for="uebernahme">Gewünschte Übernahme <span class="opt">optional</span></label>
<input id="uebernahme" name="uebernahme" type="text" placeholder="z. B. zum 01.01.2027"></div>
</div>
</fieldset>

<fieldset class="schritt" data-schritt="3">
<legend>Schritt 3 von 4: Wie erreichen wir Sie?</legend>
<label for="name">Name</label>
<input id="name" name="name" type="text" autocomplete="name" required>
<label for="rolle">Ihre Funktion <span class="opt">optional</span></label>
<select id="rolle" name="rolle">
<option value="">Bitte wählen</option>
<option>Wohnungseigentümer</option>
<option>Verwaltungsbeirat</option>
<option>Vermieter oder Eigentümer</option>
<option>Hausverwaltung oder Dienstleister</option>
<option>Sonstiges</option>
</select>
<label for="email">E-Mail</label>
<input id="email" name="email" type="email" autocomplete="email" required>
<label for="telefon">Telefon <span class="opt">optional</span></label>
<input id="telefon" name="telefon" type="tel" autocomplete="tel">
<label for="nachricht">Ihr Anliegen <span class="opt">optional</span></label>
<textarea id="nachricht" name="nachricht" rows="5"
 placeholder="Besonderheiten, Sanierungsbedarf, laufende Verfahren, aktuelle Vertragslage"></textarea>
</fieldset>

<fieldset class="schritt" data-schritt="4">
<legend>Schritt 4 von 4: Angaben prüfen und absenden</legend>
<dl class="pruefen" id="zusammenfassung"></dl>
<label class="check"><input type="checkbox" name="datenschutz" value="ja" required>
<span>Ich habe die <a href="/datenschutz/" target="_blank" rel="noopener">Datenschutzerklärung</a>
zur Kenntnis genommen und willige in die Verarbeitung meiner Angaben zur Bearbeitung
der Anfrage ein. Die Einwilligung kann jederzeit für die Zukunft widerrufen werden.</span></label>
</fieldset>

<p class="fehlermeldung" id="fehler" role="alert" hidden></p>

<div class="navigation">
<button type="button" class="cta ghost zurueck" hidden>Zurück</button>
<button type="button" class="cta weiter">Weiter</button>
<button type="submit" class="cta senden">Anfrage absenden</button>
</div>
<p class="formhinweis">Wir melden uns mit den Punkten, die für ein belastbares Angebot
noch zu klären sind. Die Anfrage ist unverbindlich und kostenfrei.</p>
</form>
"""

page("/kontakt/", "Angebot für die Verwaltung anfragen | Hausverwaltung Müller",
 "Angebot für WEG-Verwaltung, Mietverwaltung oder Sondereigentumsverwaltung in "
 "Potsdam anfragen. In vier Schritten zur unverbindlichen Anfrage.",
 "Angebot für die Verwaltung anfragen",
 "Vier kurze Schritte: Verwaltungsart, Objekt, Kontakt, Prüfen. "
 "Danach erhalten Sie von uns eine Rückmeldung mit dem weiteren Vorgehen.",
 f"""
<h2>Direkter Kontakt</h2>
<div class="cards kontaktgrid">
<div class="card"><h3>Telefon</h3><p><a href="tel:{TEL_LINK}">{TEL}</a></p></div>
<div class="card"><h3>E-Mail</h3><p><a href="mailto:{MAIL}">{MAIL}</a></p></div>
<div class="card"><h3>Anschrift</h3><p>{FIRMA}<br>{STRASSE}<br>{PLZORT}</p></div>
</div>

<h2>Anfrage in vier Schritten</h2>
{FORMULAR}

<h2>Was wir für ein Angebot benötigen</h2>
<p>Je vollständiger die Angaben, desto belastbarer die erste Einschätzung.
Entscheidend sind:</p>
<ul>
<li>Art der Verwaltung: WEG, Miete oder Sondereigentum,</li>
<li>vollständige Objektadresse und Anzahl der Einheiten,</li>
<li>bekannter Sanierungs- oder Instandhaltungsbedarf,</li>
<li>bestehende Bestellung und Vertragslage, sofern vorhanden,</li>
<li>laufende Streit-, Gewährleistungs- oder Versicherungsfälle,</li>
<li>gewünschter Übernahmezeitpunkt.</li>
</ul>
<p>Fehlt Ihnen eine Angabe, senden Sie die Anfrage trotzdem. Wir fragen die
offenen Punkte gezielt nach.</p>
{RECHT}
""",
 breadcrumb=[("/","Start"),("/kontakt/","Angebot anfragen")],
 eyebrow="Unverbindlich und kostenfrei", formular=True)

# ---------------------------------------------------------------- Danke
page("/kontakt/danke/", "Anfrage eingegangen | Hausverwaltung Müller GmbH",
 "Ihre Anfrage ist bei der Hausverwaltung Müller GmbH eingegangen.",
 "Vielen Dank für Ihre Anfrage",
 "Ihre Angaben sind bei uns eingegangen. Wir melden uns mit dem weiteren Vorgehen "
 "und den Punkten, die für ein Angebot noch zu klären sind.",
 f"""
<h2>Wie es weitergeht</h2>
<ol class="schritte">
<li><h3>Prüfung Ihrer Angaben</h3><p>Wir sehen uns Objekt, Einheitenzahl und die
gewünschte Verwaltungsart an und ordnen den Aufwand ein.</p></li>
<li><h3>Rückmeldung</h3><p>Sie erhalten eine Antwort mit offenen Fragen oder einem
Terminvorschlag für ein Gespräch.</p></li>
<li><h3>Angebot</h3><p>Auf Basis der geklärten Punkte erstellen wir ein Angebot mit
klar abgegrenztem Leistungsumfang.</p></li>
</ol>

<h2>Bis dahin</h2>
<p>Wenn ein Verwalterwechsel ansteht, lohnt vorab ein Blick auf den
<a href="/ratgeber/verwalterwechsel-weg/">Ablauf des Wechsels</a> und die
<a href="/vorlagen/">Mustervorlagen</a> für Beschluss, Vertrag und Vollmacht.</p>
<p>Für Rückfragen erreichen Sie uns unter <a href="tel:{TEL_LINK}">{TEL}</a> oder
<a href="mailto:{MAIL}">{MAIL}</a>.</p>
""",
 breadcrumb=[("/","Start"),("/kontakt/","Angebot anfragen"),("/kontakt/danke/","Bestätigung")],
 eyebrow="Eingang bestätigt", noindex=True)

# ---------------------------------------------------------------- Impressum
page("/impressum/", "Impressum | Hausverwaltung Müller GmbH",
 "Impressum und Anbieterkennzeichnung der Hausverwaltung Müller GmbH.",
 "Impressum", "",
 f"""
<h2>Anbieter</h2>
<p>{FIRMA}<br>{STRASSE}<br>{PLZORT}</p>

<h2>Vertreten durch</h2>
<p>Geschäftsführer: Timo Müller</p>

<h2>Registereintrag</h2>
<p>Registergericht: Amtsgericht Düsseldorf<br>Handelsregisternummer: HRB 104762</p>

<h2>Kontakt</h2>
<p>Telefon: <a href="tel:{TEL_LINK}">{TEL}</a><br>
E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>

<h2>Umsatzsteuer-Identifikationsnummer</h2>
<p>[USt-IdNr. ergänzen]</p>

<h2>Aufsichtsbehörde und Erlaubnis</h2>
<p>[Zuständige Aufsichtsbehörde und Angaben zur Erlaubnis nach § 34c GewO ergänzen,
einschließlich der Bezeichnung der erteilenden Stelle.]</p>

<h2>Berufsrechtliche Angaben</h2>
<p>[Berufsbezeichnung, Staat der Verleihung und maßgebliche berufsrechtliche
Regelungen ergänzen, soweit einschlägig.]</p>

<h2>Verbraucherstreitbeilegung</h2>
<p>[Angabe ergänzen, ob eine Bereitschaft oder Verpflichtung zur Teilnahme an einem
Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle besteht.]</p>

<h2>Haftung für Inhalte</h2>
<p>Die Inhalte dieser Website wurden mit Sorgfalt erstellt. Für die Richtigkeit,
Vollständigkeit und Aktualität der Inhalte wird keine Gewähr übernommen. Die Beiträge
stellen keine Rechtsberatung dar. Maßgeblich ist stets der aktuelle Stand der
jeweiligen Rechtsvorschrift im Einzelfall.</p>

<h2>Haftung für Links</h2>
<p>Für die Inhalte externer Links sind ausschließlich deren Betreiber verantwortlich.
Zum Zeitpunkt der Verlinkung waren keine Rechtsverstöße erkennbar.</p>

<h2>Urheberrecht</h2>
<p>Die auf dieser Website veröffentlichten Inhalte unterliegen dem deutschen
Urheberrecht. Die bereitgestellten Muster dürfen für eigene Zwecke heruntergeladen
und angepasst werden.</p>

<div class="hinweis"><strong>Hinweis für den Betrieb dieser Website:</strong> Die mit
eckigen Klammern gekennzeichneten Angaben sind vor der Veröffentlichung zu ergänzen.
Ein Impressum ohne die erforderlichen berufsrechtlichen Angaben genügt den
gesetzlichen Anforderungen nicht. Die Vollständigkeit sollte anwaltlich geprüft
werden.</div>
""",
 breadcrumb=[("/","Start"),("/impressum/","Impressum")], eyebrow="Rechtliches")
print("teil 6 ok")
