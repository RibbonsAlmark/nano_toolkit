import os
import cv2


def show_bbox(im_fp, lb_fp):
    img = cv2.imread(im_fp)
    im_h, im_w, channel = img.shape

    with open(lb_fp, "r") as f: lb_info = f.read()
    certify_str, cx_str, cy_str, w_str, h_str = lb_info.split(' ')
    cx_f = float(cx_str)
    cy_f = float(cy_str)
    w_f = float(w_str)
    h_f = float(h_str)

    x0 = int((cx_f - (w_f / 2)) * im_w)
    x1 = int(x0 + w_f * im_w)
    y0 = int((cy_f - (h_f / 2)) * im_h)
    y1 = int(y0 + h_f * im_h)
    cv2.rectangle(img, (x0, y0), (x1, y1), (255, 0, 0), 2)

    cv2.imshow("", img)
    cv2.waitKey(0)


if __name__ == "__main__":
    source_folder = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/targetCrop"
    img_idx = 1
    while os.path.exists(os.path.join(source_folder, f"{img_idx}.jpg")):
        print(f"show image NO.{img_idx}")
        im_fp = os.path.join(source_folder, f"{img_idx}.jpg")
        lb_fp = im_fp.replace(".jpg", ".txt")
        show_bbox(im_fp, lb_fp)
        img_idx += 1