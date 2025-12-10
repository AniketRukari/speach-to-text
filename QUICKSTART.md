# Quick Start Guide

## Installation

```bash
cd audio_dataset_pipeline
pip install -r requirements.txt
```

Also install FFmpeg:
- Windows: `choco install ffmpeg`
- Linux: `sudo apt install ffmpeg`
- Mac: `brew install ffmpeg`

## Usage

1. **Add audio files** to `raw_audio/` folder (5-20 files)
2. **Run pipeline:**
   ```bash
   python run_pipeline.py
   ```
3. **Check results** in `output/dataset_v1/`

## Common Commands

```bash
# Basic run with defaults
python run_pipeline.py

# Use better accuracy model
python run_pipeline.py --model-size small

# Stricter quality filtering
python run_pipeline.py --min-confidence 0.5 --min-words 5

# English only
python run_pipeline.py --language en

# See all options
python run_pipeline.py --help
```

## What You Get

After running, you'll find in `output/dataset_v1/`:
- `dataset.csv` - Main dataset in CSV format
- `dataset.jsonl` - Dataset in JSONL format
- `statistics.json` - Dataset statistics
- `README.txt` - Human-readable summary

## Architecture

1. **Preprocessing** - Standardize audio (16kHz mono wav)
2. **Transcription** - Convert speech to text (Whisper AI)
3. **Quality Filtering** - Remove poor samples
4. **Dataset Creation** - Structure and version output

## Troubleshooting

**No files found?**
- Check files are in `raw_audio/` folder
- Supported: mp3, wav, aac, ogg, m4a, flac

**FFmpeg error?**
- Install FFmpeg and add to PATH

**All filtered out?**
- Lower thresholds: `--min-confidence 0.1`
- Check audio isn't silent/corrupted

**Too slow?**
- Use faster model: `--model-size tiny`

---
See README.md for full documentation.
