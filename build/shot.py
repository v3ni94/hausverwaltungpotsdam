from playwright.sync_api import sync_playwright
import sys
pages=[("/","start"),("/weg-verwaltung-potsdam/","weg"),("/vorlagen/","vorlagen"),
       ("/ratgeber/verwalterwechsel-weg/","wechsel"),("/kontakt/","kontakt")]
errs=[]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome", args=["--no-sandbox"])
    d=b.new_page(viewport={"width":1280,"height":900})
    m=b.new_page(viewport={"width":390,"height":844})
    for pg,tag in [(d,"desk"),(m,"mob")]:
        pg.on("console", lambda msg: errs.append(msg.text) if msg.type=="error" else None)
    for path,name in pages:
        d.goto("http://localhost:8899"+path, wait_until="networkidle")
        d.screenshot(path=f"build/s-{name}.png", full_page=(name in ("start","vorlagen")))
        # horizontales Scrollen auf Mobil pruefen
        m.goto("http://localhost:8899"+path, wait_until="networkidle")
        ov=m.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth+1")
        if ov: errs.append(f"H-SCROLL auf {path}")
    m.goto("http://localhost:8899/", wait_until="networkidle")
    m.screenshot(path="build/s-mobil.png", full_page=True)
    b.close()
print("FEHLER:", errs or "keine")
