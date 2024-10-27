import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0  # Не допускаем отрицательное значение
            print(f"{self.name} сражается {self.days}..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} {'дней' if self.days > 1 else 'день'}!")


knight1 = Knight("Ланселот", 15)
knight2 = Knight("Гавейн", 25)

knight1.start()
knight2.start()


knight1.join()
knight2.join()

print("Битва окончена!")