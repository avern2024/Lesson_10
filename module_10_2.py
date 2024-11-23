from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f'{self.name}, на нас напали!\n')

        while self.enemies > 0:
            sleep(1)  # Ожидание 1 секунды, представляющее один день сражения
            self.days += 1
            self.enemies -= self.power

            # Определение оставшихся врагов, чтобы не появлялись зомби(отрицательное количество врагов)
            remaining_enemies = max(self.enemies, 0)

            if self.enemies <= 0:
                print(f'{self.name}, сражается {self.days} день(дня)..., осталось {remaining_enemies} воинов.\n')
                print(f'{self.name} одержал победу спустя {self.days} дней(дня)!\n')
            else:
                print(f'{self.name}, сражается {self.days} день(дня)..., осталось {remaining_enemies} воинов.')


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
thread_Knight = Knight('Ivanhoe', 50)
four_knights = Knight('Robin_Hood', 100)

knights = [
    Knight('Sir Lancelot', 10),
    Knight('Sir Galahad', 20),
    Knight('Ivanhoe', 50),
    Knight('Robin_Hood', 100),
]

# Запуск потоков
for knight in knights:
    knight.start()

# Ожидание завершения всех битв
for knight in knights:
    knight.join()

# Вывод строки об окончании сражения
print('Все битвы закончились!')
