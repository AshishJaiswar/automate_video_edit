# Import everything needed to edit video clips
from moviepy.editor import *
from glob import glob
import os


def video_editor(quote, author):
    # Import everything needed to edit video clips

    current_path = os.getcwd()
    video_path = get_video_path()
    clip = VideoFileClip(video_path)
    clip.subclip(0, 25)

    duration = clip.duration

    # Generate a text clip. You can customize the font, color, etc.
    txt_clip = TextClip(quote, font="Gabriola",
                        fontsize=65,
                        color='white')

    quotes_by = TextClip(f"~ {author}", font="Consolas-Bold", fontsize=40,
                         color='white')

    # Say that you want it to appear 10s at the center of the screen
    txt_clip = txt_clip.set_pos('center').set_duration(duration)
    quotes_by = quotes_by.set_position(("center", 1500)).set_duration(duration)

    image_layer_path = fr"{current_path}\layer\black_layer.png"
    image_clip = ImageClip(image_layer_path).set_duration(duration)

    image = CompositeVideoClip([image_clip, txt_clip, quotes_by])

    # Overlay the text clip on the first video clip
    video = CompositeVideoClip([clip, image])

    audio_path = fr"{current_path}\audio\ColorFull Flowers.mp3"
    audio_file = AudioFileClip(audio_path)
    audio = audio_file.set_end(video.duration)
    edited_audio_path = fr"{current_path}\music.mp3"
    audio.write_audiofile(edited_audio_path)
    # Write the result to a file (many options available !)
    edited_video_path = fr"{current_path}\video_by_{author}.mp4"
    video.write_videofile(edited_video_path, audio=edited_audio_path)
    os.remove(fr"{current_path}\music.mp3")


def get_video_path():
    current_path = os.getcwd()
    pattern = fr"{current_path}\*.mp4"
    files = glob(pattern)
    return files[0]
