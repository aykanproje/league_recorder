import requests
import time

def wait_for_game_start():
    print("🎮 Oyun başlangıcı bekleniyor...")
    while True:
        try:
            r = requests.get("http://127.0.0.1:2999/liveclientdata/activeplayername", timeout=1)
            if r.status_code == 200:
                print("✅ Oyun başladı!")
                return
        except:
            pass
        time.sleep(2)

def wait_for_game_end():
    print("⏳ Oyun devam ediyor...")
    while True:
        try:
            requests.get("http://127.0.0.1:2999/liveclientdata/activeplayername", timeout=1)
        except:
            print("🏁 Oyun bitti.")
            return
        time.sleep(2)
