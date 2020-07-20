'''
author: dotrungquan.info
Usage: python3 generator-password.py
'''
import random


def passgen(n):
    x = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pw = "".join(random.sample(x, n))
    print(str(pw))


def main():
    while True:
        try:
            n = int(input("Nhap do dai: "))
            if n <= 0 or n >= 30:
                print("Nhap gia tri lon hon 0 va nho hon 20!")
            else:
                passgen(n)
                break
        except ValueError:
            print("Nhap gia tri la so!")

if __name__ == "__main__":
    main()
