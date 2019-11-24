class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the musician {self.name}'

    # organize_event = Musician.play
    def play(self):
        return 'plays music'


class Dancer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the dancer {self.name}'

    # organize_event = Dancer.dance
    def dance(self):
        return 'does a dance performance'
