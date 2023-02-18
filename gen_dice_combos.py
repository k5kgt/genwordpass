import sys

def generate_dice_combinations(n):
    results = []
    for i in range(1, 7):
        if n == 1:
            results.append(str(i))
        else:
            for combination in generate_dice_combinations(n - 1):
                results.append(str(i) + combination)
    return results

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 3

combinations = generate_dice_combinations(n)
print(" ".join(combinations))
