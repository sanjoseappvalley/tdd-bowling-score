def convert_str_scores_to_int(str_list):
    int_scores = []
    for i, value in enumerate(str_list):
        if value == 'X':
            value = 10
        elif value == '/':
            value = 10 - int(str_list[i-1])
        elif value == '-':
            value = 0
        int_scores.append(int(value))
    return int_scores


def score(frames):
    score_list = list(frames)
    int_scores = convert_str_scores_to_int(score_list)

    total = 0
    for i, score in enumerate(score_list):
        if score == '/':
            total += int_scores[i] + int_scores[i+1]
        elif score == 'X':
            total += 10 + int_scores[i+1] + int_scores[i+2]
        elif score == '-':
            total += 0
        else:
            total += int(score)

    return total
