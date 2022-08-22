import os
import cv2
from cv2 import imshow
from matplotlib.image import imsave


def load_annotation(lb_fp):
    with open(lb_fp, 'r') as f: annotation = f.read()

    if annotation == '': 
        return False, -1, -1, -1, -1, -1
    else:
        obj_class, cx_r_str, cy_r_str, w_r_str, h_r_str = annotation.split(' ')

        obj_cls_i = int(obj_class)
        roi_cx_f = float(cx_r_str)
        roi_cy_f = float(cy_r_str)
        roi_w_f = float(w_r_str)
        roi_h_f = float(h_r_str)

        return True, obj_cls_i, roi_cx_f, roi_cy_f, roi_w_f, roi_h_f


def copy_margin(src_im_fp, dst_im_fp, src_lb_fp, dst_lb_fp, margin_width, resize = False, resize_width = 1024, resize_height = 1024):
    img = cv2.imread(src_im_fp)
    if resize:  img = cv2.resize(img, (resize_width, resize_height))
    im_h, im_w, channel = img.shape

    have_annotation, obj_cls_i, roi_cx_f, roi_cy_f, roi_w_f, roi_h_f = load_annotation(src_lb_fp)
    if not have_annotation:
        new_annotation = ''
    else:
        new_im_w = im_w + 2 * margin_width
        new_im_h = im_h + 2 * margin_width
        new_roi_cx_f = margin_width / new_im_w + roi_cx_f * im_w / new_im_w
        new_roi_cy_f = margin_width / new_im_h + roi_cy_f * im_h / new_im_h
        new_roi_w_f = roi_w_f * im_w / new_im_h
        new_roi_h_f = roi_h_f * im_h / new_im_h
        new_annotation = f"{obj_cls_i} {new_roi_cx_f} {new_roi_cy_f} {new_roi_w_f} {new_roi_h_f}"
    with open(dst_lb_fp, 'w') as f: f.write(new_annotation)

    dst_img = cv2.copyMakeBorder(img,margin_width,margin_width,margin_width,margin_width,borderType=cv2.BORDER_REPLICATE)

    # new_im_w = im_w + 2 * margin_width
    # new_im_h = im_h + 2 * margin_width
    # x0 = int((new_roi_cx_f - new_roi_w_f / 2) * new_im_w)
    # x1 = int(x0 + new_roi_w_f * new_im_w)
    # y0 = int((new_roi_cy_f - new_roi_h_f / 2) * new_im_h)
    # y1 = int(y0 + new_roi_h_f * new_im_h)
    # cv2.rectangle(dst_img, (x0, y0), (x1, y1), (255, 0, 0), 2)

    cv2.imwrite(dst_im_fp, dst_img)


if __name__ == "__main__":
    src_im_fold = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/target_adjustBright"
    src_lb_fold = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/target_adjustBright"

    dst_im_fold = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/target_adjustBright_addMargin"
    dst_lb_fold = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/target_adjustBright_addMargin"
    if not os.path.exists(dst_im_fold): os.makedirs(dst_im_fold)
    if not os.path.exists(dst_lb_fold): os.makedirs(dst_lb_fold)

    f_list = os.listdir(src_im_fold)
    f_num = len(f_list)
    margin_width = 150
    resize = True
    resize_width = 1024
    resize_height = 1024
    for idx, fn in enumerate(f_list):
        print(f"({idx + 1} / {f_num}) {fn}")
        if ".txt" in fn: continue

        src_im_fp = os.path.join(src_im_fold, fn)
        dst_im_fp = os.path.join(dst_im_fold, fn)
        lb_fn = fn.replace(".jpg", ".txt")
        src_lb_fp = os.path.join(src_lb_fold, lb_fn)
        dst_lb_fp = os.path.join(dst_lb_fold, lb_fn)

        copy_margin(src_im_fp, dst_im_fp, src_lb_fp, dst_lb_fp, margin_width, resize, resize_width, resize_height)
