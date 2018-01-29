import random
def question():
    while True:
        inp = input("What is your question?")
        if inp == "quit": break
        elif inp[-1] != "?":
            print("I'm sorry, I can only answer questions")
            continue
        answer_list = ["It is certain", "It is decidely so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good",
        "Very doubtful"]
        print (random.choice(answer_list))

x = question()
