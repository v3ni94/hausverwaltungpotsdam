# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,"/home/user/hausverwaltungpotsdam/build")
from gen_site import *

page("/datenschutz/", "Datenschutzerklärung | Hausverwaltung Müller GmbH",
 "Informationen zur Verarbeitung personenbezogener Daten beim Besuch dieser Website "
 "und bei der Kontaktaufnahme.",
 "Datenschutzerklärung", "",
 f"""
<div class="hinweis"><strong>Hinweis für den Betrieb dieser Website:</strong> Dieser
Text ist ein Entwurf und auf den tatsächlichen Betrieb abzustimmen, insbesondere auf
Hosting, Formularversand, Speicherfristen und eingesetzte Dienste. Vor der
Veröffentlichung ist eine Prüfung durch eine fachkundige Stelle zu empfehlen. Die in
eckigen Klammern gekennzeichneten Angaben sind zu ergänzen.</div>

<h2>1. Verantwortlicher</h2>
<p>{FIRMA}<br>{STRASSE}<br>{PLZORT}<br>
Telefon: {TEL}<br>E-Mail: {MAIL}</p>
<p>Datenschutzbeauftragter: [Angabe ergänzen oder streichen, sofern keine
Benennungspflicht besteht.]</p>

<h2>2. Verarbeitung beim Aufruf der Website</h2>
<p>Beim Aufruf dieser Website werden durch den Hosting-Anbieter technisch
erforderliche Daten in Server-Logfiles verarbeitet. Dazu gehören in der Regel die
gekürzte oder vollständige IP-Adresse, Datum und Uhrzeit des Zugriffs, die
aufgerufene Seite, der übertragene Datenumfang, der Browsertyp und das
Betriebssystem.</p>
<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Das berechtigte Interesse liegt im
sicheren und stabilen Betrieb der Website.</p>
<p>Speicherdauer: [Speicherdauer der Logfiles beim Hoster ergänzen.]</p>

<h2>3. Hosting</h2>
<p>Diese Website wird bei [Name und Anschrift des Hosting-Anbieters ergänzen]
gehostet. Mit dem Anbieter besteht ein Vertrag zur Auftragsverarbeitung nach
Art. 28 DSGVO.</p>

<h2>4. Kontaktaufnahme und Anfrageformular</h2>
<p>Wenn Sie uns über das Formular, per E-Mail oder telefonisch kontaktieren,
verarbeiten wir die von Ihnen mitgeteilten Daten zur Bearbeitung Ihrer Anfrage.</p>
<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO, soweit die Anfrage auf den
Abschluss oder die Durchführung eines Vertrags gerichtet ist, im Übrigen
Art. 6 Abs. 1 lit. f DSGVO und, soweit eine Einwilligung erteilt wurde,
Art. 6 Abs. 1 lit. a DSGVO.</p>
<p>Wir löschen die Daten, sobald sie für den Zweck nicht mehr erforderlich sind und
keine gesetzlichen Aufbewahrungspflichten entgegenstehen.</p>

<h2>5. Cookies und Reichweitenmessung</h2>
<p>Diese Website setzt keine Cookies zu Analyse- oder Marketingzwecken ein und bindet
keine externen Schriftarten, Karten oder Analysedienste ein. Sofern künftig solche
Dienste eingesetzt werden, ist diese Erklärung entsprechend zu ergänzen und
gegebenenfalls eine Einwilligungslösung vorzusehen.</p>

<h2>6. Empfänger</h2>
<p>Eine Weitergabe Ihrer Daten erfolgt nur, soweit dies zur Bearbeitung Ihres
Anliegens erforderlich ist, Sie eingewilligt haben oder eine gesetzliche
Verpflichtung besteht. Auftragsverarbeiter werden vertraglich nach Art. 28 DSGVO
verpflichtet.</p>

<h2>7. Ihre Rechte</h2>
<p>Sie haben das Recht auf Auskunft nach Art. 15 DSGVO, auf Berichtigung nach
Art. 16 DSGVO, auf Löschung nach Art. 17 DSGVO, auf Einschränkung der Verarbeitung
nach Art. 18 DSGVO, auf Datenübertragbarkeit nach Art. 20 DSGVO sowie ein
Widerspruchsrecht nach Art. 21 DSGVO. Eine erteilte Einwilligung können Sie
jederzeit mit Wirkung für die Zukunft widerrufen.</p>
<p>Sie haben zudem das Recht, sich bei einer Datenschutzaufsichtsbehörde zu
beschweren. Zuständig ist in der Regel die Aufsichtsbehörde des Bundeslandes, in dem
der Verantwortliche seinen Sitz hat.</p>

<h2>8. Erforderlichkeit der Bereitstellung</h2>
<p>Die Bereitstellung Ihrer Daten ist weder gesetzlich noch vertraglich
vorgeschrieben. Ohne die im Formular als erforderlich gekennzeichneten Angaben können
wir Ihre Anfrage jedoch nicht bearbeiten.</p>

<h2>9. Stand</h2>
<p>Stand dieser Erklärung: [Datum ergänzen]</p>
""",
 breadcrumb=[("/","Start"),("/datenschutz/","Datenschutz")], eyebrow="Rechtliches")

# 404
page("/404", "Seite nicht gefunden | Hausverwaltung Müller GmbH",
 "Die aufgerufene Seite existiert nicht.",
 "Seite nicht gefunden",
 "Die aufgerufene Adresse existiert nicht oder wurde geändert.",
 """
<p>Folgende Bereiche führen weiter:</p>
<div class="cards">
<div class="card"><h3>WEG-Verwaltung</h3><p>Verwaltung von Eigentümergemeinschaften.</p>
<a href="/weg-verwaltung-potsdam/">Zur Leistung</a></div>
<div class="card"><h3>Ratgeber</h3><p>Antworten zu Wechsel, Befugnissen und Zertifizierung.</p>
<a href="/ratgeber/">Zum Ratgeber</a></div>
<div class="card"><h3>Kontakt</h3><p>Anfrage zu Ihrem Objekt stellen.</p>
<a href="/kontakt/">Zum Kontakt</a></div>
</div>
""")
import shutil, os
shutil.move(str(SITE/"404/index.html"), str(SITE/"404.html"))
os.rmdir(SITE/"404")
print("teil 7 ok")
