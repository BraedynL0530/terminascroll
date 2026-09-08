from typing import Optional
import cv2
import os

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

def mp4_to_text(mp4_path: str, width: int = 120) -> None:
    cap = cv2.VideoCapture(mp4_path)

    ascii_chars = "@#$%m*+=+-:.·` "
    num_chars = len(ascii_chars)

    os.system("")

    try:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                break

            o_height, o_width = frame.shape[:2] #orgial

            height = int((o_height / o_width) * width * 0.55)
            resized = cv2.resize(frame, (width, height))#resizing for ratio

            frame = []

            for row in resized:
                line = ""
                for pixel in row:
                    b, g, r = pixel

                    """had to look this up because i overcomplicated stuff and didnt do grayscale
                    (299 * r + 0.587 * g + 0.114 * b)
                    apparently this is formula for rgb brightness? or human eye brightness? dunno how it works.
                    """

                    brightnes = (299 * r + 0.587 * g + 0.114 * b)
                    char_idx = (brightnes * (num_chars - 1)) / 255# ill miss spell all i want pycharm :P
                    char = ascii_chars[char_idx]

                    line += f"\033[38;2;{r};{g};{b}m{char}"

                frame.append(line + "\033[0m")


    except:
        pass
