class Heart:
    def __init__(self, bpm=72):
        self.bpm = bpm

    def beat(self):
        print("Lub-Dub")
        self.bpm+=1

    def __str__(self):
        return f"Current BPM: {self.bpm}"       
     