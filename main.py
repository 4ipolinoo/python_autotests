import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '6b16274b01487804f8043cd08e8e69c4'
HEADER = {'Content-Type':'application/json', 'trainer_token' : TOKEN}
ID_POKEMONS = '27879'
body_registration = {
    "trainer_token": TOKEN,
    "email": "dmitrystepanishev99@yandex.ru",
    "password": "1157Lbvfffff"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_update = {
    "pokemon_id": ID_POKEMONS,
    "name": "Галонозавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_pokeboll = {
    "pokemon_id": ID_POKEMONS
}
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create) 
print(response_create.status_text)'''

'''response_update = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_update)
print(response_update.text)
'''
response_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeboll)
print(response_pokeboll.text)
