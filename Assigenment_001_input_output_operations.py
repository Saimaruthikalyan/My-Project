##-------------------------------------------------------------------------
##------M.Sai Maruthi Kalyan ------8142356248 -----------------------------
##-------------------------------------------------------------------------
##                       Input-Output Functions
##-------------------------------------------------------------------------
##  1. Ask for your name and print it.

name=input('Enter your name:- ')
print(name)

##  2. Ask for your favourite colour and print it with a message.OUR

name=input('Enter your name:- ')
color=input('YOUR FAVOURITE COLOR :- ')
print(f"{name} YOUR FAVOURITE COLOR IS {color}")

##  3. Input your age and print: "You are [age] years old."

age=int(input('ENTER YOUR AGE:- '))
print(f"YOUR ARE {age} YEARS OLD")

##  4. Ask for your city and print: "[City] is a beautiful place!"

city=input('ENTER YOUR CITY NAME:- ')
print(f"{city} is a beautiful place")

##  5. Input your favourite food and print it 3 times.

food=input('your favourite food:- ')
print(food*3)
print(food,' ',food,' ',food)

##  6. Take input for your favourite animal and print it in all caps.

animal=input('ENTER YOUR FAVOURITE ANIMAL:- ')
print(animal.upper())

##  7. Ask for your hobby and print it in quotes.

hobby=input('enter your hobby:- ')
print(f"'{hobby}'")

##  8. Ask for your best friend's name and print: "[Name] is your best friend."

name=input("your best friend's name:- ")
print(f"{name} is your best friend.")

##  9. Input a random word and print its length using len().

word=input('enter a random word:- ')
print(len(word))

##  10. Ask for your dream country and print: "You want to visit [country]."

country=input('your dream country:- ')
print(f"you want to visit {country}")

##  11. Ask the user to input a number and print it.

num=int(input('enter a number:- '))
print(num)

##  12. Input two numbers and print them on the same line.

num1=int(input('enter first number:- '))
num2=int(input('enter second number:- '))
print(num1,num2,sep=',')

##  13. Ask for a name and print it with a smiley emoji.

name=input('enter your name:- ')
print(f"{name} 😊")

##  14. Input a movie title and print it with "I love this movie!"

movie=input('enter movie title:- ')
print(f'{movie} "I Love this movie!"')

##  15. Ask for your favourite game and print it with a emoji.

game=input('your favourite game:- ')
print(f"{game} 😍")

##  16. Ask for your favourite season and print it in uppercase.

season= input('your favourite season:- ')
print(season.upper())

##  17. Input a book name and print it inside asterisks: ***Book Name***

book=input('enter a book name:- ')
print(f"***{book}***")

##  18. Ask for your height and print: "You are [height] сm tall."

height=float(input('enter your height in cm:- '))
print(f"you are {height} cm tall")

##  19. Input your birth month and print it in lowercase.

month=input('enter your birth month:- ')
print(month.lower())

##  20. Ask for your favorite sport and print: "Let's play [sport]!n

sport=input('enter your favourite sport:- ')
print(f" Let's play {sport}!")

##  21. Ask for your favorite song and print: "Now playing: [song]"

song=input('enter your favourite song:- ')
print(f"Now playing: {song}")

##  22. Input a message and print it in the title case.

message=input('enter a message:- ')
print(message.title())

##  23. Ask for a fruit name and print: "You chose [fruit]."

fruit=input('enter fruit name:- ')
print(f"you choose {fruit}.")

##  24. Input a place and print it centered with dashes on both sides.

place=input('enter place:- ')
print(place.center(30,'-'))

##  25. Ask for your favorite app and print it with a phone emoji.

app=input('enter your favourite app:- ')
print(f"{app} 📱")

##  26. Input a quote and print it with quotation marks.

quote=input('enter a quote:- ')
print(f'"{quote}"')

##  27. Ask for a car brand and print: "[brand] is a nice car."

