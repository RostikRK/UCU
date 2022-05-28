import random
def data_of_questions():
    """Creates databases of questions and corresponding keys.
    """
    list1 = ["From which language is the word ‘ketchup’ derived?",
    "Which is the country with the biggest population in Europe?",
    "What are made and repaired by a cobbler?",
    "Apart from womanizing and producing films, what was the other passion of Howa\
rd Hughes?",
    "What colour are the four stars on the flag of New Zealand?",
    "Maris Piper and King Edward are varieties of what?",
    "H2O is the chemical formula for what?",
    "Blandenburg, Bremen and Lower Saxony are states in which European country?",
    "Which Olympic sport takes place in a velodrome?",
    "Which joint connects the foot to the leg?",
    "What name is shared by a brass musical instrument and a type of ice-cream co\
ne?",
    "Prior to joining the euro, what was the currency of Spain?",
    "Which American city was also the title of a 2002 Oscar-winning film starring\
Catherine Zeta-Jones and Richard Gere?",
    "What item, useful in the rain, provided the title of a hit single of Rihanna\
?",
    "Aintree racecourse is in which city?",
    "Harley Street in London is commonly associated with which profession?",
    "What is the national flower of Wales?",
    "Ringway airport serves which British city?",
    "St. Mungo’s Cathedral is in which Scottish city?",
    "Glyndebourne is associated with which type of music?",
    "What kind of food is Penne?",
    "Which Disney Princess called Gus and Jaq friends?",
    "What does the Latin Tempus mean in English?",
    "Which country in the world is believed to have the most miles of motorway?",
    "How many horses are on each team in a polo match?",
    "Which European city hosted the 1936 Summer Olympics?",
    "What is the capital city of Australia?",
    "How many planets are in our solar system?",
    "What type of rock is marble?",
    "What planet are Transformers from?",
    "Before 2014, how many times had the Mona Lisa been stolen from the Louvre?",
    "Where can you find the traditionally Juniper-flavored beer called Sahti?",
    "In which country can you find the most freshwater resources?",]
    list2 = ["Chinese", "Russia", "Shoes", "Aviation",
    "Red",
    "Potato", "Water", "Germany", "Cycling", "Ankle",
    "Cornet", "Peseta","Chicago", "Umbrella", "Liverpool", "Medicine", "Daffodil",
    "Manchester", "Glasgow", "Opera", "Pasta", "Cinderella","Time", "China",
    "Four", "Berlin", "Canberra", "Eight", "Metamorphic", "Cybertron", "Once",
    "Finland", "Brazil",
    ]
    list3 = ["In which part of your body would you find the cruciate ligament?", 
    "What is the name of the main antagonist in the Shakespeare play Othello?",
    "What element is denoted by the chemical symbol Sn in the periodic table?",
    "In tennis, what piece of fruit is found at the top of the men's Wimbledon tro\
phy?",
    "Who won the FIFA Women's World Cup in 2019?",
    "Which nuts are used in marzipan?", 
    "What is the most famous Mexican beer?",
    "Which country is the origin of the cocktail Mojito?",
    "What is Japanese sake made from?",
    "What is the chemical formula for Table Salt?",
    "At which venue is the British Grand Prix held?",
    "Which UK city is situated further west?",
    "What is the capital of Finland?",
    "What is Sheldon Cooper’s one-word catchphrase in The Big Bang Theory?",
    "What’s the name of the talking snowman in Disney’s Frozen?",
    "The name of which African animal means 'river horse'?",
    "Who invented the word 'vomit'?",
    "What does come down but never goes up?",
    "What nut is in the middle of a Ferrero Rocher?",
    "Where in England would you find the themepark Dreamland?",
    "Which English city was once known as Duroliponte?",
    "Where is the oldest tree in the world?",
    "What does a Geiger Counter measure?",
    "What is the capital city of Botswana?",
    "What's the biggest landlocked county in England?",
    "What's Hermione's cat in the Harry Potter series called?",
    "What is the most expensive spice in the world by weight?",
    "In which country did scampi originate?",
    "What type of fish are Arbroath smokies?",
    "Which technique did Vincent van Gogh use to paint his 'Sunflowers'?",
    "What is Pablo Picasso's daughter's name?",
    "According to American history, what was the bloodiest one-day battle of the Civil War?",
    "What is the romanized Arabic word for 'moon'?",
    ]
    list4 = ["Knee", "Iago", "Tin", "Pineapple","USA","Almonds","Corona",
    "Cuba", "Rice", "NaCl","Silverstone", "Edinburgh", "Helsinki", "Bazinga", "Olaf",
    "Hippopotamus", "Shakespeare", "Rain", "Hazelnut", "Margate", "Cambridge",
    "California", "Radiation", "Gaborone", "Shropshire", "Crookshanks", "Saffron",
    "Italy", "Hoddock", "Impasto", "Paloma", "Antietam", "Qamar",]
    list5 = [
    "Saying the name of what dried fruit used to be used to encourage people to s\
mile before a photo in the 1800s, before the phrase “cheese?”",
    "Which 2019 film won the Golden Raspberry Award for Worst Film this year? ",
    "What does Bridget Jones name her baby in the film series’s third instalment?",
    "A screwdriver cocktail is orange juice, ice and which spirit?",
    "Which southern Italian city is usually credited as the birthplace of the pizza?",
    "Complete the name of the classic British sitcom: Steptoe and [blank]",
    "Gordon Sumner is the real name of what famous British musician?",
    "Which planet has the most moons?",
    "Where is the smallest bone in the human body located?",
    "Elon Musk is the CEO of which global brand.",
    "Who had a hit with MMMBop in April 1997?",
    "In 2006’s Doomsday, what country is Bad Wolf Bay in?",
    "Director Taika Waititi also played which comedic Thor: Ragnarok character?",
    "What does the licence plate on the DeLorean say in Back To The Future?",
    "Who does John Boyega play in the most recent Star Wars films?",
    "What’s Marge’s maiden name?",
    "What is the most consumed manufactured drink in the world?",
    "Hendrick’s, Larios, and Seagram’s are some of the best-selling brands of which spirit?",
    "Which is the only edible food that never goes bad?",
    "What sport is dubbed the 'king of sports'?",
    "Havana is the capital of what country?",
    "In what type of matter are atoms most tightly packed?",
    "What tissues connect the muscles to the bones?",
    "In public places in the state of Florida, what's illegal to do when wearing a swimsuit?",
    "Where was the first British colony in the Americas?",
    "The wood of a cricket bat is traditionally made from which type of tree?",
    "What is the largest moon of Saturn called?",
    "What flower is named after the Latin word for wolf?",
    "What do you call a group of bears?",
    " Joyce Banda became the first female president of which African country in 2012?",
    "What colour is in 75 per cent of national flags?",
    "Aduki, borlotti and cannellini are types of what?",
    "Vanilla comes from what flowers?",
    "What Was The First Sports Film To Win An Academy Award For Best Picture?",
    "What is the common name for dried plums?",
    "What is the unit of currency in Laos"
    ]
    list6 = [
    "Prunes", "Cat", "William", "Vodka", "Naples", "Son", "Sting", "Jupetus","Ear",
    "Tesla","Hanson", "Norway", "Korg", "Outatime", "finn", "Bouvier", "tea", "gin",
    "Honey", "Soccer","Cuba", "Solid", "Tendons", "sing", "roanok", "willow", "titan",
    "Lupin", "Sloth", "Malawi", "Red", "Beans", "Orchids", "Rocky", "Prunes", "kip",
    ]
    ans1 = dict(zip(list1, list2))
    ans2 = dict(zip(list3, list4))
    ans3 = dict(zip(list5, list6))
    return ans1, ans2, ans3, list1, list3, list5

