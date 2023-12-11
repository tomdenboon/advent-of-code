import functools

CARD_VALUE = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

def determine_hand(card_counts):
    match len(card_counts):
        case 5: return 1
        case 4: return 2    
        case 3: return 3 if 2 in card_counts.values() else 4
        case 2: return 5 if 3 in card_counts.values() else 6
        case 1: return 7

def sort_by_val(x, y):
    if x[1] != y[1]:
        return x[1] - y[1]

    for i, j in zip(x[0], y[0]):
        if i == j:
            continue
        else:
            return i - j
    return 0

def part_one(input_as_string: str):
    scored_hand = []
    for line in input_as_string.splitlines():
        hand, score = line.strip().split()
        card_counts = dict([(c, hand.count(c)) for c in set(hand)])
        scored_hand.append(([CARD_VALUE[c] for c in hand], determine_hand(card_counts), int(score)))
    scored_hand.sort(key=functools.cmp_to_key(sort_by_val))
    return sum([(i + 1) * s[2] for i, s in enumerate(scored_hand)])
        
def part_two(input_as_string: str):
    CARD_VALUE['J'] = 1
    scored_hand = []
    for line in input_as_string.splitlines():
        hand, score = line.strip().split()
        card_counts = dict([(c, hand.count(c)) for c in set(hand)])
        if 'J' in card_counts and len(card_counts) > 1:
            j = card_counts.pop('J')
            m = max(card_counts, key=card_counts.get)
            card_counts[m] += j
        scored_hand.append(([CARD_VALUE[c] for c in hand], determine_hand(card_counts), int(score)))
    scored_hand.sort(key=functools.cmp_to_key(sort_by_val))
    return sum([(i + 1) * s[2] for i, s in enumerate(scored_hand)])