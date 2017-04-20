import os
from games_odds.webScraping.scrapingWilliamHill import ScrapingWilliamHill

class MainViewsApi(ScrapingWilliamHill):
    def get_tbody(self, file_link, links):
        if os.path.getsize(file_link) == 0:
            return self.get_tbody_ids(links)
        else:
            with open(file_link, "w"):
                pass
            if os.path.getsize(file_link) == 0:
                return self.get_tbody_ids(links)

    def check_file_not_empty(self, file_link):
        if os.path.getsize(file_link) > 0:
            return True
        else:
            return False