brand=input('car brand:- ')
print(f"{brand} is a nice car")

##  28. Ask for your nickname and print it reversed.

nickname=input('enter your nickname:- ')
print(''.join(reversed(nickname)))

##  29. Input your favorite subject and print: "Subject: [subject]"

subject=input('enter your favourite subject:- ')
print(f'"subject: {subject}"')

##  30. Ask for a number and print it 5 times in a row.

num=int(input('enter a number:- '))
for i in range(1,5+1):
    print(num)

##  31. Input your lucky number and print: "Lucky number: [num]"

num=int(input('enter your luckey number:- '))
print(f"LUCKEY NUMBER: [{num}]")

##  32. Ask for your school name and print it with a heart emoji.

school=input('enter your school name:- ')
print(f"{school} ❤️!")

##  33. Input your favorite drink and print: "Cheers to [drink]!"

drink=input('enter your favorite drink:- ')
print(f'"cheers to {drink}!')

##  34. Ask for your email and print: "Your email is: [email]"

email=input('enter your email:- ')
print(f'"your email is : {email}"')

##  35. Ask for a favorite emoji and print it 10 times.

emoji=input('your favorite emoji:- ')
for i in range(1,10+1):
    print(emoji)

##  36. Input your favorite day of the week and print it with stars around it.

day=input('enter your favorite day:- ')
print('*'*20)
print(day.center(20,'*'))
print('*'*20)

##  37. Ask for your favorite ice cream flavor and print it in uppercase.

ice=inpur('enter your favorite ice cream:- ')
print(ice.upper())

##  38. Ask for a number and print it squared (no logic, use **2).

num=int(input('enter a number:- '))
print(num**2)

##  39. Ask for your favorite superhero and print: "[Hero] to the rescue!"

hero=input('enter a favorite superhero:- ').upper()
print(f'"{hero} to the rescue!"')

##  40. Input your favorite dessert and print: "Mmm... [dessert]"

dessert=input('enter a favorite dessert:- ').upper()
print(f'"Mmm...{dessert}"')

##  41. Ask for the name of a festival and print a greeting using it.

festival = input('enter a festival:- ')
print(f'Happy {festival} vides')

##  42. Input a website name and print: "Browsing [site]..."

web=input('enter a website name:- ')
print(f'"Browsing {web}..."')

##  43. Ask for your favorite number and print: "You picked [number]!"

num=int(input('enter a favorite number:- '))
print(f'"you picked {num}!"')

##  44. Input a flower name and print: "[Flower] is beautiful."

flower=input('enter a flower name:- ')
print(f'"{flower} is Beautiful."')

##  45. Ask for the name of your pet and print it with a paw emoji.

pet=input('enter your are pet name:- ')
print(f'{pet}🐾')

##  46. Input your favorite clothing brand and print: "Wearing [brand] today."

brand=input('Enter your favorite clothing brand:-  ')
print(f'"Wearing {brand} Today."')

##  47. Ask for a language you want to learn and print it with a globe emoji.

lang=input('enter your language:- ')
print(f'{lang}🌏')

##  48. Input a message and print it between two lines of dashes.

message=input('enter a message:- ')
print(f'--{message}--')

##  49. Ask for your favorite festival food and print it with a plate emoji.

food=input('enter your favorite festival food:- ')
print(f'{food}🌏')

##  50. Ask for your favorite artist or singer and print: "Listening to [artist]"

singer=input('enter your favorite artist or singer:- ')
print(f'Listening to {singer}')

##  51. Ask for a color and print it three times separated by commas.

color=input('enter a color:- ')
print(color,color,color,sep=',')

##  52. Input a shape and print it with a fun message.

shape=input('enter a shape:- ')
print(f'{shape} is funny ')

##  53. Ask for a brand of phone and print: "[brand] user detected"

brand=input('enter a brand of phone:- ')
print(f'{brand} user detected')

##  54. Input your favourite YouTuber and print: "Subscribed to [name]!