def presetting():
    """Tells the setting of the game and rules. Also creates the characteristics of \
the character (variables) on which the conditions of the game depend
    """
    print("Hello! Before starting the game lets create your character. Please \
enter your name: ")
    name =input(">>> ")
    while True:
        print("Great. Now input your age.")
        try:
            age = int(input(">>> "))
            if age>0 and age<=60:
                break
            else:
                print("You lied")
        except ValueError:
            print("Write correct value")
    
    print("And the last: enter whether you are a man or a woman. (m/w)")
    gender = input(">>> ").lower()
    if gender == "m":
        all_years = random.randint(60, 78)
    elif gender == "w":
        all_years = random.randint(65, 83)
    else:
        print("Wrong input. Create character Again? (Y/N) ")
        if input(">>> ").upper() == "Y":
            presetting()
        else:
            quit()
    tries = all_years - age
    print("Great we are ready to start.")
    print(age,"years ago ",name," was born. At the age of",int(age/3*2),"you \
met a Sas\
hka. After a short acquaintance you became friends.\n Years passed and yo\
u began to notice that he was not getting old. \n One day you decided to \
ask him: What is your secret why you do not grow old.\n He answered: Ther\
e is one sage who trades in human years of life.\n And if you want you ca\
n play a game with him for these lives.\n If you win you will get more ti\
me but if not you will die. You can't stop in the middle of the game.\n A\
nd also you are just able to double the years of life. Then you asked: Wh\
ere I can find him?\n Sashka answered: Hogwards street drib 47. After a f\
ew days of reflection you decided to risk.\n Game rules:\n1) you are ask\
ed questions, the answear is hiden but you are able to get a hint.\n2) Hin\
t: you are able to guess a letter of the word.(it costs a few years of li\
fe depending on your difficulty level). \n3) It possible to guess all word \
immediatly.\n4) You are just able to double the length of life. \n5) If years\
 = 0 you die " )
    return tries, all_years

    



