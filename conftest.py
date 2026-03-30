import pytest
from utils.driver_factory import create_driver


@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot(
                f"reports/screenshots/{item.name}.png"
    )