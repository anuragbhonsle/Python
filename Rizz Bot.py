import random

def get_rizz_pickup_line():
    rizz_pickup_lines = [
        "Are you a magician? Because whenever I look at you, everyone else disappears.",
        "Do you have a map? I keep getting lost in your eyes.",
        "Are you a Wi-Fi signal? Because I'm feeling a connection.",
        "Is your name Google? Because you've got everything I've been searching for.",
        "If you were a vegetable, you'd be a cute-cumber!",
        "Are you made of copper and tellurium? Because you’re Cu-Te.",
        "Is this the Hogwarts Express? Because it feels like you and I are headed somewhere magical.",
        "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
        "Excuse me, but I think the stars tonight are outshone by your smile.",
        "If you were a cat, you’d purr-fect.",
    ]

    return random.choice(rizz_pickup_lines)

def main():
    print("Welcome to the Rizz Pickup Lines Box!")
    input("Press Enter to get a Rizz pickup line...")
    
    while True:
        pickup_line = get_rizz_pickup_line()
        print("\nRizz Pickup Line:\n", pickup_line)
        
        another = input("\nWant another Rizz pickup line? (yes/no): ").lower()
        if another != 'yes':
            print("Thanks for using the Rizz Pickup Lines Box. May your lines be smooth and charming!")
            break

if __name__ == "__main__":
    main()