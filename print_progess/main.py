import time


def print_progess(text, idx, task_num, end=False):
    if idx == task_num or end:
        end_text = "\n"
    else:
        end_text = ''
    
    dots = '.' * (idx % 7) + ' ' * (7 - (idx % 7))
    print(f"\r{text} {dots} ({idx}/{task_num})", end=end_text)


if __name__ == "__main__":
    task_num = 100
    for i in range(task_num):
        print_progess("test", i + 1, task_num)
        time.sleep(0.1)