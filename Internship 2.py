def count_words(text):
    """
    This function takes a string of text and returns the number of words in it.
    """
    # We split the text by spaces, which separates the words into a list
    words = text.split()
    # The number of elements in the list is the number of words
    return len(words)

def main():
    """
    The main function that runs the Word Counter program.
    It asks the user to input a sentence or paragraph and then tells them how many words are in the text.
    """
    print("Welcome to the Word Counter Program!")
    
    # We'll keep running the program until the user decides to quit
    while True:
        try:
            # Prompt the user for input
            user_input = input("Please enter a sentence or paragraph (or type 'exit' to quit): ")
            
            # Check if the user wants to exit
            if user_input.lower() == 'exit':
                print("Thanks for using the Word Counter Program. Goodbye!")
                break
            
            # If the input is empty or just spaces, we'll ask the user to try again
            if not user_input.strip():
                print("Oops! It looks like you didn't enter anything. Please try again.")
                continue
            
            # We use the count_words function to find out how many words the user entered
            word_count = count_words(user_input)
            
            # Display the result to the user
            print(f"There are {word_count} words in the text you entered.")
        
        except Exception as e:
            # If something unexpected happens, we'll let the user know
            print(f"An error occurred: {e}")

# This is where the program starts
if __name__ == "__main__":
    main()
