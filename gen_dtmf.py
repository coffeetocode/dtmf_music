import numpy as np
import scipy.io.wavfile as wav
import argparse
import os

# Define DTMF frequencies for each digit
DTMF_FREQUENCIES = {
    '1': (697, 1209), '2': (697, 1336), '3': (697, 1477),
    '4': (770, 1209), '5': (770, 1336), '6': (770, 1477),
    '7': (852, 1209), '8': (852, 1336), '9': (852, 1477),
    '0': (941, 1336)
}

# Generate DTMF tone for a digit
def generate_tone(frequencies, duration=0.2, sample_rate=8000):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequencies[0] * t) + np.sin(2 * np.pi * frequencies[1] * t)
    return (wave * 32767).astype(np.int16)

# Generate DTMF sequence for a phone number
def generate_dtmf_tones(phone_number, tone_duration=0.2, silence_duration=0.05, sample_rate=8000):
    dtmf_sequence = []
    silence = np.zeros(int(sample_rate * silence_duration), dtype=np.int16)

    for digit in phone_number:
        if digit in DTMF_FREQUENCIES:
            dtmf_sequence.append(generate_tone(DTMF_FREQUENCIES[digit], duration=tone_duration, sample_rate=sample_rate))
            dtmf_sequence.append(silence)  # Add short silence between tones

    return np.concatenate(dtmf_sequence)

def get_output_filename(phone_number):
    return f"dtmf_{phone_number}.wav"

def main():
    parser = argparse.ArgumentParser(description='Generate DTMF tones for a phone number')
    parser.add_argument('phone_number', help='Phone number to generate tones for')
    parser.add_argument('--duration', type=float, default=0.2,
                      help='Duration of each tone in seconds (default: 0.2)')
    parser.add_argument('--force', action='store_true',
                      help='Force regeneration even if file exists')
    args = parser.parse_args()

    # Clean the phone number to keep only digits
    phone_number = ''.join(filter(str.isdigit, args.phone_number))
    if not phone_number:
        print("Error: No valid digits in the provided phone number")
        return

    output_file = get_output_filename(phone_number)
    
    # Check if file already exists
    if os.path.exists(output_file) and not args.force:
        print(f"Using existing file: {output_file}")
        return

    # Generate new tones
    sample_rate = 8000
    dtmf_tones = generate_dtmf_tones(phone_number, tone_duration=args.duration, sample_rate=sample_rate)

    # Save to a WAV file
    wav.write(output_file, sample_rate, dtmf_tones)
    print(f"DTMF tones generated and saved as {output_file}")

if __name__ == '__main__':
    main()
