def get_weather(temp:float) -> str:
    if temp > 20:
        return 'hot'
    else:
        return 'cold'
