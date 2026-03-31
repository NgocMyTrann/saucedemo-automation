# SauceDemo Automation Project

## 📌 Overview
SauceDemo Automation Framework
This project is a test automation framework built using Selenium, Python, and Pytest for testing an e-commerce web application.

## 🛠 Tech Stack
- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Allure Report
- Git & GitHub

## 📂 Project Structure
tests/ → Test cases  
pages/ → Page Object classes  
utils/ → Driver setup & config  
testdata/ → Test data  
reports/ → Screenshots  
conftest.py → Pytest fixtures  

## 🚀 How to run
git clone https://github.com/NgocMyTrann/saucedemo-automation.git
cd saucedemo-automation

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

pytest --alluredir=allure-results
allure serve allure-results

## ✨ Features
- Page Object Model (POM)
- Data-driven testing (pytest parametrize)
- End-to-end test flow (login → cart → checkout)
- Screenshot on test failure
- Allure reporting integration

## ✅ Test Coverage
- Login validation (valid & invalid cases)
- Add product to cart
- Checkout process

## 📊 Test Report

![Allure Report](link_image)

### 1. Clone project
git clone https://github.com/NgocMyTrann/saucedemo-automation.git

### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run test
pytest --alluredir=allure-results

### 5. Generate report
allure serve allure-results
