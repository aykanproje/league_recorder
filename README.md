# 🎮 League Recorder

A lightweight auto-highlight system for League of Legends — powered by **NVIDIA ShadowPlay**.

---

## Why this project?

Apps like **Outplayed** or **Medal.tv** are great at capturing highlights automatically — but they eat up your system resources and can noticeably affect in-game performance.

ShadowPlay, on the other hand, is incredibly efficient thanks to GPU-accelerated encoding — but it doesn’t support automatic highlight detection.

This tool bridges that gap.  
It gives you **automatic kill/death/objective clips** with **zero FPS loss**, using ShadowPlay in the background.

---

## What it does

- ⏺️ Starts full-match recording using ShadowPlay (manual mode)
- 🧠 Detects key events (kills, deaths, barons, dragons etc.) in real-time using Riot’s Live Client API
- ✂️ At the end of the match, cuts the full video into clips based on those events
- 📂 Organizes clips into folders by match date and event type

All highlights, neatly grouped and timestamped — no extra bloat, no background memory hogs.
