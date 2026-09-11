# -*- coding: utf-8 -*-
import sys; sys.path.insert(0,"/home/user/hausverwaltungpotsdam/build")
from gen_site import *
from pages_1 import CTA_WEG, RECHT

# ---------------------------------------------------------------- Ratgeber-Hub
page("/ratgeber/", "Ratgeber für Wohnungseigentümer und Vermieter | Müller",
 "Ratgeber zur WEG-Verwaltung: Hausverwaltung kündigen, Verwalterwechsel, "
 "Befugnisse der Verwaltung und zertifizierter Verwalter.",
 "Ratgeber für Eigentümer und Verwaltungsbeiräte",
 "Die Fragen, die uns Eigentümergemeinschaften am häufigsten stellen, "
 "strukturiert beantwortet und mit den einschlägigen Vorschriften eingeordnet.",
 f"""
<div class="cards">
<div class="card"><h3>Hausverwaltung einer WEG kündigen</h3>
<p>Warum Abberufung und Verwaltervertrag zwei verschiedene Dinge sind und wer
tatsächlich entscheidet.</p>
<a href="/ratgeber/hausverwaltung-weg-kuendigen/">Zum Beitrag</a></div>
<div class="card"><h3>Verwalterwechsel Schritt für Schritt</h3>
<p>Von der Prüfung der Ausgangslage über die Beschlüsse bis zur Übergabe der
Unterlagen und Konten.</p>
<a href="/ratgeber/verwalterwechsel-weg/">Zum Beitrag</a></div>
<div class="card"><h3>Was darf eine Hausverwaltung?</h3>
<p>Interne Befugnisse, Vertretung nach außen und die Vorgänge, die einen
Eigentümerbeschluss voraussetzen.</p>
<a href="/ratgeber/was-darf-eine-hausverwaltung/">Zum Beitrag</a></div>
<div class="card"><h3>Zertifizierter Verwalter</h3>
<p>Was die Bezeichnung bedeutet, worin sie sich von der Gewerbeerlaubnis
unterscheidet und was Eigentümer verlangen können.</p>
<a href="/ratgeber/zertifizierter-verwalter/">Zum Beitrag</a></div>
</div>
<h2>Arbeitsvorlagen</h2>
<p>Ergänzend stellen wir Muster für Beschlussprotokoll, Verwaltervertrag und
Vollmacht als PDF bereit.</p>
<p><a class="cta ghost" href="/vorlagen/">Zu den Vorlagen</a></p>
{RECHT}
""",
 breadcrumb=[("/","Start"),("/ratgeber/","Ratgeber")])

