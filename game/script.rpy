# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image side eileen happy = "fun_sad.png"
image side eileen = "side_eileen.png"



define us = Character("amanda", image="eileen")
define tm = Character("team members")
define tl = Character("jhon")
define alien = Character("cthulhi")

define us = Character("amanda")
define india = Character("linda")
define thai = Character("Somchai")
define france = Character("oliver")

# The game starts here.

label start:

    scene bg room
    show fun sad
    alien "hi iam Cthulhi from planet B-569 i am here to study humans and their culture"
    show fun sad
    alien "you guys don't fear iam good"
    tm "how did you know we are here"
    show fun sad
    alien "we got an signal from this spaceship"
    tl "ok"
    show fun sad
    alien "where are you guys from"
    india"i am Linda and iam from india"
    us "iam Amanda iam from states"
    thai "iam Somchai iam from thailand"
    france "i am Oliver from france"
    jump select

label select:
    #select the story you want
menu:
    "select any one country"

    "india":
        india"i will tell about my country"
        jump india
    "france.":
        jump france

        france"i will tell about my country."
    "united states":
        jump france

        us"i will tell about my country."
    "thailand":
        jump thailand

        thai"i will tell about my country."


label india:
    
    india "Indian culture is the heritage of social norms, ethical values, traditional customs, belief systems,
    political systems, artifacts and technologies that originated in or are associated with the Indian 
    subcontinent"
    india "The term also applies beyond India to countries and cultures whose histories are strongly 
    connected to India by immigration, "
    india "colonization, or influence, particularly in South Asia and 
    Southeast Asia. India's languages, religions, dance, music, architecture, food and customs differ 
    from place to place within the country."
    india "Indian culture, often labelled as a combination of several cultures, has been influenced 
    by a history that is several millennia old, beginning with the Indus Valley Civilization."
    india "Many elements of Indian culture, such as Indian religions, mathematics, philosophy, cuisine, 
    languages, dance, music and movies have had a profound impact across the Indosphere, Greater 
    India and the world."



    jump select

label united_states:
    
    tl "you will be getting to know most of mystery"
    "ok lets move on with story"

    jump select

label france:
    
    france "The culture of France has been shaped by geography, by historical events, and by foreign and internal
    forces and groups. France, and in particular Paris, has played an important role as a center of high 
    culture since the 17th century and from the 19th century on, worldwide"
    france "From the late 19th century, France has also played an important role in cinema, fashion, cuisine, literature, technology, the social sciences, and mathematics. "
    france "The importance of French culture has waxed and waned over the centuries, depending on its economic, political and military importance."
    france "French culture today is marked both by great regional and socioeconomic differences and strong unifying tendencies."



    jump select

label thailand:
    
    thai "The culture of Thailand has evolved greatly over time, from its relative isolation during 
    the Sukhothai era, to its more contemporary Ayutthaya era, which absorbed influences from all over Asia."
    thai " Limited Indian, Chinese, Burmese, Khmer and other Southeast Asian influences are still evident in traditional Thai culture"
    thai"Buddhism, Animism and Westernization also play a significant role in shaping the modern culture."
    thai "Present day Thailand has a culture that is a combination of various local rituals from different parts of the country,
    along with Buddhist values and oriental trends like in many parts of Asia. "
    thai "The monarchy and royal institutions of Chakri dynasty remain highly revered according to original 
    Siamese culture, whereas "
    thai "societal values in Thailand tend to be more collectivist and religiously secular
    than in other Southeast Asian cultures which have undergone influences from western colonization."

    jump select


    # This ends the game.

    return