youtuber=input('enter your favourite youtuber:- ')
print(f'Subscribed to {youtuber}')

##  55. Ask for your favourite holiday destination and print it in the title case.

destination=input('enter your favourite destination:- ').title()
print(destination)

##  56. Ask for a favourite app and print it repeated with slashes in between.

app=input('enter a favourite app:- ')
print(app,app,app,sep='/')


##  57. Ask for your favourite snack and print: "Snack time: [snack] "

snack=input('enter your favourite snack:- ')
print(f'"Snack time: {snack}"')

##  58. Input a day and print: "Today is [day]."

day = input('enter day:- ').title()
print(f'Today is {day}')

##  59. Ask for a cartoon character and print it with a playful message.

cartoon = input('enter your fav cartoon:- ')
print(f'{cartoon} make myday funny and joy!')

##  60. Input your favourite animal and print it three times on new lines.

animal=input('enter your favourite animal:- ')
print( animal,'\n' ,animal,'\n' ,animal,sep='')

##  61. Ask for your birth year and print: "You were born in [year]."

year=int(input('enter your birth year:- '))
print(f'You were born in {year}.')

##  62. Ask for your current mood and print it with an emoji.

mood=input('enter your current mood :- ')
print(f'you are {mood}😊')

##  63. Input a favourite word and print it in reverse with spaces.

word=input('your favourite word:- ')
print(' '.join(word[::-1]))

##  64. Ask for your favourite number and print it as part of a sentence.

num=int(input('enter your favourite number? :'))
print(f'your are favourite number is {num}')

##  65. Input a number and print it as part of a math-looking output (e.g. "5 + 5 = 10").

num=int(input('enter a number: '))
print(f'"{num/2} + {num/2} = {num}"')

##  66. Ask for your favourite social media platform and print a short caption.

media=input('enter your favourite social media : ')
print(f'"{media[:4:]}"')

##  67. Input a word and print it with each character separated by a space.

word=input('enter a word :- ')
print(' '.join(word))

##  68. Ask for your favourite series or TV show and print it with popcorn emoji.

ss=input('enter your favourite series or TV show :- ')
print(f'{ss} 🍿')

##  69. Input a text and print it inside a box made of *.

text=input('enter a text :- ')
print((len(text)+4) * '*')
print(f'* {text} *')
print((len(text)+4) * '*')

##  70. Ask for a thing you're grateful for and print a thankful message.

inp=input("enter a thing you're grateful : ")
print(f"thank you  for sharing you're grateful {inp} ,its wonderful moment in your life.")

##  71. Ask for your dream job and print: "Future [job] in progress!"

job= input('enter a your Dream Job : ')
print(f'"Future {job} in progress!"')

##  72. Input your favourite animal and print it followed by 5 paw prints.

animal=input('enter your favourite animal: ')
print(f'{animal} 🐾🐾🐾🐾🐾.!')

##  73. Ask for your favourite author and print a book quote-style message.

author=input('enter your favourite author:- ')
print(f'{author} is very famous person and very well known author. his books was fantistic.')

##  74. Input your favourite pizza topping and print it in all lowercase.

pizza=input('enter your favourite pizza topping : ')
print(pizza.lower())

##  75. Ask for your lucky charm and print: "[charm] is lucky for you"

charm=input('enter your lucky charm : ')
print(f'"{charm} is lucky for you."')

##  76. Ask the user to input their favourite tech gadget and print it with sparkles.

gadget=input('enter your favourite tech gadget : ')
print(f'✨{gadget}✨')

##  77. Input your current city and print it with a location pin emoji.

city=input('enter your current city :- ')
print(f'{city}📍')

##  78. Ask for your favourite beach or hill station and print a travel slogan.

place=input('enter your favourite beach or hill station : ')
print(f'"{place} - Adventure is calling. Will you answer?"')

##  79. Ask for a place you want to visit and print it inside a hashtag (e.g. #Paris).

place=input('enter a place you want to visit : ')
print(f'#{place}')

