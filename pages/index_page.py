from pages.base_page import BasePage


class IndexPage(BasePage):

    def __init__(self, page, url):
        super().__init__(page,url)

    def navigate_index (self):
        self.navigate("web/index.php/admin/viewSystemUsers")

    def navigate_pim(self) :
        self.navigate("web/index.php/pim/viewEmployeeList")

    def navigate_recruitment (self):
        self.navigate("web/index.php/recruitment/viewCandidates")