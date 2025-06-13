from pytube import YouTube
import os

# 📁 Path where your transcripts are saved
transcript_folder = "fleetstack_transcripts"

# 🔁 Loop through each .txt file in the folder
for filename in os.listdir(transcript_folder):
    if filename.endswith(".txt"):
        video_id = filename.replace(".txt", "")
        try:
            yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
            title = yt.title

            # Clean up filename (remove slashes and invalid characters)
            safe_title = "".join(c for c in title if c.isalnum() or c in " -_").rstrip()
            new_filename = f"{safe_title}.txt"

            old_path = os.path.join(transcript_folder, filename)
            new_path = os.path.join(transcript_folder, new_filename)

            os.rename(old_path, new_path)
            print(f"✅ Renamed: {filename} → {new_filename}")
        except Exception as e:
            print(f"❌ Failed to fetch title for {video_id}: {e}")
