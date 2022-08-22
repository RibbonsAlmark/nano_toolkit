import imp
import os
import re
from shutil import copyfile

src_fold = "./target"
dst_fold = "./target_new"


if __name__ == "__main__":
    if not os.path.exists(dst_fold): os.makedirs(dst_fold)

    for fn in os.listdir(src_fold):
        ori_idx = int(re.findall('-?\d+', fn)[0])
        new_idx = int((ori_idx - 1) / 11)

        ori_fp = os.path.join(src_fold, fn)
        new_fp = os.path.join(dst_fold, fn.replace(str(ori_idx), str(new_idx)))

        copyfile(ori_fp, new_fp)
        print(f"{ori_fp} -> {new_fp}")