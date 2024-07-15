class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            # Исправлена логическая ошибка. У кого больше скорость, тот и первый.
            participant = max(self.participants, key=lambda x: x.speed)
            finishers[place] = participant
            place += 1
            self.participants.remove(participant)

            # Не исправлена ошибка, здесь достаточно быть первым в списке и пройти заданную дистанцию
            # за одинаковое количество циклов с реальным победителем.
            # for participant in self.participants:
            #     participant.run()
            #     if participant.distance >= self.full_distance:
            #         finishers[place] = participant
            #         place += 1
            #         self.participants.remove(participant)

        return finishers
