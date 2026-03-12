# useing dictionary 
# write a programm where i enter text emoji which convert it to real emoji
message = input(f'>')
words = message.split(' ')
emojis = {
    ':-)': '😄',
    ':)':'😄',
    ':-(':'😞',
    ':(':'😞'
}
output = ''
for word in words:
    output += emojis.get(word,word) + ' '
print(output)    
