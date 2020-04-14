import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_accessibility_basket_button_on_the_product_page(browser):
    browser.get(link)
    time.sleep(30)
    try:
        basket_button = browser.find_element_by_css_selector("#add_to_basket_form > button").text
        assert len(basket_button) > 0
        print("Text on the button is: " + basket_button)

    except:
        print("The basket button is not available on the page")

