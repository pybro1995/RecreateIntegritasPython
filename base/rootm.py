from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException
from utilities.util import read_data_from_excel

path_to_locators = "D:\\workspace\\RecreateIntegritas\\pages\\testdata\\locators.xlsx"


def get_element(driver, element_name):
    locator_type = read_data_from_excel(path_to_locators, "login_page", element_name=element_name,
                                        locator_type=True)
    locator_value = read_data_from_excel(path_to_locators, "login_page", element_name=element_name,
                                         locator_value=True)

    locator_type = locator_type.lower()

    if locator_type == "tagname":
        by_locator_obj = By.TAG_NAME
    elif locator_type == "id":
        by_locator_obj = By.ID
    elif locator_type == "name":
        by_locator_obj = By.NAME
    elif locator_type == "classname":
        by_locator_obj = By.CLASS_NAME
    elif locator_type == "linktext":
        by_locator_obj = By.LINK_TEXT
    elif locator_type == "partiallinktext":
        by_locator_obj = By.PARTIAL_LINK_TEXT
    elif locator_type == "cssselector":
        by_locator_obj = By.CSS_SELECTOR
    elif locator_type == "xpath":
        by_locator_obj = By.XPATH
    else:
        raise ValueError("locator type is invalid")

    try:
        element = driver.find_element(by_locator_obj, locator_value)
        return element
    except ElementNotVisibleException:
        print("Element Not Found")
        return None


def send_values(driver, element_name, value):
    try:
        get_element(driver, element_name).send_keys(value)
    except Exception:
        print("not valid element")


def click_on_element(driver, element_name):
    try:
        get_element(driver, element_name).click()
    except Exception:
        print("not valid element")
