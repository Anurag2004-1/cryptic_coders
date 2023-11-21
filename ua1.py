import pandas as pd

def get_user_input():
    while True:
        try:
            adhar_id = int(input("Enter Aadhar ID: "))
            voter_id = int(input("Enter Voter ID: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return adhar_id, voter_id

def check_aadhar_voter_match(adhar_id, voter_id, dataset):
    # Check if the provided Aadhar ID exists in the dataset
    if adhar_id in dataset['aadhar_id'].values:
        # If Aadhar ID exists, get the corresponding row
        row = dataset[dataset['aadhar_id'] == adhar_id]

        # Check if the provided Voter ID matches the Voter ID in the corresponding row
        if voter_id == row['voter_id'].values[0]:
             ua2()
        else:
            print("Aadhar ID and Voter ID do not match.")
    else:
        print("Aadhar ID not found in the dataset.")

def main():
    try:
       
        file_path = r"C:\Users\ASUS\OneDrive\Desktop\datasets\cc.xlsx"
        dataset = pd.read_excel(file_path)

        adhar_id, voter_id = get_user_input()
        check_aadhar_voter_match(adhar_id, voter_id, dataset)

    except FileNotFoundError:
        print(f"File not found at {file_path}. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()





