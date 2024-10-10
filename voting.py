votes = {}

def init_voting(players):
    """Инициализация голосов для игроков"""
    global votes
    votes = {player: 0 for player in players}

def vote(voter, target):
    """Голосование одного игрока против другого"""
    if target not in votes:
        raise ValueError("Неверный игрок для голосования")
    votes[target] += 1

def tally_votes():
    """Подсчёт голосов и выбор игрока для исключения"""
    max_votes = max(votes.values())
    players_with_max_votes = [player for player, count in votes.items() if count == max_votes]

    if len(players_with_max_votes) == 1:
        return players_with_max_votes[0]
    else:
        return None  # Ничья

def reset_votes():
    """Сброс голосов после дня"""
    global votes
    votes = {player: 0 for player in votes}
