# transcripts
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