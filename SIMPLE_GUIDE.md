# Audio Dataset Builder - Explained for Everyone! 🎤

## What Does This Do?

Imagine you have a bunch of audio recordings - maybe you talking, singing, or reading a book. This tool is like a **magic machine** that:

1. **Listens** to your audio files
2. **Writes down** what it hears (like typing out the words)
3. **Organizes** everything neatly
4. **Saves** it all in an easy-to-use folder

It's like having a super-fast robot assistant that can listen to recordings and make a perfectly organized notebook!

## Why Would You Use This?

Let's say you have 10 recordings of people talking. Instead of listening to each one and typing what they say (which takes FOREVER), this tool does it all automatically! It's perfect for:

- 📚 Making text versions of voice recordings
- 🎯 Organizing audio collections
- 🔬 Science projects with speech data
- 🎓 School projects about language or audio

## How Does It Work? (Step by Step)

### Step 1: Give It Your Audio Files 🎵

You have some audio files on your computer - maybe they're:
- mp3 files (like music files)
- wav files (like sound effects)
- m4a files (like voice memos from your phone)
- Or other audio types!

You put these files in a special folder called `raw_audio`.

**Real-life example:** It's like putting dirty clothes in a laundry basket!

---

### Step 2: The Machine Cleans Up Your Audio 🧹

The tool takes your audio and makes it perfect:

**What it does:**
- Makes all audio files the same type (wav files)
- Removes awkward silence at the beginning and end
- Makes the volume the same for all files (not too loud, not too quiet)
- Makes sure everything sounds clear

**Why this matters:**
Imagine you have 5 friends all talking, but one whispers, one shouts, and one has music playing. You want everyone at the same volume so you can hear clearly!

**Real-life example:** It's like washing and ironing your clothes so they all look nice and neat!

---

### Step 3: The Machine Listens and Writes 👂✍️

This is the coolest part! The tool uses **Whisper AI** (a super-smart computer program) to:
- Listen to what people are saying in the audio
- Write down every word it hears
- Figure out what language they're speaking
- Tell you how confident it is (like "I'm 90% sure this is correct!")

**Real-life example:** It's like having a friend who can listen to a recording and type out everything that was said - but this friend types SUPER FAST and never gets tired!

---

### Step 4: The Machine Checks for Quality ✅

Not all audio is good quality. The tool is smart and throws away bad recordings:

**What it checks:**

1. **Is the audio too short or too long?**
   - Too short (like 1 second): Probably just a click or noise
   - Too long (like 1 hour): Maybe too much to handle
   - Just right (like 5-60 seconds): Perfect!

2. **Did it understand the words clearly?**
   - No words heard: Maybe just static or noise - SKIP IT!
   - Only 1 or 2 words: Probably not useful - SKIP IT!
   - Lots of clear words: KEEP IT! ✓
   - Same word repeated 50 times: Something's wrong - SKIP IT!

**Real-life example:** It's like sorting your clothes after washing - keeping the good ones and throwing away anything with holes or stains!

---

### Step 5: The Machine Organizes Everything 📊

Now the tool creates a beautiful, organized collection! It saves:

**Files you get:**

1. **dataset.csv** - Like a spreadsheet (you can open in Excel!)
   - Shows: filename, what was said, how long, confidence score, language, etc.

2. **dataset.jsonl** - Computer-friendly format
   - Same information, but easier for programs to read

3. **statistics.json** - Summary numbers
   - How many recordings total?
   - How many words in total?
   - Average length of recordings
   - What languages detected?

4. **README.txt** - A friendly summary you can read
   - Shows you a preview of what you got!

**Real-life example:** It's like organizing your clean clothes into your dresser with labels - "T-shirts here, pants here, socks here!"

---

### Step 6: Versioning (Keeping Track) 🗂️

Every time you run the tool, it saves your results in a new "version":
- First time: `dataset_v1`
- Second time: `dataset_v2`
- Third time: `dataset_v3`

