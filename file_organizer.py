import os
import shutil
from datetime import datetime
from config import OUTPUT_ROOT

def organize_clips(clips, match_dir):
    for clip in clips:
        category = clip_category(clip["type"])
        target_dir = os.path.join(match_dir, "clips", category)
        os.makedirs(target_dir, exist_ok=True)
        fname = os.path.basename(clip["path"])
        shutil.move(clip["path"], os.path.join(target_dir, fname))
        print(f"📂 Taşındı: {fname} → {category}/")
    print(f"\n✅ Klipler organize edildi: {match_dir}")

def clip_category(event_type):
    if event_type == "ChampionKill":
        return "Kills"
    elif event_type == "ChampionDie":
        return "Deaths"
    else:
        return "Objectives"
