"""
This program calculates the Life path and Heart desire number with the
help of the Name and DOB input provided by the user. The program stores
the result in a text file.
"""

def life_path_no(dob):
    """ Life path number calculation is done by adding the digits of the DOB entered by user """
    if type(dob) not in [int]:
        raise TypeError ("The DOB must be a non-negative number")
    if dob < 0:
        raise ValueError("The DOB cannot be negative")
    dob_str = str(dob)
    life_path = "0"
    while dob > 9:
        dob = int("0")
        for char in dob_str:
            char = int(char)
            dob += char
        life_path = str(dob)
        dob_str = str(dob)
    if life_path == '1':
        print("\nNumber 1: You are The Leader\n"
              "Strengths: Ones are natural-born leaders, ambitious, and usually successful "
              "in the professional\nrealm. Charming, diplomatic, and always interesting to"
              " be around.\n"
              "Challenges: Ones are caring to the point that they may be overprotective "
              "and domineering.\n"
              "May also be prone to anger issues.")
    elif life_path == '2':
        print("\nNumber 2: You are The Mediator\n"
              "Strengths: These people are deeply kind, caring, and empathetic."
              " They’re often artists, "
              "though their skill\n for diffusing tense situations may also make"
              " them skilled as politicians.\n"
              "Challenges: Deep sensitivity and conflict aversion can make 2s overly dependent in"
              "their personal \nrelationships. They may have a hard time standing"
              " up for their needs.")
    elif life_path == '3':
        print("\nNumber 3: You are The Communicator\n"
              "Strengths: Threes love attention and generally come by it easily. They can "
              "achieve a great many things and\n are likely precocious as children. Always "
              "high energy.\nChallenges: Just as easily as threes start big, exciting projects, "
              "they often abandon them. Threes \nlikely find it difficult to focus/commit and "
              "may become too focused on others’ perceptions of them.")
    elif life_path == '4':
        print("\nNumber 4: You are The Teacher"
              "\n"
              "Strengths: This is generally a very principled, reliable person, which makes "
              "them a desirable friend and\n co-worker. People generally know what to expect "
              "from a four.\nChallenges: This type can become rigid, too fixated on rules"
              " and norms."
              " Fours may find themselves easily \nfrustrated by people who create their"
              " own guidelines or stray too far outside the box.")
    elif life_path == '5':
        print("\nNumber 5: You are The Freedom Seeker\n"
              "Strengths: Fives are inquisitive and intellectual, often making for great "
              "journalists and educators. \nStrong communication skills with a childlike "
              "sense of wonder for simple pleasures.\nChallenges: Fives may indulge a little too "
              "much in their favorite hobbies, like shopping or partying.\n"
              "May also come off a bit superficial and noncommittal in relationships.")
    elif life_path == '6':
        print("\nNumber 6: You are The Nurturer\n"
              "Strengths: This type is likely to be an impassioned speaker and activist, "
              "whether professionally or\npersonally, on behalf of one’s loved ones. Their "
              "curiosity makes them great lawyers,and therapists.\nChallenges: Sixes may have"
              " a hard time with consistency, especially when it comes to taking care of \n"
              "themselves (sort of the “Mark Ruffalo eating cold pizza in Spotlight” type).")
    elif life_path == '7':
        print("\nNumber 7: You are The Seeker\n"
              "Strengths: Deeply creative with a strong and vivid imagination, sevens thrive in "
              "the internal world. \nThey’re able to entertain themselves endlessly and are "
              "rarely bored.\nChallenges: Unsurprisingly, this type can be a bit shy and may have "
              "a hard time connecting with other \npeople. They may also have a hard time relaxing,"
              " moving constantly between work and constructive hobby.")
    elif life_path == '8':
        print("\nNumber 8: You are The Powerhouse\n"
              "Strengths: Eights are good with money, aware of its omnipresence from a"
              " very young age. They’re ambitious \n"
              "and willing to work hard to be self-sufficient and comfortable.\n"
              "Challenges: This type’s skill with money means they might be susceptible"
              " to gifters, whether \n"
              "professionally or personally. They’re also at risk of becoming workaholics.")
    elif life_path == '9':
        print("\nNumber 9: You are The Humanitarian\n"
              "Strengths: Nines are idealistic and deeply principled, unwilling to"
              " compromise their values in favor of \n"
              "convenience. They tend to be stylish, agreeable, and generous.\n"
              "Challenges: This type risks codependency in personal relationships and "
              "may have trouble enjoying the\n"
              "present rather than focusing so heavily on their dreams for the future.")
    else:
        print("I don't know who you are!")
    return life_path


