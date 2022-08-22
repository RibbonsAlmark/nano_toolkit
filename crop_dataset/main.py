from __future__ import annotations
from multiprocessing.spawn import import_main_path
from unicodedata import category
import os
import cv2


w_crop = 2048
h_crop = 2048
zoom_rate = 2048/5120


def crop_image(src_im_path, src_lb_path, dst_im_path, dst_lb_path):
    with open(src_lb_path, 'r') as f: annotation = f.read()

    if annotation == '': return
    
    img = cv2.imread(src_im_path)
    im_h, im_w, channel = img.shape

    obj_class, cx_r_str, cy_r_str, w_r_str, h_r_str = annotation.split(' ')

    roi_cx_f = float(cx_r_str)
    roi_cy_f = float(cy_r_str)
    roi_w_f = float(w_r_str)
    roi_h_f = float(h_r_str)

    x0 = max(0, int((roi_cx_f - roi_w_f / 2) * im_w * (1 - zoom_rate)))
    y0 = max(0, int((roi_cy_f - roi_h_f / 2) * im_h * (1 - zoom_rate)))
    x1 = x0 + w_crop
    y1 = y0 + h_crop
    
    roi_cx_new = int(roi_cx_f * im_w) - x0
    roi_cy_new = int(roi_cy_f * im_h) - y0
    roi_w_new = min(int(roi_w_f * im_w), roi_cx_new * 2, (w_crop - roi_cx_new) * 2)
    roi_h_new = min(int(roi_h_f * im_h), roi_cy_new * 2, (h_crop - roi_cy_new) * 2)

    img_crop = img[y0:y1, x0:x1]
    cv2.imwrite(dst_im_path, img_crop)
    new_annotation = f"0 {roi_cx_new / w_crop} {roi_cy_new / h_crop} {roi_w_new / w_crop} {roi_h_new / h_crop}"
    with open(dst_lb_path, 'w') as f: f.write(new_annotation)




if __name__ == "__main__":
    src_im_fold = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/target"
    src_lb_fold = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/target"

    dst_im_fold = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/targetCrop"
    dst_lb_fold = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/targetCrop"
    if not os.path.exists(dst_im_fold): os.makedirs(dst_im_fold)
    if not os.path.exists(dst_lb_fold): os.makedirs(dst_lb_fold)

    f_list = os.listdir(src_im_fold)
    f_num = len(f_list)
    for idx, img_fn in enumerate(f_list):
        print(f"({idx + 1} / {f_num}) crop {img_fn}")
        if ".txt" in img_fn: continue
        src_im_path = os.path.join(src_im_fold, img_fn)
        src_lb_path = os.path.join(src_lb_fold, img_fn.replace(".jpg", ".txt"))
        dst_im_path = os.path.join(dst_im_fold, img_fn)
        dst_lb_path = os.path.join(dst_lb_fold, img_fn.replace(".jpg", ".txt"))
        crop_image(src_im_path, src_lb_path, dst_im_path, dst_lb_path)
