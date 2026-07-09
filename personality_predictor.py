def predict_personality(scores):
    return max(scores, key=scores.get)