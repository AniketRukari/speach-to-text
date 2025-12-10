"""
Simple audio converter using pydub (which can use alternative backends)
Converts m4a to wav format
"""
from pydub import AudioSegment
import sys

def convert_m4a_to_wav(input_file, output_file):
    """Convert m4a to wav"""
    try:
        print(f"Loading {input_file}...")
        audio = AudioSegment.from_file(input_file, format="m4a")
        
        print(f"Converting to wav...")
        audio.export(output_file, format="wav")
        
        print(f"Successfully converted to {output_file}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    input_file = "raw_audio/recording.m4a"
    output_file = "raw_audio/recording.wav"
    
    convert_m4a_to_wav(input_file, output_file)
