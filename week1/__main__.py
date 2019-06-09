def ifelse(n):

    used = 0
    if n % 2 == 1:
        used = 1
    else:
        if n > 5 and n < 21:
            used = 1

    if used == 1:
        print("Weird")
        return "Weird"
    else:
        print("Not Weird")
        return "Not Weird"

def main():
    n = int(input())
    ifelse(n)

if __name__ == '__main__':
    main()