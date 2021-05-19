team_a = input("Name of first team (In 3 letters Ex- IND,CSK): ")
team_b = input("Name of second team (In 3 letters Ex- IND,CSK): ")
#inputs for the team names

overs = int(input("Total no. of overs (Ex- 50 for ODI, 20 for T20): "))
runs_a = int(input("Total runs scored by " + team_a + " against " + team_b + ": "))
overs_a = int(input("No. of overs " + team_a + " faced: "))
runs_b = int(input("Total runs scored by " + team_b + " against " + team_a + ": "))
overs_b = int(input("No. of overs " + team_b + " faced: "))
#inputs for the runs scored and overs played by each team

net_rr_a = str((runs_a / overs_a) - (runs_b / overs))
net_rr_b = str((runs_b / overs_b) - (runs_a / overs))

print("")
print("Points Table:")
print("No. Team NRR")

if net_rr_a > net_rr_b:
    print("1   " + team_a + "  " + net_rr_a)
    print("2   " + team_b + "  " + net_rr_b)
elif (net_rr_a == net_rr_b):
    print("1   " + team_a + "  " + net_rr_a)
    print("1   " + team_b + "  " + net_rr_b)
    print("It's a tie. The 2 teams need to play another match.")
else:
    print("1   " + team_b + "  " + net_rr_b)
    print("2   " + team_a + "  " + net_rr_a)
