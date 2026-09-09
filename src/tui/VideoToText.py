from logging import exception
from typing import Optional
import cv2
import os
import yt_dlp
#im gonna use threading or async.io, im thinking threading is actually optmial here


"""
ive been told in reviews that static typing is useful and makes code more readable,
if anyone sees this file tell me if i did too much!
"""
def downloaderQueue(video_url: str, playlist_url:Optional[str] = None) -> None:
    if playlist_url:#concurancy? i might im addicted to it
        pass # this needs to make a downloader instant for Each video in the yt playlist shorts or not
    elif video_url:
        pass
    else:
        raise ValueError("No video url provided")

def downloader(video_url: str) -> None:
    ydl_opts = {
        'keepvideo': True,
        'format': 'bestvideo[height<=360]+bestaudio/best[height<=360]/best',
        'outtmpl': '%(id)s.%(ext)s',
        'merge_output_format': 'mp4',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        video_id = yt_dlp.YoutubeDL.extract_id(video_url)
        expected_mp4 = os.path.abspath(f"{video_id}.mp4")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        mp4ToText(expected_mp4)

    except exception as e:
        print(f"Error downloading video: {e}")

    finally:
        if os.path.exists(expected_mp4):
            os.remove(expected_mp4)

def mp4ToText(mp4_path: str, width: int = 120) -> None: #probally gonna need to optimize this
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
            resized = cv2.resize(frame, (width, height))#resizi1ng for ratio

            acsii_frame = []

            for row in resized:
                line = ""
                for pixel in row:
                    b, g, r = pixel

                    """had to look this up because i overcomplicated stuff and didnt do grayscale
                    (299 * r + 0.587 * g + 0.114 * b)
                    apparently this is formula for rgb brightness? or human eye brightness? dunno how it works.
                    """

                    brightnes = (0.299 * r + 0.587 * g + 0.114 * b)
                    char_idx = (brightnes * (num_chars - 1)) // 255# ill miss spell all i want pycharm :P
                    char = ascii_chars[char_idx]

                    line += f"\033[38;2;{r};{g};{b}m{char}"

                acsii_frame.append(line + "\033[0m")



    except exception as e:
        print(f"Error converting video to text: {e}") #might need to use logger instead of print statements idk how pypi works

