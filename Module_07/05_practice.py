import zipfile
from pprint import pprint
from random import randint


class Chatterer:
    analize_count = 4
    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        sequence = ' ' * self.analize_count
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                line = line[:-1]
                for char in line:
                    if sequence in self.stat:
                        if char in self.stat[sequence]:
                            self.stat[sequence][char] += 1
                        else:
                            self.stat[sequence][char] = 1
                    else:
                        self.stat[sequence] = {char: 1}
                    sequence = sequence[1:] + char

    def prepare(self):
        self.totals = {}
        self.stat_for_generate = {}
        for sequence, char_stat in self.stat.items():
            self.totals[sequence] = 0
            self.stat_for_generate[sequence] = []
            for char, count in char_stat.items():
                self.totals[sequence] += count
                self.stat_for_generate[sequence].append([count, char])
            self.stat_for_generate[sequence].sort(reverse=True)

    def chat(self, out_file_name=None, N=1000):
        N = N
        printed = 0
        if out_file_name is not None:
            file = open(out_file_name, 'w', encoding='utf8')
        else:
            file = None

        sequence = ' ' * self.analize_count
        spaces_printed = 0
        while printed < N:
            char_stat = self.stat_for_generate[sequence]
            total = self.totals[sequence]
            dice = randint(1, total)
            pos = 0
            for count, char in char_stat:
                pos += count
                if dice <= pos:
                    break
            if file:
                file.write(char)
            else:
                print(char, end='')
            if char == ' ':
                spaces_printed += 1
                if spaces_printed >= 10:
                    if file:
                        file.write('\n')
                    else:
                        print()
                    spaces_printed = 0
            printed += 1
            sequence = sequence[1:] + char
        if file:
            file.close()


chattere = Chatterer(file_name='voyna_i_mir.txt')
chattere.collect()
chattere.prepare()
chattere.chat(out_file_name='out.txt')
