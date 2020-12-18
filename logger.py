from datetime import datetime


def log(filter_name, file_name):
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    with open('images.log', 'a') as f:
        f.write(f"{timestamp} {filter_name} has been apply on {file_name}\n")


def dump_log():
    with open('images.log', 'r') as f:
        print(f.read())
