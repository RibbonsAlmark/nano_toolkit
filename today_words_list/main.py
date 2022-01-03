import os
import datetime





class TodayWords:

    def __init__(self, start_date=datetime.datetime(2021, 10, 25)) -> None:
        self.start_date = start_date
        self.start_wl_idx = 1                          # "wl" is a shorten of "words list"
        self.ebbinghaus_list = [0, 1, 3, 7]
        self.task_load_max = len(self.ebbinghaus_list) # self.task_load_max = 4
        self.wl_num = 20                               # TODO: ...

    def __get_wl_list(self, task_load=4):
        wl_list = []
        self.current_date = datetime.datetime.today()
        delta_days = (self.current_date - self.start_date).days
        for idxp in range(self.task_load_max):
            if idxp >= task_load: break
            if delta_days < self.ebbinghaus_list[idxp]: break
            wl_idx = (self.start_wl_idx + delta_days + 20 - self.ebbinghaus_list[idxp]) % self.wl_num
            if wl_idx == 0: wl_idx = self.wl_num
            wl_list.append(wl_idx)
        return wl_list


    def print_wl(self):
        v_root = "/home/setsuna/Documents/setsuna_workspace/projects/iVocabulary/iVocabularies"
        for wl_idx in self.__get_wl_list():
            wl_fn = f"list{wl_idx}.txt"
            wl_fp = os.path.join(v_root, wl_fn)
            print(wl_fp)




if __name__ == "__main__":
    tw = TodayWords()
    tw.print_wl()