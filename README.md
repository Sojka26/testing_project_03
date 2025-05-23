# Automatizované UI testy pro Engeto.cz

Tento projekt obsahuje tři automatizované UI testy pomocí frameworku [Playwright](https://playwright.dev/python/) a `pytest`.  
Testují základní funkcionality webu [https://engeto.cz](https://engeto.cz) ve viditelném režimu (prohlížeč se skutečně otevře).

---

##  Testované funkcionality

### 1. Navigace na stránku s kurzy – `test_navigation_to_courses`
- Kliká na odkaz **„Kurzy“** v horním menu.
- Ověřuje, že došlo k přesměrování na stránku s kurzy.
-  Typ interakce: *navigační menu*

### 2. Odeslání e-mailu do newsletteru – `test_subscribe_to_newsletter`
- Vyplní pole **„Zadej svůj e-mail“**.
- Klikne na **„Odebírat“**.
- Ověřuje, že stránka zůstává funkční.
-  Typ interakce: *formulář*

### 3. Výběr kurzu – `test_navigation_to_frontend_course`
- Kliká na odkaz **„Front-end Developer Akademie“**.
- Ověřuje, že došlo k přesměrování na stránku kurzu.
- Typ interakce: *kliknutí na produkt/kartu*

---

##  Pauza po testu

Po každém testu testovací prohlížeč **zůstane otevřený 3 sekundy**, aby bylo možné výsledek vizuálně ověřit.  
Tato prodleva je implementována přímo ve `fixture`.

---

##  Požadavky

- Python 3.8+
- `pytest`
- `playwright`

Instalace a spuštění

```bash
pip install pytest playwright
playwright install
pytest test_engeto.py
