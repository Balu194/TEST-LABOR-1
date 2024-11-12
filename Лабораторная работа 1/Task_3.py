list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс серединытгь

len(list_players)
middle_index = len(list_players) // 2

team_1 = list_players[:middle_index]
team_2 = list_players[middle_index:]

print(len(list_players))
print(team_1)
print(team_2)
