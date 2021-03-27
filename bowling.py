def score(frames):
    total = 0
    last_was_spare, last_was_strike = False, False
    consecutive_strike = False

    for roll1, roll2 in frames.split():
        if last_was_spare:
            total = total + int(roll1)
            last_was_spare = False

        if last_was_strike:
            if roll2 == "X":
                consecutive_strike = True  # another strike, continue
            elif roll2 == "/":  # no more consecutive_strike but a spare
                if consecutive_strike:  # previous bowl was a strike
                    total += 10 + int(roll1)  # for first strike
                    consecutive_strike = False
                roll2score = 10 - int(roll1)  # convert / to number, keep var roll2 as '/'
                total += int(roll1) + roll2score  # for second strike
                last_was_strike = False
            else:    # no more consecutive_strike
                if consecutive_strike:  # previous bowl was a strike
                    total += 10 + int(roll1)
                    consecutive_strike = False
                total += int(roll1) + int(roll2)
                last_was_strike = False

        if roll2 == '/':
            total += 10
            last_was_spare = True
        elif roll2 == 'X':
            total += 10
            last_was_strike = True
        else:
            total = total + int(roll1) + int(roll2)

    return total


# score('XX XX 5/ 12')
