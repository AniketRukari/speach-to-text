"""
Dataset Structuring Module
Creates structured dataset with metadata in CSV/JSONL format.
"""
import os
import json
import pandas as pd
from pathlib import Path
from datetime import datetime


def create_dataset_metadata(filtered_samples, output_dir, version):
    """
    Create structured dataset with metadata.
    
    Args:
        filtered_samples: List of samples that passed quality filters
        output_dir: Directory to save dataset
        version: Version number/string for the dataset
    
    Returns:
        Dataset metadata dictionary
    """
    dataset_records = []
    
    for sample in filtered_samples:
        filename = sample['filename']
        preproc = sample['preprocessing']
        transcr = sample['transcription']
        
        record = {
            'sample_id': Path(filename).stem,
            'filename': filename,
            'audio_path': preproc.get('output_path', ''),
            'transcription': transcr.get('text', ''),
            'duration_seconds': preproc.get('final_duration', 0),
            'sample_rate': preproc.get('sample_rate', 16000),
            'language': transcr.get('language', 'unknown'),
            'confidence': transcr.get('confidence', 0.0),
            'word_count': transcr.get('word_count', 0),
            'segments': transcr.get('segments', 0),
            'original_duration': preproc.get('original_duration', 0),
            'trimmed_duration': preproc.get('original_duration', 0) - preproc.get('final_duration', 0),
        }
        
        dataset_records.append(record)
    
    # Create DataFrame
    df = pd.DataFrame(dataset_records)
    
    # Sort by sample_id
    df = df.sort_values('sample_id').reset_index(drop=True)
    
    # Calculate dataset statistics
    stats = {
        'version': version,
        'created_at': datetime.now().isoformat(),
        'total_samples': int(len(df)),
        'total_duration_seconds': float(df['duration_seconds'].sum()),
        'total_words': int(df['word_count'].sum()),
        'avg_duration': float(df['duration_seconds'].mean()),
        'avg_confidence': float(df['confidence'].mean()),
        'languages': {str(k): int(v) for k, v in df['language'].value_counts().to_dict().items()},
        'min_duration': float(df['duration_seconds'].min()),
        'max_duration': float(df['duration_seconds'].max()),
    }
    
    return df, stats


def save_dataset(df, stats, output_dir, version):
    """
    Save dataset in multiple formats with versioning.
    
    Args:
        df: Dataset DataFrame
        stats: Dataset statistics dictionary
        output_dir: Output directory
        version: Version identifier
    
    Returns:
        Dictionary with paths to saved files
    """
    # Create versioned output directory
    version_dir = Path(output_dir) / f"dataset_v{version}"
    version_dir.mkdir(parents=True, exist_ok=True)
    
    # Save CSV
    csv_path = version_dir / "dataset.csv"
    df.to_csv(csv_path, index=False)
    
    # Save JSONL (one JSON object per line)
    jsonl_path = version_dir / "dataset.jsonl"
    with open(jsonl_path, 'w', encoding='utf-8') as f:
        for _, row in df.iterrows():
            json.dump(row.to_dict(), f, ensure_ascii=False)
            f.write('\n')
    
    # Save statistics
    stats_path = version_dir / "statistics.json"
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    # Save human-readable summary
    summary_path = version_dir / "README.txt"
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(f"Dataset Version {version}\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Created: {stats['created_at']}\n\n")
        f.write("Statistics:\n")
        f.write(f"  Total samples: {stats['total_samples']}\n")
        f.write(f"  Total duration: {stats['total_duration_seconds']:.2f} seconds ({stats['total_duration_seconds']/60:.2f} minutes)\n")
        f.write(f"  Total words: {stats['total_words']}\n")
        f.write(f"  Average duration: {stats['avg_duration']:.2f} seconds\n")
        f.write(f"  Average confidence: {stats['avg_confidence']:.2f}\n")
        f.write(f"  Duration range: {stats['min_duration']:.2f}s - {stats['max_duration']:.2f}s\n")
        f.write(f"\nLanguages:\n")
        for lang, count in stats['languages'].items():
            f.write(f"  {lang}: {count} samples\n")
        f.write("\n" + "=" * 60 + "\n")
        f.write("\nSample preview:\n")
        for idx, row in df.head(5).iterrows():
            f.write(f"\n[{row['sample_id']}]\n")
            f.write(f"  Duration: {row['duration_seconds']:.2f}s\n")
            f.write(f"  Confidence: {row['confidence']:.2f}\n")
            f.write(f"  Transcription: {row['transcription'][:100]}...\n")
    
    print(f"\nDataset saved to: {version_dir}")
    print(f"  - CSV: {csv_path.name}")
    print(f"  - JSONL: {jsonl_path.name}")
    print(f"  - Statistics: {stats_path.name}")
    print(f"  - Summary: {summary_path.name}")
    
    return {
        'version_dir': str(version_dir),
        'csv_path': str(csv_path),
        'jsonl_path': str(jsonl_path),
        'stats_path': str(stats_path),
        'summary_path': str(summary_path)
    }


def print_dataset_summary(df, stats):
    """
    Print a summary of the dataset.
    """
    print("\n" + "="*60)
    print("DATASET SUMMARY")
    print("="*60)
    print(f"Version: {stats['version']}")
    print(f"Created: {stats['created_at']}")
    print(f"\nStatistics:")
    print(f"  Total samples: {stats['total_samples']}")
    print(f"  Total duration: {stats['total_duration_seconds']:.2f}s ({stats['total_duration_seconds']/60:.2f} min)")
    print(f"  Total words: {stats['total_words']}")
    print(f"  Average duration: {stats['avg_duration']:.2f}s")
    print(f"  Average confidence: {stats['avg_confidence']:.2f}")
    print(f"  Duration range: {stats['min_duration']:.2f}s - {stats['max_duration']:.2f}s")
    print(f"\nLanguages:")
    for lang, count in stats['languages'].items():
        print(f"  {lang}: {count} samples")
    print("="*60)


if __name__ == "__main__":
    print("Dataset structuring module loaded successfully")
