# with the help of dictionary. write a code the u enter the number and to output will be in words
numbers = input(f'Enter the number : ')
words = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three',
    '4' : 'four',
    '5' : 'five',
    '6' : 'six',
    '7' : 'seven',
    '8' : 'eight',
    '9' : 'nine',
}
output = ''
for n in numbers:
    output  += words.get(n,'"not a number"') + " "
print(output)