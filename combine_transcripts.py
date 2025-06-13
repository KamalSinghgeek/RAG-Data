import os

# Set your folder path
transcripts_dir = "fleetstack_transcripts"  # <- Replace with your actual path
output_file = "combined_transcripts_single_line.txt"

with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in os.listdir(transcripts_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(transcripts_dir, filename)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read().replace("\n", " ").strip()  # Convert to single line
                title = os.path.splitext(filename)[0]
                outfile.write(f"FILE NAME:\n{title}:\n{content}\n\n{'-'*80}\n\n")

print(f"✅ Combined file written to: {output_file}")
