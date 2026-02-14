from pydub import AudioSegment

# Load the m4a file
audio = AudioSegment.from_file("Intro.m4a", format="m4a")

# Export as wav
audio.export("Intro.wav", format="wav")