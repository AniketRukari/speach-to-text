"""
Quality Filtering Module
Implements two filtering mechanisms:
1. Duration-based filtering (remove too short/long audio)
2. Transcription quality filtering (remove low confidence, empty, or nonsensical text)
"""
import re


def filter_by_duration(sample, min_duration=2.0, max_duration=300.0):
    duration = sample.get('final_duration', 0)
    
    if duration < min_duration:
        return False, f"Too short: {duration:.2f}s < {min_duration}s"
    
    if duration > max_duration:
        return False, f"Too long: {duration:.2f}s > {max_duration}s"
    
    return True, "Duration OK"


def filter_by_transcription_quality(sample, min_confidence=0.3, min_words=3):

    text = sample.get('text', '').strip()
    confidence = sample.get('confidence', 0.0)
    word_count = sample.get('word_count', 0)
    
    # Check if transcription was successful
    if not sample.get('success', False):
        return False, f"Transcription failed: {sample.get('error', 'Unknown error')}"
    
    # Check for empty transcription
    if not text:
        return False, "Empty transcription"
    
    # Check confidence
    if confidence < min_confidence:
        return False, f"Low confidence: {confidence:.2f} < {min_confidence}"
    
    # Check word count
    if word_count < min_words:
        return False, f"Too few words: {word_count} < {min_words}"
    
    # Check for meaningful content (at least some alphabetic characters)
    if not re.search(r'[a-zA-Z]', text):
        return False, "No alphabetic characters found"
    
    # Check for excessive repetition (same word repeated many times)
    words = text.lower().split()
    if len(words) > 0:
        unique_ratio = len(set(words)) / len(words)
        if unique_ratio < 0.3 and len(words) > 5:
            return False, f"Excessive repetition detected (unique ratio: {unique_ratio:.2f})"
    
    return True, "Quality OK"


def apply_filters(samples, preprocess_results, transcription_results,
                 min_duration=2.0, max_duration=300.0,
                 min_confidence=0.3, min_words=3):
    """
    Apply all quality filters to samples.
    
    Args:
        samples: List of sample identifiers or filenames
        preprocess_results: List of preprocessing results
        transcription_results: List of transcription results
        Filter parameters for duration and quality
    
    Returns:
        filtered_samples: List of samples that passed all filters
        filter_report: Dictionary with filtering statistics
    """
    filtered_samples = []
    filter_report = {
        'total': len(samples),
        'passed': 0,
        'failed_duration': 0,
        'failed_quality': 0,
        'failed_both': 0,
        'reasons': []
    }

    # Create lookup dictionaries (case-insensitive)
    preprocess_dict = {r['output_file'].lower(): r for r in preprocess_results if r.get('success')}
    transcribe_dict = {r['filename'].lower(): r for r in transcription_results}
    
    for sample in samples:
        # Get preprocessing and transcription data (case-insensitive lookup)
        sample_lower = sample.lower()
        preproc = preprocess_dict.get(sample_lower, {})
        transcr = transcribe_dict.get(sample_lower, {})
        
        # Skip if no transcription data found (file wasn't processed)
        if not transcr:
            continue
        
        # Apply filters
        duration_pass, duration_reason = filter_by_duration(preproc, min_duration, max_duration)
        quality_pass, quality_reason = filter_by_transcription_quality(
            transcr, min_confidence, min_words
        )
        
        # Combine results
        if duration_pass and quality_pass:
            filtered_samples.append({
                'filename': sample,
                'preprocessing': preproc,
                'transcription': transcr,
                'status': 'passed'
            })
            filter_report['passed'] += 1
        else:
            reasons = []
            if not duration_pass:
                reasons.append(duration_reason)
                filter_report['failed_duration'] += 1
            if not quality_pass:
                reasons.append(quality_reason)
                filter_report['failed_quality'] += 1
            
            if not duration_pass and not quality_pass:
                filter_report['failed_both'] += 1
            
            filter_report['reasons'].append({
                'filename': sample,
                'reasons': reasons
            })
    
    return filtered_samples, filter_report


def print_filter_report(filter_report):
    """
    Print a summary of the filtering results.
    """
    print("\n" + "="*60)
    print("QUALITY FILTERING REPORT")
    print("="*60)
    print(f"Total samples: {filter_report['total']}")
    print(f"Passed all filters: {filter_report['passed']}")
    print(f"Failed duration filter: {filter_report['failed_duration']}")
    print(f"Failed quality filter: {filter_report['failed_quality']}")
    print(f"Failed both filters: {filter_report['failed_both']}")
    
    if filter_report['reasons']:
        print("\nFailed samples:")
        for item in filter_report['reasons']:
            print(f"  {item['filename']}:")
            for reason in item['reasons']:
                print(f"    - {reason}")
    
    print("="*60)


if __name__ == "__main__":
    # Test the filtering
    print("Quality filtering module loaded successfully")
    print("This module provides duration and transcription quality filters")
