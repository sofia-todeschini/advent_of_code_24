#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def check_enabled(astring, current_state):
    if "do(" in astring:
        return True
    if "don't(" in astring:
        return False
    
    return current_state


def check_mul(astring):

    to_examine = astring.split(",")
    if len(to_examine) != 2:
        return 0
    
    try:
        num1 = int(to_examine[0])
        num2 = int(to_examine[1])
    except ValueError:
        return 0

    if num1 > 999 or num2 > 999:
        return 0
    
    return num1 * num2


def main():
    
    with open("input.txt", "r") as f:
        data = f.read().replace('\n', '')
    
    split1 = data.split("mul(")

    split2 = [item for elem in split1 for item in elem.split(")")]

    sum = 0
    is_mul_enabled = True

    for elem in split2:
        is_mul_enabled = check_enabled(elem, is_mul_enabled)
        if is_mul_enabled:
            sum += check_mul(elem)
    
    print(sum)


if __name__ == "__main__":
    main()
