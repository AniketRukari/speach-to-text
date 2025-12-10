# Audio Dataset Pipeline

A small end-to-end system that transforms raw audio files into a structured, usable dataset suitable for speech-to-text (STT) experimentation.

## Overview

This pipeline takes raw audio files in various formats (mp3, wav, aac, ogg) and converts them into a clean, structured dataset with:
- Standardized audio files (16kHz mono wav)
- High-quality transcriptions using OpenAI Whisper
- Comprehensive metadata (duration, confidence, language, etc.)
- Quality filtering to remove poor samples
- Dataset versioning for reproducibility

## Pipeline Architecture

```
Raw Audio Files (mp3/wav/aac/ogg)
    ↓
[1] PREPROCESSING
    - Load and resample to 16kHz mono
    - Trim silence from edges
    - Normalize volume to -20 dBFS
    ↓
Processed Audio (standardized wav files)
    ↓
[2] TRANSCRIPTION
    - Automatic speech recognition using Whisper
    - Language detection
    - Confidence scoring
    ↓
Transcribed Audio + Text
    ↓
[3] QUALITY FILTERING
    Filter 1: Duration-based (2s - 300s)
    Filter 2: Transcription quality
        - Minimum confidence threshold
        - Minimum word count
        - No empty/nonsensical text
        - No excessive repetition
    ↓
High-Quality Samples
    ↓
[4] DATASET CREATION
    - Structure metadata (CSV + JSONL)
    - Calculate statistics
    - Version and save
    ↓
Final Dataset (versioned in output/dataset_vN/)
```

## Directory Structure

```
audio_dataset_pipeline/
├── raw_audio/              # Place your raw audio files here
├── processed_audio/        # Preprocessed audio (auto-generated)
├── output/                 # Final datasets (auto-generated)
│   └── dataset_v1/
│       ├── dataset.csv
│       ├── dataset.jsonl
│       ├── statistics.json
│       └── README.txt
├── preprocess.py           # Stage 1: Audio preprocessing
├── transcribe.py           # Stage 2: Transcription
├── filter_quality.py       # Stage 3: Quality filtering
├── create_dataset.py       # Stage 4: Dataset structuring
├── run_pipeline.py         # Main pipeline orchestrator
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **Audio processing**: librosa, soundfile, pydub, scipy
- **Speech-to-text**: openai-whisper
- **Data handling**: pandas
- **Utilities**: tqdm

### 2. Install FFmpeg (Required for audio format conversion)

**Windows:**
```bash
# Using Chocolatey
choco install ffmpeg

# Or download from https://ffmpeg.org/download.html
```

**Linux/Mac:**
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# Mac
brew install ffmpeg
```

## Usage

### Quick Start

1. **Add your audio files** to the `raw_audio/` directory
   - Supports: mp3, wav, aac, ogg, m4a, flac
   - Recommended: 5-20 samples for testing

2. **Run the pipeline:**
   ```bash
   python run_pipeline.py
   ```

3. **Find your dataset** in `output/dataset_v1/`

### Advanced Usage

**Specify version:**
```bash
python run_pipeline.py --version 2
```

**Use different Whisper model:**
```bash
# tiny: Fastest, lowest accuracy
# base: Good balance (default)
# small/medium: Better accuracy
# large: Best accuracy, slowest
python run_pipeline.py --model-size small
```

**Adjust quality filters:**
```bash
python run_pipeline.py \
    --min-duration 3 \
    --max-duration 120 \
    --min-confidence 0.5 \
    --min-words 5
```

**Specify language:**
```bash
python run_pipeline.py --language en
```

**See all options:**
```bash
python run_pipeline.py --help
```

## Pipeline Components

### 1. Preprocessing (`preprocess.py`)

**Purpose:** Standardize audio format and quality

**Operations:**
- Load audio and resample to 16kHz (optimal for Whisper)
- Convert to mono channel
- Trim silence from start/end (threshold: 20 dB)
- Normalize volume to -20 dBFS (standard for speech)
- Save as wav format

**Why:**
- Consistent format improves model performance
- Removes noise and silence
- Normalizes volume levels across samples

### 2. Transcription (`transcribe.py`)

**Purpose:** Convert speech to text using AI

**Method:** OpenAI Whisper (local model)
- State-of-the-art open-source STT
- Multilingual support (auto-detection)
- No API keys required
- Runs locally on your machine

**Output:**
- Transcribed text
- Detected language
- Confidence score (derived from no_speech_prob)
- Word count and segment information

### 3. Quality Filtering (`filter_quality.py`)

**Purpose:** Remove low-quality or problematic samples

**Filter 1: Duration-based**
- Minimum: 2 seconds (configurable)
- Maximum: 300 seconds (configurable)
- Removes very short clicks or very long files

