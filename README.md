# PriMock57

This repository contains the data and annotations described in the papers:
* **PriMock57: A Dataset Of Primary Care Mock Consultations**
* **Human Evaluation and Correlation with Automatic Metrics in Consultation Note Generation**

Dataset of 57 mock medical primary care consultations, containing:
1) Audio recordings of the consultations;
2) Manual utterance-level transcriptions of the recordings;
3) Consultation notes written by the consulting clinicians.

The consultations were held over 5 days by 7 Babylon Health clinicians 
and 57 Babylon Health employees acting as patients, using case cards 
with presenting complaints, symptoms, medical & general history etc.

This repository contains 4 folders: 
`audio`, `notes`, `transcrips` and `scripts`.

### audio
This folder contains the audio recordings of the consultations.
- The recordings are saved in separate channels for doctors & patients
- Total audio duration is 8h:38m (17h:16m if counting the separate channels)
- Audio is saved in wav 16bit/16khz format; the original source is 
video streams with Opus audio encoding.


### notes
This folder contains consultation notes written by the consulting clinicians,
either during or shortly after each consultation.
- Clinicians were asked to highlight important medical information in their 
notes; this was not extensive, depending on whether time allowed.
- The notes are provided in JSON format, and each contains the following fields:
  - `day`: Consultation day
  - `consultation`: Consultation #
  - `presenting_complaint`: Patient's presenting complaint
  - `note`: Consultation note
  - `highlights`: List of clinician highlighted terms in the note

### transcripts
This folder contains the manual transcrips of each audio recording.
- The transcription is done on an utterance level; the transcriber first
identified utterances in the audio, then provided timings for the utterance
along with a transcription.
- The transcription is provided in TextGrid format
(https://www.fon.hum.uva.nl/praat/manual/TextGrid.html).
- Each utterance is an Interval:
  - `xmin`: start time
  - `xmax`: end time
  - `text`: transcription
- The transcripts contain the following tags:
  - `<UNSURE>`: Transcriber was unsure of the transcription provided
  - `<UNIN/>`: An unintelligible audio section
  
### scripts
This folder contains a number of data transformation scripts.
All scripts should be ran from the base directory; for the Python scripts,
please also install dependencies in `requirements.txt`.
- `mix_audio.sh`: Script to mix patient and doctor recordings in single 
audio file. Please install Sox dependency (http://sox.sourceforge.net/)
- `textgrid_to_transcript`: Script to merge utterances into readable 
transcripts. Usage: ```python textgrid_to_transcript.py 
--transcript_path=transcripts --output_path=output/joined_transcripts```
- `extract_utterances.py`: Script to extract audio utterances & prepare 
reference file for sclite. Usage: ```python extract_utterances.py 
--audio_path=audio --transcript_path=transcripts --output_path=output```

# Citing
[...]
