from young_win.Page.base_page import BasePage
from young_win.Page.player import Player


class Detail(BasePage):
    def goto_miniplayer(self):
        self.steps('../Data/detail.yaml')
        return self

    def goto_player(self):
        self.steps('../Data/detail.yaml')
        return Player(self._driver)

    def get_miniplayer_title(self):
        return self.steps('../Data/detail.yaml')

    def get_miniplayer_subtitle(self):
        return self.steps('../Data/detail.yaml')

    def get_miniplayer_pic(self):
        return self.steps('../Data/detail.yaml')

    def get_miniplayer_progressview(self):
        return self.steps('../Data/detail.yaml')

    def get_miniplayer_play_icon(self):
        return self.steps('../Data/detail.yaml')

    def miniplayer_play_status(self):
        return self.steps('../Data/detail.yaml')

    def get_miniplayer_close(self):
        return self.steps('../Data/detail.yaml')

    def back_to_previous(self):
        self.steps('../Data/detail.yaml')
        from young_win.Page.search import Search
        return Search(self._driver)

