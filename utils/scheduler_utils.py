# utils/scheduler_utils.py

def suggest_optimal_load(time_slot: str, current_load: float) -> float:
    if time_slot == "Morning":
        return current_load + 5
    elif time_slot == "Afternoon":
        return current_load
    elif time_slot == "Evening":
        return current_load - 10
    return current_load
