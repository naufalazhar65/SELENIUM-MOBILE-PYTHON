import pytest
from appium import webdriver
import test_android.android_test as test

@pytest.fixture(autouse=True)
def teardown_method():
    yield
    driver.quit()

# Set Android capabilities
caps = {
    "deviceName": "Google Pixel 4",
    "platformName": "Android",
    "platformVersion": "12",
    "udid": "emulator-5554",
    "noReset": False,
    "appium:app": "/Users/naufalazhar/Documents/NAUFAL_AZHAR/SELENIUM-PYTHON-MOBILE/app/MyDemoAppRN.apk",    
    # "appPackage": "com.fileupload.filesharing.upfile",
    # "appActivity": "com.fileupload.filesharing.upfile.ui.main.MainActivity",
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# Run Android tests
def run_test_cases(test_cases):
    for test_case in test_cases:
        test_case(driver)

def test_main():
    print("----- Running Android tests -----")
    test_cases = [test.test_android]
    
    run_test_cases(test_cases)
    print("----- Android tests passed successfully! -----")
