DTMF Tone Generator
=================

A Python script that generates DTMF (Dual-Tone Multi-Frequency) tones for phone numbers and saves them as WAV files. The generator creates standard telephone keypad tones with configurable durations. Support for ♩ and ♪.

Example: [dtmf_555-123-4567.wav](examples/dtmf_555-123-4567.wav)

Why? 
* Mostly for funzies. Also because I want to help some kids memorize some phone numbers, it's easier if it's set to a tune, and it amuses me to have the tune actually be (or at least resemble) the DTMF tones. 
* An exuse to play with Claude Sonnet / CLINE w/ Memory Bank

Requirements
-----------
- Python 3.x
- numpy
- scipy

Setup
-----
1. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   venv\Scripts\activate     # On Windows
   ```

2. Install dependencies:
   ```
   pip install numpy scipy
   ```

Usage
-----
Basic usage:
```
python gen_dtmf.py <phone_number>
```

Options:
- --duration: Set the same duration for all tones (default: 0.2)
  - Use seconds (e.g., 0.3)
  - Use ♩ for quarter note (0.3s)
  - Use ♪ for eighth note (0.15s)
- --durations: Set individual durations for each character
  - Can mix numbers, ♩, and ♪
  - Example: --durations ♩ ♪ ♪ ♩ 0.5 ♩
- --force: Force regeneration of existing files
- --no-play: Generate the file without playing it

Examples
--------
1. Generate tones for a phone number ([.wav file](examples/dtmf_555-123-4567.wav)):
   ```
   python gen_dtmf.py 555-123-4567
   ```

2. Use custom duration for all tones:
   ```
   python gen_dtmf.py 555-123-4567 --duration 0.3
   ```

3. Use different durations with musical notation:
   ```
   python gen_dtmf.py 123-456 --durations ♩ ♪ ♪ ♩ 0.5 ♩
   ```

4. Force regeneration of existing file:
   ```
   python gen_dtmf.py 555-123-4567 --force
   ```

5. Shave and a haircut... two bits ☺ ([.wav file](examples/dtmf_51234_59.wav))
   ```
   python gen_dtmf.py "51234_59" --durations ♩ ♪ ♪ ♩ ♩ 0.5 ♩ ♩
   ```

Output
------
The script generates WAV files named 'dtmf_<number>.wav' in the current directory. Non-digit characters in the phone number are filtered out for the filename.

Features
--------
- Standard DTMF frequencies for telephone keypad tones (0-9, *, #)
- Configurable tone durations (global or per-character)
- Support for spaces, dashes, and underscores as silence
- Brief silence between tones for clarity
- Automatic caching (reuses existing WAV files)
- Built-in audio playback on macOS

Special Characters
----------------
Silence characters:
- Space character " "
- Dash "-"
- Underscore "_"

DTMF characters:
- Digits 0-9
- Star "*"
- Pound "#"

These characters count as positions when using --durations. For example:
```
python gen_dtmf.py "123-456" --durations 0.1 0.2 0.3 0.5 0.1 0.2 0.3
```
In this case, the dash will be a 0.5 second silence.
