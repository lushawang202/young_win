from selenium.webdriver.common.by import By

from young_win.Page.base_page import BasePage


class Player(BasePage):
    _path = r'D:\Automation_Project\aaa\young_win\Data\player.yaml'

    def minimize(self):
        self.steps(self._path)

    def get_miniplayer(self):
        return self.steps(self._path)

    def get_title(self):
        return self.steps(self._path)

    def get_trial_icon(self):
        return self.steps(self._path)

    def get_pic(self):
        return self.steps(self._path)

    def get_slide(self):
        return self.steps(self._path)

    def slide_pic_to_left(self):
        self.steps(self._path)
        return self

    def slide_pic_to_right(self):
        self.steps(self._path)
        return self

    def get_slide_page_info(self):
        return self.steps(self._path)

    def get_slide_num(self):
        return self.steps(self._path)

    def set_time_counter_15(self):
        self.steps(self._path)
        pass

    def get_time_counter_text(self):
        self.steps(self._path)
        return self

    def set_speed(self):
        self.steps(self._path)
        pass

    def download(self):
        self.steps(self._path)
        return self

    def download_tip_for_nonvip(self):
        self.steps(self._path)
        return self

    def goto_share(self):
        self.steps(self._path)
        return self

    def share_title_desc(self):
        self.steps(self._path)
        return self

    def share_subtitle_desc(self):
        self.steps(self._path)
        return self

    def share_cancel(self):
        self.steps(self._path)
        return self

    def share_moments(self):
        self.steps(self._path)

    def share_moments_status(self):
        self.steps(self._path)

    def back_to_young_win(self):
        self.steps(self._path)

    # def share_friend(self):
    #     self.steps(self._path)
    #
    # def share_qq(self):
    #     self.steps(self._path)
    #
    # def share_qqzone(self):
    #     self.steps(self._path)
    #
    # def get_timeline(self):
    #     self.steps(self._path)
    #
    # def get_playhead(self):
    #     self.steps(self._path)
    #
    # def get_progress(self):
    #     self.steps(self._path)
    #
    # def tap_on_timeline(self):
    #     self.steps(self._path)
    #
    # def drag_playhead(self):
    #     self.steps(self._path)
    #
    # def get_start_time(self):
    #     self.steps(self._path)
    #
    # def get_end_time(self):
    #     self.steps(self._path)
    #
    # def get_playlist(self):
    #     self.steps(self._path)
    #
    # def switch_program(self):
    #     self.steps(self._path)
    #
    # def go_previous(self):
    #     self.steps(self._path)
    #
    # def go_next(self):
    #     self.steps(self._path)
    #
    # def pause(self):
    #     self.steps(self._path)
    #
    # def get_document(self):
    #     self.steps(self._path)
    #
    # def get_series_pic(self):
    #     self.steps(self._path)
    #
    # def get_series_title(self):
    #     self.steps(self._path)
    #
    # def get_series_learners(self):
    #     self.steps(self._path)
    #
    # def goto_buy(self):
    #     self.steps(self._path)
    #
    # def goto_leave_msg(self):
    #     self.steps(self._path)
    #
    # def goto_top_msg(self):
    #     self.steps(self._path)
    #
    # def add_favourite(self):
    #     self.steps(self._path)
    #
    # def get_msg_eles(self):
    #     self.steps(self._path)
    #
    # def msg_thumb_up(self):
    #     self.steps(self._path)
    #
    # def scroll_to_bottom(self):
    #     self.steps(self._path)
    #
    # def get_mini_controller(self):
    #     self.steps(self._path)
