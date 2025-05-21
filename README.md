# testing_project_03
# Automatizované testy pro web engeto.cz

Tento projekt obsahuje tři automatizované testy vytvořené pomocí frameworku [Playwright](https://playwright.dev/python/) a `pytest`.

Testy kontrolují klikatelné odkazy na stránce [https://engeto.cz](https://engeto.cz), ověřují jejich viditelnost a správné přesměrování.

---

## 🧪 Co testujeme

Testy ověřují, že:

- Odkaz **"Přehled IT kurzů"** je viditelný a vede na stránku s kurzy.
- Odkaz **"Kurzy"** v horním menu přesměruje na správný obsah.
- Odkaz **"FAQ"** přesměruje na stránku s častými dotazy.


---

## 🛠️ Požadavky

- Python 3.8+
- Playwright
- pytest

---

## 💾 Instalace

```bash
pip install playwright pytest
playwright install
