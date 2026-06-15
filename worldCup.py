import csv
import sys
import os

base_directory = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(base_directory, "Team_stats.csv")

# Initialise stats & 3 chance team selection
print("Welcome to the 2026 FIFA World Cup Team Management Simulation!")

selected_team = ""
strength = 0.0
form = 0
injuries = 0

attempts = 0
max_attempts = 3
team_found = False

while attempts < max_attempts:
    remaining = max_attempts - attempts
    print(f"--- Team Selection Phase (Attempts Remaining: {remaining}) ---")
    user_choice = input("Enter a country to manage (e.g., Argentina, Mexico, Japan): ").strip()

    try:
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if row["Team"].lower() == user_choice.lower():
                    selected_team = row["Team"]
                    strength = float(row["Team strength"])
                    form = int(row["Team form"])
                    injuries = int(row["Number of injuries"])
                    team_found = True
                    break  
                    
    except FileNotFoundError:
        print("\nFile not found in this folder!")
        print("Please check file name and try again.")
        sys.exit()

    if team_found:
        print(f"\nAccess Granted! Successfully appointed as manager of {selected_team}!")
        break
        
    attempts += 1
    print("Team not found in the dataset. Please try a different country.\n")

if not team_found:
    print("Too many failed attempts. Shutting down simulation system.")
    sys.exit() 


#The Tournament Loop

stage = "Preparation"

while True:
    print(f"\n-------------------------------------------")
    print(f"CURRENT STAGE: {stage}")
    print(f"Team: {selected_team} | Baseline Strength: {strength:.1f} | Squad Form: {form} | Injured Players: {injuries}")
    print(f"-------------------------------------------")
    
    #Pre-Tournament Preparation ---
    if stage == "Preparation":
        print("\nChoose your weekly tournament strategy:")
        print("1. Rest Day (Reduces squad injuries, but momentum/form drops)")
        print("2. Intense Tactical Training (Boosts team form, but risk of injury)")
        
        action = input("Select strategy (1 or 2): ").strip()
        
        if action == "1":
            print("\nStrategy: Rest Day.")
            print("The squad spent the day in physical recovery. Injury risk minimized!")
            injuries = max(0, injuries - 1)
            form = max(5, form - 1)
            stage = "Group Stage"
            
            continue
            
        elif action == "2":
            print("\nStrategy: Intense Tactical Training.")
            print("High-intensity drills executed perfectly! Team chemistry and form increased.")
            form += 3
            injuries += 1
            stage = "Group Stage"

    #Group stage matches
    elif stage == "Group Stage":
        print(f"\nThe Group Stage matches are underway for {selected_team}...")
        
        pass 
        
        performance_score = strength + (form * 2) - (injuries * 4)
        
        if performance_score > 95:
            print(f"Group Stage Result: Match points calculated... SUCCESS!")
            print(f"{selected_team} finishes top of the group and advances to the Knockout Stages!")
            stage = "Knockouts"
        else:
            print(f"Group Stage Result: Match points calculated... FAILURE.")
            print(f"{selected_team} has been eliminated from the World Cup. You have been dismissed as manager.")
            break

    #The knockout stages and finals
    elif stage == "Knockouts":
        print(f"\nWelcome to the Knockout Rounds! One loss means your team goes home.")
        
        final_championship_score = strength + (form * 2) - (injuries * 6)
        
        if final_championship_score > 102:
            print(f"\nCHAMPIONS OF THE WORLD!!!")
            print(f"{selected_team} has won the 2026 FIFA World Cup!")
        else:
            print(f"\nHeartbreak in the Final Stages!")
            print(f"Your team put up a massive fight, but lost a devastating penalty shootout.")
            
        break 