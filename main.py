# 2.2
# Po połączeniu  ostatniego znaku z pierwszym znakiem powstanie pierścień wyrazowy.
# Napisz  program w wybranym przez siebie języku programowania, który policzy ile w
# pierścieniu pięć kolejnych znaków tworzy palindrom.


def main():
    word = input("Enter word: ")
    result = []
    for i in range(len(word)):
        w = ""
        k = i
        for j in range(5):
            w += word[k]
            if k + 1 == len(word):
                k = 0
            else:
                k += 1
        if w == w[::-1]:
            result.append(w)
    if len(result) == 0:
        print("Pierścień nie zawiera palindromów.")
    else:
        print(result)
        print(f'W pierścieniu pięć kolejnych znaków tworzy palindrom {len(result)} razy.')


if __name__ == "__main__":
    main()
