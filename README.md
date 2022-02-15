#PriMock57
Dataset of 57 mock medical primary care consultations: audio, consultation notes, human utterance-level transcripts.

Held over 5 days by 7 Babylon Health clinicians and 57 Babylon Health employees acting as patients.

Patients were using X case cards with presenting complaints, symptoms, medical & general history etc.


###audio
- separate channels for clinicians & patients
- Xh:Ym of total audio
- saved in wav 16bit/16khz format
- source: opus/webm streams


###notes
- Written by the consulting clinician during / after each consultation.
- Clinicians highlighted important medical information; this was not extensive depending on whether time allowed.
- JSON format. Fields:
  - `day`: Consultation day
  - `consultation`: Consultation #
  - `presenting_complaint`: Patient's presenting complaint
  - `note`: Consultation note
  - `highlights`: List of clinician highlighted terms in the note

###transcripts
- Utterance-split transcription
- In TextGrid format (https://www.fon.hum.uva.nl/praat/manual/TextGrid.html). Each utterance is an Interval:
  - `xmin`: start time
  - `xmax`: end time
  - `text`: transcription
- transcriber tags
  - `<UNSURE>`: Not certain of transcription
  - `<UNIN/>`: Unintelligible audio
  
###scripts
- script to merge audio in 2-channel?
- script to merge utterance transcripts into txt
- script to extract audio utterances
- script to make kaldi stuff for WER eval