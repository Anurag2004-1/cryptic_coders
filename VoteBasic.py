import pandas as pd
from pathlib import Path

def vote():
    print("Welcome to the Voting System!")
    

    # Check if the voting record file exists, if not, create it
    voting_record_file = Path("voting_record.xlsx")
    if not voting_record_file.is_file():
        create_voting_record()

    # Load the existing voting record
    voting_record = pd.read_excel("voting_record.xlsx")

    # Display available political parties
    print("\nPolitical Parties:")
    for i, party in enumerate(voting_record.columns[1:], 1):
        print(f"{i}. {party}")

    # Get user vote
    try:
        user_vote = int(input("\nEnter the number corresponding to your chosen political party: "))
        if 1 <= user_vote <= 5:
            party_name = voting_record.columns[user_vote]
            print(f"\nYou voted for {party_name}!")
            
            # Update the voting record
            voting_record[party_name] += 1
            voting_record.to_excel("voting_record.xlsx", index=False)

            print("Thank you for voting!")
        else:
            print("Invalid vote. Please choose a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def create_voting_record():
    # Create an initial voting record with parties and zero votes
    parties = ["Party A", "Party B", "Party C", "Party D", "Party E"]
    voting_record = pd.DataFrame(columns=["Voter ID"] + parties)
    voting_record.to_excel("voting_record.xlsx", index=False)

if __name__ == "__main__":
    vote()
