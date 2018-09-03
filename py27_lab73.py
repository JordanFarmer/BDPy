class Team:
    name = 'Normal Team'

    def __str__(self):
        return 'team has a name:%s' % self.name


team1 = Team()
print team1.name

team1.name = 'RD team'
print team1.name

del team1.name
print team1.name
team1.size = 7
print team1.name, team1.size
print team1