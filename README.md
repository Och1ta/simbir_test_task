# Selenium Pytest Automation

Автоматизация тестирования веб-формы с использованием Selenium и Pytest.

## Описание

Этот проект использует Page Object Model (POM) для организации кода, а тесты разделены по функциональности.

## Установка
### Клонирование проекта
```bash
git clone https://github.com/Och1ta/simbir_test_task.git
```
```bash
cd simbir_test_task
```
### Создать виртуальное окружение
```bash
python3 -m venv venv
```
### Активировать вирутальное окружение: 
### macOS/Linux
```bash
source venv/bin/activate
```
### Windows  
```bash
venv\Scripts\activate  
```
### Установка зависимостей
```bash
pip install -r requirements.txt
```
### Установите Allure CLI
*  MacOS 
```bash 
brew install allure
```
*  Windows 
```bash
choco install allure
```
*  Linux
```bash
sudo apt-add-repository ppa:qameta/allure
sudo apt update
sudo apt install allure
```
### Запуск c Allure
```bash
pytest --alluredir=allure-results
```
### Просмотр отчета Allure
```bash
allure serve allure-results
```

## Автор:

[Кабанов Антон](https://t.me/Memoterasik)