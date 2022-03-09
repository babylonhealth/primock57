# scripts
This folder contains a number of data transformation scripts.
For the Python scripts, please install the dependencies in `requirements.txt`.
- `mix_audio.sh`: Script to mix patient and doctor recordings in single 
audio file. Please install Sox dependency (http://sox.sourceforge.net/,
`brew install sox` on a Mac).
- `textgrid_to_transcript`: Script to merge utterances into readable 
transcripts. Usage: ```python textgrid_to_transcript.py
--transcript_path=../transcripts --output_path=../output/joined_transcripts```
- `extract_utterances.py`: Script to extract audio utterances & prepare 
reference file for calculating Word Error Rate with sclite 
(https://github.com/usnistgov/SCTK).
Usage: ```python extract_utterances.py
--audio_path=../audio --transcript_path=../transcripts --output_path=../output```

