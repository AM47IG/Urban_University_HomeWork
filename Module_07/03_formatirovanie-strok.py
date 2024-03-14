from random import randint


class Team:
    quantity_of_team = 0
    quantity_of_all_members = 0
    cnt_welcome_to_the_team = 0
    cnt_end_game = 0
    solved_tasks_total = 0
    time_total = 0

    def __init__(self, name, quantity_of_members):
        Team.quantity_of_team += 1
        Team.quantity_of_all_members += quantity_of_members
        self.name = name
        self.quantity_of_members = quantity_of_members
        self.total_score = 0
        self.count_of_solved_tasks = 0
        self.count_of_tasks = -1
        self.time = 0


    def welcome_to_the_team(self):
        print('Приветствуем команду %s' % self.name)
        print('В команде %s %s участников!' % (self.name, self.quantity_of_members), '\n')
        Team.cnt_welcome_to_the_team += 1
        if Team.cnt_welcome_to_the_team == Team.quantity_of_team:
            print('Итого сегодня в командах участников: %s!' % Team.quantity_of_all_members, '\n')

    def solved_the_tasks(self):
        time = randint(700, 4000)
        if time > 3600:
            print('Команда {} не решила задачу!'.format(self.name))
            self.count_of_tasks += 1
            return None
        score = 6 - 3600 // time
        self.total_score += score
        self.time += time
        Team.time_total += time
        self.count_of_solved_tasks += 1
        self.count_of_tasks += 1
        Team.solved_tasks_total += 1
        print('Команда {} решила задачу и получает за это {} очков!'.format(self.name, score))

    def act(self):
        if self.count_of_tasks == -1:
            self.welcome_to_the_team()
            self.count_of_tasks += 1
        elif self.count_of_tasks < 20:
            self.solved_the_tasks()
        else:
            print('\nКоманда {} закончила игру со счётом {}! \nВсе задачи решены за {} сек.'.format(
                self.name, self.total_score, self.time))
            Team.cnt_end_game += 1

    def __le__(self, other):
        if self.count_of_solved_tasks < other.count_of_solved_tasks:
            print(f'Победа команды {other.name}')
        elif other.count_of_solved_tasks < self.count_of_solved_tasks:
            print(f'Победа команды {self.name}')
        else:
            print(f'Команды {self.name} и {other.name} делят победу!')


print(f'{'Игра началась':-^40}')
team1 = Team('"Мастера кода"', randint(3, 6))
team2 = Team('"Волшебники данных"', randint(3, 6))
team1.act()
team2.act()
while Team.cnt_end_game != Team.quantity_of_team:
    team1.act()
    team2.act()
    print()

print(f'{'Игра окончена':-^40}')
print(f'\nКоманды решили {team1.count_of_solved_tasks} и {team2.count_of_solved_tasks} задач.\n')

team1 <= team2

tasks_total = Team.solved_tasks_total
time_avg = Team.time_total / tasks_total
print(f'\nСегодня было решенно {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!')
