from argparse import ArgumentParser
from MidiGenerator import MidiGenerator
from NotesGenerator import NotesGenerator

argparser = ArgumentParser(description='Generate track')
argparser.add_argument('path', type=str, metavar='OUTPUT_FILE', help='Set output file path')
argparser.add_argument('--type', type=str, help='Set genre: jazz, movie, hiphop, rock', default='jazz')
argparser.add_argument('--inst', type=str, help='Set instrument: guitar,piano,bird,violin,trumpet', default='piano')
argparser.add_argument('--bpm', type=int, help='Set beats per minute', default=240)
argparser.add_argument('--length', type=float, help='Set track length (min)', default=0.5)
argparser.add_argument('--rand', type=bool, help='Add random notes to track: True, False', default=True)

def main():
    args = argparser.parse_args()
    print(args)

    ngen = NotesGenerator(args.type, 12)
    ngen.generate_notes()

    mgen = MidiGenerator(args.length, args.bpm, args.inst, ngen.prob_matrix, args.rand, args.path)
    mgen.generate_midi()


main()