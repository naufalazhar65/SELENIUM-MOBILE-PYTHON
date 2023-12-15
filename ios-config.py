import pytest
from appium import webdriver
import test_ios.ios_test as test

@pytest.fixture(autouse=True)
def teardown_method():
    yield
    driver.quit()

# Set iOS capabilities
caps = {
    "deviceName": "iPhone 15 pro",
    "platformName": "iOS",
    "platformVersion": "17.0",
    "udid": "90DCAF9D-C7D3-4488-9A41-FE4CC8616CF2",
    "app": "./app/MyRNDemoApp.app",
    "noReset": False,
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

# Run iOS tests
def run_test_cases(test_cases):
    for test_case in test_cases:
        test_case(driver)

def test_main():
    print("----- Running iOS tests -----")
    test_cases = [test.test_login,
                  test.test_sort_button,
                  test.test_add_to_cart,
                  test.test_invalid_checkout 
                  # test.test_invalid_checkout
                  ]
    
    run_test_cases(test_cases)
    print("----- iOS tests passed successfully! -----")
