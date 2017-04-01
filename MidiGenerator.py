import os

from midiutil.MidiFile import MIDIFile
import numpy.random

class MidiGenerator:

    def __init__(self, leng, beats, inst, probabilty,ran,path):
        self.length = leng
        self.bpm = beats
        self.instrument = inst
        self.prob_matrix = probabilty
        self.rand = ran
        self.path = path


    def generate_midi(self):
        MyMIDI = MIDIFile(1)
        s = len(self.prob_matrix)

        track = 0
        time = 0
        volume = 110
        channel = 0
        program = self.get_instrument(self.instrument)
        pitch = numpy.random.randint(0, s, 1)[0]

        MyMIDI.addTempo(track, time, self.bpm)
        MyMIDI.addProgramChange(track, channel, time, program)

        for i in range (0,int(self.length*self.bpm)):
            pitch = (numpy.random.choice(s, 1, False, self.prob_matrix[pitch % s])[0])
            if self.rand:
                pitch += (12 * numpy.random.randint(0, 2, 1)[0]) + numpy.random.randint(2*s, 5*s, 1)[0]
                pitch = pitch % 128

            duration = numpy.random.randint(50, 400, 1)[0] / 200
            MyMIDI.addNote(track, channel, pitch, time, duration, volume)
            time += duration

        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "wb") as f:
            MyMIDI.writeFile(f)
            f.close()


    def get_instrument(self, instrument):
        if instrument == 'guitar':
            return 25
        elif instrument == 'piano':
            return 1
        elif instrument == 'bird':
            return 123
        elif instrument == 'violin':
            return 40
        elif instrument == 'trumpet':
            return 56
