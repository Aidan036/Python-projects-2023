def ask_yes_no(question):
    """ask a yes or no question,"""
    response = None
    while response not in  ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """ask for number within a range"""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it")
    input("\n\nPress the enter key to exit.")