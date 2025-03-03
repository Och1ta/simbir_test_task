import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from constants import (
    XPATH_NAME, XPATH_PASSWORD, XPATH_CHECKBOX,
    XPATH_COLOR, XPATH_DROPDOWN, XPATH_EMAIL,
    XPATH_TEXTAREA, XPATH_BUTTON
)


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнение поля имени: {name}")
    def fill_name(self, name):
        name_field = self.driver.find_element(*XPATH_NAME)
        name_field.click()
        name_field.send_keys(name)

    @allure.step("Заполнение поля пароля")
    def fill_password(self, password):
        password_field = self.driver.find_element(*XPATH_PASSWORD)
        password_field.click()
        password_field.send_keys(password)

    @allure.step("Выбор чекбоксов: {indexes}")
    def select_checkboxes(self, indexes):
        checkboxes = self.driver.find_elements(*XPATH_CHECKBOX)
        for index in indexes:
            checkboxes[index].click()

    @allure.step("Выбор цвета")
    def select_color(self):
        color_label = self.driver.find_element(*XPATH_COLOR)
        self.driver.execute_script("arguments[0].click();", color_label)

    @allure.step("Выбор значения в выпадающем списке")
    def select_dropdown(self):
        dropdown = Select(self.driver.find_element(*XPATH_DROPDOWN))
        dropdown.select_by_index(1)

    @allure.step("Заполнение поля email: {email}")
    def fill_email(self, email):
        email_field = self.driver.find_element(*XPATH_EMAIL)
        email_field.send_keys(email)

    @allure.step("Обработка списка элементов")
    def process_list_items(self):
        list_items = self.driver.find_elements(
            By.XPATH,
            "//label[contains(text(), 'Automation tools')]/following-sibling::ul/li"
        )
        texts = [li.text.strip() for li in list_items if li.text.strip()]
        count_word = len(texts)
        max_length_word = max(" ".join(texts).split(), key=len, default="")
        return count_word, max_length_word

    @allure.step("Заполнение текстового поля")
    def fill_textarea(self, count_word, max_length_word):
        textarea = self.driver.find_element(*XPATH_TEXTAREA)
        textarea.send_keys(f"{count_word}\n{max_length_word}")

    @allure.step("Отправка формы")
    def submit_form(self):
        self.driver.find_element(*XPATH_BUTTON).click()

    @allure.step("Получение введенного имени")
    def get_name_value(self):
        return self.driver.find_element(*XPATH_NAME).get_attribute("value")

    @allure.step("Получение введенного пароля")
    def get_password_value(self):
        return self.driver.find_element(*XPATH_PASSWORD).get_attribute("value")

    @allure.step("Проверка, выбран ли чекбокс {index}")
    def is_checkbox_selected(self, index):
        checkboxes = self.driver.find_elements(*XPATH_CHECKBOX)
        return checkboxes[index].is_selected()

    @allure.step("Проверка, выбран ли цвет")
    def is_color_selected(self):
        return self.driver.find_element(*XPATH_COLOR).is_selected()

    @allure.step("Получение введенного email")
    def get_email_value(self):
        return self.driver.find_element(*XPATH_EMAIL).get_attribute("value")

    @allure.step("Ожидание появления сообщения об успехе")
    def get_success_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "success-message"))
        ).text
