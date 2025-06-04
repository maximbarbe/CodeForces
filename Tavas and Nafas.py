words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
n = int(input())
if n <= 19:
    print(words[n])
else:
    if n % 10 == 0:
        print(tens[n//10 - 2])
    else:
        print(f"{tens[n//10 - 2]}-{words[n%10]}")