import json
import wave
import tqdm
import random
from utils import preprocess_text
random.seed(42)


def write_manifest(manifest, output_path):
    with open(output_path, 'w') as f:
        f.write('\n'.join([json.dumps(l) for l in manifest]))


def main():
    with open('../output/transcript.ref.txt') as f:
        lines = f.readlines()
    manifest_all = []
    all_lengths = []
    for l in tqdm.tqdm(lines):
        utt_transcript = preprocess_text(l.split(' (')[0])
        # if len(utt_transcript) >= 0:
        utt_id = l.split(' (')[1].split(')')[0]
        audio_path = f"../output/audio_utterances/{utt_id}.wav"
        with wave.open(audio_path, 'rb') as w:
            audio_length = w.getnframes() / w.getframerate()
        if audio_length > 0.01:
            all_lengths.append(audio_length)
            manifest_all.append({
                "audio_filepath": f"/home/jupyter/audio/utterances/{utt_id}.wav",
                "duration": round(audio_length, 4),
                "text": preprocess_text(utt_transcript)
            })
    random.shuffle(manifest_all)
    train_size = int(len(manifest_all)*0.8)
    val_size = int(len(manifest_all)*0.1)
    manifest_train = manifest_all[:train_size]
    manifest_val = manifest_all[train_size:train_size+val_size]
    manifest_test = manifest_all[train_size+val_size:]
    assert len(manifest_all) == len(manifest_train) + len(manifest_val) + len(manifest_test)
    write_manifest(manifest_all, '../output/manifest_all_e.jsonl')
    write_manifest(manifest_train, '../output/manifest_train_e.jsonl')
    write_manifest(manifest_val, '../output/manifest_val_e.jsonl')
    write_manifest(manifest_test, '../output/manifest_test_e.jsonl')

    print(max(all_lengths))
    print(min(all_lengths))

main()
