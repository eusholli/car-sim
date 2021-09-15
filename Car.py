import pandas as pd


class Car:

    def __init__(self, front_left=0.0,
                 front_right=0.0, back_left=0.0,
                 back_right=0.0, x_location=0.0, y_location=0.0,
                 direction=0.0, speed=0.0):

        self.front_left = 0.2
        self.front_right = 0.0
        self.back_left = 0.0
        self.back_right = 0.0
        self.x_location = 0.0
        self.y_location = 0.0
        self.direction = 0.0
        self.speed = 0.0

        cols = list(self.__dict__.keys())
        self.df = pd.DataFrame(columns=cols)

    def record_status(self):
        row = dict(self.__dict__)
        del row['df']
        self.df = self.df.append(row, ignore_index=True)


car = Car()
print(car.df)

for i in range(5):
    car.record_status()

print(car.df.head())
car.df.info()
