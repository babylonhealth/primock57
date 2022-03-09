import os
from glob import glob
from utils import get_utterances_textgrid, strip_transcript_tags


def get_combined_transcript(transcript_path_doctor, transcript_path_patient):
    utterances_doctor = get_utterances_textgrid(transcript_path_doctor)
    utterances_patient = get_utterances_textgrid(transcript_path_patient)
    for u in utterances_doctor:
        u['speaker'] = 'Doctor'
    for u in utterances_patient:
        u['speaker'] = 'Patient'
    combined_utterances = utterances_doctor + utterances_patient
    combined_utterances.sort(key=lambda x: x['from'])
    return [f"{u['speaker']}: {strip_transcript_tags(u['text'])}"
            for u in combined_utterances]


def __parse_args():
    import argparse
    parser = argparse.ArgumentParser(
        description='Compile joined transcripts from TextGrid files')
    parser.add_argument('--transcript_path',
                        help='Folder containing TextGrid transcripts')
    parser.add_argument('--output_path', help='Output folder')
    return parser.parse_args()


def main():
    args = __parse_args()
    os.makedirs(args.output_path, exist_ok=True)
    transcript_paths_doctor = glob(f'{args.transcript_path}/*doctor.TextGrid')
    for path_doctor in transcript_paths_doctor:
        print(path_doctor)
        path_patient = path_doctor.replace('doctor', 'patient')
        output_path_transcript = os.path.join(args.output_path,
                                              os.path.basename(path_doctor)
                                              .replace('_doctor.TextGrid',
                                                       '.txt'))
        transcript_sentences = get_combined_transcript(path_doctor,
                                                       path_patient)
        with open(output_path_transcript, 'w') as f:
            f.write('\n'.join(transcript_sentences))


if __name__ == '__main__':
    main()
