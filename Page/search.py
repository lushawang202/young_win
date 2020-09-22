#!/usr/bin/env python
# -*- coding: utf-8 -*-

from young_win.Page.base_page import BasePage
from young_win.Page.detail import Detail
from young_win.Page.player import Player


class Search(BasePage):
    _path = '../Data/search.yaml'

    def query(self, search_name):
        self._input_param['search_name'] = search_name
        self.steps(self._path)
        return self

    def goto_detail(self):
        self.steps(self._path)
        return Detail(self._driver)

    def goto_player(self):
        self.steps(self._path)
        return Player(self._driver)

    def cancel(self):
        self.steps(self._path)
        from young_win.Page.main import Main
        return Main(self._driver)
