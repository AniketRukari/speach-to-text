"""
Audio Dataset Pipeline - Main Orchestrator
End-to-end pipeline for converting raw audio files into a structured STT dataset.

Usage:
    python run_pipeline.py [--version VERSION] [--model-size MODEL]
    
Example:
    python run_pipeline.py --version 1 --model-size base
"""
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

# Import pipeline modules
import preprocess
import transcribe
import filter_quality
import create_dataset


def get_next_version(output_dir):
    """
    Get the next available version number.
    
    Args:
        output_dir: Output directory path
    
    Returns:
        Next version number
    """
    output_path = Path(output_dir)
    if not output_path.exists():
        return 1
    
    # Find existing version directories
    existing_versions = []
    for item in output_path.iterdir():
        if item.is_dir() and item.name.startswith('dataset_v'):
            try:
                version = int(item.name.replace('dataset_v', ''))
                existing_versions.append(version)
            except ValueError:
                continue
    
    if not existing_versions:
        return 1
    
    return max(existing_versions) + 1


def run_pipeline(raw_audio_dir="raw_audio",
                processed_audio_dir="processed_audio",
                output_dir="output",
                version=None,
                model_size="base",
                min_duration=2.0,
                max_duration=300.0,
                min_confidence=0.3,
                min_words=3,
                language=None,
                input_file=None):
    """
    Run the complete audio dataset pipeline.
    
    Pipeline stages:
    1. Preprocessing: Convert, trim, normalize audio
    2. Transcription: Generate text using Whisper
    3. Quality filtering: Remove low-quality samples
    4. Dataset creation: Structure and save dataset
    
    Args:
        raw_audio_dir: Input directory with raw audio files
        processed_audio_dir: Directory for processed audio
        output_dir: Directory for final dataset
        version: Dataset version (auto-increments if None)
        model_size: Whisper model size (tiny/base/small/medium/large)
        min_duration: Minimum audio duration in seconds
        max_duration: Maximum audio duration in seconds
        min_confidence: Minimum transcription confidence
        min_words: Minimum word count
        language: Target language code (None for auto-detect)
        input_file: Process only this specific file (optional)
    
    Returns:
        Dictionary with pipeline results
    """
    print("="*60)
    print("AUDIO DATASET PIPELINE")
    print("="*60)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Show if processing specific file
    if input_file:
        print(f"Processing specific file: {input_file}\n")
    
    # Determine version
    if version is None:
        version = get_next_version(output_dir)
    print(f"Dataset version: {version}\n")
    
    # Stage 1: Preprocessing
    print("\n" + "="*60)
    print("STAGE 1: AUDIO PREPROCESSING")
    print("="*60)
    preprocess_results = preprocess.preprocess_audio_batch(
        raw_audio_dir,
        processed_audio_dir,
        target_sr=16000,
        specific_file=input_file
    )
    
    if not preprocess_results:
        print("ERROR: No audio files found to process!")
        return None
    
    successful_preprocess = [r for r in preprocess_results if r['success']]
    if not successful_preprocess:
        print("ERROR: All preprocessing failed!")
        return None
    
    # Stage 2: Transcription
    print("\n" + "="*60)
    print("STAGE 2: TRANSCRIPTION")
    print("="*60)
    transcription_results = transcribe.transcribe_batch(
        processed_audio_dir,
        model_size=model_size,
        language=language
    )
    
    if not transcription_results:
        print("ERROR: No files transcribed!")
        return None
    
    # Stage 3: Quality Filtering
    print("\n" + "="*60)
    print("STAGE 3: QUALITY FILTERING")
    print("="*60)
    
    # Get list of processed files
    processed_files = [r['output_file'] for r in successful_preprocess]
    
    # Debug: Show what we're filtering
    print(f"Processed files to filter: {processed_files}")
    print(f"Transcription results available: {[r['filename'] for r in transcription_results]}")
    
    filtered_samples, filter_report = filter_quality.apply_filters(
        processed_files,
        preprocess_results,
        transcription_results,
        min_duration=min_duration,
        max_duration=max_duration,
        min_confidence=min_confidence,
        min_words=min_words
    )
    
    filter_quality.print_filter_report(filter_report)
    
    if not filtered_samples:
        print("ERROR: No samples passed quality filters!")
        return None
    
    # Stage 4: Dataset Creation
    print("\n" + "="*60)
    print("STAGE 4: DATASET CREATION")
    print("="*60)
    
    df, stats = create_dataset.create_dataset_metadata(
        filtered_samples,
        output_dir,
        version
    )
    
    create_dataset.print_dataset_summary(df, stats)
    
    saved_paths = create_dataset.save_dataset(df, stats, output_dir, version)
    
    # Final summary
    print("\n" + "="*60)
    print("PIPELINE COMPLETE")
    print("="*60)
    print(f"Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"\nInput: {len(preprocess_results)} raw audio files")
    print(f"Preprocessed: {len(successful_preprocess)} files")
    print(f"Transcribed: {len([r for r in transcription_results if r['success']])} files")
    print(f"Final dataset: {len(filtered_samples)} samples")
    print(f"\nDataset saved to: {saved_paths['version_dir']}")
    print("="*60)
    
    return {
        'version': version,
        'preprocess_results': preprocess_results,
        'transcription_results': transcription_results,
        'filter_report': filter_report,
        'filtered_samples': filtered_samples,
        'dataset': df,
        'statistics': stats,
        'saved_paths': saved_paths
    }


def main():
    """
    Command-line interface for the pipeline.
    """
    parser = argparse.ArgumentParser(
        description='Audio Dataset Pipeline - Convert raw audio to structured STT dataset',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_pipeline.py
  python run_pipeline.py --version 2 --model-size small
  python run_pipeline.py --min-duration 3 --min-confidence 0.5
  python run_pipeline.py --language en
  python run_pipeline.py --input-file test2.mp3
  python run_pipeline.py --input-file "C:\\path\\to\\audio\\test2.mp3"
        """
    )
    
    parser.add_argument(
        '--input-file',
        type=str,
        default=None,
        help='Process only this specific audio file (provide full path or filename in raw_audio/)'
    )
    
    parser.add_argument(
        '--raw-audio-dir',
        default='raw_audio',
        help='Directory containing raw audio files (default: raw_audio)'
    )
    
    parser.add_argument(
        '--processed-audio-dir',
        default='processed_audio',
        help='Directory for processed audio (default: processed_audio)'
    )
    
    parser.add_argument(
        '--output-dir',
        default='output',
        help='Directory for final dataset (default: output)'
    )
    
    parser.add_argument(
        '--version',
        type=int,
        default=None,
        help='Dataset version number (auto-increments if not specified)'
    )
    
    parser.add_argument(
        '--model-size',
        choices=['tiny', 'base', 'small', 'medium', 'large'],
        default='base',
        help='Whisper model size (default: base)'
    )
    
    parser.add_argument(
        '--min-duration',
        type=float,
        default=2.0,
        help='Minimum audio duration in seconds (default: 2.0)'
    )
    
    parser.add_argument(
        '--max-duration',
        type=float,
        default=300.0,
        help='Maximum audio duration in seconds (default: 300.0)'
    )
    
    parser.add_argument(
        '--min-confidence',
        type=float,
        default=0.3,
        help='Minimum transcription confidence (default: 0.3)'
    )
    
    parser.add_argument(
        '--min-words',
        type=int,
        default=3,
        help='Minimum word count (default: 3)'
    )
    
    parser.add_argument(
        '--language',
        default=None,
        help='Target language code (e.g., en, es, fr). Auto-detect if not specified.'
    )
    
    args = parser.parse_args()
    
    # Run pipeline
    result = run_pipeline(
        raw_audio_dir=args.raw_audio_dir,
        processed_audio_dir=args.processed_audio_dir,
        output_dir=args.output_dir,
        version=args.version,
        model_size=args.model_size,
        min_duration=args.min_duration,
        max_duration=args.max_duration,
        min_confidence=args.min_confidence,
        min_words=args.min_words,
        language=args.language,
        input_file=args.input_file
    )
    
    if result is None:
        sys.exit(1)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
