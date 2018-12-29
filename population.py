from sample import Sample


class Population:
    def __init__(self, skeleton, M, spellcheck):
        self.skeleton = skeleton
        self.m = M
        self.samples = []
        self.spellcheck = spellcheck

    def generate_population(self):
        for i in range(0, self.m):
            sample = Sample(self.skeleton, self.spellcheck)
#            sample.generate_population()
            self.samples.append(sample)

    def offspring(self):
        pass

    def trim(self):
        pass