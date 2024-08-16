def count_words(text):
    words = text.split()
    return len(words)

def main():
    print("Welcome to the Word Counter Program!")
    
    while True:
        try:
           
            user_input = input("Please enter a sentence or paragraph (or type 'exit' to quit): ")
            
            if user_input.lower() == 'exit':
                print("Thanks for using the Word Counter Program. Goodbye!")
                break
            
            if not user_input.strip():
                print("Oops! It looks like you didn't enter anything. Please try again.")
                continue
            
            word_count = count_words(user_input)
            
         
            print(f"There are {word_count} words in the text you entered.")
        
        except Exception as e:
        
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
