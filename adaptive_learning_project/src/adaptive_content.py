def get_adaptive_content(state):
    if state == "Confused":
        return "Easy content with examples"
    elif state == "Overloaded":
        return "Simplified summary content"
    elif state == "Bored":
        return "Challenging advanced content"
    elif state == "Motivated":
        return "Expert-level content"
    elif state == "Distracted":
        return "Interactive quiz or game-based activity"
    else:
        return "Normal content"
