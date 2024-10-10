
kills = []
votes_history = []

def add_kill(player):
    """Добавить игрока в список убитых"""
    kills.append(player)

def add_vote(day, votes):
    """Добавить результаты голосования за день"""
    votes_history.append({'day': day, 'votes': votes})

def show_statistics():
    """Вывести игровую статистику"""
    print("Статистика игры:")
    print(f"Убитые: {', '.join(kills)}")
    print("История голосования:")
    for vote in votes_history:
        print(f"День {vote['day']}: {vote['votes']}")
