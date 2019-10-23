from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from utilities.util import read_data_from_excel

path_to_locators = "D:\\workspace\\RecreateIntegritas\\pages\\testdata\\locators.xlsx"


class RootPage:
    """Custom webdriver methods"""
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, element_name, sheet_name):
        locator_type = read_data_from_excel(path_to_locators, sheet_name, element_name=element_name,
                                            locator_type=True)
        locator_value = read_data_from_excel(path_to_locators, sheet_name, element_name=element_name,
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
            element = self.driver.find_element(by_locator_obj, locator_value)
            return element
        except NoSuchElementException:
            print("Element Not Found")
            return None

    def get_elements(self, element_name, sheet_name):
        """The return type is list of web elements
            Empty list if no elements are found"""
        locator_type = read_data_from_excel(path_to_locators, sheet_name, element_name=element_name,
                                            locator_type=True)
        locator_value = read_data_from_excel(path_to_locators, sheet_name, element_name=element_name,
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

        element = self.driver.find_elements(by_locator_obj, locator_value)
        return element

    def send_values(self, element_name, sheet_name, value):
        self.get_element(element_name, sheet_name).send_keys(value)

    def click_on_element(self, element_name, sheet_name):
        self.get_element(element_name, sheet_name).click()

    def get_text(self, element_name, sheet_name):
        return self.get_element(element_name, sheet_name).text

    def is_element_present(self, element_name, sheet_name):
        if self.get_element(element_name, sheet_name) is None:
            return False
        else:
            return True
