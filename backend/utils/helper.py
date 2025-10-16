def format_driver_name(name: str) -> str:
    return name.title().strip()

def calculate_points(position: int) -> int:
    table = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
    return table[position - 1] if 1 <= position <= 10 else 0