import os
from glob import glob
from tqdm import tqdm

from utils import get_utterances_textgrid,\
    get_partial_audio, write_wave, preprocess_text


def __parse_args():
    import argparse
    parser = argparse.ArgumentParser(
        description='Prepare audio files and transcripts for WER testing')
    parser.add_argument('--audio_path', help='Folder containing audio files')
    parser.add_argument('--transcript_path',
                        help='Folder containing TextGrid transcripts')
    parser.add_argument('--output_path', help='Output folder')
    return parser.parse_args()


def main():
    args = __parse_args()
    # Find all recordings in the audio folder and make sure they match the
    # transcripts
    audio_files = glob(f'{args.audio_path}/*.wav')
    transcript_files = glob(f'{args.transcript_path}/*.TextGrid')
    all_utterances = {}
    for af in audio_files:
        c_id = os.path.splitext(os.path.basename(af))[0]
        single_transcript_path = f'{args.transcript_path}/{c_id}.TextGrid'
        assert single_transcript_path in transcript_files
        utterances = get_utterances_textgrid(single_transcript_path)

        for idx, u in enumerate(utterances):
            utt_id = f"{c_id}_u{idx}"
            all_utterances[utt_id] = {
                'text': u['text'],
                'audio_file': af,
                'from_sec': u['from'],
                'to_sec': u['to'],
            }

    print('Writing individual utterance audio files...')
    utterance_audio_folder = os.path.join(args.output_path, 'audio_utterances')
    os.makedirs(utterance_audio_folder, exist_ok=True)
    for utt_id, utt in tqdm(all_utterances.items()):
        utt_audio = get_partial_audio(utt['audio_file'],
                                      utt['from_sec'],
                                      utt['to_sec'])
        write_wave(os.path.join(utterance_audio_folder, f'{utt_id}.wav'),
                   utt_audio)

    print('Writing reference transcript file...')
    reference_transcript_path = os.path.join(args.output_path,
                                             'transcript.ref.txt')
    with open(reference_transcript_path, 'w') as f:
        for utt_id, utt in all_utterances.items():
            cleaned_text = preprocess_text(utt['text'])
            if len(cleaned_text) > 0:
                f.write(f"{cleaned_text} ({utt_id})\n")
    print('Done!')


if __name__ == '__main__':
    main()
