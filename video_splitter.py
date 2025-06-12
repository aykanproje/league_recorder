import subprocess
import os
from datetime import timedelta

PRE_EVENT_SECONDS = 10
POST_EVENT_SECONDS = 5
TMP_DIR = "tmp_clips"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def seconds_since(start_time, event_time):
    delta = event_time - start_time
    return max(0, delta.total_seconds())

def split_video(full_video_path, event_log, match_start_time):
    ensure_dir(TMP_DIR)
    output_paths = []
    for idx, event in enumerate(event_log):
        start = seconds_since(match_start_time, event["timestamp"]) - PRE_EVENT_SECONDS
        end = seconds_since(match_start_time, event["timestamp"]) + POST_EVENT_SECONDS
        out_name = f"{event['type'].lower()}_{idx+1:03d}.mp4"
        out_path = os.path.join(TMP_DIR, out_name)
        cmd = [
            "ffmpeg", "-y",
            "-i", full_video_path,
            "-ss", str(start),
            "-to", str(end),
            "-c", "copy",
            out_path
        ]
        print(f"✂️ Klip çıkarılıyor: {out_name} ({start}s - {end}s)")
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        output_paths.append({"type": event["type"], "path": out_path})
    return output_paths