##  80. Input your favourite clothing item and print a fashion message.

cloths=input('enter your favourite clothing : ')
print(f'"{cloths}" in this style you are good try it go ahead.')

##  81. Input your favourite car and print it with speed linesOD.

car=input('enter your favourite car : ')
print(f'{car} with speed lines 100.')

##  82. Ask what you're currently listening to and print it with a speaker emoji.

listenging=input("enter you're currently listening : ")
print(f'{listenging}🔊')

##  83. Ask for your favourite childhood toy and print a nostalgic message.

toy=input('enter your favourite childhood toy : ')
print(f'{toy} is a nostalgic.')

##  84. Input your favourite planet and print it with a space emoji.

planet=input('enter your favourite planet : ')
print(f'{planet}🌌')

##  85. Ask for your favourite day and print a countdown message.                         ????????

day=input('enter your favourite day : ')
today= input('enter current day : ')
a={'monday':1,
  'tuesday':2,
  'wednesday':3,
  'thusday':4,
  'friday':5,
  'saturday':6,
  'sunday':7}
print(f'{day}- {(a[today]-a[day])%7} days to go.')

##  86. Ask for your favourite weather and print a sentence with a weather emoji.

weather=input('enter your favourite weather: ')
print(f'{weather} 🌡️')

##  87. Input a favourite scent and print a perfume ad-style sentence.

scent=input('enter your favourite scent: ')
print(f'{scent} perfume is perfect for you.')

##  88. Ask for your birthdate and print it in dd-mm-yyyy format.                       ??????????

date=input('enter you birth date in dd-mm-yyyy formate: ')
print(date)

##  89. Ask for your current feeling and print it in bold text (use **feeling**).      ?????????

feeling=input('enter your current feeling: ')
print(feeling)

##  90. Ask for your favorite chocolate and print it with hearts and sweet emojis.

chocolate=input('enter your favorite chocolate: ')
print(f'{chocolate} 💕🍫')

##  91. Input a random object around you and print a poetic line using it.

objects=input('enter a random object around you: ')
print(f'{objects} this is not only a {objects}. its a lucky charm for my dreams')

##  92. Ask for a skill you want to learn and print: "Learning [skill] begins today!"

skill=input('enter a skill you want to learn: ')
print(f'"Learning {skill} begins today!"')

##  93. Ask for your favorite meme and print it as a meme caption.                ???????????

meme=input('enter your favorite meme: ')
print(f'{meme}!')

##  94. Input a pet name and print it with hearts and bones.

pet=input('enter pet name: ')
print(f'💕🦴{pet}🦴💕')

##  95. Ask for your favorite online store and print a shipping quote.

store=input('enter your favorite online store: ')
print(f'your order is shipping from {store}')

##  96. Input a number and print a fake lottery ticket with it.

num=int(input('enter a number: '))
print(f'"{num}" it is a fake lottery ticket.')

##  97. Ask for your birthday month and print a zodiac-style greeting.

month=input('enter your birthday month: ').capitalize()
zodiac= {
    "January": "Capricorn",
    "February": "Aquarius",
    "March": "Pisces",
    "April": "Aries",
    "May": "Taurus",
    "June": "Gemini",
    "July": "Cancer",
    "August": "Leo ",
    "September": "Virgo",
    "October": "Libra",
    "November": "Scorpio",
    "December": "Sagittarius"
}
print(f'"{month}" and your zodiac is "{zodiac[month]}".it bring you a bright career and help to achive goals.')

##  98. Input your favorite emoji and print it in a big line.                    ???????

emoji=input('enter your favorite emoji: ')
print(f'|{emoji}|')


##  99. Ask for your favorite drink and print a cool café-style line.

drink=input('enter your favorite drink: ').upper()
print(f'{drink} is chill have it..')

##  100. Ask what you'd do with a million dollars and print a dream line

dream=input('enter what you do with a million dollars : ')
print(f'my dream is to {dream}')

