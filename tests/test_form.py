import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from pages.form_page import FormPage
from constants import INPUT_NAME, INPUT_PASSWORD, INPUT_EMAIL, XPATH_CHECKBOX


@pytest.fixture(scope="function")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://practice-automation.com/form-fields/")
    yield driver
    driver.quit()


@pytest.fixture
def filled_form(driver):
    form_page = FormPage(driver)
    form_page.fill_name(INPUT_NAME)
    form_page.fill_password(INPUT_PASSWORD)
    form_page.fill_email(INPUT_EMAIL)

    checkboxes = driver.find_elements(*XPATH_CHECKBOX)
    if len(checkboxes) > 2:
        form_page.select_checkboxes([1, 2])

    form_page.select_color()
    form_page.select_dropdown()
    word_count, max_length_word = form_page.process_list_items()
    form_page.fill_textarea(word_count, max_length_word)
    return form_page


def test_input_fields(driver):
    form_page = FormPage(driver)
    form_page.fill_name(INPUT_NAME)
    form_page.fill_password(INPUT_PASSWORD)
    form_page.fill_email(INPUT_EMAIL)

    assert form_page.get_name_value() == INPUT_NAME, "Имя введено неправильно"
    assert form_page.get_password_value() == INPUT_PASSWORD, "Пароль введен неправильно"
    assert form_page.get_email_value() == INPUT_EMAIL, "Email введен неправильно"


def test_checkboxes_and_color(driver):
    form_page = FormPage(driver)
    checkboxes = driver.find_elements(*XPATH_CHECKBOX)

    if len(checkboxes) > 2:
        form_page.select_checkboxes([1, 2])
        assert form_page.is_checkbox_selected(1), "Чекбокс Молока не отмечен"
        assert form_page.is_checkbox_selected(2), "Чекбокс Кофе не отмечен"
    else:
        pytest.skip("Недостаточно чекбоксов на странице")

    form_page.select_color()
    assert form_page.is_color_selected(), "Цвет не выбран"



def test_dropdown_and_textarea(driver):
    form_page = FormPage(driver)
    form_page.select_dropdown()
    word_count, max_length_word = form_page.process_list_items()
    form_page.fill_textarea(word_count, max_length_word)

    assert word_count > 0, "Список инструментов пуст"
    assert len(max_length_word) > 0, "Максимальное слово не найдено"


def test_form_submission(filled_form):
    submit_button = WebDriverWait(filled_form.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "submit-btn"))
    )

    try:
        submit_button.click()
    except:
        filled_form.driver.execute_script("arguments[0].click();", submit_button)

    alert = WebDriverWait(filled_form.driver, 10).until(EC.alert_is_present())
    alert_text = alert.text

    assert alert_text == "Message received!", "Сообщение после отправки неверное"
    alert.accept()
