"""
Test script to process audio without silence trimming
"""
import whisper

# Load Whisper model
print("Loading Whisper model...")
model = whisper.load_model("base")

# Transcribe the original file (without preprocessing)
print("Transcribing original TEST2.m4a (no preprocessing)...")
result = model.transcribe("raw_audio/TEST2.m4a")

print("\n" + "="*60)
print("TRANSCRIPTION (No preprocessing)")
print("="*60)
print(f"Text: {result['text']}")
print(f"Language: {result['language']}")
print(f"\nSegments:")
for seg in result['segments']:
    print(f"  [{seg['start']:.2f}s - {seg['end']:.2f}s]: {seg['text']}")
print("="*60)
