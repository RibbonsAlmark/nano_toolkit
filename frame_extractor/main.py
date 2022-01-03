import os
import cv2


# TODO: make it multi-thread
if __name__ == "__main__":
    vedio_path = "/home/setsuna/Documents/setsuna_workspace/work/高速相机目标检测算法调研/由亮到暗，丢失目标.mp4"
    target_folder = "/home/setsuna/Documents/setsuna_workspace/work/高速相机目标检测算法调研/vedio_frames"

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    v_cap = cv2.VideoCapture(vedio_path)
    v_frame_num = int(v_cap.get(7))

    count = 0
    success = True
    while success:
        print(f"\rExtracting frame NO.{count} ({count + 1}/{v_frame_num}) ...", end='')
        if cv2.waitKey(10) == 27: break
        if count == v_frame_num: break
        success,image = v_cap.read()
        img_name = f"frame{count}.jpg"
        img_path = os.path.join(target_folder, img_name)
        cv2.imwrite(img_path, image) # it cost times, will get way more faster when make this multi-thread
        count += 1

    print("FINISHED !")