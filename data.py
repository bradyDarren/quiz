import requests

parameters = {
    'amount':10,
    'type':'boolean',
}

response = requests.get(url='https://opentdb.com/api.php' , params=parameters)
response.raise_for_status()

question_data = response.json()['results']
# print(question_data)

# question_data = [
#     {"question": "Snail blood is blue.", "answer": "true"},
#     {"question": "An octopus has four hearts.", "answer": "false"},
#     {"question": "Tomatoes were once banned in France.", "answer": "true"},
#     {"question": "A snail can sleep for three years.", "answer": "true"},
#     {"question": "The bumblebee bat is the world's smallest mammal.", "answer": "true"},
#     {"question": "There are 206 bones in the human body at birth.", "answer": "false"},
#     {"question": "A group of flamingos is called a stand.", "answer": "true"},
#     {"question": "Diamonds rain on Saturn.", "answer": "true"},
#     {"question": "Ancient Egyptians used crushed ashes and eggshells as toothpaste.", "answer": "true"},
#     {"question": "The only bird that can fly backwards is the parrot.", "answer": "false"},
#     {"question": "There are 118 elements in the periodic table.", "answer": "true"},
#     {"question": "The skin is the largest organ in the human body.", "answer": "true"},
#     {"question": "The saltwater crocodile has the most powerful bite.", "answer": "true"},
#     {"question": "Hippo milk is pink.", "answer": "true"},
#     {"question": "The average lifespan of a taste bud is 30 to 60 days.", "answer": "false"},
#     {"question": "Laika was the first animal in space.", "answer": "true"},
#     {"question": "Saudi Arabia has no rivers.", "answer": "true"},
#     {"question": "A cockroach can live without its head for a month.", "answer": "false"},
#     {"question": "The Greenland shark is the world's longest-living animal.", "answer": "true"},
#     {"question": "The first video game was Pong.", "answer": "false"},
# ]