# ---------------------------------------------------------------- kündigen
faq_k = [
 ("Kann eine WEG ihren Verwalter jederzeit abberufen?",
  "Ja. § 26 Abs. 3 WEG bestimmt, dass der Verwalter jederzeit abberufen werden kann. "
  "Der Verwaltervertrag ist davon zu unterscheiden. Das Gesetz legt fest, dass er "
  "spätestens sechs Monate nach der Abberufung endet. Die konkrete Vertragslage sollte "
  "trotzdem geprüft werden."),
 ("Wer entscheidet über die Abberufung?",
  "Über Bestellung und Abberufung entscheiden die Wohnungseigentümer durch Beschluss. "
  "Für einen rechtssicheren Ablauf müssen unter anderem die Anforderungen an Einladung "
  "und Beschlussgegenstand berücksichtigt werden."),
 ("Muss bereits eine neue Hausverwaltung feststehen?",
  "§ 26 WEG macht die Abberufung nicht davon abhängig, dass gleichzeitig ein Nachfolger "
  "bestellt wird. Praktisch ist ein abgestimmter Übergang aber meist sinnvoll, damit "
  "Verwaltung, Vertretung, Konten, Unterlagen und laufende Vorgänge nicht ungeklärt "
  "bleiben. Das ist eine organisatorische Empfehlung, keine gesetzliche Bedingung."),
 ("Kann ein einzelner Eigentümer die Hausverwaltung kündigen?",
  "Nein. Der Verwalter wird durch die Wohnungseigentümer bestellt und abberufen. Ein "
  "einzelner Eigentümer kann das Thema auf die Tagesordnung bringen lassen, die "
  "Entscheidung trifft aber die Gemeinschaft durch Beschluss."),
]
page("/ratgeber/hausverwaltung-weg-kuendigen/",
 "Hausverwaltung einer WEG kündigen: Ablauf und Beschluss",
 "Wie können WEG-Eigentümer ihre Hausverwaltung wechseln? Abberufung, Vertrag, "
 "Beschluss, Fristen und die nächsten Schritte verständlich erklärt.",
 "Wie kündigt eine WEG ihre Hausverwaltung?",
 "Der häufigste Fehler liegt nicht im Willen zum Wechsel, sondern darin, "
 "Abberufung und Verwaltervertrag als dieselbe Sache zu behandeln.",
 f"""
<h2>Abberufung und Vertrag unterscheiden</h2>
<p>Im Wohnungseigentumsrecht gibt es nicht die eine Kündigung der Hausverwaltung.
Es gibt zwei Vorgänge, die zusammengehören, aber rechtlich getrennt sind.</p>
<p><strong>Die Abberufung</strong> beendet das Amt. Nach § 26 Abs. 3 WEG kann der
Verwalter jederzeit abberufen werden. Es bedarf dafür nach dem Gesetz keines
besonderen Grundes.</p>
<p><strong>Der Verwaltervertrag</strong> regelt Leistungen, Vergütung und Laufzeit.
Nach der gesetzlichen Regelung endet er spätestens sechs Monate nach der Abberufung.
Was darüber hinaus vereinbart wurde, ergibt sich aus dem konkreten Vertrag.</p>
<p>Wer nur den Vertrag prüft, übersieht den Bestellungsbeschluss. Wer nur abberuft,
klärt die Vertragsfolgen nicht. Beides gehört auf den Tisch.</p>

<h2>Wer entscheidet?</h2>
<p>Die Entscheidung liegt bei den Wohnungseigentümern. Sie beschließen über
Bestellung und Abberufung. Ein einzelner Eigentümer, der Verwaltungsbeirat oder der
Beiratsvorsitzende können den Wechsel vorbereiten, aber nicht allein beschließen.</p>

<h2>Die Eigentümerversammlung vorbereiten</h2>
<p>Damit ein Beschluss wirksam gefasst werden kann, muss der Beschlussgegenstand
bereits bei der Einberufung bezeichnet sein. Die Einladung erfolgt grundsätzlich in
Textform. Die Einberufungsfrist soll nach § 24 Abs. 4 WEG mindestens drei Wochen
betragen, sofern kein Fall besonderer Dringlichkeit vorliegt.</p>
<p>Praktisch bewährt sich, drei Punkte getrennt vorzubereiten:</p>
<ol>
<li>Abberufung der bisherigen Verwaltung zu einem bestimmten Termin,</li>
<li>Bestellung der neuen Verwaltung mit Beginn und Ende der Bestellung,</li>
<li>Ermächtigung zum Abschluss des neuen Verwaltervertrags.</li>
</ol>
<p>Der dritte Punkt wird häufig vergessen. Gegenüber dem Verwalter wird die
Gemeinschaft nach § 9b Abs. 2 WEG durch den Vorsitzenden des Verwaltungsbeirats oder
einen durch Beschluss ermächtigten Wohnungseigentümer vertreten.</p>

<h2>Was mit dem laufenden Vertrag passiert</h2>
<p>Die Abberufung wirkt auf das Amt. Für die vertragliche Seite sind die gesetzliche
Regelung und der konkrete Vertrag maßgeblich, etwa zu Vergütung bis zum
Vertragsende, zur Abrechnung des laufenden Wirtschaftsjahres und zur Herausgabe der
Unterlagen. Bei streitigen Konstellationen, insbesondere wenn die bisherige
Verwaltung Ansprüche geltend macht, sollte rechtlicher Rat eingeholt werden.</p>

<h2>Typische Fehler</h2>
<ul>
<li>Der Beschlussgegenstand ist in der Einladung nicht eindeutig bezeichnet.</li>
<li>Abberufung und Neubestellung werden in einem unklaren Sammelbeschluss vermischt.</li>
<li>Die Ermächtigung zum Vertragsabschluss fehlt, der Vertrag bleibt in der Schwebe.</li>
<li>Der Wechselstichtag passt nicht zum Abrechnungszeitraum.</li>
<li>Die Übergabe von Konten, Zugängen und Unterlagen ist nicht terminiert.</li>
<li>Laufende Schäden, Gewährleistungs- und Gerichtsverfahren werden nicht übergeben.</li>
</ul>

<h2>Nächste Schritte</h2>
<p>Der Ablauf eines vollständigen Wechsels ist im Beitrag
<a href="/ratgeber/verwalterwechsel-weg/">Verwalterwechsel Schritt für Schritt</a>
dargestellt. Für die Dokumentation der Beschlüsse stellen wir ein
<a href="/vorlagen/">Musterprotokoll</a> bereit.</p>
{CTA_WEG}

<h2>Häufige Fragen</h2>
{faq_html(faq_k)}
{RECHT}
""",
 breadcrumb=[("/","Start"),("/ratgeber/","Ratgeber"),
             ("/ratgeber/hausverwaltung-weg-kuendigen/","Hausverwaltung kündigen")],
 faq=faq_k)
print("teil 3 ok")
