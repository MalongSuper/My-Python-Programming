# Football Match Simulation
class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.goals_scored_by_opponent = 0

    def win(self):
        self.points += 3

    def tie(self):
        self.points += 1

    def scored_by_opponent(self, goal):
        self.goals_scored_by_opponent += goal


teams = []
while True:
    team_name = input("Enter a football team's name (or do not enter to finish): ")
    if team_name.lower() == '':
        break
    teams.append(Team(team_name))

# Simulate some games
for i in range(len(teams)):
    for j in range(i + 1, len(teams)):
        result = input(f"Enter result of game between {teams[i].name} and {teams[j].name} (w/t/l): ")
        goals = int(input(f"Enter goals scored by {teams[j].name}: "))
        teams[i].scored_by_opponent(goals)
        if result == 'w':
            teams[i].win()
        elif result == 't':
            teams[i].tie()
            teams[j].tie()
        else:
            teams[j].win()

# Sort teams by points and goals scored by opponent
teams.sort(key=lambda football_team: (football_team.points, -football_team.goals_scored_by_opponent), reverse=True)

# Display rankings
print("Rankings:")
for i, team in enumerate(teams, start=1):
    print(f"{i}. {team.name} - {team.points} points, {team.goals_scored_by_opponent} goals scored by opponent")
