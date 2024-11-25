def algo(input_texte):
    return input_texte.count('(') - input_texte.count(')')

def test():
    assert algo('(())') == 0
    assert algo('()()') == 0
    assert algo('(((') == 3
    assert algo('(()(()(') == 3
    assert algo('))(((((') == 3
    assert algo('())') == -1
    assert algo('))(') == -1
    assert algo(')))') == -3
    assert algo(')())())') == -3
    print("All tests pass")
    return True

def main():
    test()
    with open('/Users/jackmassey/Desktop/AdventOfCode/2015/day01/input/input.txt', 'r') as f:
        print(algo(f.read()))


if __name__ == '__main__':
    main()
