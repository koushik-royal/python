def check_voting_eligibility(age):
    voting_age = 18
    if age >= voting_age:
        print("You are eligible to vote.")
    else:
        years_left = voting_age - age
        print(f"You are not eligible to vote. You will be eligible in {years_left} years.")

age = int(input("Enter your age: "))
check_voting_eligibility(age)
