import random

def assign_roles(players):
    """Распределение ролей среди игроков"""
    roles = {}
    roles_list = ['Mafia', 'Doctor', 'Commissioner'] + ['Citizen'] * (len(players) - 3)
    random.shuffle(roles_list)

    for player, role in zip(players, roles_list):
        roles[player] = role
        print(f"{player} получил роль: {role}")
    return roles

def get_role(roles, player):
    """Получить роль игрока"""
    return roles.get(player)

def is_mafia(roles, player):
    """Проверить, является ли игрок мафией"""
    return roles.get(player) == 'Mafia'
