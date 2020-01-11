dic = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand'
}


def num_to_letter(n):
    if n == 1000:
        return "onethousand"
    a, b = n // 100, n % 100
    letter = ''
    if a != 0:
        letter += dic[a] + dic[100]
        if b != 0:
            letter += 'and'
    m = b
    if m in dic.keys():
        letter += dic[m]
        return letter
    else:
        a, b = (m // 10) * 10, m % 10
        letter += dic[a] + dic[b]
    return letter


print(num_to_letter(342), len(num_to_letter(342)))
print(num_to_letter(115), len(num_to_letter(115)))
print(sum([len(num_to_letter(n)) for n in range(1, 1000+1)]))
