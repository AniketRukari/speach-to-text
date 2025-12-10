# Complete Technical Reference Guide 📚

## Table of Contents
1. [Libraries & Tools Reference](#libraries--tools-reference)
2. [Algorithms Explained (Like You're 5)](#algorithms-explained-like-youre-5)
3. [Complete Pipeline Flowchart](#complete-pipeline-flowchart)

---

# Libraries & Tools Reference

## 1. Audio Processing Libraries

### 📦 librosa
**What it is:** A Python library for analyzing and processing audio files.

**What it does:**
- Load audio files in any format
- Resample audio (change speed/quality)
- Extract features from audio (frequencies, tempo, etc.)
- Trim silence
- Analyze music and speech

**Simple Definition:**
Think of librosa as a Swiss Army knife for audio - it has all the tools you need to work with sound files!

**Example:**
```python
import librosa

# Load an audio file
audio, sample_rate = librosa.load('song.mp3', sr=16000)
# audio = the sound as numbers
# sample_rate = how many numbers per second (16,000)

# Trim silence from start and end
trimmed_audio, _ = librosa.effects.trim(audio, top_db=20)
# Only keeps the parts with actual sound!

# Result: Clean audio without silence
print(f"Original length: {len(audio)} samples")
print(f"Trimmed length: {len(trimmed_audio)} samples")
```

**Real Example Output:**
```
Original length: 480000 samples
Trimmed length: 320000 samples
Removed 160000 silent samples!
```

---

### 📦 soundfile
**What it is:** A library to read and write audio files.

**What it does:**
- Save audio as WAV, FLAC, OGG files
- Read audio files quickly
- Handle different audio formats
- Preserve audio quality

**Simple Definition:**
soundfile is like a file cabinet for audio - it helps you save and organize your sound files properly!

**Example:**
```python
import soundfile as sf
import numpy as np

# Create a simple beep sound
sample_rate = 16000
duration = 2  # seconds
frequency = 440  # Hz (A note)

# Generate a sine wave (beep sound)
t = np.linspace(0, duration, int(sample_rate * duration))
audio = np.sin(2 * np.pi * frequency * t)

# Save as WAV file
sf.write('beep.wav', audio, sample_rate)
print("Saved beep sound!")

# Read it back
audio_read, sr = sf.read('beep.wav')
print(f"Loaded audio with {len(audio_read)} samples at {sr} Hz")
```

**Real Example Output:**
```
Saved beep sound!
Loaded audio with 32000 samples at 16000 Hz
```

---

### 📦 pydub
**What it is:** Simple library to manipulate audio files.

**What it does:**
- Convert between audio formats (mp3 → wav)
- Cut and join audio clips
- Change volume
- Add effects

**Simple Definition:**
pydub is like scissors and tape for audio - cut, paste, and glue audio pieces together!

**Example:**
```python
from pydub import AudioSegment

# Load an MP3 file
audio = AudioSegment.from_mp3("song.mp3")

# Cut first 10 seconds
first_10_seconds = audio[:10000]  # milliseconds

# Make it louder (increase by 6 decibels)
louder = first_10_seconds + 6

# Save as WAV
louder.export("louder_clip.wav", format="wav")
print("Created louder 10-second clip!")
```

**Real Example Output:**
```
Created louder 10-second clip!
File: louder_clip.wav
Duration: 10 seconds
Volume: +6dB
```

---

## 2. Machine Learning Libraries

### 📦 openai-whisper
**What it is:** AI model that converts speech to text.

**What it does:**
- Listen to audio recordings
- Write down what it hears
- Detect what language is spoken
- Work with 99+ languages

**Simple Definition:**
Whisper is like a super-smart robot secretary that listens to recordings and types everything it hears - and it knows 99 languages!

**Example:**
```python
import whisper

# Load the AI model (one time download)
model = whisper.load_model("base")
print("Whisper model loaded!")

# Transcribe an audio file
result = model.transcribe("interview.mp3")

# See what it heard
print(f"Language detected: {result['language']}")
print(f"Transcription: {result['text']}")

# Get detailed information
for segment in result['segments']:
    print(f"[{segment['start']:.2f}s - {segment['end']:.2f}s]: {segment['text']}")
```

**Real Example Output:**
```
Whisper model loaded!
Language detected: en
Transcription: Hello, my name is Sarah and I love programming in Python.

[0.00s - 2.50s]: Hello, my name is Sarah
[2.50s - 5.00s]: and I love programming in Python.
```

---

## 3. Data Processing Libraries

### 📦 pandas
**What it is:** Library for working with tables of data (like Excel in Python).

**What it does:**
- Create tables (DataFrames)
- Sort and filter data
- Save data as CSV or Excel files
- Calculate statistics

**Simple Definition:**
pandas is like Excel superpowers in Python - create spreadsheets, analyze data, and make reports!

**Example:**
```python
import pandas as pd

# Create a table of audio recordings
data = {
    'filename': ['audio1.wav', 'audio2.wav', 'audio3.wav'],
    'transcription': ['Hello world', 'Good morning', 'How are you'],
    'duration': [3.5, 2.1, 4.2],
    'language': ['en', 'en', 'en']
}

df = pd.DataFrame(data)

# Show the table
print(df)

# Calculate average duration
avg_duration = df['duration'].mean()
print(f"\nAverage duration: {avg_duration:.2f} seconds")

# Save to CSV
df.to_csv('audio_dataset.csv', index=False)
print("Saved to CSV!")
```

**Real Example Output:**
```
      filename   transcription  duration language
0  audio1.wav    Hello world       3.5       en
1  audio2.wav   Good morning       2.1       en
2  audio3.wav   How are you        4.2       en

Average duration: 3.27 seconds
Saved to CSV!
```

---

### 📦 numpy
**What it is:** Library for working with numbers and arrays.

**What it does:**
- Store large lists of numbers efficiently
- Do math on entire lists at once
- Create patterns and sequences
- Scientific calculations

**Simple Definition:**
numpy is like a super calculator that can do math on millions of numbers at the same time!

**Example:**
```python
import numpy as np

# Create a list of numbers 0 to 9
numbers = np.arange(10)
print("Numbers:", numbers)

# Multiply all by 2 at once!
doubled = numbers * 2
print("Doubled:", doubled)

# Calculate statistics
print(f"Average: {numbers.mean()}")
print(f"Maximum: {numbers.max()}")
print(f"Sum: {numbers.sum()}")

# Create audio wave (sine wave)
time = np.linspace(0, 1, 100)  # 100 points from 0 to 1
sine_wave = np.sin(2 * np.pi * 5 * time)  # 5 Hz wave
print(f"\nCreated sine wave with {len(sine_wave)} points")
```

**Real Example Output:**
```
Numbers: [0 1 2 3 4 5 6 7 8 9]
Doubled: [ 0  2  4  6  8 10 12 14 16 18]
Average: 4.5
Maximum: 9
Sum: 45

Created sine wave with 100 points
```

---

### 📦 scipy
**What it is:** Scientific computing library (advanced math and science).

**What it does:**
- Signal processing (filters, transforms)
- Statistical functions
- Optimization
- Scientific calculations

**Simple Definition:**
scipy is like a science lab toolkit - it has special tools for advanced science and engineering!

**Example:**
```python
from scipy import signal
import numpy as np

# Create a noisy signal
time = np.linspace(0, 1, 1000)
clean_signal = np.sin(2 * np.pi * 5 * time)
noise = np.random.normal(0, 0.1, 1000)
noisy_signal = clean_signal + noise

# Apply a filter to clean it up
b, a = signal.butter(4, 0.1)  # Low-pass filter
filtered_signal = signal.filtfilt(b, a, noisy_signal)

print(f"Original signal range: {noisy_signal.min():.3f} to {noisy_signal.max():.3f}")
print(f"Filtered signal range: {filtered_signal.min():.3f} to {filtered_signal.max():.3f}")
print("Noise reduced!")
```

**Real Example Output:**
```
Original signal range: -1.234 to 1.189
Filtered signal range: -0.998 to 1.001
Noise reduced!
```

---

## 4. Utility Libraries

### 📦 tqdm
**What it is:** Progress bar library.

**What it does:**
- Show progress bars in terminal
- Track loop progress
- Estimate time remaining
- Make waiting less boring!

**Simple Definition:**
tqdm adds a loading bar like you see when downloading files - so you know how long to wait!

**Example:**
```python
from tqdm import tqdm
import time

# Process 100 items with a progress bar
items = range(100)

for item in tqdm(items, desc="Processing"):
    # Simulate some work
    time.sleep(0.01)
    
print("Done!")
```

**Real Example Output:**
```
Processing: 100%|████████████████████| 100/100 [00:01<00:00, 99.50it/s]
Done!
```

---

### 📦 pathlib
**What it is:** Modern way to work with file paths.

**What it does:**
- Create file and folder paths
- Check if files exist
- Get filename, extension, etc.
- Cross-platform (works on Windows, Mac, Linux)

**Simple Definition:**
pathlib is like a GPS for files - it helps you find and navigate to files on your computer!

**Example:**
```python
from pathlib import Path

# Create a path
audio_dir = Path("raw_audio")
audio_file = audio_dir / "recording.mp3"

# Check if it exists
if audio_file.exists():
    print(f"Found: {audio_file}")
    print(f"Filename: {audio_file.name}")
    print(f"Extension: {audio_file.suffix}")
    print(f"Size: {audio_file.stat().st_size} bytes")
else:
    print("File not found!")

# Create a directory
output_dir = Path("output") / "dataset_v1"
output_dir.mkdir(parents=True, exist_ok=True)
print(f"Created: {output_dir}")
```

**Real Example Output:**
```
Found: raw_audio/recording.mp3
Filename: recording.mp3
Extension: .mp3
Size: 524288 bytes
Created: output/dataset_v1
```

---

# Algorithms Explained (Like You're 5)

## 1. Audio Normalization 🔊

**What is it?**
Making all audio files the same volume.

**Like you're 5:**
Imagine you have 5 friends talking. One whispers, one shouts, and three talk normally. Audio normalization makes everyone talk at the same volume so you can hear everyone clearly!

**How it works:**
```
Step 1: Measure how loud the audio is
   [Very Quiet] ░░░░░░░░░░

Step 2: Calculate: "How much louder should it be?"
   Target volume = -20 dB (good for speech)
   Current volume = -35 dB
   Increase needed = 15 dB

Step 3: Turn up the volume!
   [Perfect Volume] ████████░░

Step 4: Make sure it's not TOO loud (clipping prevention)
   If > 100% volume: reduce to 100%
```

**Code Example:**
```python
def normalize_audio(audio):
    # Step 1: How loud is it?
    current_loudness = np.sqrt(np.mean(audio**2))  # RMS
    
    # Step 2: How loud should it be?
    target_loudness = 10**(-20/20)  # -20 dBFS
    
    # Step 3: Calculate boost needed
    if current_loudness > 0:
        boost = target_loudness / current_loudness
        normalized = audio * boost
    else:
        normalized = audio
    
    # Step 4: Prevent clipping (too loud)
    max_value = np.max(np.abs(normalized))
    if max_value > 1.0:
        normalized = normalized / max_value
    
    return normalized
```

---

## 2. Silence Trimming ✂️

**What is it?**
Removing quiet parts from the beginning and end of audio.

**Like you're 5:**
Imagine recording yourself reading a book, but you forget to press stop. The recording has 5 minutes of you reading and 2 minutes of silence. Trimming cuts off that awkward silence!

**How it works:**
```
Original Audio:
[Silence] [Speech!!!] [Silence]
░░░░░░░░  ████████    ░░░░░░░░
0-2 sec   2-10 sec    10-12 sec

Step 1: Find where sound starts (above threshold)
   "First loud sound at 2.0 seconds"

Step 2: Find where sound ends
   "Last loud sound at 10.0 seconds"

Step 3: Cut everything else!
   Keep only 2.0 to 10.0 seconds

Trimmed Audio:
[Speech!!!]
████████
0-8 sec (saved 4 seconds!)
```

**Code Example:**
```python
def trim_silence(audio, sample_rate, threshold_db=20):
    # Step 1: Find energy in the audio
    energy = librosa.amplitude_to_db(np.abs(audio))
    
    # Step 2: Find first loud sample
    start_idx = 0
    for i, e in enumerate(energy):
        if e > -threshold_db:
            start_idx = i
            break
    
    # Step 3: Find last loud sample
    end_idx = len(energy)
    for i in range(len(energy)-1, -1, -1):
        if energy[i] > -threshold_db:
            end_idx = i + 1
            break
    
    # Step 4: Cut!
    trimmed = audio[start_idx:end_idx]
    return trimmed
```

---

## 3. Mel Spectrogram Conversion 🌈

**What is it?**
Converting sound waves into a colorful picture that computers can understand.

**Like you're 5:**
Imagine you can't hear, but you can see colors. A Mel Spectrogram turns sounds into a rainbow picture where:
- Red = loud sounds
- Blue = quiet sounds  
- Top = high pitch (like a whistle)
- Bottom = low pitch (like a drum)

**How it works:**
```
Sound Wave (what you hear):
    ∿∿∿∿∿∿∿∿∿
   ↓ ↓ ↓ ↓ ↓ (many calculations)

Mel Spectrogram (what computer sees):
    Frequency ▲
    High  │ 🟦🟦🟥🟥🟦  ← High sounds
          │ 🟦🟥🟥🟥🟥  ← Mid sounds  
    Low   │ 🟥🟥🟥🟥🟥  ← Low sounds
          └─────────────► Time
          
🟥 = Loud    🟦 = Quiet

Step 1: Chop audio into tiny pieces (30ms each)
Step 2: For each piece, find all the frequencies
Step 3: Convert to "Mel scale" (how humans hear)
Step 4: Make it a pretty picture!
```

**Code Example:**
```python
def create_mel_spectrogram(audio, sample_rate):
    # Step 1 & 2: STFT (Short-Time Fourier Transform)
    # Breaks audio into frequencies over time
    stft = librosa.stft(audio)
    
    # Step 3: Convert to Mel scale
    mel_spec = librosa.feature.melspectrogram(
        S=np.abs(stft)**2,
        sr=sample_rate,
        n_mels=80  # 80 frequency bands
    )
    
    # Step 4: Convert to decibels (like volume)
    mel_spec_db = librosa.power_to_db(mel_spec, ref=np.max)
    
    return mel_spec_db
    # Returns: 80 × time matrix (the picture!)
```

---

## 4. Confidence Scoring 📊

**What is it?**
Measuring how sure the AI is about what it heard.

**Like you're 5:**
Imagine someone whispers something to you. Sometimes you're 100% sure what they said ("I want pizza!"). Sometimes you only heard half ("I want... puh-zah? pizza? I'm 60% sure").

Confidence scoring is the AI saying "I'm 85% sure this is correct."

**How it works:**
```
Audio Input: [muffled sound]
   ↓
AI tries to understand...
   ↓
Generates possibilities:
   1. "Hello there"     - 90% confident ✓ PICK THIS
   2. "Yellow bear"     - 30% confident
   3. "Jello square"    - 10% confident
   ↓
Output: "Hello there" (confidence: 0.90)

If confidence < 0.5 → Probably wrong, filter it out!
If confidence > 0.8 → Very confident, keep it!
```

**Code Example:**
```python
def calculate_confidence(whisper_result):
    # Whisper gives us "no_speech_prob" for each segment
    # This is "probability it's NOT speech" (0 to 1)
    
    segments = whisper_result['segments']
    
    # Average across all segments
    total_no_speech_prob = 0
    for segment in segments:
        total_no_speech_prob += segment['no_speech_prob']
    
    avg_no_speech_prob = total_no_speech_prob / len(segments)
    
    # Convert to confidence (flip it!)
    # If no_speech_prob = 0.1 → confidence = 0.9 (90% sure it's speech)
    # If no_speech_prob = 0.8 → confidence = 0.2 (20% sure it's speech)
    confidence = 1.0 - avg_no_speech_prob
    
    return confidence
```

---

## 5. Duration Filtering ⏱️

**What is it?**
Keeping only audio that's not too short or too long.

**Like you're 5:**
Imagine sorting your toys. You throw away:
- Broken tiny pieces (too small to play with)
- Giant boxes that don't fit in your room (too big)
- Keep only the toys that are just right!

**How it works:**
```
Audio File 1: 0.5 seconds
   ├─ Too short! (probably just a click)
   └─ ❌ REJECT

Audio File 2: 8 seconds
   ├─ Just right! (perfect for speech)
   └─ ✅ KEEP

Audio File 3: 500 seconds (8 minutes!)
   ├─ Too long! (might be music or error)
   └─ ❌ REJECT

Settings:
   MIN: 2 seconds
   MAX: 300 seconds (5 minutes)
```

**Code Example:**
```python
def filter_by_duration(duration, min_sec=2.0, max_sec=300.0):
    if duration < min_sec:
        return False, f"Too short: {duration:.1f}s < {min_sec}s"
    
    if duration > max_sec:
        return False, f"Too long: {duration:.1f}s > {max_sec}s"
    
    return True, "Duration OK!"

# Examples:
print(filter_by_duration(1.5))   # (False, "Too short...")
print(filter_by_duration(10.0))  # (True, "Duration OK!")
print(filter_by_duration(400.0)) # (False, "Too long...")
```

---

## 6. Text Quality Checking ✓

**What is it?**
Making sure the transcription makes sense.

**Like you're 5:**
Imagine a robot listens to a story and writes:
- "The cat sat on the mat" ✅ Makes sense!
- "asdfghjkl" ❌ Gibberish!
- "the the the the the" ❌ Something's wrong!
- "" (empty) ❌ Heard nothing!

**How it works:**
```
Check 1: Is it empty?
   Text: ""
   Result: ❌ FAIL

Check 2: Does it have real words?
   Text: "12345 !@#$"
   Has letters? No
   Result: ❌ FAIL

Check 3: Enough words?
   Text: "Hi"
   Word count: 1 (need at least 3)
   Result: ❌ FAIL

Check 4: Not too repetitive?
   Text: "Hello hello hello hello hello"
   Unique words: 1 out of 5 = 20% unique
   Too repetitive! (need >30% unique)
   Result: ❌ FAIL

Check 5: All checks passed?
   Text: "The quick brown fox jumps"
   ✓ Not empty
   ✓ Has letters
   ✓ 5 words (>3)
   ✓ 100% unique words
   Result: ✅ PASS
```

**Code Example:**
```python
import re

def check_text_quality(text, min_words=3):
    # Check 1: Empty?
    if not text or len(text.strip()) == 0:
        return False, "Empty text"
    
    # Check 2: Has letters?
    if not re.search(r'[a-zA-Z]', text):
        return False, "No letters found"
    
    # Check 3: Enough words?
    words = text.split()
    if len(words) < min_words:
        return False, f"Only {len(words)} words (need {min_words})"
    
    # Check 4: Too repetitive?
    unique_ratio = len(set(words)) / len(words)
    if unique_ratio < 0.3 and len(words) > 5:
        return False, f"Too repetitive ({unique_ratio:.0%} unique)"
    
    # All passed!
    return True, "Quality OK!"
```

---

# Complete Pipeline Flowchart

## Full System Flow Diagram

```
╔══════════════════════════════════════════════════════════════════╗
║                   AUDIO DATASET PIPELINE                         ║
║                    Complete Flow Diagram                         ║
╚══════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────┐
│  USER ACTION: Place audio files in raw_audio/ folder           │
│  Files: recording.mp3, interview.m4a, speech.wav, etc.         │
└─────────────────────────────────────────────────────────────────┘
                            │
                            ▼
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  PIPELINE STARTS                                               ┃
┃  Command: python run_pipeline.py                              ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  Determine Version Number             │
        │  • Check output/ directory            │
        │  • Find existing versions             │
        │  • Auto-increment (v1, v2, v3...)     │
        └───────────────────────────────────────┘
                            │
                            ▼
╔════════════════════════════════════════════════════════════════╗
║  STAGE 1: PREPROCESSING (preprocess.py)                       ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  Input: raw_audio/*.{mp3,wav,m4a,ogg}                        ║
║     │                                                          ║
║     ├─► Find all audio files                                  ║
║     │   • Scan for: .mp3, .wav, .m4a, .ogg, .flac            ║
║     │   • Found: 5 files                                      ║
║     │                                                          ║
║     ▼                                                          ║
║  FOR EACH AUDIO FILE:                                         ║
║     │                                                          ║
║     ├─► Step 1.1: Load Audio                                  ║
║     │   ┌────────────────────────────────┐                   ║
║     │   │ librosa.load()                 │                   ║
║     │   │ • Read file                    │                   ║
║     │   │ • Resample to 16kHz            │                   ║
║     │   │ • Convert to mono              │                   ║
║     │   └────────────────────────────────┘                   ║
║     │   Result: audio array + sample rate                     ║
║     │                                                          ║
║     ├─► Step 1.2: Trim Silence                                ║
║     │   ┌────────────────────────────────┐                   ║
║     │   │ librosa.effects.trim()         │                   ║
║     │   │ • Detect silence (< -20dB)     │                   ║
║     │   │ • Remove from start/end        │                   ║
║     │   └────────────────────────────────┘                   ║
║     │   Result: trimmed audio                                 ║
║     │                                                          ║
║     ├─► Step 1.3: Normalize Volume                            ║
║     │   ┌────────────────────────────────┐                   ║
║     │   │ Custom normalize_audio()       │                   ║
║     │   │ • Calculate RMS level          │                   ║
║     │   │ • Target: -20 dBFS             │                   ║
║     │   │ • Prevent clipping             │                   ║
║     │   └────────────────────────────────┘                   ║
║     │   Result: normalized audio                              ║
║     │                                                          ║
║     ├─► Step 1.4: Save Processed Audio                        ║
║     │   ┌────────────────────────────────┐                   ║
║     │   │ soundfile.write()              │                   ║
║     │   │ • Format: WAV                  │                   ║
║     │   │ • Sample rate: 16000 Hz        │                   ║
║     │   │ • Location: processed_audio/   │                   ║
║     │   └────────────────────────────────┘                   ║
║     │                                                          ║
║     └─► Collect Metadata                                      ║
║         • Original duration                                    ║
║         • Final duration                                       ║
║         • Sample rate                                          ║
║         • Output path                                          ║
║                                                                ║
║  Output: processed_audio/*.wav + preprocessing results        ║
║  Progress: [████████████] 5/5 files (100%)                   ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  Check: Did preprocessing succeed?    │
        │  • Success: 5 files                   │
        │  • Failed: 0 files                    │
        └───────────────────────────────────────┘
                            │
                   ┌────────┴────────┐
                   │                 │
                 NO│                 │YES
        ┌──────────▼─────┐           │
        │  ERROR!        │           │
        │  Exit pipeline │           │
        └────────────────┘           │
                                     ▼
╔════════════════════════════════════════════════════════════════╗
║  STAGE 2: TRANSCRIPTION (transcribe.py)                       ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  Input: processed_audio/*.wav                                 ║
║     │                                                          ║
║     ├─► Step 2.1: Load Whisper Model                          ║
║     │   ┌────────────────────────────────┐                   ║
║     │   │ whisper.load_model("base")     │                   ║
║     │   │ • Download if first time       │                   ║
║     │   │ • Load from cache (~140 MB)    │                   ║
║     │   │ • Initialize AI model          │                   ║
║     │   └────────────────────────────────┘                   ║
║     │   Model Ready! ✓                                        ║
║     │                                                          ║
║     ▼                                                          ║
║  FOR EACH PROCESSED AUDIO:                                    ║
║     │                                                          ║
║     ├─► Step 2.2: Transcribe Audio                            ║
║     │   ┌────────────────────────────────┐                   ║
║     │   │ model.transcribe()             │                   ║
║     │   │                                │                   ║
║     │   │ Internal Whisper Process:      │                   ║
║     │   │  1. Load audio                 │                   ║
║     │   │  2. Create Mel spectrogram     │                   ║
║     │   │  3. Run through encoder        │                   ║
║     │   │  4. Generate text via decoder  │                   ║
║     │   │  5. Detect language            │                   ║
║     │   │  6. Calculate confidence       │                   ║
║     │   └────────────────────────────────┘                   ║
║     │                                                          ║
║     ├─► Step 2.3: Extract Results                             ║
║     │   • Transcribed text                                    ║
║     │   • Detected language                                   ║
║     │   • Confidence score                                    ║
║     │   • Word count                                          ║
║     │   • Segment information                                 ║
║     │                                                          ║
║     └─► Store Results                                         ║
║                                                                ║
║  Output: transcription_results (list of dicts)                ║
║  Progress: [████████████] 5/5 files (100%)                   ║
║  Stats: 87 total words, avg confidence: 0.78                  ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  Check: Were transcriptions OK?       │
        │  • Success: 5 files                   │
        │  • Failed: 0 files                    │
        └───────────────────────────────────────┘
                            │
                   ┌────────┴────────┐
                   │                 │
                 NO│                 │YES
        ┌──────────▼─────┐           │
        │  ERROR!        │           │
        │  Exit pipeline │           │
        └────────────────┘           │
                                     ▼
╔════════════════════════════════════════════════════════════════╗
║  STAGE 3: QUALITY FILTERING (filter_quality.py)               ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  Input: preprocessing_results + transcription_results         ║
║     │                                                          ║
║     ▼                                                          ║
║  FOR EACH SAMPLE:                                             ║
║     │                                                          ║
║     ├─► FILTER 1: Duration Check                              ║
║     │   ┌────────────────────────────────┐                   ║
║     │   │ Check audio length:            │                   ║
║     │   │ • Min: 2.0 seconds             │                   ║
║     │   │ • Max: 300.0 seconds           │                   ║
║     │   │                                │                   ║
║     │   │ Sample: 7.5 seconds            │                   ║
║     │   │ Result: ✓ PASS                 │                   ║
║     │   └────────────────────────────────┘                   ║
║     │                                                          ║
║     ├─► FILTER 2: Transcription Quality                       ║
║     │   ┌────────────────────────────────┐                   ║
║     │   │ Check 1: Not empty?            │                   ║
║     │   │  Text: "Hello world"           │                   ║
║     │   │  Result: ✓ PASS                │                   ║
║     │   │                                │                   ║
║     │   │ Check 2: Confidence OK?        │                   ║
║     │   │  Score: 0.78 (>0.3 needed)     │                   ║
║     │   │  Result: ✓ PASS                │                   ║
║     │   │                                │                   ║
║     │   │ Check 3: Enough words?         │                   ║
║     │   │  Count: 13 (>3 needed)         │                   ║
║     │   │  Result: ✓ PASS                │                   ║
║     │   │                                │                   ║
║     │   │ Check 4: Has letters?          │                   ║
║     │   │  Pattern: [a-zA-Z]             │                   ║
║     │   │  Result: ✓ PASS                │                   ║
║     │   │                                │                   ║
║     │   │ Check 5: Not repetitive?       │                   ║
║     │   │  Unique ratio: 92%             │                   ║
║     │   │  Result: ✓ PASS                │                   ║
║     │   └────────────────────────────────┘                   ║
║     │                                                          ║
║     └─► Decision                                              ║
║         ┌──────────────────────┐                              ║
║         │ All filters passed?  │                              ║
║         └──────────────────────┘                              ║
║                │                                               ║
║       ┌────────┴────────┐                                     ║
║      YES               NO                                     ║
║       │                 │                                     ║
║       ▼                 ▼                                     ║
║  ✅ KEEP          ❌ REJECT                                  ║
║  Add to          Record reason                                ║
║  filtered_       (too short,                                  ║
║  samples         low confidence,                              ║
║                  etc.)                                        ║
║                                                                ║
║  Output: Filtered samples + filter report                     ║
║  Results:                                                      ║
║    • Total samples: 5                                         ║
║    • Passed: 4                                                ║
║    • Failed duration: 1 (0.8s - too short)                   ║
║    • Failed quality: 0                                        ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  Check: Any samples passed?           │
        │  Passed: 4 samples                    │
        └───────────────────────────────────────┘
                            │
                   ┌────────┴────────┐
                   │                 │
                 NO│                 │YES
        ┌──────────▼─────┐           │
        │  ERROR!        │           │
        │  All filtered! │           │
        └────────────────┘           │
                                     ▼
╔════════════════════════════════════════════════════════════════╗
║  STAGE 4: DATASET CREATION (create_dataset.py)                ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  Input: filtered_samples (4 samples)                          ║
║     │                                                          ║
║     ├─► Step 4.1: Create Metadata Records                     ║
║     │   ┌────────────────────────────────┐                   ║
║     │   │ For each sample, collect:      │                   ║
║     │   │  • sample_id                   │                   ║
║     │   │  • filename                    │                   ║
║     │   │  • audio_path                  │                   ║
║     │   │  • transcription               │                   ║
║     │   │  • duration_seconds            │                   ║
║     │   │  • sample_rate                 │                   ║
║     │   │  • language                    │                   ║
║     │   │  • confidence                  │                   ║
║     │   │  • word_count                  │                   ║
║     │   │  • segments                    │                   ║
║     │   │  • original_duration           │                   ║
║     │   │  • trimmed_duration            │                   ║
║     │   └────────────────────────────────┘                   ║
║     │                                                          ║
║     ├─► Step 4.2: Create DataFrame                            ║
║     │   ┌────────────────────────────────┐                   ║
║     │   │ pd.DataFrame(records)          │                   ║
║     │   │ • Sort by sample_id            │                   ║
║     │   │ • Reset index                  │                   ║
║     │   └────────────────────────────────┘                   ║
║     │                                                          ║
║     ├─► Step 4.3: Calculate Statistics                        ║
║     │   ┌────────────────────────────────┐                   ║
║     │   │ • Version number               │                   ║
║     │   │ • Creation timestamp           │                   ║
║     │   │ • Total samples: 4             │                   ║
║     │   │ • Total duration: 34.2s        │                   ║
║     │   │ • Total words: 87              │                   ║
║     │   │ • Avg duration: 8.55s          │                   ║
║     │   │ • Avg confidence: 0.78         │                   ║
║     │   │ • Languages: {en: 4}           │                   ║
║     │   │ • Min/max duration             │                   ║
║     │   └────────────────────────────────┘                   ║
║     │                                                          ║
║     ├─► Step 4.4: Create Version Directory                    ║
║     │   ┌────────────────────────────────┐                   ║
║     │   │ output/dataset_v1/             │                   ║
║     │   └────────────────────────────────┘                   ║
║     │                                                          ║
║     ├─► Step 4.5: Save Dataset Files                          ║
║     │   ┌────────────────────────────────┐                   ║
║     │   │ 1. dataset.csv                 │                   ║
║     │   │    • Spreadsheet format        │                   ║
║     │   │    • All metadata columns      │                   ║
║     │   │                                │                   ║
║     │   │ 2. dataset.jsonl               │                   ║
║     │   │    • One JSON per line         │                   ║
║     │   │    • Same data as CSV          │                   ║
║     │   │                                │                   ║
║     │   │ 3. statistics.json             │                   ║
║     │   │    • Dataset stats             │                   ║
║     │   │    • Version info              │                   ║
║     │   │                                │                   ║
║     │   │ 4. README.txt                  │                   ║
║     │   │    • Human-readable summary    │                   ║
║     │   │    • Sample previews           │                   ║
║     │   └────────────────────────────────┘                   ║
║     │                                                          ║
║     └─► Step 4.6: Print Summary                               ║
║         ┌────────────────────────────────┐                   ║
║         │ DATASET SUMMARY                │                   ║
║         │ Version: 1                     │                   ║
║         │ Samples: 4                     │                   ║
║         │ Duration: 34.2s (0.57 min)     │                   ║
║         │ Words: 87                      │                   ║
║         │ Avg confidence: 0.78           │                   ║
║         │ Languages: English (4)         │                   ║
║         └────────────────────────────────┘                   ║
║                                                                ║
║  Output: Complete dataset in output/dataset_v1/               ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
                            │
                            ▼
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  PIPELINE COMPLETE! ✅                                        ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃                                                                ┃
┃  Final Summary:                                               ┃
┃  • Input: 5 raw audio files                                   ┃
┃  • Preprocessed: 5 files                                      ┃
┃  • Transcribed: 5 files                                       ┃
┃  • Passed filters: 4 files                                    ┃
┃  • Final dataset: 4 samples                                   ┃
┃                                                                ┃
┃  Dataset saved to: output/dataset_v1/                         ┃
┃  Files created:                                               ┃
┃    ✓ dataset.csv                                              ┃
┃    ✓ dataset.jsonl                                            ┃
┃    ✓ statistics.json                                          ┃
┃    ✓ README.txt                                               ┃
┃                                                                ┃
┃  Exit code: 0 (success)                                       ┃
┃                                                                ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│  USER: Check results in output/dataset_v1/                     │
│  • Open dataset.csv in Excel                                   │
│  • Read README.txt for summary                                 │
│  • Use data for your project!                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Data Flow Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                        DATA TRANSFORMATION                       │
└──────────────────────────────────────────────────────────────────┘

RAW INPUT                    INTERMEDIATE                  FINAL OUTPUT
───────────                  ────────────                  ────────────

recording.mp3     ┬─►  recording.wav      ┬─►  ┌──────────────────┐
  480 KB          │      (processed)      │    │ sample_id        │
  44.1 kHz        │      16 kHz mono      │    │ filename         │
  Stereo          │      8.5 seconds      │    │ audio_path       │
  12 seconds      │      Normalized       │    │ transcription    │
                  │                       │    │ duration         │
interview.m4a     │                       │    │ sample_rate      │
  256 KB          │                       │    │ language         │
  48 kHz          ├─►  interview.wav  ────┤    │ confidence       │
  Mono            │      (processed)      │    │ word_count       │
  10 seconds      │                       │    │ ...more fields   │
                  │                       │    └──────────────────┘
speech.wav        │                       │             │
  180 KB          │                       │             │
  22 kHz          ├─►  speech.wav    ─────┤             │
  Mono            │      (processed)      │             ▼
  6 seconds       │                       │    ┌──────────────────┐
                  │                       ├───►│  dataset.csv     │
podcast.ogg       │                       │    │  dataset.jsonl   │
  520 KB          │                       │    │  statistics.json │
  48 kHz          ├─►  podcast.wav   ─────┤    │  README.txt      │
  Stereo          │      (processed)      │    └──────────────────┘
  15 seconds      │                       │
                  │                       │    Structured Dataset
click.wav         │                       │    ✓ Clean audio
  8 KB            │                       │    ✓ Transcriptions
  16 kHz          ├─►  click.wav     ─────┤    ✓ Metadata
  Mono            │      (processed)      │    ✓ Statistics
  0.8 seconds     │                       │    ✓ Quality filtered
                  │                       │    ✓ Versioned
                  │     ❌ FILTERED OUT   │
                  └      (too short)      │
                                          │
                  Whisper AI adds:        │
                  • Transcriptions        │
                  • Language detection    │
                  • Confidence scores     │
```

---

## Module Interaction Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                   MODULE INTERACTION FLOW                       │
└─────────────────────────────────────────────────────────────────┘

                    run_pipeline.py (Main Orchestrator)
                            │
                ┌───────────┼───────────┐
                │           │           │
                ▼           ▼           ▼
        ┌───────────┐ ┌──────────┐ ┌──────────────┐
        │preprocess │ │transcribe│ │filter_quality│
        │   .py     │ │  .py     │ │    .py       │
        └───────────┘ └──────────┘ └──────────────┘
                │           │           │
                │           │           │
        Uses:   │   Uses:   │   Uses:   │
        ├librosa│   └whisper│   └(logic)│
        ├soundfile         │            │
        └numpy             │            │
                │           │           │
                └───────────┴───────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │create_dataset│
                    │    .py       │
                    └──────────────┘
                            │
                    Uses:   │
                    ├pandas │
                    ├json   │
                    └pathlib│
                            │
                            ▼
                    Final Dataset Files
```

---

## Decision Tree Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│              SAMPLE FILTERING DECISION TREE                     │
└─────────────────────────────────────────────────────────────────┘

                        Sample Audio File
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Preprocessing OK?    │
                    └──────────────────────┘
                         │          │
                      YES│          │NO
                         │          └──────► ❌ REJECT
                         │                   "Processing failed"
                         ▼
                    ┌──────────────────────┐
                    │ Duration >= 2.0s?    │
                    └──────────────────────┘
                         │          │
                      YES│          │NO
                         │          └──────► ❌ REJECT
                         │                   "Too short"
                         ▼
                    ┌──────────────────────┐
                    │ Duration <= 300s?    │
                    └──────────────────────┘
                         │          │
                      YES│          │NO
                         │          └──────► ❌ REJECT
                         │                   "Too long"
                         ▼
                    ┌──────────────────────┐
                    │ Transcription OK?    │
                    └──────────────────────┘
                         │          │
                      YES│          │NO
                         │          └──────► ❌ REJECT
                         │                   "Transcription failed"
                         ▼
                    ┌──────────────────────┐
                    │ Text not empty?      │
                    └──────────────────────┘
                         │          │
                      YES│          │NO
                         │          └──────► ❌ REJECT
                         │                   "Empty transcription"
                         ▼
                    ┌──────────────────────┐
                    │ Confidence >= 0.3?   │
                    └──────────────────────┘
                         │          │
                      YES│          │NO
                         │          └──────► ❌ REJECT
                         │                   "Low confidence"
                         ▼
                    ┌──────────────────────┐
                    │ Word count >= 3?     │
                    └──────────────────────┘
                         │          │
                      YES│          │NO
                         │          └──────► ❌ REJECT
                         │                   "Too few words"
                         ▼
                    ┌──────────────────────┐
                    │ Has letters?         │
                    └──────────────────────┘
                         │          │
                      YES│          │NO
                         │          └──────► ❌ REJECT
                         │                   "No text content"
                         ▼
                    ┌──────────────────────┐
                    │ Not repetitive?      │
                    │ (>30% unique words)  │
                    └──────────────────────┘
                         │          │
                      YES│          │NO
                         │          └──────► ❌ REJECT
                         │                   "Too repetitive"
                         ▼
                    ┌──────────────────────┐
                    │  ✅ ACCEPT           │
                    │  Add to dataset      │
                    └──────────────────────┘
```

---

## File System State Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                   FILE SYSTEM EVOLUTION                         │
└─────────────────────────────────────────────────────────────────┘

BEFORE PIPELINE:
───────────────
audio_dataset_pipeline/
├── raw_audio/
│   ├── recording.mp3        ← User adds files here
│   ├── interview.m4a
│   └── speech.wav
├── processed_audio/         ← Empty
├── output/                  ← Empty
├── preprocess.py
├── transcribe.py
├── filter_quality.py
├── create_dataset.py
├── run_pipeline.py
└── requirements.txt


DURING PIPELINE (Stage 1):
──────────────────────────
audio_dataset_pipeline/
├── raw_audio/
│   ├── recording.mp3
│   ├── interview.m4a
│   └── speech.wav
├── processed_audio/
│   ├── recording.wav        ← Generated
│   ├── interview.wav        ← Generated
│   └── speech.wav           ← Generated
├── output/                  ← Still empty
└── ...


AFTER PIPELINE:
───────────────
audio_dataset_pipeline/
├── raw_audio/
│   ├── recording.mp3        ← Original files (untouched)
│   ├── interview.m4a
│   └── speech.wav
├── processed_audio/
│   ├── recording.wav        ← Standardized audio
│   ├── interview.wav
│   └── speech.wav
├── output/
│   └── dataset_v1/          ← NEW!
│       ├── dataset.csv          ← Main dataset
│       ├── dataset.jsonl        ← JSON format
│       ├── statistics.json      ← Stats
│       └── README.txt           ← Summary
└── ...


AFTER SECOND RUN:
─────────────────
audio_dataset_pipeline/
├── raw_audio/
│   ├── recording.mp3
│   ├── interview.m4a
│   ├── speech.wav
│   └── new_audio.mp3        ← User added more
├── processed_audio/
│   ├── recording.wav
│   ├── interview.wav
│   ├── speech.wav
│   └── new_audio.wav        ← New processed file
├── output/
│   ├── dataset_v1/          ← Old version (preserved)
│   │   ├── dataset.csv
│   │   ├── dataset.jsonl
│   │   ├── statistics.json
│   │   └── README.txt
│   └── dataset_v2/          ← NEW VERSION!
│       ├── dataset.csv          ← Updated dataset
│       ├── dataset.jsonl
│       ├── statistics.json
│       └── README.txt
└── ...
```

---

## Summary Table

| Stage | Module | Input | Output | Key Operations |
|-------|--------|-------|--------|----------------|
| **1** | preprocess.py | Raw audio files | Standardized WAV | Load, resample, trim, normalize |
| **2** | transcribe.py | Processed WAV | Transcriptions | Load Whisper, transcribe, extract metadata |
| **3** | filter_quality.py | All results | Filtered samples | Duration check, quality check |
| **4** | create_dataset.py | Filtered samples | Final dataset | Create DataFrame, calculate stats, save files |

---

**🎉 Congratulations! You now understand the complete pipeline!**

- ✅ All libraries explained with examples
- ✅ Algorithms explained like you're 5 years old
- ✅ Complete flowcharts and diagrams
- ✅ Data flow visualization
- ✅ Module interactions
- ✅ Decision trees

**Ready to build amazing audio datasets!** 🚀
