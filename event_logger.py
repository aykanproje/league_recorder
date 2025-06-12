import requests
import time
from datetime import datetime

def collect_events():
    events = []
    print("📡 Event dinlemesi başladı...")
    while True:
        try:
            r = requests.get("http://127.0.0.1:2999/liveclientdata/eventdata", timeout=1)
            data = r.json()
            for ev in data.get("Events", []):
                if ev["EventName"] in ["ChampionKill", "ChampionDie", "BaronKill", "DragonKill", "TurretKilled"]:
                    ts = datetime.now()
                    summary = {"type": ev["EventName"], "timestamp": ts}
                    if summary not in events:
                        events.append(summary)
                        print(f"📝 Event: {summary['type']} @ {ts.time()}")
        except:
            break
        time.sleep(1)
    return events
