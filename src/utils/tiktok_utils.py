import datetime
from datetime import datetime as dt
import cv2
from pathlib import Path

str2num = {'K': 1000, 'M': 1000000}

def process_time(time_txt: str) -> datetime:
    # print(time_txt)
    if 'ago' in time_txt:
        n_ago, is_date = int(time_txt.split()[0][:-1]), time_txt.split()[0][-1]
        date = dt.today()
        if is_date == 'd':
            n_ago = datetime.timedelta(n_ago)
        else:
            n_ago = datetime.timedelta(hours = n_ago)
        date = date - n_ago        
        return date    
    elif len(time_txt.split('-')) < 3:
        time_txt+= '-' + str(dt.today().year)
        return dt.strptime(time_txt, '%m-%d-%Y')
    else:
        return dt.strptime(time_txt, '%m-%d-%Y')

def process_number(number_str: str) -> int:
    if number_str[-1].isnumeric():
        return int(number_str)
    else:
        rank = str2num[number_str[-1]]
        element = [int(i) for i in number_str[:-1].split('.')]
        num = element[0]*rank + element[1]*(rank//10)
        return num
        
def is_newest(query_date: datetime, last_date: datetime) -> bool:
    if query_date <= last_date:
        return False
    return True

def cut_frame(username: str, id: int, video_source: str,  db_path: str, save_interval: int = 3,) -> list:
    cap = cv2.VideoCapture(video_source)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = 0
    names = []
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame_count += 1

            if frame_count % (fps * save_interval) == 0:
                # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img_dir = f'{db_path}/{username}/{id}'
                Path(img_dir).mkdir(parents = True, exist_ok = True)

                #img name:
                img_name = f'{img_dir}/{frame_count}.jpg'
                cv2.imwrite(img_name, frame)
                names.append(img_name)
    #            # optional 
                # frame_count = 0

        # Break the loop
        else:
            break

    cap.release()
    return names