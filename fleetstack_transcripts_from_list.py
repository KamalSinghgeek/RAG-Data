from youtube_transcript_api import YouTubeTranscriptApi
import os

# ✅ All 45 Fleet Stack video URLs
video_urls = [
    "https://www.youtube.com/watch?v=MhTFmx99_Y8",
    "https://www.youtube.com/watch?v=6YC68whO8Aw",
    "https://www.youtube.com/watch?v=pS17j14L89c",
    "https://www.youtube.com/watch?v=5C8pMenKaFE",
    "https://www.youtube.com/watch?v=zMJETWKtDqk",
    "https://www.youtube.com/watch?v=VvWFvAAXVLA",
    "https://www.youtube.com/watch?v=5HD8MpW2Ims",
    "https://www.youtube.com/watch?v=lB5nPSddHBg",
    "https://www.youtube.com/watch?v=WGetGTEgwGE",
    "https://www.youtube.com/watch?v=fT7zK7KD8lw",
    "https://www.youtube.com/watch?v=uI-b8b40ZIA",
    "https://www.youtube.com/watch?v=gG4YqI17MOQ",
    "https://www.youtube.com/watch?v=7HC9sCmbodA",
    "https://www.youtube.com/watch?v=FYB9xPR-3bE",
    "https://www.youtube.com/watch?v=oCyxKYSSU90",
    "https://www.youtube.com/watch?v=mSEUbK4h560",
    "https://www.youtube.com/watch?v=tXIxziLb2xg",
    "https://www.youtube.com/watch?v=APReC1rvERA",
    "https://www.youtube.com/watch?v=icvyFDV8s2c",
    "https://www.youtube.com/watch?v=TzrYHr6MNF8",
    "https://www.youtube.com/watch?v=RTya4g_SALU",
    "https://www.youtube.com/watch?v=FuWnQC6SHiM",
    "https://www.youtube.com/watch?v=8ygGbhFeKNg",
    "https://www.youtube.com/watch?v=C94xOuTQMCI",
    "https://www.youtube.com/watch?v=O00MQKC1KTo",
    "https://www.youtube.com/watch?v=WoAck6O0FWk",
    "https://www.youtube.com/watch?v=XgjWNQj7nQ8",
    "https://www.youtube.com/watch?v=VrpBUvk9qNs",
    "https://www.youtube.com/watch?v=5jKe5njE4T8",
    "https://www.youtube.com/watch?v=s3dU-853_44",
    "https://www.youtube.com/watch?v=CubXwM2wcZY",
    "https://www.youtube.com/watch?v=3fz92PLZvsc",
    "https://www.youtube.com/watch?v=Bjjg0m6sCN4",
    "https://www.youtube.com/watch?v=fi__Jybz05M",
    "https://www.youtube.com/watch?v=m2OEx0MvsFY",
    "https://www.youtube.com/watch?v=tbyzfMJagno",
    "https://www.youtube.com/watch?v=NEj18TR0u88",
    "https://www.youtube.com/watch?v=YfebT3weQqQ",
    "https://www.youtube.com/watch?v=J6YWqugB_z0",
    "https://www.youtube.com/watch?v=KVcn0iCJmxc",
    "https://www.youtube.com/watch?v=Qh2RjmnklhM",
    "https://www.youtube.com/watch?v=S2dBQuTMLdU",
    "https://www.youtube.com/watch?v=tZJUq9GLHvo",
    "https://www.youtube.com/watch?v=cXW_SKlep3U",
    "https://www.youtube.com/watch?v=UJ30B4mnxHA"
]

# 📁 Folder to store transcripts
os.makedirs("fleetstack_transcripts", exist_ok=True)

# 🔁 Transcribe and save each video
for i, url in enumerate(video_urls, 1):
    video_id = url.split("v=")[-1]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        content = "\n".join([entry["text"] for entry in transcript])

        with open(f"fleetstack_transcripts/{video_id}.txt", "w", encoding="utf-8") as f:
            f.write(content)

        print(f"[{i}] ✅ Transcript saved: {video_id}.txt")
    except Exception as e:
        print(f"[{i}] ❌ Failed for {video_id}: {e}")
