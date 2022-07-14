# PriMock57

This repository contains the data and annotations described in the papers:
* [**PriMock57: A Dataset Of Primary Care Mock Consultations**](https://arxiv.org/abs/2204.00333)
* [**Human Evaluation and Correlation with Automatic Metrics in Consultation Note Generation**](https://arxiv.org/abs/2204.00447)

The dataset consists of 57 mock medical primary care consultations held over 
5 days by 7 Babylon clinicians and 57 Babylon employees acting 
as patients, using case cards  with presenting complaints, symptoms, medical 
& general history etc. The data in this repository includes:
1) Audio recordings of the consultations (`audio` folder);
2) Manual utterance-level transcriptions of the recordings (`transcripts` folder);
3) Consultation notes written by the consulting clinicians (`notes` folder);
4) Human evaluation annotations & data (`human_eval_data` folder).

The `scripts` folder includes some data transformation scripts
(utterance extraction, transcript collation etc.)

More detailed descriptions are found in each folder's `README.md` files.

### How to clone
Due to their size, the audio files are stored using Git Large File Storage
(https://git-lfs.github.com/). To clone the repository:
1. Install Git LFS using the link above. For Mac, you can use Homebrew:
`brew install git-lfs`
2. Set up Git LFS for your user account: `git lfs install`
3. You can now clone this repository: `git clone https://github.com/babylonhealth/primock57.git`

### Contacts
* Alex Papadopoulos Korfiatis (alex.papadopoulos@babylonhealth.com)
* Francesco Moramarco (francesco.moramarco@babylonhealth.com)

### Citing
```
@inproceedings{korfiatis2022primock57,
  title={(in press): PriMock57: A Dataset Of Primary Care Mock Consultations},
  author={Papadopoulos Korfiatis, Alex and Moramarco, Francesco and Sarac, Radmila and Savkov, Aleksandar},
  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics},
  year={2022}
}
```

```
@inproceedings{moramarco2022human,
  title={(In press): Human Evaluation and Correlation with Automatic Metrics in Consultation Note Generation},
  author={Moramarco, Francesco and Papadopoulos Korfiatis, Alex and Perera, Mark and Juric, Damir and Flann, Jack and Reiter, Ehud and Belz, Anya and Savkov, Aleksandar},
  booktitle={Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics},
  year={2022}
}
```