**Why?** So you can compare! Maybe you add more audio files later and want to see how your collection grew.

**Real-life example:** It's like taking a photo of your Lego creation each time you add new pieces!

---

## The Whole Journey (Visual)

```
🎵 Your Audio Files (messy, different types)
        ⬇️
🧹 Step 1: Clean and standardize
        ⬇️
👂 Step 2: Listen and write down words
        ⬇️
✅ Step 3: Check quality (keep only good ones)
        ⬇️
📊 Step 4: Organize into neat files
        ⬇️
🎉 Your Dataset (ready to use!)
```

---

## What's Inside Each Part?

### 📁 Folders

- **raw_audio/** - Where YOU put your original audio files
- **processed_audio/** - Where the TOOL saves cleaned audio
- **output/** - Where your FINAL organized dataset lives

### 🐍 Python Files (The Brain!)

Each file is like a worker with one specific job:

1. **preprocess.py** - The Cleaner
   - Job: Clean up audio files
   - Makes: Standardized wav files

2. **transcribe.py** - The Listener & Writer
   - Job: Listen to audio and write down words
   - Uses: Whisper AI (super smart!)

3. **filter_quality.py** - The Quality Inspector
   - Job: Check if audio is good or bad
   - Keeps: Only the good stuff!

4. **create_dataset.py** - The Organizer
   - Job: Put everything in neat files
   - Makes: CSV, JSON, and summary files

5. **run_pipeline.py** - The Boss!
   - Job: Tells all the other workers what to do
   - This is the ONE file you run!

---

## How to Use It (Super Simple!)

### Before You Start:

1. **Install Python** (the programming language) on your computer
2. **Install the tools** the program needs:
   ```
   pip install -r requirements.txt
   ```
3. **Install FFmpeg** (helps with audio files):
   ```
   winget install --id Gyan.FFmpeg -e
   ```

### Running It:

1. Put your audio files in the `raw_audio` folder
2. Open PowerShell (or Command Prompt)
3. Type this magic command:
   ```
   python run_pipeline.py
   ```
4. Wait for it to finish (you'll see progress bars!)
5. Check the `output` folder for your results!

---

## What You'll See While It Runs

The tool will show you progress like this:

```
============================================================
AUDIO DATASET PIPELINE
============================================================

STAGE 1: AUDIO PREPROCESSING
Found 5 audio files to process
Processing audio: 100% ████████████ 5/5

STAGE 2: TRANSCRIPTION
Transcribing 5 audio files...
Transcribing: 100% ████████████ 5/5

STAGE 3: QUALITY FILTERING
Passed all filters: 4
Failed: 1 (too short)

STAGE 4: DATASET CREATION
Dataset saved to: output/dataset_v1

PIPELINE COMPLETE! 🎉
```

---

## Cool Features!

### 🌍 Multilingual (Many Languages!)

The tool can understand LOTS of languages:
- English, Spanish, French, German
- Chinese, Japanese, Korean
- And 90+ more!

It automatically detects what language is being spoken!

### 🎯 Smart Filtering

The tool is smart enough to know:
- ❌ "beep beep beep" = Not useful
- ❌ "..." (silence) = Not useful
- ❌ "the the the the the..." = Something's wrong
- ✅ "Hello, how are you today?" = Perfect!

### 📊 Detailed Information

For EACH recording, you get:
- What was said (the transcription)
- How long it is
- What language it's in
- How confident the AI is
- How many words
- Original length vs. cleaned length

---

## Example: What You Get

**You record yourself saying:**
"Hi! My name is Sarah. I love pizza and video games!"

**The tool creates:**

| Info | Value |
|------|-------|
| **Transcription** | "Hi! My name is Sarah. I love pizza and video games!" |
| **Duration** | 6.2 seconds |
| **Language** | English |
| **Confidence** | 95% |
| **Word Count** | 11 words |
| **Quality** | ✅ Passed |

---

## Troubleshooting (When Things Go Wrong)

### "No audio files found!"
🔍 **Problem:** You forgot to put files in `raw_audio` folder
✅ **Solution:** Add some audio files there!

### "FFmpeg not found!"
🔍 **Problem:** The audio converter isn't installed
✅ **Solution:** Install FFmpeg (see instructions above)

### "All samples filtered out!"
🔍 **Problem:** Your audio might be too short, too quiet, or bad quality
✅ **Solution:** Try longer recordings with clear speech

### "It's too slow!"
🔍 **Problem:** Using a large AI model
✅ **Solution:** Use `--model-size tiny` for faster (but less accurate) results

---

## Advanced Options (For Experts!)

You can customize the tool with special commands:

```bash
# Use a smarter (but slower) AI
python run_pipeline.py --model-size large

# Only keep really good quality audio
python run_pipeline.py --min-confidence 0.8 --min-words 10

# Only process English
python run_pipeline.py --language en

# Combine options!
python run_pipeline.py --model-size small --min-confidence 0.6
```

---

## Real-World Use Cases

### 📖 Story Example: The School Project

**Emma's Problem:**
Emma has 10 audio recordings of interviews with her grandparents about life in the 1950s. She needs to write them all down for her history project, but typing takes FOREVER!

**Solution:**
1. Emma puts all 10 recordings in `raw_audio`
2. Runs: `python run_pipeline.py`
3. Gets back: All 10 interviews typed out perfectly!
4. Opens `dataset.csv` in Excel and has all the text ready to copy!

**Time saved:** Instead of 5 hours of typing, Emma spent 5 minutes!

---

### 🎵 Music Example: The Podcast Organizer

**Tom's Problem:**
Tom makes a podcast and has 50 episodes. He wants to know what he talked about in each one, but listening to them all would take 25 hours!

**Solution:**
1. Tom puts all 50 podcast files in `raw_audio`
2. Runs the pipeline
3. Gets a spreadsheet with EVERY episode transcribed!
4. Can now search for keywords and find which episode talked about what topic!

---

## Fun Facts About The Technology

### 🤖 What is Whisper AI?

Whisper is like a super-smart robot made by OpenAI (the same company that made ChatGPT). It was trained by listening to 680,000 HOURS of audio - that's like listening non-stop for 77 years!

### 📊 What is a Dataset?

A dataset is just a fancy word for "organized collection of information." Like:
- A phone book is a dataset of names and numbers
- A recipe book is a dataset of recipes
- Your tool makes a dataset of audio + text!

---

## Summary (The TL;DR)

**What it does:** Turns audio files into organized text + data

**How it works:** 
1. Clean audio
2. Listen with AI
3. Check quality
4. Organize nicely

**Why it's cool:**
- Saves TONS of time
- Super accurate
- Easy to use
- Automatic organization

**Bottom line:** It's like having a super-fast assistant that never gets tired and can type what it hears faster than you can blink!

---

## Questions?

**Q: Do I need internet?**
A: Only for the first time (to download the AI). After that, it works offline!

**Q: How accurate is it?**
A: Usually 90-95% accurate with clear audio. Even better than some humans!

**Q: Can it understand accents?**
A: Yes! It's pretty good with different accents.

**Q: Is it free?**
A: Yes! All the tools used are free and open-source.

**Q: How long does it take?**
A: About 1-2 seconds per second of audio. So a 10-minute recording takes about 10-20 minutes to process.

---

## Final Thoughts

This tool is like having a magical notebook that can hear! 🎧📝

Give it messy audio → Get back organized data! ✨

Perfect for students, researchers, podcasters, or anyone who works with audio and wants to save time!

**Remember:** The computer does the boring work (listening and typing) so you can do the fun work (using the information)!

---

Made with ❤️ for making life easier!

**Version:** 1.0  
**Date:** December 2025  
**Difficulty:** Easy (if you can follow instructions!)  
**Cool Factor:** 🌟🌟🌟🌟🌟
