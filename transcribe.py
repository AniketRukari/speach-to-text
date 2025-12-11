"""
Transcription Module
Uses OpenAI Whisper for automatic speech recognition.
"""
import os
import whisper
from pathlib import Path
from tqdm import tqdm


def load_whisper_model(model_size="base"):
    print(f"Loading Whisper model ({model_size})...")
    model = whisper.load_model(model_size)
    print("Model loaded successfully")
    return model


def transcribe_audio(model, audio_path, language=None):
    try:
        # Transcribe
        result = model.transcribe(
            str(audio_path),
            language=language,
            fp16=False  # Set to False for CPU compatibility
        )
        
        # Extract information
        text = result['text'].strip()
        detected_language = result.get('language', 'unknown')
        
        # Calculate average confidence from segments
        segments = result.get('segments', [])
        if segments:
            # Whisper doesn't directly provide confidence, but we can use
            # no_speech_prob as a proxy (lower is better)
            avg_no_speech_prob = sum(s.get('no_speech_prob', 0) for s in segments) / len(segments)
            confidence = 1.0 - avg_no_speech_prob
        else:
            confidence = 0.5  # Default if no segments
        
        return {
            'success': True,
            'text': text,
            'language': detected_language,
            'confidence': confidence,
            'word_count': len(text.split()),
            'segments': len(segments)
        }
    
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'text': '',
            'confidence': 0.0
        }


def transcribe_batch(audio_dir, model_size="base", language=None):
    """
    Transcribe all audio files in a directory.
    
    Args:
        audio_dir: Directory containing audio files to transcribe
        model_size: Whisper model size
        language: Optional language code
    
    Returns:
        List of transcription results
    """
    audio_path = Path(audio_dir)
    
    # Load model once
    model = load_whisper_model(model_size)
    
    # Find all wav files (should be preprocessed)
    audio_files = list(audio_path.glob('*.wav'))
    
    if not audio_files:
        print(f"No .wav files found in {audio_dir}")
        return []
    
    results = []
    
    print(f"\nTranscribing {len(audio_files)} audio files...")
    
    for audio_file in tqdm(audio_files, desc="Transcribing"):
        result = transcribe_audio(model, audio_file, language)
        result['filename'] = audio_file.name
        result['audio_path'] = str(audio_file)
        results.append(result)
    
    # Print summary
    successful = sum(1 for r in results if r['success'])
    print(f"\nTranscription complete: {successful}/{len(results)} files transcribed successfully")
    
    if successful > 0:
        avg_confidence = sum(r['confidence'] for r in results if r['success']) / successful
        total_words = sum(r['word_count'] for r in results if r['success'])
        print(f"Average confidence: {avg_confidence:.2f}")
        print(f"Total words transcribed: {total_words}")
    
    return results


if __name__ == "__main__":
    # Test the transcription
    audio_dir = "processed_audio"
    
    results = transcribe_batch(audio_dir, model_size="base")
    
    # Print sample transcriptions
    print("\nSample transcriptions:")
    for result in results[:3]:
        if result['success']:
            print(f"\n{result['filename']}:")
            print(f"  Text: {result['text'][:100]}...")
            print(f"  Confidence: {result['confidence']:.2f}")
            print(f"  Language: {result['language']}")

