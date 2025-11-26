##-------------------------------------------------------------------------
##------M.Sai Maruthi Kalyan ------8142356248 -----------------------------
##-------------------------------------------------------------------------
##                       Simple_if Functions
##-------------------------------------------------------------------------
## 1. Ask for your name and print it.
name = input('Enter your name:- ')
if name:
    print(name)

## 2. Ask for your favourite colour and print it with a message.
name = input('Enter your name:- ')
color = input('YOUR FAVOURITE COLOR :- ')
if color:
    print(f"{name} YOUR FAVOURITE COLOR IS {color}")

## 3. Input your age and print: "You are [age] years old."
age = input('ENTER YOUR AGE:- ')
if age:
    print(f"YOU ARE {age} YEARS OLD")

## 4. Ask for your city and print: "[City] is a beautiful place!"
city = input('ENTER YOUR CITY NAME:- ')
if city:
    print(f"{city} is a beautiful place")

## 5. Input your favourite food and print it 3 times.
food = input('your favourite food:- ')
if food:
    print(food*3)
    print(food, food, food)

## 6. Take input for your favourite animal and print it in all caps.
animal = input('ENTER YOUR FAVOURITE ANIMAL:- ')
if animal:
    print(animal.upper())

## 7. Ask for your hobby and print it in quotes.
hobby = input('enter your hobby:- ')
if hobby:
    print(f"'{hobby}'")

## 8. Ask for your best friend's name and print.
friend = input("your best friend's name:- ")
if friend:
    print(f"{friend} is your best friend.")

## 9. Input a random word and print its length.
word = input('enter a random word:- ')
if word:
    print(len(word))

## 10. Ask for your dream country.
country = input('your dream country:- ')
if country:
    print(f"you want to visit {country}")

## 11. Ask the user to input a number and print it.
num = input('enter a number:- ')
if num:
    print(num)

## 12. Input two numbers and print them on the same line.
num1 = input('enter first number:- ')
num2 = input('enter second number:- ')
if num1 and num2:
    print(num1, num2, sep=',')

## 13. Ask for a name and print it with a smiley emoji.
name = input('enter your name:- ')
if name:
    print(f"{name} 😊")

## 14. Input a movie title.
movie = input('enter movie title:- ')
if movie:
    print(f'{movie} "I Love this movie!"')

## 15. Ask for your favourite game and print it with a emoji.
game = input('your favourite game:- ')
if game:
    print(f"{game} 😍")

## 16. Ask for your favourite season and print it in uppercase.
season = input('your favourite season:- ')
if season:
    print(season.upper())

## 17. Input a book name and print it inside asterisks.
book = input('enter a book name:- ')
if book:
    print(f"***{book}***")

## 18. Ask for your height.
height = input('enter your height in cm:- ')
if height:
    print(f"you are {height} cm tall")

## 19. Input your birth month.
month = input('enter your birth month:- ')
if month:
    print(month.lower())

## 20. Ask for your favorite sport.
sport = input('enter your favourite sport:- ')
if sport:
    print(f" Let's play {sport}!")

## 21. Ask for your favorite song.
song = input('enter your favourite song:- ')
if song:
    print(f"Now playing: {song}")

## 22. Input a message and print it in the title case.
message = input('enter a message:- ')
if message:
    print(message.title())

## 23. Ask for a fruit name.
fruit = input('enter fruit name:- ')
if fruit:
    print(f"you choose {fruit}.")

## 24. Input a place and print it centered with dashes.
place = input('enter place:- ')
if place:
    print(place.center(30,'-'))

## 25. Ask for your favorite app.
app = input('enter your favourite app:- ')
if app:
    print(f"{app} 📱")

## 26. Input a quote.
quote = input('enter a quote:- ')
if quote:
    print(f'"{quote}"')

## 27. Ask for a car brand.
brand = input('car brand:- ')
if brand:
    print(f"{brand} is a nice car")

## 28. Ask for your nickname.
nickname = input('enter your nickname:- ')
if nickname:
    print(''.join(reversed(nickname)))

## 29. Input your favorite subject.
subject = input('enter your favourite subject:- ')
if subject:
    print(f"Subject: {subject}")

## 30. Ask for a number and print it 5 times.
num = input('enter a number:- ')
if num:
    for i in range(5):
        print(num)

## 31. Input your lucky number.
num = input('enter your luckey number:- ')
if num:
    print(f"LUCKEY NUMBER: [{num}]")

## 32. Ask for your school name.
school = input('enter your school name:- ')
if school:
    print(f"{school} ❤️!")

## 33. Input your favorite drink.
drink = input('enter your favorite drink:- ')
if drink:
    print(f"Cheers to {drink}!")

## 34. Ask for your email.
email = input('enter your email:- ')
if email:
    print(f"Your email is: {email}")

## 35. Ask for a favorite emoji.
emoji = input('your favorite emoji:- ')
if emoji:
    for i in range(10):
        print(emoji)

