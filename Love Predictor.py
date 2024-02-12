import random

def love_predictor(boy_name, girl_name):
    if boy_name.lower().startswith('a') and girl_name.lower().startswith('v'):
        return 100
    else:
        return random.randint(1, 99)

# Example usage:
boy_name = input("Enter the boy's name: ")
girl_name = input("Enter the girl's name: ")

love_score = love_predictor(boy_name, girl_name)
print(f"Love Score: {love_score}")
