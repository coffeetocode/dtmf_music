# Project Brief

This project is a DTMF (Dual-Tone Multi-Frequency) tone generator that creates audio files containing the tones for phone numbers. The generator creates WAV files with the standard DTMF frequencies used in telephone systems.

## Core Requirements
- Generate DTMF tones for phone numbers
- Output WAV files with the generated tones
- Support standard telephone keypad frequencies
- Include brief silence between tones for clarity
- Cache generated tones by reusing existing WAV files
- Configurable tone duration
- Command-line interface for easy usage

## Features
- Generates WAV files named `dtmf_<number>.wav`
- Checks for existing files before regenerating tones
- Configurable tone duration via command line argument
- Force regeneration option available
- Filters non-digit characters from input
