import os

# 📁 Folder where your transcripts are stored
transcript_dir = "fleetstack_transcripts"

# 📄 Load the title-ID pairs from your titles.txt
title_map = {}
with open("titles.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

# 🔄 Build dictionary from alternating lines (Title, ID)
for i in range(0, len(lines), 2):
    title = lines[i]
    video_id = lines[i + 1]
    safe_title = "".join(c for c in title if c.isalnum() or c in " _-").strip()
    title_map[video_id] = safe_title

# 🔁 Rename each transcript file
for file in os.listdir(transcript_dir):
    if file.endswith(".txt"):
        video_id = file.replace(".txt", "")
        if video_id in title_map:
            new_filename = f"{title_map[video_id]}.txt"
            old_path = os.path.join(transcript_dir, file)
            new_path = os.path.join(transcript_dir, new_filename)
            os.rename(old_path, new_path)
            print(f"✅ Renamed: {file} → {new_filename}")
        else:
            print(f"❌ No title found for {video_id}")
