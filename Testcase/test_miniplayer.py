#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from Page.App import App


class TestMiniplayer:
    def setup_class(self):
        self.main = App().start().main()
        self.search_name = '音律启蒙'
        self.miniplayer = self.main.goto_search().query(self.search_name).goto_detail().goto_miniplayer()

    def teardown_class(self):
        self.miniplayer.back_to_previous().cancel()

    def test_miniplayer_title(self):
        assert self.miniplayer.get_miniplayer_title() is not None

    def test_miniplayer_pic(self):
        assert self.miniplayer.get_miniplayer_pic() is True

    def test_miniplayer_subtitle(self):
        assert self.miniplayer.get_miniplayer_subtitle() is True

    def test_miniplayer_progressview(self):
        assert self.miniplayer.get_miniplayer_progressview() is True

    def test_miniplayer_play_icon(self):
        assert self.miniplayer.get_miniplayer_play_icon() is True

    def test_miniplayer_close(self):
        assert self.miniplayer.get_miniplayer_close() is True


if __name__ == '__main__':
    pytest.main(['alluredir', '../report/', 'clean-alluredir'])