def heart_desire_no(string_name):
    """
    Heart desire number is calculated by adding the corresponding
    digits in the name of a user
    """
    if type(string_name) not in [str]:
        raise TypeError ("The NAME must be a string")
    string_name = string_name.upper()
    # pylint: disable=line-too-long
    calc_table = {'A': 1, 'J': 1, 'S': 1, 'B': 2, 'K': 2, 'T': 2,  'C': 3,  'L': 3, 'U': 3, 'D': 4, 'M': 4, 'V': 4,
                  'E': 5, 'N': 5, 'W': 5, 'F': 6, 'O': 6, 'X': 6, 'G': 7, 'P': 7, 'Y': 7, 'H': 8, 'Q': 8, 'Z': 8,
                  'I': 9, 'R': 9, ' ': 0}
    name = list(string_name)
    total = 0
    for letter in name:
        value = calc_table[letter]
        total += value
    if total <= 9 or total == 11 or total == 22:
        total = str(total)
    else:
        total = str((total - 1) % 9 + 1 if total > 0 else 0)
    if total == '1':
        print("\nYour Hear desire number is 1.\n"
              "The desire of a number one is to express their individual visions and ideas to the world. These people are\n"
              "highly motivated and driven and enjoy thinking “ outside the box”. The numbers one’s are also driven and\n"
              "competitive, especially when they honestly feel passionate about someone or something. They are incredibly\n"
              "strong-willed, yet need to be mindful as they can become narrow-minded and stubborn. If you have a Heart’s\n"
              "Desire Number 1 your purpose for your soul in this life to learn about how to take the creative and \n"
              "individual ideas that you have and then integrate these into the life that you are living. Your character\n"
              "is also known as a “ mover and shaker” and you prefer to lead rather than follow.")
    elif total == '2':
        print("\nYour Hear desire number is 2.\n"
              "People under Heart Desire Number 2 have a desire to work and connect with others to create and leave an\n"
              "impact on others and our world. These people are extremely in-tune with what others need and find it easy\n"
              "to adapt to different situations and people. The number two also finds it easy to get along with just \n"
              "about everyone. These people have a compassionate, intuitive, and caring nature. The two’s sometimes need \n"
              "to ensure that they do not let others take advantage of them. If you are a two, you can be susceptible to \n"
              "overthinking or overly sensitive. Your purpose for this life has to do with learning the best way to work \n"
              "with others in order to create the best things when it comes to the overall greater good.")
    elif total == '3':
        print("\nYour Hear desire number is 3.\n"
              "The number three’s have the desires to express themselves through their passions, their creativity and \n"
              "what they stand for. These people are very positive and usually, have a very active social life. These \n"
              "people also have deep emotions and thoughts and finding the right outlet will always be beneficial for \n"
              "this personality type. The threes tend to be driven when they feel inspired, yet in some instances, their \n"
              "energy can become scattered, and this is when they find it challenging to remain directed. One of the \n"
              "purposes of the three’s is to express their emotions through work and personal relationships.")
    elif total == '4':
        print("\nYour Hear desire number is 4.\n"
              "The desire of the number four is to seek stability and grounded-ness, in order to bring their visions and\n"
              "goals to life. These people are thoughtful and logical souls that are on this earth to create order and\n"
              "structure. These people are very responsible, organized and do very well in the jobs that provide a way \n"
              "for them to manage people. While four might be fantastic when it comes to managing others, they often \n"
              "neglect their own lives. This can result in limitations, which leads to stagnation. The purpose of a 4 in \n"
              "this life is to learn how to become more open-minded when it comes to new opportunities and possibilities \n"
              "& at the same time staying grounded. In this way, the fours can leave a lasting impression on this world.")
    elif total == '5':
        print("\nYour Hear desire number is 5.\n"
              "If you are a number five, you love adventure in every aspect of your life. You are always yearning for\n"
              "excitement and freedom. You do not enjoy routines for very long, and you continuously need change to make\n"
              "sure you stay interested. The fives are versatile, adaptable, and have active imaginations. This is a \n"
              "trait that makes these people highly creative and fast, thinkers. The fives can struggle when it comes to \n"
              "responsibility along with order, yet when you learn to understand this characteristic about yourself, this\n"
              "will help you immensely along your journey. Your purpose while on this earth involves learning to find the\n"
              "freedom you crave through the things you are committed to.")
    elif total == '6':
        print("\nYour Hear desire number is 6.\n"
              "The goal of a number six is to continually serve and help others. These people will always think about\n"
              "others before they will think about themselves. However, without enough balance, this could quickly become\n"
              "detrimental to the well-being and health of a number six. While the number 6 Heart Desire number is\n"
              "considerate and caring of others, it is essential that these individuals first learn to be kind and caring\n"
              "to themselves. The six is sympathetic and generous towards others, yet in some instances, the number six \n"
              "can become overly involved when it comes to the problems of others. If you are a six, you are probably\n"
              "very protective over others, and at times you are also very headstrong. Your purpose for this life \n"
              "involves learning how you can heal or help others by first healing and improving yourself. Once you take\n"
              "care of your own needs, you will become a far more powerful healer.")
    elif total == '7':
        print("\nYour Hear desire number is 7.\n"
              "The number seven Heart’s Desire is associated with people who are always striving to gain more knowledge \n"
              "and wisdom. If you are a seven, you probably enjoy learning, and reading and you will most likely still\n"
              "be one of those life-long students. The seven’s enjoy sharing their knowledge and teaching others. \n"
              "The seven’s also have a very sharp and active mind and they are usually highly intelligent. However, this \n"
              "strong mind might become detrimental when it leads to overthinking, obsessing, stress and anxiety. It may\n"
              "also make these people withdrawn. Learning how to tame the thoughts in your mind using techniques such as \n"
              "meditation can be extremely beneficial to you. The purpose of the number seven’s is to gain knowledge and \n"
              "wisdom, yet also to be an involved part of this world.")
    elif total == '8':
        print("\nYour Hear desire number is 8.\n"
              "The desire of the number eight’s is to obtain power in order to uplift themselves and others. These people\n"
              "have powerful ambition and drive and enjoy being in the limelight. If you are an 8, you probably enjoy\n"
              "leading others, and you are very focused when it comes to achieving goals. When you are balanced, you have\n"
              "the ability to go very far along with becoming one of those inspiring leaders. However, when you are off\n"
              "balance, you may become dominating or materialistic. When you learn how to become humble and to avoid\n"
              "competing with others, your life purpose will become very apparent. Your goal for this life is to guide \n"
              "and lead others with an open mind and a generous heart.")
    elif total == '9':
        print("\nYour Hear desire number is 9.\n"
              "The people with a Heart’s Desire Number 9 have a strong urge to protect our environment and to service\n"
              "people that are in need. These people are drawn to causes such as protecting Mother Earth and animals.\n"
              "They are also very compassionate and intuitive towards others and are at their happiest when they are of\n"
              "service to people in need. The nine’s have a strong desire to gain an understanding of humanity on the \n"
              "larger scales and are usually drawn to finding out more about different religions and cultures. While \n"
              "the nines are incredibly giving, they need to stay focused on not becoming narrow-minded or overly \n"
              "righteous when it comes to their beliefs. The purpose of the nine is to use their talents and skills to \n"
              "care for people and help heal our planet.")
    elif total == '11':
        print("\nYour Hear desire number is 11.\n"
              "The desire of a number 11 is to advance in this life spiritually to obtain an understanding that is deeper\n"
              "about themselves and the world that they live in. These people are highly in-tune with other people, and\n"
              "some even hold intuitive or psychic gifts. They are compassionate souls and can often feel what emotions\n"
              "others are going through. When out of balance this extremely high awareness level can easily manifest into\n"
              "anxiety or nervousness. The eleven’s love working with people and collaborating ideas to bring goals and\n"
              "plans to fruition. The eleven is usually drawn to sharing the information they have on religion and\n"
              "spirituality, yet they need to take care that they do not push or force the beliefs they have onto others.\n"
              "The purpose of the number 11 is to assist others through their advancements on a spiritual level.\n")
    elif total == '22':
        print("\nYour Hear desire number is 22.\n"
              "The desire of the number 22 is to guide and teach others to become the best versions of themselves. These\n"
              "people are highly intelligent and often look for comfort and stability in every aspect of their lives.\n"
              " When they feel confident or comfortable with specific areas in their life, they become more open to \n"
              "passing on this knowledge to others. They have strong foresight and intuition, which makes these people \n"
              "outstanding managers and leaders. When out of balance number 22 can become stubborn or dominating about \n"
              "their ideas. The purpose of the number 22 is to guide and teach others how to create a more loving and \n"
              "tolerant world.")
    else:
        print("\nI don't know who you are!")
    return total


# Enter your Name and Birthday details
print("Enter your date of Birth (DDMMYYYY): ")
birth_date = int(input())

print("Enter your full name: ")
YOUR_NAME = str(input())

with open('output.txt', 'w+') as f:
    f.write('________________________________Numerology Report of ' + YOUR_NAME.upper() +
            ' ________________________________\n\n')
    f.write('Your Life Path number is ' + str(life_path_no(birth_date)) + '.\n')
    f.write('Your Heart Desire number is ' + str(heart_desire_no(YOUR_NAME)) + '.\n')
