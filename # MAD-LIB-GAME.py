# MAD-LIB-GAME

''' HEY USER TRY THIS GAME'''

answer=input("HORROR , COMEDY , SIMPLE: ")
if answer=="HORROR":
    noun=input("ENTER A NOUN: ")
    word=input("ENTER A WORD: ")
    place=input("ENTER A PLACE: ")
    gender=input("ENTER A GENDER (HE OR SHE): ")
    gender1=input("ENTER A GENDER(HIS OR HER): ")
    print(f"A bachelor's party ends with two dead {noun}s in the {place}. Both of them are missing their {word}. {noun} wearing a black dress is holding a knife in hand and threatening to kill a frightened man. {gender} is terrified because {gender} does not want to kill anybody, but {gender1} body refuses to obey her mind.")
elif answer=="COMEDY":
    name=input("ENTER A NAME: ")
    word=input("ENTER A WORD: ")
    word1=input("ENTER ANOTHER WORD: ")
    word2=input("ENTER ANOTHER WORD: ")
    adj=input("ENTER A ADJECTIVE: ")
    obj=input("ENTER A OBJECT: ")
    print(f"I was walking with my {name}, when I tripped and hit my {word} on the ground really hard. I yelled out “OW, MY {word1}” although my mom heard “OW, MY {word2}.” She started yelling about how that was a {adj} word and we didn’t say that word, and she was going to wash my mouth out with {obj}")
   

else:
     noun=input("ENTER A NOUN: ")
     name=input("ENTER A NAME: ")
     animal=input("ENTER A ANIMAL: ")
     adj=input("ENTER A ADJECTIVE: ")
     place=input("ENTER A PLACE: ")
     print(f"Once, there was {name} who became bored when he watched over the {place} {noun} grazing on the hillside. To entertain himself, he sang out, “{animal}! {animal}! The {animal} is chasing the {noun}! When the villagers heard the cry, they ran up the hill to drive the wolf away. But when they arrived, they saw no wolf. The boy was amused when he saw their {adj} faces.")

user=input("LIKE THE STORY: ")
if user=="YES"or"yes":
    print("THANK YOU")
