class BasePage:
    def __init__(self, page, url):
        self.page = page
        self.base_url = url

    def navigate (self, endpoint: str | None):
        self.page.goto (self.base_url+endpoint)

    
    def fill_input(self, locator, value):
        self.page.get_by_placeholder(locator).fill(value)

    def click_element(self, locator):
        self.page.locator(locator).click()