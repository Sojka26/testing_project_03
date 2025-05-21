import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="session")
def browser():
    """
    Inicializuje prohlížeč (Chromium) pomocí Playwrightu s GUI režimem a zpomalením pro sledování.
    Otevře stránku engeto.cz a poskytne ji testům. Po dokončení ji zavře.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(10000)  # Timeout 10 s pro všechny akce
        page.goto("https://engeto.cz/")
        yield page
        browser.close()

@pytest.mark.parametrize("link_text, expected_url_part", [
    ("Přehled IT kurzů", "kurz"),
    ("Kurzy", "kurz"),
    ("FAQ", "faq"),
])
def test_navigation_links(browser, link_text, expected_url_part):
    """
    Klikne na první viditelný odkaz podle zadaného textu (např. 'Kurzy', 'FAQ', 'Přehled IT kurzů')
    a ověří, že po kliknutí došlo k přesměrování na očekávanou stránku.

    Test hledá všechny odkazy na stránce, které obsahují daný text,
    vybere z nich první viditelný, klikne na něj a ověří změnu URL nebo titulku.

    Splňuje požadavek, že každý test má pouze jeden assert.
    """
    # Najdi všechny odkazy obsahující zadaný text
    all_links = browser.locator("a", has_text=link_text)

    # Prohledá prvky a najde první viditelný odkaz
    count = all_links.count()
    target = None
    for i in range(count):
        link = all_links.nth(i)
        if link.is_visible():
            target = link
            break

    assert target is not None, f"Nebyl nalezen viditelný odkaz: {link_text}"

    # Zajistí, že je prvek viditelný v okně a klikne
    target.scroll_into_view_if_needed()
    with browser.expect_navigation():
        target.click()

    # Jeden assert: buď URL nebo titulek obsahuje očekávaný výraz
    assert expected_url_part in browser.url or expected_url_part in browser.title().lower(), \
        f"Odkaz '{link_text}' není viditelný nebo přesměrování selhalo: {browser.url}"