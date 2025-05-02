import requests


base_url = 'https://pokeapi.co/api/v2/'

def get_pokemon_data(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response} occurred!")
        print("Please try again!")
        return None

def print_pokemon_data(pokemon_data):
    pokemon_id = pokemon_data["id"]
    pokemon_name = pokemon_data["name"].capitalize()
    pokemon_height = pokemon_data["height"]
    pokemon_weight = pokemon_data["weight"]
    pokemon_types = ", ".join([type['type']['name'].capitalize()for type in pokemon_data["types"]])
    pokemon_abilities = ", ".join([ability["ability"]['name'].capitalize() for ability in pokemon_data["abilities"]])
    pokemon_stats = [(stat['stat']['name'].capitalize() , stat['base_stat']) for stat in pokemon_data["stats"]]
    pokemon_bst = sum(stat[1] for stat in pokemon_stats)
    
    
    print(f"""
    *****************************
             =POKEDEX=     
    *****************************     
          
    Pokedex Num : {pokemon_id}   
    Name        : {pokemon_name}   
    Height      : {pokemon_height*4} inch
    Weight      : {pokemon_weight/10} kg
    
    Types       : {pokemon_types}
    Abilities   : {pokemon_abilities}
    
    Bst ({pokemon_bst}) :-
    
    {pokemon_stats[0][0]} : {pokemon_stats[0][1]}
    {pokemon_stats[1][0]} : {pokemon_stats[1][1]}
    {pokemon_stats[2][0]} : {pokemon_stats[2][1]}
    {pokemon_stats[3][0]} : {pokemon_stats[3][1]}
    {pokemon_stats[4][0]} : {pokemon_stats[4][1]}
    {pokemon_stats[5][0]} : {pokemon_stats[5][1]}
    
    *****************************
                       
    """)

def main():
    while True:
        name = input("\nPlease enter your desired pokemon name or pokedex num : ").strip().lower()
        pokemon_data = get_pokemon_data(name)
        if pokemon_data:
            print_pokemon_data(pokemon_data)
            break
        else:
            continue

if __name__ == "__main__":        
    main()