## 36. Input your favorite day.
day = input('enter your favorite day:- ')
if day:
    print('*'*20)
    print(day.center(20,'*'))
    print('*'*20)

## 37. Ask for your favorite ice cream flavor.
ice = input('enter your favorite ice cream:- ')
if ice:
    print(ice.upper())

## 38. Ask for a number squared.
num = input('enter a number:- ')
if num:
    print(int(num)**2)

## 39. Ask for your favorite superhero.
hero = input('enter a favorite superhero:- ')
if hero:
    print(f"{hero} to the rescue!")

## 40. Input your favorite dessert.
dessert = input('enter a favorite dessert:- ')
if dessert:
    print(f"Mmm... {dessert}")

## 41. Ask for a festival name.
festival = input('enter a festival:- ')
if festival:
    print(f"Happy {festival} wishes")

## 42. Input a website.
web = input('enter a website name:- ')
if web:
    print(f"Browsing {web}...")

## 43. Ask for your favorite number.
num = input('enter a favorite number:- ')
if num:
    print(f"You picked {num}!")

## 44. Input a flower name.
flower = input('enter a flower name:- ')
if flower:
    print(f"{flower} is Beautiful.")

## 45. Ask for pet name.
pet = input('enter your pet name:- ')
if pet:
    print(f"{pet}🐾")

## 46. Input your favorite clothing brand.
brand = input('Enter your favorite clothing brand:- ')
if brand:
    print(f"Wearing {brand} Today.")

## 47. Ask for a language you want to learn.
lang = input('enter your language:- ')
if lang:
    print(f"{lang}🌏")

## 48. Input a message between dashes.
message = input('enter a message:- ')
if message:
    print(f"--{message}--")

## 49. Ask for festival food.
food = input('enter your favorite festival food:- ')
if food:
    print(f"{food} 🍽️")

## 50. Ask for your favorite artist.
singer = input('enter your favorite artist or singer:- ')
if singer:
    print(f"Listening to {singer}")
## 51. Ask for a color and print it three times separated by commas.
color = input('enter a color:- ')
if color:
    print(color, color, color, sep=',')

## 52. Input a shape and print it with a fun message.
shape = input('enter a shape:- ')
if shape:
    print(f"{shape} is funny")

## 53. Ask for a brand of phone.
brand = input('enter a brand of phone:- ')
if brand:
    print(f"{brand} user detected")

## 54. Input your favourite YouTuber.
youtuber = input('enter your favourite youtuber:- ')
if youtuber:
    print(f"Subscribed to {youtuber}!")

## 55. Ask for your favourite holiday destination.
destination = input('enter your favourite destination:- ')
if destination:
    print(destination.title())

## 56. Ask for a favourite app and repeat with slashes.
app = input('enter a favourite app:- ')
if app:
    print(app, app, app, sep='/')

## 57. Ask for your favourite snack.
snack = input('enter your favourite snack:- ')
if snack:
    print(f"Snack time: {snack}")

## 58. Input a day.
day = input('enter day:- ')
if day:
    print(f"Today is {day.title()}")

## 59. Ask for a cartoon character.
cartoon = input('enter your fav cartoon:- ')
if cartoon:
    print(f"{cartoon} makes my day funny and joyful!")

## 60. Input your favourite animal (print 3 times).
animal = input('enter your favourite animal:- ')
if animal:
    print(animal, animal, animal, sep="\n")

## 61. Ask for your birth year.
year = input('enter your birth year:- ')
if year:
    print(f"You were born in {year}.")

## 62. Ask for your current mood.
mood = input('enter your current mood :- ')
if mood:
    print(f"You are {mood} 😊")

## 63. Input a favourite word and print reversed with spaces.
word = input('your favourite word:- ')
if word:
    print(' '.join(word[::-1]))

## 64. Ask for your favourite number.
num = input('enter your favourite number? : ')
if num:
    print(f"Your favourite number is {num}")

## 65. Input a number and print math-like output.
num = input('enter a number: ')
if num:
    n = int(num)
    print(f"{n//2} + {n//2} = {n}")

## 66. Ask for your favourite social media.
media = input('enter your favourite social media : ')
if media:
    print(media[:4])

## 67. Input a word and print chars separated by space.
word = input('enter a word :- ')
if word:
    print(' '.join(word))

## 68. Ask for your favourite series or TV show.
ss = input('enter your favourite series or TV show :- ')
if ss:
    print(f"{ss} 🍿")

## 69. Input text and print in a box of *.
text = input('enter a text :- ')
if text:
    print((len(text)+4) * '*')
    print(f"* {text} *")
    print((len(text)+4) * '*')

## 70. Ask for a thing you're grateful for.
inp = input("enter a thing you're grateful : ")
if inp:
    print(f"Thank you for sharing you're grateful for {inp}, it's a wonderful moment in your life.")

