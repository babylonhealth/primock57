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


def get_utterances_audacity(aud_path):
    with open(aud_path, 'r') as _f:
        lines = _f.readlines()
    utterances = []
    for line in lines:
        components = line.split('\t')
        text = components[2].strip()
        utterances.append({'text': text,
                           'from': float(components[0]),
                           'to': float(components[1])})
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


def strip_transcript_tags(text):
    tags = ["<UNSURE>", "</UNSURE>", "<UNIN/>", "<INAUDIBLE_SPEECH/>"]
    for t in tags:
        text = text.replace(t, "")
    text = re.sub(r'\s+', ' ', text)
    text = text.lstrip().rstrip()
    return text


def preprocess_text(text):
    text = strip_transcript_tags(text)
    text = text.lower()
    text = text.replace('-', ' ')
    text = re.sub(r'[^a-z \']+', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lstrip().rstrip()
    return text
