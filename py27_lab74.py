class Team:
    member = 7

    def working_hour(self):
        return self.day

    def all_working_hour(self):
        self.day = 7
        return self.day * self.member

    @classmethod
    def get_member(cls):
        return cls.member

    @staticmethod
    def calculate(x, y):
        return x ** y


t1 = Team()
print 'all working hour=%d' % t1.all_working_hour()
# switch these two will error
print 'working hour=%d' % t1.working_hour()
print 'class method=%d,%d' % (Team.get_member(), t1.get_member())
print 'calculate result=%d,%d' % (t1.calculate(3, 5), Team.calculate(2, 4))