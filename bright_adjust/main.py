import os
import cv2
import numpy as np
import shutil


def bright_adjust(src_im_path, src_lb_path, dst_im_path, dst_lb_path, adjust_rate):
    img = cv2.imread(src_im_path)
    im_h, im_w, channel = img.shape
    blank = np.zeros([im_h, im_w, channel], img.dtype)
    rst = cv2.addWeighted(img, adjust_rate, blank, 1-adjust_rate, 3)
    cv2.imwrite(dst_im_path, rst)
    shutil.copyfile(src_lb_path, dst_lb_path)
    return


if __name__ == "__main__":
    src_im_fold = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/targetCrop"
    src_lb_fold = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/targetCrop"

    dst_im_fold = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/targetCrop_bj"
    dst_lb_fold = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/targetCrop_bj"
    if not os.path.exists(dst_im_fold): os.makedirs(dst_im_fold)
    if not os.path.exists(dst_lb_fold): os.makedirs(dst_lb_fold)

    f_list = os.listdir(src_im_fold)
    f_num = len(f_list)
    for idx, img_fn in enumerate(f_list):
        print(f"({idx + 1} / {f_num}) adjust bright of {img_fn}")
        if ".txt" in img_fn: continue
        src_im_path = os.path.join(src_im_fold, img_fn)
        src_lb_path = os.path.join(src_lb_fold, img_fn.replace(".jpg", ".txt"))

        dst_im_path = os.path.join(dst_im_fold, f"40_{img_fn}")
        lb_fn = img_fn.replace(".jpg", ".txt")
        dst_lb_path = os.path.join(dst_lb_fold, f"40_{lb_fn}")
        bright_adjust(src_im_path, src_lb_path, dst_im_path, dst_lb_path, 0.4)
        dst_im_path = os.path.join(dst_im_fold, f"60_{img_fn}")
        lb_fn = img_fn.replace(".jpg", ".txt")
        dst_lb_path = os.path.join(dst_lb_fold, f"60_{lb_fn}")
        bright_adjust(src_im_path, src_lb_path, dst_im_path, dst_lb_path, 0.6)
        dst_im_path = os.path.join(dst_im_fold, f"80_{img_fn}")
        lb_fn = img_fn.replace(".jpg", ".txt")
        dst_lb_path = os.path.join(dst_lb_fold, f"80_{lb_fn}")
        bright_adjust(src_im_path, src_lb_path, dst_im_path, dst_lb_path, 0.8)
        dst_im_path = os.path.join(dst_im_fold, f"120_{img_fn}")
        lb_fn = img_fn.replace(".jpg", ".txt")
        dst_lb_path = os.path.join(dst_lb_fold, f"120_{lb_fn}")
        bright_adjust(src_im_path, src_lb_path, dst_im_path, dst_lb_path, 1.2)
        dst_im_path = os.path.join(dst_im_fold, f"140_{img_fn}")
        lb_fn = img_fn.replace(".jpg", ".txt")
        dst_lb_path = os.path.join(dst_lb_fold, f"140_{lb_fn}")
        bright_adjust(src_im_path, src_lb_path, dst_im_path, dst_lb_path, 1.4)