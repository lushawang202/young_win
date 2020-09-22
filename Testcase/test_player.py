import allure
import pytest
from time import sleep
from Page.App import App


class TestPlayer:
    def setup_class(self):
        self.main = App().start().main()
        self.search_name = '音律启蒙'
        self.miniplayer = self.main.goto_search().query(self.search_name).goto_detail().goto_miniplayer()
        self.player = self.miniplayer.goto_player()

    def teardown_class(self):
        self.miniplayer.back_to_previous().cancel()

    def test_player_title(self):
        assert self.player.get_title() is not None

    def test_player_trial_icon(self):
        assert self.player.get_trial_icon() is True

    def test_player_slide_resume(self):
        self.aquire_slide_num()
        old_cur_num = self.cur_seg_num
        old_total_num = self.total_seg_num
        if old_cur_num == old_total_num:
            self.player.slide_pic_to_right()
            self.aquire_slide_num()
            assert self.cur_seg_num == old_cur_num - 1
            assert self.total_seg_num == old_total_num
            sleep(5)
            self.aquire_slide_num()
            assert self.cur_seg_num == old_cur_num
            assert self.total_seg_num == old_total_num
        elif old_cur_num < old_total_num:
            self.player.slide_pic_to_left()
            self.aquire_slide_num()
            assert self.cur_seg_num == old_cur_num + 1
            assert self.total_seg_num == old_total_num
            sleep(5)
            self.aquire_slide_num()
            assert self.cur_seg_num == old_cur_num
            assert self.total_seg_num == old_total_num

    def test_player_pic_or_slide(self):
        if self.player.get_slide():
            assert self.slide_player_to_left() is True
            assert self.slide_player_to_right() is True
            assert self.slide_player_to_left() is True
        elif self.player.get_pic():
            assert self.player.get_slide_page_info() is False

    def test_goto_miniplayer(self):
        self.player.minimize()
        assert self.player.get_miniplayer() is True

    def slide_player_to_left(self):
        self.aquire_slide_num()
        old_cur_num = self.cur_seg_num
        old_total_num = self.total_seg_num
        while True:
            if old_cur_num == old_total_num:
                self.player.slide_pic_to_left()
                self.aquire_slide_num()
                if self.cur_seg_num == old_cur_num and self.total_seg_num == old_total_num:
                    return True
                else:
                    return False
            elif old_cur_num < old_total_num:
                try:
                    while True:
                        self.player.slide_pic_to_left()
                        self.aquire_slide_num()
                        assert self.cur_seg_num == old_cur_num + 1
                        assert self.total_seg_num == old_total_num
                        old_cur_num = self.cur_seg_num
                        if self.cur_seg_num == old_total_num:
                            break
                except AssertionError:
                    return False

    def slide_player_to_right(self):
        self.aquire_slide_num()
        old_cur_num = self.cur_seg_num
        old_total_num = self.total_seg_num
        while True:
            if old_cur_num == 1:
                self.player.slide_pic_to_right()
                self.aquire_slide_num()
                if self.cur_seg_num == 1 and self.total_seg_num == old_total_num:
                    return True
                else:
                    return False
            elif old_cur_num > 1:
                try:
                    while True:
                        self.player.slide_pic_to_right()
                        self.aquire_slide_num()
                        assert self.cur_seg_num == old_cur_num - 1
                        assert self.total_seg_num == old_total_num
                        old_cur_num = self.cur_seg_num
                        if self.cur_seg_num == 1:
                            break
                except AssertionError:
                    return False

    def aquire_slide_num(self):
        self.slide_num = self.player.get_slide_num()
        self.cur_seg_num = int(self.slide_num[0])
        self.total_seg_num = int(self.slide_num[1])


if __name__ == '__main__':
    pytest.main(['reruns', '2'])
