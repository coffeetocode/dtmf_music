# Technical Context

## Development Setup
- Python virtual environment (venv) is required for this project
- Virtual environment is located in `venv/` directory
- Activate virtual environment before running or developing:
  ```bash
  source venv/bin/activate
  ```

## Dependencies
The project requires the following Python packages:
- numpy: For numerical computations and array operations
- scipy: For audio file handling (specifically scipy.io.wavfile)

### Installation
After activating the virtual environment:
```bash
pip install numpy scipy
```

## Technical Constraints
- Sample rate: 8000 Hz (standard for DTMF tones)
- Audio output: 16-bit WAV file
- Default tone duration: 0.2 seconds per digit (configurable)
- Silence duration: 0.05 seconds between tones
- Output format: WAV files named dtmf_<number>.wav

## Usage
After activating the virtual environment, run the script with:
```bash
python gen_dtmf.py <phone_number> [options]
```

### Command Line Arguments
- `phone_number`: Required. The phone number to generate tones for (non-digit characters are filtered out)
- `--duration`: Optional. Duration of each tone in seconds (default: 0.2)
- `--force`: Optional. Force regeneration even if file exists

### Examples
```bash
# Generate tones for a phone number
python gen_dtmf.py 555-123-4567

# Generate tones with custom duration
python gen_dtmf.py 5551234567 --duration 0.3

# Force regeneration of existing file
python gen_dtmf.py 5551234567 --force
```
