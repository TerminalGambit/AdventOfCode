def algo(input_texte):
    floor = 0
    for i, char in enumerate(input_texte):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            return i + 1
    return floor

def test():
    assert algo(')') == 1
    assert algo('()())') == 5
    print("All tests pass")
    return True

def main():
    test()
    with open('/Users/jackmassey/Desktop/AdventOfCode/2015/day01/input/input.txt', 'r') as f:
        print(algo(f.read()))


if __name__ == '__main__':
    main()
