
import time


class Ora:
    def __init__(self, string):
        hour, minu = map(int, string.split(':'))
        if hour > 23 or hour < 0 or minu > 59 or minu < 0:
            raise Exception('Invalid Parameters')
        self.hour = hour
        self.minu = minu

    def __eq__(self, other):
        if self.hour == other.hour:
            return self.minu == other.minu
        return False

    def __lt__(self, other):
        if self.hour == other.hour:
            return self.minu < other.minu
        return self.hour < other.hour

    def __gt__(self, other):
        if self.hour == other.hour:
            return self.minu > other.minu
        return self.hour > other.hour

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __str__(self):
        return '{:02d}:{:02d}'.format(self.hour, self.minu)

    def __repr__(self):
        return '{:02d}:{:02d}'.format(self.hour, self.minu)

    @classmethod
    def now(cls):
        now = time.localtime()
        return cls(f'{now.tm_hour}:{now.tm_min}')


class Interval:
    def __init__(self, o1, o2):
        self.start = o1
        self.end = o2

    @classmethod
    def empty(cls):
        return cls(Ora("00:00"), Ora("00:00"))

    def isNow(self):
        now = Ora.now()
        if self.end < self.start:
            return now <= self.end or now >= self.start
        return now <= self.end and now >= self.start

    def __str__(self):
        return f'{str(self.start)}-{str(self.end)}'

    def __repr__(self):
        return f'{repr(self.start)}-{repr(self.end)}'
