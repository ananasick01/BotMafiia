current_phase = 'night'  # Начинаем с ночной фазы

def next_phase():
    """Переключение между фазами дня и ночи"""
    global current_phase
    if current_phase == 'night':
        current_phase = 'day'
    else:
        current_phase = 'night'

def get_current_phase():
    """Текущая фаза игры"""
    return current_phase

def simulate_night():
    """Симуляция ночной фазы (мафия выбирает жертву, доктор спасает, комиссар проверяет)"""
    print("Ночная фаза началась. Мафия выбирает жертву...")

    # Симуляция действий игроков
    return "Ночь окончена, начинается день."

def simulate_day():
    """Симуляция дневной фазы (голосование)"""
    print("Дневная фаза началась. Игроки обсуждают и голосуют...")

    # Симуляция обсуждения
    return "День окончен, начинается ночь."