**Filter 2: Transcription quality**
- Confidence threshold: 0.3+ (configurable)
- Minimum words: 3+ (configurable)
- Rejects empty transcriptions
- Rejects non-alphabetic output
- Detects excessive repetition (unique word ratio < 0.3)

**Why:**
- Ensures dataset quality
- Removes edge cases that could hurt model training
- Filters out transcription failures

### 4. Dataset Creation (`create_dataset.py`)

**Purpose:** Structure and save the final dataset

**Output Formats:**

1. **CSV** (`dataset.csv`)
   - Tabular format for pandas/Excel
   - Columns: sample_id, filename, audio_path, transcription, duration, confidence, etc.

2. **JSONL** (`dataset.jsonl`)
   - One JSON object per line
   - Easy to stream/process large datasets

3. **Statistics** (`statistics.json`)
   - Dataset metadata
   - Total samples, duration, words
   - Language distribution
   - Min/max/average metrics

4. **Summary** (`README.txt`)
   - Human-readable overview
   - Sample previews

**Versioning:**
- Each run creates a new version: `dataset_v1`, `dataset_v2`, etc.
- Auto-increments if version not specified
- Preserves historical datasets for comparison

## Dataset Schema

Each sample in the final dataset contains:

| Field | Description |
|-------|-------------|
| `sample_id` | Unique identifier (filename stem) |
| `filename` | Processed audio filename |
| `audio_path` | Full path to processed audio |
| `transcription` | Transcribed text |
| `duration_seconds` | Audio duration after processing |
| `sample_rate` | Audio sample rate (16000 Hz) |
| `language` | Detected language code |
| `confidence` | Transcription confidence (0-1) |
| `word_count` | Number of words in transcription |
| `segments` | Number of speech segments |
| `original_duration` | Duration before trimming |
| `trimmed_duration` | Amount trimmed (silence) |

## Example Output

```
PIPELINE COMPLETE
============================================================
Input: 10 raw audio files
Preprocessed: 10 files
Transcribed: 9 files
Final dataset: 7 samples

Dataset saved to: output/dataset_v1

DATASET SUMMARY
============================================================
Version: 1
Created: 2025-12-09T10:30:45

Statistics:
  Total samples: 7
  Total duration: 142.35s (2.37 min)
  Total words: 189
  Average duration: 20.34s
  Average confidence: 0.78
  Duration range: 3.24s - 45.67s

Languages:
  en: 7 samples
============================================================
```

## Configuration

Default parameters in `run_pipeline.py`:

```python
min_duration=2.0          # Minimum audio duration (seconds)
max_duration=300.0        # Maximum audio duration (seconds)
min_confidence=0.3        # Minimum transcription confidence
min_words=3               # Minimum word count
model_size='base'         # Whisper model size
target_sr=16000          # Target sample rate (Hz)
```

## Troubleshooting

**No audio files found:**
- Check that files are in `raw_audio/` directory
- Verify supported formats: mp3, wav, aac, ogg, m4a, flac

**FFmpeg not found:**
- Install FFmpeg (see Installation section)
- Make sure it's in your system PATH

**Whisper download slow:**
- First run downloads the model (~140 MB for 'base')
- Subsequent runs use cached model

**All samples filtered out:**
- Lower quality thresholds: `--min-confidence 0.1 --min-words 1`
- Check audio quality (not silent/corrupted)
- Try a larger Whisper model: `--model-size small`

**Memory issues:**
- Use smaller Whisper model: `--model-size tiny`
- Process fewer files at once
- Close other applications

## Technical Details

**Audio Processing:**
- Library: librosa (industry-standard audio processing)
- Format: 16-bit PCM WAV
- Sample rate: 16kHz (optimal for speech recognition)
- Channels: Mono
- Normalization: -20 dBFS RMS

**Transcription:**
- Model: OpenAI Whisper
- Context: 30-second chunks with overlap
- Precision: FP32 (CPU compatible)
- Languages: 99+ supported (auto-detected)

**Data Format:**
- CSV: RFC 4180 compliant
- JSONL: UTF-8 encoded, one object per line
- Timestamps: ISO 8601 format

## Extending the Pipeline

You can customize or extend the pipeline:

1. **Add new filters:**
   - Edit `filter_quality.py`
   - Add functions returning `(pass: bool, reason: str)`

2. **Change preprocessing:**
   - Modify `preprocess.py`
   - Adjust normalization, trimming, etc.

3. **Use different STT:**
   - Replace `transcribe.py`
   - Maintain same output format

4. **Add metadata fields:**
   - Update `create_dataset.py`
   - Add columns to dataset records

## License

This project uses:
- OpenAI Whisper (MIT License)
- librosa (ISC License)
- Other open-source libraries

## Support

For issues or questions:
1. Check this README
2. Review error messages in terminal
3. Verify all dependencies installed
4. Check that FFmpeg is available

---

**Created:** December 2025
**Pipeline Version:** 1.0
