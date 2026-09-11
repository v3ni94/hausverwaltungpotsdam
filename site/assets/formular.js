/* Anfragestrecke der Hausverwaltung Müller GmbH.
   Progressive Verbesserung: ohne JavaScript bleiben alle Felder sichtbar und
   das Formular vollständig absendbar. */
(function () {
  "use strict";
  var f = document.getElementById("anfrage");
  if (!f) return;

  /* Rückmeldung, wenn der Versand serverseitig fehlgeschlagen ist */
  if (new URLSearchParams(window.location.search).get("status") === "fehler") {
    var m = document.createElement("p");
    m.className = "meldung";
    m.setAttribute("role", "alert");
    m.innerHTML = "<strong>Die Anfrage konnte nicht gesendet werden.</strong>" +
      "Bitte prüfen Sie Ihre Angaben und versuchen Sie es erneut. " +
      "Alternativ erreichen Sie uns unter " +
      '<a href="tel:+4930439733333">030 439733333</a> oder ' +
      '<a href="mailto:potsdam@muellerhv.de">potsdam@muellerhv.de</a>.';
    f.parentNode.insertBefore(m, f);
  }

  var schritte = Array.prototype.slice.call(f.querySelectorAll(".schritt"));
  if (schritte.length < 2) return;
  var punkte   = Array.prototype.slice.call(f.querySelectorAll(".fortschritt li"));
  var bZurueck = f.querySelector(".zurueck");
  var bWeiter  = f.querySelector(".weiter");
  var bSenden  = f.querySelector(".senden");
  var fehler   = document.getElementById("fehler");
  var summe    = document.getElementById("zusammenfassung");
  var fort     = f.querySelector(".fortschritt");
  var aktuell  = 0;

  f.classList.add("mit-js");
  if (fort) fort.removeAttribute("aria-hidden");

  /* Verwaltungsart aus der Adresszeile vorbelegen, etwa /kontakt/?anliegen=weg */
  var karte = { weg: "WEG-Verwaltung", miete: "Mietverwaltung",
                sev: "Sondereigentumsverwaltung" };
  var p = new URLSearchParams(window.location.search);
  var quelle = document.getElementById("quelle");
  if (quelle) quelle.value = document.referrer || "direkt";
  var vor = karte[(p.get("anliegen") || "").toLowerCase()];
  if (vor) {
    var r = f.querySelector('input[name="verwaltungsart"][value="' + vor + '"]');
    if (r) r.checked = true;
  }

  function zeige(i) {
    aktuell = i;
    schritte.forEach(function (s, n) { s.hidden = n !== i; });
    punkte.forEach(function (li, n) {
      li.classList.toggle("aktiv", n === i);
      li.classList.toggle("erledigt", n < i);
    });
    bZurueck.hidden = i === 0;
    bWeiter.hidden  = i === schritte.length - 1;
    bSenden.hidden  = i !== schritte.length - 1;
    fehler.hidden = true;
    if (i === schritte.length - 1) fasseZusammen();
    var kopf = f.querySelector(".schritt:not([hidden]) legend");
    if (kopf) kopf.focus();
    var oben = f.getBoundingClientRect().top + window.scrollY - 90;
    if (window.scrollY > oben) window.scrollTo({ top: oben, behavior: "smooth" });
  }

  function pruefe(i) {
    var felder = schritte[i].querySelectorAll("input, select, textarea");
    for (var n = 0; n < felder.length; n++) {
      if (!felder[n].checkValidity()) {
        fehler.textContent = felder[n].validationMessage ||
          "Bitte ergänzen Sie die markierte Angabe.";
        fehler.hidden = false;
        felder[n].focus();
        return false;
      }
    }
    return true;
  }

  var titel = {
    verwaltungsart: "Verwaltungsart", strasse: "Straße und Hausnummer",
    plz: "Postleitzahl", ort: "Ort", einheiten: "Einheiten",
    uebernahme: "Übernahme", name: "Name", rolle: "Funktion",
    email: "E-Mail", telefon: "Telefon", nachricht: "Anliegen"
  };

  function fasseZusammen() {
    if (!summe) return;
    summe.innerHTML = "";
    Object.keys(titel).forEach(function (k) {
      var el = f.elements[k];
      if (!el) return;
      var wert = el.value;
      if (el.length && el[0] && el[0].type === "radio") {
        wert = "";
        for (var n = 0; n < el.length; n++) if (el[n].checked) wert = el[n].value;
      }
      if (!wert) return;
      var dt = document.createElement("dt"); dt.textContent = titel[k];
      var dd = document.createElement("dd"); dd.textContent = wert;
      summe.appendChild(dt); summe.appendChild(dd);
    });
  }

  bWeiter.addEventListener("click", function () {
    if (pruefe(aktuell)) zeige(aktuell + 1);
  });
  bZurueck.addEventListener("click", function () { zeige(aktuell - 1); });

  /* Auswahl im ersten Schritt führt direkt weiter */
  f.querySelectorAll('input[name="verwaltungsart"]').forEach(function (r) {
    r.addEventListener("change", function () {
      if (aktuell === 0) window.setTimeout(function () { zeige(1); }, 180);
    });
  });

  /* Eingabetaste springt zum nächsten Schritt statt abzusenden */
  f.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && e.target.tagName !== "TEXTAREA" &&
        aktuell < schritte.length - 1) {
      e.preventDefault();
      if (pruefe(aktuell)) zeige(aktuell + 1);
    }
  });

  f.addEventListener("submit", function (e) {
    for (var i = 0; i < schritte.length; i++) {
      if (!pruefe(i)) { e.preventDefault(); zeige(i); pruefe(i); return; }
    }
    bSenden.disabled = true;
    bSenden.textContent = "Wird gesendet …";
  });

  zeige(0);
})();
