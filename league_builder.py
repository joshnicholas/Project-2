import csv

# open spreadsheet and create a list of tuples from the data

def open_and_list(csv_path_temp):
    with open(csv_path_temp) as spread:
        list_of_twoples = [tuple(line) for line in csv.reader(spread)]
    return list_of_twoples

# sort the list into two lists, one experienced and one not

def experienced_or_not(original_list, experienced):
    while True:
        list = []
        for line in original_list[1:]:
            if experienced in line:
                list.append(line)
        return list
        break

# sort experienced and inexperienced into teams

def sort_onto_team(experienced, inexperienced):
    team = []
    for index in range(3):
        team.append(experienced.pop())
        team.append(inexperienced.pop())
    return team

# print a text file for each team

def text_please(team_name, team):
    with open("teams.txt", 'a') as text:
        text.write("\n" + str(team_name) + ": \n")
        for twoples in team:
            text.write("\n")
            for twople in twoples:
                text.write(str(twople) + ", ")
        text.write("\n")

# main function

def lets_go():

    csv_path = 'soccer_players.csv'

    with open("teams.txt", "w") as output_file:
        output_file.write("The super awesome soccer League: \n")

    main_list = open_and_list(csv_path)

    experienced_players = experienced_or_not(main_list, "YES")
    inexperienced_players = experienced_or_not(main_list, "NO")

    team_a = sort_onto_team(experienced_players, inexperienced_players)
    team_b = sort_onto_team(experienced_players, inexperienced_players)
    team_c = sort_onto_team(experienced_players, inexperienced_players)

    text_please("Sharks", team_a)
    text_please("Dragons", team_b)
    text_please("Raptors", team_c)

if __name__ == "__main__":
    lets_go()