## 71. Ask for your dream job.
job = input('enter your Dream Job : ')
if job:
    print(f"Future {job} in progress!")

## 72. Input favourite animal and print with paw prints.
animal = input('enter your favourite animal: ')
if animal:
    print(f"{animal} 🐾🐾🐾🐾🐾")

## 73. Ask for your favourite author.
author = input('enter your favourite author:- ')
if author:
    print(f"{author} is a very famous and well-known author. Their books are fantastic.")

## 74. Input your favourite pizza topping.
pizza = input('enter your favourite pizza topping : ')
if pizza:
    print(pizza.lower())

## 75. Ask for your lucky charm.
charm = input('enter your lucky charm : ')
if charm:
    print(f"{charm} is lucky for you.")

## 76. Ask for favourite tech gadget.
gadget = input('enter your favourite tech gadget : ')
if gadget:
    print(f"✨{gadget}✨")

## 77. Input your current city.
city = input('enter your current city :- ')
if city:
    print(f"{city}📍")

## 78. Ask for your favourite beach or hill station.
place = input('enter your favourite beach or hill station : ')
if place:
    print(f"{place} - Adventure is calling. Will you answer?")

## 79. Ask for a place you want to visit.
place = input('enter a place you want to visit : ')
if place:
    print(f"#{place}")

## 80. Input your favourite clothing item.
cloths = input('enter your favourite clothing : ')
if cloths:
    print(f"{cloths} - this style looks good, try it!")

## 81. Input your favourite car.
car = input('enter your favourite car : ')
if car:
    print(f"{car} with speed lines 🚗💨")

## 82. Ask what you're currently listening to.
listening = input("enter what you're currently listening : ")
if listening:
    print(f"{listening} 🔊")

## 83. Ask for favourite childhood toy.
toy = input('enter your favourite childhood toy : ')
if toy:
    print(f"{toy} brings back nostalgic memories.")

## 84. Input your favourite planet.
planet = input('enter your favourite planet : ')
if planet:
    print(f"{planet} 🌌")

## 85. Ask for your favourite day and countdown.
day = input('enter your favourite day : ').lower()
today = input('enter current day : ').lower()
days = {'monday':1,'tuesday':2,'wednesday':3,'thursday':4,'friday':5,'saturday':6,'sunday':7}
if day in days and today in days:
    print(f"{day} - {(days[day] - days[today])%7} days to go.")

## 86. Ask for your favourite weather.
weather = input('enter your favourite weather: ')
if weather:
    print(f"{weather} 🌡️")

## 87. Input a favourite scent.
scent = input('enter your favourite scent: ')
if scent:
    print(f"{scent} perfume is perfect for you.")

## 88. Ask for your birthdate.
date = input('enter your birth date in dd-mm-yyyy format: ')
if date:
    print(date)

## 89. Ask for your current feeling.
feeling = input('enter your current feeling: ')
if feeling:
    print(f"**{feeling}**")

## 90. Ask for your favorite chocolate.
chocolate = input('enter your favorite chocolate: ')
if chocolate:
    print(f"{chocolate} 💕🍫")

## 91. Input a random object around you.
objects = input('enter a random object around you: ')
if objects:
    print(f"{objects} is not just an object, it's a lucky charm for my dreams.")

## 92. Ask for a skill you want to learn.
skill = input('enter a skill you want to learn: ')
if skill:
    print(f"Learning {skill} begins today!")

## 93. Ask for your favorite meme.
meme = input('enter your favorite meme: ')
if meme:
    print(f"{meme}!")

## 94. Input a pet name and print it with hearts and bones.
pet = input('enter pet name: ')
if pet:
    print(f"💕🦴{pet}🦴💕")

## 95. Ask for your favorite online store.
store = input('enter your favorite online store: ')
if store:
    print(f"Your order is shipping from {store}")

## 96. Input a number and print a fake lottery ticket.
num = input('enter a number: ')
if num:
    print(f"{num} is your fake lottery ticket.")

## 97. Ask for your birthday month and zodiac.
month = input('enter your birthday month: ').capitalize()
zodiac = {
    "January":"Capricorn","February":"Aquarius","March":"Pisces","April":"Aries",
    "May":"Taurus","June":"Gemini","July":"Cancer","August":"Leo",
    "September":"Virgo","October":"Libra","November":"Scorpio","December":"Sagittarius"
}
if month in zodiac:
    print(f"{month} → Zodiac: {zodiac[month]}")

## 98. Input your favorite emoji.
emoji = input('enter your favorite emoji: ')
if emoji:
    print(f"|{emoji*10}|")

## 99. Ask for your favorite drink.
drink = input('enter your favorite drink: ')
if drink:
    print(f"{drink.upper()} is chill, have it!")

## 100. Ask what you'd do with a million dollars.
dream = input('enter what you do with a million dollars : ')
if dream:
    print(f"My dream is to {dream}")
