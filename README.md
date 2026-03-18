# SauceDemo Automation Project

## 📌 Overview
This project is a test automation framework built for the SauceDemo website.

## 🛠 Tech Stack
- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Allure Report

## 📂 Project Structure
- tests/ → test cases
- pages/ → page objects
- testdata/ → test data
- utils/ → driver setup & config

## ✅ Test Scenarios
- Login
- Add product to cart
- Checkout flow

## 🚀 How to run

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