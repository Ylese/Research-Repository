adj = ["Geeky", "Nerdy", "Tech-savvy", "Cyber", "Innovative", "Digital", 
"Caffeinated", "Screaming", "Techoholic", "Gigabit", "Futuristic", 
"Cloudy", "Wireless", "Pixelated", "Robotronic", "Artificial", 
"Viral", "Quantum", "Epic", "Databionic"]

noun = ["Banana", "Penguin", "Noodle", "Cupcake", "Bumblebee", "Pickle", 
"Flamingo", "Pancake", "Snickerdoodle", "Cucumber", 
"Wombat", "Marshmallow", "Llama", "Gummy Bear", "Muffin", "Koala", 
"Panda", "Popcorn", "Jigsaw", "Raindrop"]

titles = ["Master of Memes", "Pixel Picasso", "Code Wizard", "Digital Dynamo", 
"Tech Ninja", "Byte Buccaneer", "Debugging Diva", "Chief Emoji Officer", "Virtual Virtuoso", "Data Jedi", "Wi-Fi Whisperer", "Chief Troubleshooting Titan", "Byte-sized Comedian", "Pixel Puncher", "Algorithm Alchemist", "Digital Doodle Dandy", "Error Eradicator", "Byte Blaster", 
"Techie Tinkerer", "Chief of Laughter Loops"]

from random import choice
color = "\033[35m"
res = "\033[0m"
print("Best nickname for you is", color, choice(adj), choice(noun), choice(titles), res)