<?php
/**
 * Anfrageformular der Hausverwaltung Müller GmbH.
 * Nimmt die Angaben der Anfragestrecke entgegen und stellt sie per E-Mail zu.
 *
 * Einstellungen: siehe Block "Konfiguration". Weitere Änderungen sind für den
 * Betrieb nicht erforderlich.
 */

/* ----------------------------------------------------------- Konfiguration */
$empfaenger   = 'lead@muellerhv.de';
$absender     = 'website@hausverwaltungpotsdam.de'; // Muss zur Domain gehören,
                                                    // sonst lehnen Mailserver ab.
$antwort_seite = '/kontakt/danke/';
$fehler_seite  = '/kontakt/?status=fehler';

/* ----------------------------------------------------------- Hilfsfunktionen */
function feld($name, $max = 500) {
    $wert = isset($_POST[$name]) ? (string) $_POST[$name] : '';
    $wert = str_replace(array("\r", "\n"), ' ', $wert);
    $wert = trim(strip_tags($wert));
    return mb_substr($wert, 0, $max);
}
function text($name, $max = 4000) {
    $wert = isset($_POST[$name]) ? (string) $_POST[$name] : '';
    $wert = trim(strip_tags($wert));
    return mb_substr($wert, 0, $max);
}
function weiter($ziel) { header('Location: ' . $ziel, true, 303); exit; }

/* ----------------------------------------------------------- Zugangsprüfung */
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { weiter('/kontakt/'); }

/* Honigtopf: von Menschen nie ausgefüllt, von Formularrobotern meist schon. */
if (feld('website') !== '') { weiter($antwort_seite); }

/* ----------------------------------------------------------- Daten einlesen */
$art        = feld('verwaltungsart', 60);
$strasse    = feld('strasse', 120);
$plz        = feld('plz', 5);
$ort        = feld('ort', 80);
$einheiten  = feld('einheiten', 6);
$uebernahme = feld('uebernahme', 80);
$name       = feld('name', 120);
$rolle      = feld('rolle', 60);
$email      = feld('email', 160);
$telefon    = feld('telefon', 60);
$nachricht  = text('nachricht');
$quelle     = feld('quelle', 200);
$einwilligung = feld('datenschutz', 5);

/* ----------------------------------------------------------- Prüfung */
$pflicht = array($art, $strasse, $plz, $ort, $einheiten, $name, $email);
foreach ($pflicht as $wert) {
    if ($wert === '') { weiter($fehler_seite); }
}
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) { weiter($fehler_seite); }
if (!preg_match('/^[0-9]{5}$/', $plz))          { weiter($fehler_seite); }
if (!ctype_digit($einheiten))                   { weiter($fehler_seite); }
if ($einwilligung !== 'ja')                     { weiter($fehler_seite); }

/* ----------------------------------------------------------- Nachricht */
$zeilen = array(
    'Neue Anfrage über hausverwaltungpotsdam.de',
    '',
    'Verwaltungsart:   ' . $art,
    '',
    'OBJEKT',
    'Adresse:          ' . $strasse . ', ' . $plz . ' ' . $ort,
    'Einheiten:        ' . $einheiten,
    'Übernahme:        ' . ($uebernahme !== '' ? $uebernahme : 'keine Angabe'),
    '',
    'KONTAKT',
    'Name:             ' . $name,
    'Funktion:         ' . ($rolle !== '' ? $rolle : 'keine Angabe'),
    'E-Mail:           ' . $email,
    'Telefon:          ' . ($telefon !== '' ? $telefon : 'keine Angabe'),
    '',
    'ANLIEGEN',
    ($nachricht !== '' ? $nachricht : 'keine Angabe'),
    '',
    '---',
    'Einwilligung Datenschutz: erteilt',
    'Eingang:          ' . date('d.m.Y H:i'),
    'Herkunft:         ' . ($quelle !== '' ? $quelle : 'unbekannt'),
);
$inhalt = implode("\n", $zeilen) . "\n";

$betreff = 'Anfrage ' . $art . ', ' . $plz . ' ' . $ort . ', ' . $einheiten . ' Einheiten';

$kopf = array(
    'From: Website hausverwaltungpotsdam.de <' . $absender . '>',
    'Reply-To: ' . $name . ' <' . $email . '>',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
    'X-Mailer: PHP/' . phpversion(),
);

$ok = @mail(
    $empfaenger,
    '=?UTF-8?B?' . base64_encode($betreff) . '?=',
    $inhalt,
    implode("\r\n", $kopf),
    '-f' . $absender
);

weiter($ok ? $antwort_seite : $fehler_seite);
