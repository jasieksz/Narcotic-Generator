from mido import MidiFile

class NotesGenerator:

    def __init__(self,t,s):
        self.type = t
        self.freq_matrix = [[0 for x in range(s)] for y in range(s)]
        self.prob_matrix = [[0 for x in range(s)] for y in range(s)]


    jazzList = ['tracks/jazz/back_to_black.mid','tracks/jazz/chamelon.mid',
                'tracks/jazz/hit_the_road.mid','tracks/jazz/take_five.mid']

    movieList = ['tracks/movie/jurassic_park.mid','tracks/movie/matrix.mid','tracks/movie/star_wars.mid',
                 'tracks/movie/pirates.mid', 'tracks/movie/skyfall.mid']

    hiphopList = ['tracks/hiphop/praise_you.mid','tracks/hiphop/slim_shady.mid','still.mid']

    rockList = ['tracks/rock/because.mid','tracks/rock/karma_police.mid','tracks/rock/tnt.mid']

    typeToFileMap = {'jazz': jazzList, 'movie': movieList, 'hiphop': hiphopList, 'rock': rockList}


    def update_matrix(self,midi):
        s = len(self.freq_matrix[0])
        notes = [msg.note
                 for t in midi.tracks
                 for msg in t
                 if (msg.type == 'note_on')]

        for i in range(0, len(notes) - 1):
            self.freq_matrix[notes[i] % s][notes[i + 1] % s] += 1

    def calculate_prob(self):
        s = len(self.freq_matrix[0])
        for i in range(0, s):
            suma = sum(self.freq_matrix[i])
            for j in range(0, s):
                if suma == 0:
                    self.prob_matrix[i][j] = 1 / s
                else:
                    self.prob_matrix[i][j] = self.freq_matrix[i][j] / suma

    def generate_notes(self):
        for i in self.typeToFileMap[self.type]:
            self.update_matrix(MidiFile(i))
        self.calculate_prob()
