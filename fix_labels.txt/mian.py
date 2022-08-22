import os 

if __name__ == "__main__":
    lb_folder = "/home/setsuna/Documents/setsuna_workspace/work/xxxOS/dataset/datasets/box_dataset/labels"
    for fn in os.listdir(lb_folder):
        lb_fp = os.path.join(lb_folder, fn)
        print(lb_fp)

        with open(lb_fp, 'r') as f:
            content = f.read()
            content = '0' + content[1:]

        with open(lb_fp, 'w') as f: f.write(content)
        