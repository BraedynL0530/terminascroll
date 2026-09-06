from typing import Optional
import cv2

#ive been told in reviews that static typing is useful and makes code more readable,
#if anyone sees this file tell me if i did too much!

def downloaderQueue(video_url: str, playlist_url:Optional[str] = None) -> None:
    if playlist_url:#concurancy? i might im addicted to it
        pass # this needs to make a downloader instant for Each video in the yt playlist shorts or not
    elif video_url:
        pass
    else:
        raise ValueError("No video url provided")

def downloader(video_url: str) -> None:
    try:
        #download mp4 and either separate if that's a thing or download mp3 separate
        pass
    finally:
        pass#delete the mp4 files(3 stays for sound)
    pass

def mp4_to_text(mp4_path: str) -> str:
    cap = cv2.VideoCapture(mp4_path)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        #yip yap
    pass