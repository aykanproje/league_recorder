import os
from datetime import datetime

def create_match_folder(base_path="D:/Klipler"):
    now = datetime.now()
    session_folder = now.strftime("%Y-%m-%d_Session")
    match_folder = now.strftime("%H-%M-%S_Match")
    full_path = os.path.join(base_path, session_folder, match_folder)
    os.makedirs(os.path.join(full_path, "clips/Kills"), exist_ok=True)
    os.makedirs(os.path.join(full_path, "clips/Deaths"), exist_ok=True)
    os.makedirs(os.path.join(full_path, "clips/Objectives"), exist_ok=True)
    return full_path
