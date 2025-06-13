import os
import chardet

transcript_dir = "fleetstack_transcripts"

# Detect encoding of titles.txt
with open("titles.txt", "rb") as f:
    raw = f.read()
    encoding = chardet.detect(raw)["encoding"]
    print(f"Detected encoding: {encoding}")

lines = raw.decode(encoding).splitlines()

# Build ID → Title map (assuming alternating lines: Title, ID)
title_map = {}
for i in range(0, len(lines) - 1, 2):
    title = lines[i].strip()
    video_id = lines[i + 1].strip()
    safe_title = "".join(c for c in title if c.isalnum() or c in " _-").strip()
    title_map[video_id] = safe_title

# Rename transcript files
renamed_count = 0
for file in os.listdir(transcript_dir):
    if file.endswith(".txt"):
        video_id = file.replace(".txt", "")
        if video_id in title_map:
            new_filename = f"{title_map[video_id]}.txt"
            old_path = os.path.join(transcript_dir, file)
            new_path = os.path.join(transcript_dir, new_filename)
            os.rename(old_path, new_path)
            print(f"✅ Renamed: {file} → {new_filename}")
            renamed_count += 1
        else:
            print(f"❌ No title found for {video_id}")

print(f"\n🎉 Done! Renamed {renamed_count} transcript files.")
