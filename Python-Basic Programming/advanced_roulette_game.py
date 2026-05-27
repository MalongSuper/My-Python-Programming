# Advanced Roulette Game
import random

roulette_rules = {"Green": [0], "Red": [], "Black": []}

for i in range(1, 37):
    # Pockets 1–10
    if 1 <= i <= 10:
        if i % 2 == 1:
            roulette_rules["Red"].append(i)
        else:
            roulette_rules["Black"].append(i)
    # Pockets 11–18
    elif 11 <= i <= 18:
        if i % 2 == 1:
            roulette_rules["Black"].append(i)
        else:
            roulette_rules["Red"].append(i)
    # Pockets 19–28
    elif 19 <= i <= 28:
        if i % 2 == 1:
            roulette_rules["Red"].append(i)
        else:
            roulette_rules["Black"].append(i)
    # Pockets 29–36
    elif 29 <= i <= 36:
        if i % 2 == 1:
            roulette_rules["Black"].append(i)
        else:
            roulette_rules["Red"].append(i)


# Randomize a sequence with 7 numbers from 0 to 36
def random_sequence():
    return random.sample(range(0, 37), 7)


def get_color(number):
    if number in roulette_rules["Green"]:
        return "Green"
    elif number in roulette_rules["Red"]:
        return "Red"
    elif number in roulette_rules["Black"]:
        return "Black"
    return None


# Count the number of red, black, and green
def count_color(sequence):
    red = 0
    black = 0
    green = 0
    for number in sequence:
        if number in roulette_rules["Red"]:
            red += 1
        elif number in roulette_rules["Black"]:
            black += 1
        elif number in roulette_rules["Green"]:
            green += 1
    return red, black, green


def winning_game(sequence1, sequence2):
    p1_red, p1_black, p1_green = count_color(sequence1)
    p2_red, p2_black, p2_green = count_color(sequence2)

    # Winning condition 1: Three Green Pockets (highest priority)
    if p1_green == 3 and p2_green != 3:
        return "Player 1 wins (3 Green Pockets)!"
    elif p2_green == 3 and p1_green != 3:
        return "Player 2 wins (3 Green Pockets)!"
    elif p1_green == 3 and p2_green == 3:
        return "Draw (Both have 3 Green Pockets)!"
    else:
        # No winner from Green Pockets, proceed to Advantage rules

        p1_dominant_color_count = 0
        p2_dominant_color_count = 0
        p1_qualifies_for_advantage = False
        p2_qualifies_for_advantage = False

        # Determine Player 1's dominant color count and if they qualify for an advantage
        if p1_red >= 4 and p1_black >= 1:
            p1_dominant_color_count = p1_red
            p1_qualifies_for_advantage = True
        if p1_black >= 4 and p1_red >= 1:
            # If P1 also qualifies for black advantage, take the higher count
            if p1_black > p1_dominant_color_count:
                p1_dominant_color_count = p1_black
            p1_qualifies_for_advantage = True

        # Determine Player 2's dominant color count and if they qualify for an advantage
        if p2_red >= 4 and p2_black >= 1:
            p2_dominant_color_count = p2_red
            p2_qualifies_for_advantage = True
        if p2_black >= 4 and p2_red >= 1:
            # If P2 also qualifies for black advantage, take the higher count
            if p2_black > p2_dominant_color_count:
                p2_dominant_color_count = p2_black
            p2_qualifies_for_advantage = True

        # Apply advantage and tie-breaking rules
        if p1_qualifies_for_advantage and not p2_qualifies_for_advantage:
            return "Player 1 wins (Advantage)!"
        elif p2_qualifies_for_advantage and not p1_qualifies_for_advantage:
            return "Player 2 wins (Advantage)!"
        elif p1_qualifies_for_advantage and p2_qualifies_for_advantage:
            # Both satisfy their own color advantage condition, apply HIGHER dominant count rule
            if p1_dominant_color_count > p2_dominant_color_count:
                return "Player 1 wins (Higher Dominant Color Count)!"
            elif p2_dominant_color_count > p1_dominant_color_count:
                return "Player 2 wins (Higher Dominant Color Count)!"
            else: # Dominant counts are equal
                return "Draw (Equal Dominant Color Count)!"
        else:
            return "Draw or No one wins."


def main():
    sequence1 = random_sequence()
    sequence2 = random_sequence()
    sequence1_color = [get_color(number) for number in sequence1]
    sequence2_color = [get_color(number) for number in sequence2]

    print("Player 1 Sequence:", sequence1)
    print("=> Player 1 Sequence Color:", sequence1_color)
    print("\nPlayer 2 Sequence:", sequence2)
    print("=> Player 1 Sequence Color:", sequence2_color)

    sequence1_red, sequence1_black, sequence1_green = count_color(sequence1)
    print("\nPlayer 1 Sequence Color Count:")
    print(f"- Red: {sequence1_red}")
    print(f"- Black: {sequence1_black}")
    print(f"- Green: {sequence1_green}")

    sequence2_red, sequence2_black, sequence2_green = count_color(sequence2)
    print("\nPlayer 2 Sequence Color Count:")
    print(f"- Red: {sequence2_red}")
    print(f"- Black: {sequence2_black}")
    print(f"- Green: {sequence2_green}")

    # Call the winning_game function
    final_result = winning_game(sequence1, sequence2)
    print(final_result)


main()
