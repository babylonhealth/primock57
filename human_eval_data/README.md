# Data for the paper "Human Evaluation and Correlation with Automatic Metricsin Consultation Note Generation"


This folder contains the data produced by the human evaluation and the correlation study on consultation Note Generation. It can be used to reproduce the study as well as to evaluate further automatic metrics.

The files included are:

## results.csv
It contains the raw results from the human evaluation, with the following headers:
- Evaluator: id of the human subject (out of 5)
- Consultation: id of the consultation  (out of 57)
- Model: id of the model (out of 10 models + 1 human written note identified with id "doctor")
- Evaluator Note: the note written by the given evaluator for the given consultation (57 consultations x 5 evaluators = 285 notes)
- Model Note: the note produced by the given model for the given consultation (57 consultations x 5 models per consultation = 285 notes)
- Post-edited note: the Model Note after being post-edited by the given evaluator. Format is text with xml annotations to mark additions (omissions) and deletions (incorrect statements)
- Post-edit time: Time (in seconds) to post-edit a note (i.e. time to produce the Post-edited note from the Model Note)
- Incorrect Statements: List of incorrect statements extracted by the evaluator from the Post-edited note. Statements beginning with ! are critical. Statements beginning with - are non-critcal.
- Omissions: List of omissions extracted by the evaluator from the Post-edited note. Omissions beginning with ! are critical. Omissions beginning with - are non-critcal.
- Other Issues: Qualitative feedback given by the evaluator for the given note


## other-issues-taxonomy-examples.csv
It contains the Other Issues from results.csv grouped according to our taxonomy. Headers are in first column (one per row). 


## metric-scores.json
It contains the scores for all 18 metrics and each reference type (human\_note, edited\_note, eval\_note,) as well as taking the average and the maximum.
