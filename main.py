from game_monitor import wait_for_game_start, wait_for_game_end
from recording_control import start_recording, stop_recording
from event_logger import collect_events
from session_manager import create_match_folder
from video_splitter import split_video
from file_organizer import organize_clips
import time
from datetime import datetime

def get_latest_video_file():
    import os
    from config import VIDEO_FOLDER
    files = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(".mp4")]
    files.sort(key=lambda f: os.path.getmtime(os.path.join(VIDEO_FOLDER, f)), reverse=True)
    return os.path.join(VIDEO_FOLDER, files[0])

def main():
    wait_for_game_start()
    match_start = datetime.now()
    match_dir = create_match_folder()

    start_recording()
    events = collect_events()
    wait_for_game_end()
    stop_recording()

    time.sleep(2)
    full_path = get_latest_video_file()
    clips = split_video(full_path, events, match_start)
    organize_clips(clips, match_dir)

if __name__ == "__main__":
    main()
