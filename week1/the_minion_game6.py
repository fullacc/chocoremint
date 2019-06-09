def minion_game():
    s = input()
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0

    for i in range(len(s)):
        if s[i] in vowels:
            kevin += (len(s)-i)
        else:
            stuart += (len(s)-i)

    if kevin > stuart:
        print("Kevin", kevin)
        return "Kevin",kevin
    elif kevin < stuart:
        print("Stuart", stuart)
        return "Stuart",stuart
    else:
        print("Draw")
        return "Draw"


def main():
    minion_game()


if __name__ == '__main__':
    main()
