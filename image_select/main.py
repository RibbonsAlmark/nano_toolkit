import os
from shutil import copyfile
from tkinter import messagebox, Tk


if __name__ == "__main__":
    source_folder = "/home/setsuna/Documents/setsuna_workspace/work/高速相机目标检测算法调研/vedio_frames"
    target_folder = "/home/setsuna/Documents/setsuna_workspace/work/高速相机目标检测算法调研/vedio_frames_less4"
    num_required = 50
    rate_start_at = 0
    rate_end_at = 1

    if not os.path.exists(target_folder): os.makedirs(target_folder)

    file_name_list = os.listdir(source_folder)

    num_all_im = len(file_name_list)
    idx_start_at = rate_start_at * num_all_im
    idx_end_at = int(rate_end_at * num_all_im)
    num_src_im = idx_end_at - idx_start_at + 1
    group_size = max(1, int(num_src_im/num_required))

    copied_num = 0
    for im_idx in range(idx_start_at, idx_end_at + 1):
        if copied_num >= num_required: break
        if (im_idx - idx_start_at) % group_size != 0: continue
        # source_path = os.path.join(source_folder, file_name_list[im_idx])
        # target_path = os.path.join(target_folder, file_name_list[im_idx])
        # print(f"NO.{im_idx}: {file_name_list[im_idx]}")
        img_name = f"frame{im_idx}.jpg"
        source_path = os.path.join(source_folder, img_name)
        target_path = os.path.join(target_folder, img_name)
        copyfile(source_path, target_path)
        copied_num += 1
        print(f"\rCopying ({copied_num}/{num_required}) ...", end='')

    window = Tk()
    window.withdraw() 
    messagebox.showinfo(title='hint', message='FINISHED !')

    