def levels():
    """gets difficulty levels and adds more variables depending on the choice
    """
    while True:   
        print("Select the difficulty level( easy, normal, hardcore): ")
        level = input(">>> ").lower()
        if level == "easy":
            minus = 1
            break
        elif level == "normal":
            minus =  2
            break
        elif level == "hardcore":
            minus = 3
            break
        else:
            print("Error")
    return minus, level




def play(tries, minus, all_years, level, list1, list3, list5, ans1, ans2, ans3):
    """ starts the loop until the condition is met, in the loop itself choose\
s the riddle and the solution, then encrypts all the letters of the word, the\
n checks whether the entered letter has been guessed before, if so, nothing c\
hanges, if not, provided that this letter is in the word opens it if not subt\
racts points. Then checks the same thing but with the whole word.
    """
    sircumspect = True
    i = 0
    while(sircumspect):
        guessed = False
        guessed_letters = []
        guessed_words = []
        print("Good luck")
        if level == "easy":
            x = random.randint(0, len(list1)-1)
            y = list1[x]
            word = ans1[y]
        elif level == "normal":
            x = random.randint(0, len(list3)-1)
            y = list3[x]
            word = ans2[y]
        elif level == "hardcore":
            x = random.randint(0, len(list5)-1)
            y = list5[x]
            word = ans3[y]
        word = word.upper()
        word_completion = "_" * len(word)
        if i == 0:
            print("The first question is:", y)
        elif i >= 1 and tries>0:
            print("Next question is:", y)
        print(word_completion)
        print("\n")
        print("The years of life left:", tries)
        print("The years to double your life length:", all_years*2)
        print("\n")
        while not guessed and tries > 0:
            print("Please guess a letter or word: ")
            guess = input(">>> ").upper()
            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You already guessed the letter", guess)
                elif guess not in word:
                    print(guess, "is not in the word.")
                    tries -= minus
                    guessed_letters.append(guess)
                else:
                    print("Good job,", guess, "is in the word!")
                    guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(word) if\
 letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(word) and guess.isalpha():
                if guess in guessed_words:
                    print("You already guessed the word", guess)
                elif guess != word:
                    print(guess, "is not the word.")
                    tries -= minus
                    guessed_words.append(guess)
                else:
                    guessed = True
                    word_completion = word
            else:
                print("Not a valid guess.")
            print(y)
            print(word_completion)
            print("\n")
            print("The years of life left:", tries)
            print("The years to double your life length:", all_years*2)
            print("\n")
        if guessed and 0<tries<=all_years*2:
            print("Congrats, you guessed the word!")
            tries += 10
            i += 1
        elif guessed and tries >= all_years*2:
            print("Yeah great you win the second life!")
            sircumspect = False
        else:
            print("Sorry, you ran out of lifes. The word was " + word + ". May\
be in next life you will be more lucky!")
            sircumspect = False




def main():
    """Runs functions in order
    """
    
    ans1, ans2, ans3, list1, list3, list5, = data_of_questions()
    tries, all_years = presetting()
    minus, level  = levels()
    play(tries, minus, all_years, level, list1, list3, list5, ans1, ans2, ans3)
    while True:
        if input("Play Again? (Y/N) \n>>> ").upper() == "Y":
            ans1, ans2, ans3, list1, list3, list5 = data_of_questions()
            tries, all_years = presetting()
            minus, level  = levels()
            play(tries, minus, all_years, level, list1, list3, list5, ans1, ans2, ans3)
        else:
            quit()


if __name__ == "__main__":
    main()