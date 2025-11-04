"""Random choice picker - selects from options 11 times then announces winner"""
import random

def choose(options):
    """Make a choice from given options (runs 11 rounds + winner)"""
    print(f"Options: {', '.join(options)}")
    print("\nRunning selection 11 times...\n")
    
    for i in range(1, 12):
        choice = random.choice(options)
        print(f"Round {i}: {choice}")
    
    final_choice = random.choice(options)
    print(f"\n🏆 WINNER: {final_choice}")