message = input("> ")
words = message.split( " ")
emojis = {
   ":)" : "🙂",
   ":(" : "🙁",
   "lol" : "😂",
   "sick":"😨",
   "happy": "😀",
   "mermaid": "🧜‍"
}
outcome = " "
for word in words:
   outcome += emojis.get(word, word) + " "
print(outcome)
