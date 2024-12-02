def expert_system():
    print("Welcome to the Medical Expert System!")
    print("Answer the following questions with 'yes' or 'no'.\n")

    # Initial symptoms
    fever = input("Do you have a fever? ").lower()
    cough = input("Do you have a cough? ").lower()
    sore_throat = input("Do you have a sore throat? ").lower()
    headache = input("Do you have a headache? ").lower()

    # Rules
    if fever == "yes" and cough == "yes" and sore_throat == "yes":
        print("\nDiagnosis: You may have the flu. Please consult a doctor.")
    elif fever == "yes" and headache == "yes":
        print("\nDiagnosis: You may have a viral infection. Stay hydrated and rest.")
    elif cough == "yes" and sore_throat == "yes":
        print("\nDiagnosis: You may have a cold. Drink warm fluids and rest.")
    else:
        print("\nDiagnosis: Symptoms are unclear. Please consult a doctor for a proper diagnosis.")

# Run the expert system
expert_system()


def banking_expert_system():
    print("Welcome to the Banking Expert System!")
    print("Answer the following questions with 'yes' or 'no'.\n")

    # User needs
    open_account = input("Do you want to open a new account? ").lower()
    apply_loan = input("Are you interested in applying for a loan? ").lower()
    credit_card = input("Do you need a credit card? ").lower()
    investment = input("Are you looking for investment options? ").lower()

    # Rules
    if open_account == "yes":
        print("\nSuggestion: Visit your nearest branch or apply online to open a savings or current account.")
    elif apply_loan == "yes":
        print("\nSuggestion: Check your eligibility for a personal loan, home loan, or business loan.")
    elif credit_card == "yes":
        print("\nSuggestion: Explore credit card options like cashback, rewards, or low-interest cards.")
    elif investment == "yes":
        print("\nSuggestion: Consider fixed deposits, mutual funds, or recurring deposit schemes.")
    else:
        print("\nSuggestion: For other queries, contact customer support or visit your bank branch.")

# Run the expert system
banking_expert_system()
