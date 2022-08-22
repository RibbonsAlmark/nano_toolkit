import os
from shutil import copyfile


if __name__ == "__main__":
    source_img_folder_list = [
        "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/target",
        "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/targetLoss",
        "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/targetCrop",
        "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/target_bj",
        "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/targetLoss_bj",
        "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/source_assets/datasets/targetCrop_bj"
    ]

    images_folder = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/dataset/JPEGImages"
    labels_folder = "/home/setsuna/Documents/setsuna_workspace/work/Datasets/umbrallerPier_hispd/dataset/labels"
    if not os.path.exists(images_folder):os.mkdir(images_folder)
    if not os.path.exists(labels_folder):os.mkdir(labels_folder)

    idx = 0
    for src_folder in source_img_folder_list:
        for fn in os.listdir(src_folder):
            if fn.endswith(".txt"): continue
            src_img_fp = os.path.join(src_folder, fn)
            src_txt_fp = src_img_fp.replace(".jpg", ".txt")
            tgt_img_fp = os.path.join(images_folder, f"{idx}.jpg")
            tgt_txt_fp = os.path.join(labels_folder, f"{idx}.txt")
            copyfile(src_img_fp, tgt_img_fp)
            copyfile(src_txt_fp, tgt_txt_fp)
            idx += 1