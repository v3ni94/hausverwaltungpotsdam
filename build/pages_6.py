# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,"/home/user/hausverwaltungpotsdam/build")
from gen_site import *
from pages_1 import RECHT

# ---------------------------------------------------------------- Kontakt
page("/kontakt/", "Kontakt und Anfrage | Hausverwaltung Müller GmbH",
 "Anfrage an die Hausverwaltung Müller GmbH zu WEG-Verwaltung, Mietverwaltung "
 "oder Sondereigentumsverwaltung in Potsdam.",
 "Kontakt und Anfrage",
 "Beschreiben Sie kurz Ihr Objekt und Ihr Anliegen. Wir melden uns mit den "
 "Angaben, die wir für ein belastbares Angebot benötigen.",
 f"""
<div class="cards">
<div class="card"><h3>Anschrift</h3>
<p>{FIRMA}<br>{STRASSE}<br>{PLZORT}</p></div>
<div class="card"><h3>Telefon</h3><p>{TEL}</p></div>
<div class="card"><h3>E-Mail</h3><p>{MAIL}</p></div>
</div>

<h2>Anfrage senden</h2>
<!-- Hinweis für den Betreiber: action mit dem Endpunkt des Formulardienstes oder
     des eigenen Mailskripts belegen. Ohne gültige action wird nichts versendet. -->
<form method="post" action="[Formular-Endpunkt ergänzen]">
<label for="anliegen">Anliegen</label>
<select id="anliegen" name="anliegen">
<option value="weg">WEG-Verwaltung oder Verwalterwechsel</option>
<option value="miete">Mietverwaltung</option>
<option value="sev">Sondereigentumsverwaltung</option>
<option value="sonstiges">Sonstiges</option>
</select>

<label for="name">Name</label>
<input id="name" name="name" type="text" autocomplete="name" required>

<label for="email">E-Mail</label>
<input id="email" name="email" type="email" autocomplete="email" required>

<label for="telefon">Telefon (optional)</label>
<input id="telefon" name="telefon" type="tel" autocomplete="tel">

<label for="objekt">Objekt, Ort und Anzahl der Einheiten</label>
<input id="objekt" name="objekt" type="text">

<label for="nachricht">Ihr Anliegen</label>
<textarea id="nachricht" name="nachricht" required></textarea>

<label class="check"><input type="checkbox" name="datenschutz" value="ja" required>
<span>Ich habe die <a href="/datenschutz/">Datenschutzerklärung</a> zur Kenntnis
genommen und willige in die Verarbeitung meiner Angaben zur Bearbeitung der Anfrage
ein.</span></label>

<p style="margin-top:22px"><button class="cta" type="submit">Anfrage senden</button></p>
</form>

<h2>Was wir für ein Angebot benötigen</h2>
<ul>
<li>Art der Verwaltung: WEG, Miete oder Sondereigentum,</li>
<li>Lage, Baujahr und Größe des Objekts sowie Anzahl der Einheiten,</li>
<li>bekannter Sanierungs- oder Instandhaltungsbedarf,</li>
<li>bestehende Bestellung und Vertragslage, sofern vorhanden,</li>
<li>laufende Streit-, Gewährleistungs- oder Versicherungsfälle,</li>
<li>gewünschter Übernahmezeitpunkt.</li>
</ul>
{RECHT}
""",
 breadcrumb=[("/","Start"),("/kontakt/","Kontakt")])

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
<p>Telefon: {TEL}<br>E-Mail: {MAIL}</p>

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
Ein Impressum ohne vollständige Kontaktangaben und ohne die erforderlichen
berufsrechtlichen Angaben genügt den gesetzlichen Anforderungen nicht. Die
Vollständigkeit sollte anwaltlich geprüft werden.</div>
""",
 breadcrumb=[("/","Start"),("/impressum/","Impressum")])
print("teil 6 ok")
