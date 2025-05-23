import pytest
from playwright.sync_api import sync_playwright, Page
import typing

@pytest.fixture
def page() -> typing.Generator[Page, None, None]:
    """
    Spustí Playwright pro každý test v samostatném  prostředí.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://engeto.cz/", wait_until="networkidle")
        yield page
        page.wait_for_timeout(3000)  # ⏱ zůstaň na stránce 3 sekundy po testu
        browser.close()


def test_navigation_to_courses(page: Page):
    """
    Kliknutím na odkaz 'Kurzy' v horním menu  je ověřeno  přesměrování na stránku kurzů.
    """
    kurzy_odkaz = page.get_by_role("link", name="Kurzy").first
    kurzy_odkaz.scroll_into_view_if_needed()

    with page.expect_navigation():
        kurzy_odkaz.click()

    assert any(klic in page.url for klic in ["kurz", "bootcamp"]), \
        f"Přesměrování na kurzy selhalo: {page.url}"


def test_subscribe_to_newsletter(page: Page):
    """
    Vyplněním e-mailu do pole a kliknutím na tlačítko 'Odebírat'je ověřena funkčnost přihlášení k odběru newsletteru.
    """
    email_input = page.get_by_placeholder("Zadej svůj e-mail").first
    email_input.scroll_into_view_if_needed()
    email_input.fill("mara1x@email.cz")

    subscribe_link = page.get_by_role("link", name="Odebírat").first
    subscribe_link.scroll_into_view_if_needed()
    subscribe_link.click()

    page.wait_for_timeout(1000)
    assert "engeto.cz" in page.url, "Po odeslání formuláře došlo k neočekávanému přesměrování"


def test_navigation_to_frontend_course(page: Page):
    """
    Klikne na kurz 'Front-end Developer Akademie' a ověří přesměrování na detail kurzu.
   
    """
    kurz_odkaz = page.get_by_role("link", name="Front-end Developer Akademie").first
    kurz_odkaz.scroll_into_view_if_needed()

    try:
        kurz_odkaz.wait_for(timeout=3000)
        with page.expect_navigation():
            kurz_odkaz.click()
    except:
        page.evaluate("(el) => el.click()", kurz_odkaz)
        page.wait_for_timeout(1500)

    assert any(klic in page.url for klic in ["webova", "akademie"]), \
        f"Přesměrování na kurz selhalo: {page.url}"
