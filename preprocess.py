"""
Audio Preprocessing Module
Converts raw audio files to standardized format (16kHz mono wav),
trims silence, and normalizes volume.
"""
import os
import librosa
import soundfile as sf
import numpy as np
from pathlib import Path
from tqdm import tqdm


def load_audio(audio_path, target_sr=16000):
    audio, sr = librosa.load(audio_path, sr=target_sr, mono=True)
    return audio, sr


def trim_silence(audio, sr, top_db=20):
    trimmed_audio, _ = librosa.effects.trim(audio, top_db=top_db)
    return trimmed_audio


def normalize_audio(audio):
    # Calculate RMS
    rms = np.sqrt(np.mean(audio**2))
    
    # Target RMS for -20 dBFS
    target_rms = 10**(-20/20)
    
    # Normalize
    if rms > 0:
        normalized_audio = audio * (target_rms / rms)
    else:
        normalized_audio = audio
    
    # Prevent clipping
    max_val = np.max(np.abs(normalized_audio))
    if max_val > 1.0:
        normalized_audio = normalized_audio / max_val
    
    return normalized_audio


def preprocess_audio_file(input_path, output_path, target_sr=16000):
    try:
        # Load audio
        audio, sr = load_audio(input_path, target_sr)
        
        # Get original duration
        original_duration = len(audio) / sr
        
        # Trim silence
        audio = trim_silence(audio, sr)
        
        # Normalize
        audio = normalize_audio(audio)
        
        # Get final duration
        final_duration = len(audio) / sr
        
        # Save processed audio
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        sf.write(output_path, audio, sr)
        
        return {
            'success': True,
            'original_duration': original_duration,
            'final_duration': final_duration,
            'sample_rate': sr,
            'output_path': output_path
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


def preprocess_audio_batch(input_dir, output_dir, target_sr=16000, specific_file=None):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Supported audio formats
    audio_extensions = ['.mp3', '.wav', '.aac', '.ogg', '.m4a', '.flac']
    
    # If specific file is provided, process only that file
    if specific_file:
        specific_path = Path(specific_file)
        
        # Check if it's a full path or just a filename
        if specific_path.exists():
            audio_files = [specific_path]
        else:
            # Try looking in input_dir
            potential_file = input_path / specific_file
            if potential_file.exists():
                audio_files = [potential_file]
            else:
                print(f"Error: File '{specific_file}' not found!")
                return []
    else:
        # Find all audio files in directory
        audio_files = []
        for ext in audio_extensions:
            audio_files.extend(input_path.glob(f'*{ext}'))
    
    results = []
    
    print(f"Found {len(audio_files)} audio files to process")
    
    for audio_file in tqdm(audio_files, desc="Processing audio"):
        # Create output filename (always .wav)
        output_file = output_path / f"{audio_file.stem}.wav"
        
        result = preprocess_audio_file(
            str(audio_file),
            str(output_file),
            target_sr
        )
        
        result['input_file'] = audio_file.name
        result['output_file'] = output_file.name
        
        results.append(result)
    
    # Print summary
    successful = sum(1 for r in results if r['success'])
    print(f"\nPreprocessing complete: {successful}/{len(results)} files processed successfully")
    
    return results


if __name__ == "__main__":
    # Test the preprocessing
    input_dir = "raw_audio"
    output_dir = "processed_audio"
    
    results = preprocess_audio_batch(input_dir, output_dir)
    
    # Print any errors
    for result in results:
        if not result['success']:
            print(f"Error processing {result['input_file']}: {result['error']}")
