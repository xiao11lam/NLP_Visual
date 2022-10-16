from pydub import AudioSegment
import os
from pydub.silence import split_on_silence

if not os.path.isdir("splitaudio"):
    os.mkdir("splitaudio")

audio = AudioSegment.from_file("Wk4 vowels_BOR.wav")
lengthaudio = len(audio)
print("Length of Audio File", lengthaudio)

start = 0
# In Milliseconds, this will cut 10 Sec of audio
threshold = 1000
end = 0
counter = 0



chunks = split_on_silence (
    # Use the loaded audio.
    audio, 
    # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
    min_silence_len = 80,
    # Consider a chunk silent if it's quieter than -16 dBFS.
    # (You may want to adjust this parameter.)
    silence_thresh = -18
)



# Process each chunk with your parameters
for i, chunk in enumerate(chunks):
    # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
    silence_chunk = AudioSegment.silent(duration=500)

    # Add the padding chunk to beginning and end of the entire chunk.
    audio_chunk = silence_chunk + chunk + silence_chunk

    # Normalize the entire chunk.
    # normalized_chunk = match_target_amplitude(audio_chunk, -20.0)


    filename = f'splitaudio/chunk{counter}.wav'

    audio_chunk.export(filename, format="wav")
    counter +=1

