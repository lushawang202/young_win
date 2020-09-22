#!/usr/bin/env python
# -*- coding: utf-8 -*-

from young_win.Page.base_page import BasePage
from young_win.Page.search import Search


class Main(BasePage):
    def goto_search(self):
        self.steps('../Data/main.yaml')
        return Search(self._driver)
