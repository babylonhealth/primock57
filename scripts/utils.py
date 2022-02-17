import re
import textgrid
import wave


def get_utterances_textgrid(tg_path):
    tg = textgrid.TextGrid()
    tg.read(tg_path)
    utterances = []
    for tier in tg.tiers:
        for interval in tier.intervals:
            if len(interval.mark) > 0:
                utterances.append({'text': interval.mark,
                                   'from': interval.minTime,
                                   'to': interval.maxTime})
    return utterances


def get_partial_audio(audio_file_path, from_sec, to_sec):
    with wave.open(audio_file_path, 'rb') as f:
        framerate = f.getframerate()
        assert framerate == 16000, 'Wave file framerate needs to be 16000!'
        n_frames = f.getnframes()
        frames = f.readframes(n_frames)
    from_bytes = 2 * int(from_sec * framerate)
    # We need to make sure to only get full frames (2 bytes)
    to_bytes = 2 * int(to_sec * framerate)
    return frames[from_bytes:to_bytes]


def write_wave(file_path, audio_frames):
    with wave.open(file_path, 'wb') as f:
        f.setparams((1, 2, 16000, 0, 'NONE', 'no compression'))
        f.writeframes(audio_frames)


def preprocess_reference(ref_str: str) -> str:
    # Remove punctuation
    ref_str = ref_str.replace('’', '\'')
    ref_str = re.sub(r'<.*>', ' ', ref_str)
    ref_str = re.sub(r'[^a-zA-Z\s\']', ' ', ref_str)
    ref_str = re.sub(r'\s+', ' ', ref_str)
    return ref_str.strip().lower()