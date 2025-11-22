def detect_cognitive_state(pauses, rewinds, idle_time, tab_switch, quiz_score, fast_forward):
    if pauses > 5 or rewinds > 3:
        return "Confused"
    elif idle_time > 120 or tab_switch > 2:
        return "Distracted"
    elif fast_forward > 4:
        return "Bored"
    elif quiz_score < 40:
        return "Overloaded"
    elif quiz_score > 80 and pauses == 0 and rewinds == 0:
        return "Motivated"
    else:
        return "Normal"
