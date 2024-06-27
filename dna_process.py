"""
9.1PP Divide and Conquer - DNA Processing
"""
__author__ = "ZUBAIR AHMED"

import dna_implement as di

def choice_1(cleaned_sequence: str):
    """ Displays the cleaned DNA sequence and its complement """
    complement = di.generate_complement(cleaned_sequence)
    print(cleaned_sequence)
    print('|' * len(cleaned_sequence))
    print(complement)

def choice_3(cleaned_sequence: str):
    """ Transcribes and prints the entire cleaned DNA sequence to mRNA """
    mrna = di.transcribe_sequence(cleaned_sequence)
    print(f"After Transcribing the entire sequence: {mrna}")

def choice_4(cleaned_sequence: str):
    """ Transcribes and prints a specified section of the cleaned DNA sequence to mRNA """
    start = int(input("Enter start position: "))
    length = int(input("Enter length of section: "))
    mrna_section = di.transcribe_section(cleaned_sequence, start, length)
    print(f"After Transcribing a section of the sequence: {mrna_section}")

def display_menu():
    """ User Interface Module """
    print("1. Display the sequence with its complement")
    print("2. Display the error rate")
    print("3. Transcribe the entire sequence")
    print("4. Transcribe a section of the sequence")
    print("5. Splice another sequence onto the end")
    print("6. Quit")
    print("DNA Processor")

def input_functions() -> tuple[str, float]:
    """ Taking inputs for the cleaned sequence and error rate """
    cleaned_sequence = di.clean_sequence(input("Enter a DNA sequence: ")) 
    error_rate = di.calculate_error_rate(cleaned_sequence)
    print(f"Error rate: {error_rate}%")
    return cleaned_sequence, error_rate

def input_while(cleaned_sequence: str, error_rate: float):
    """ Taking input choices for the while loop """
    choice = ""
    while choice != "6":
        print(f"\nWorking sequence: {cleaned_sequence}")
        display_menu()
        
        choice = input("Select an option: ")
        if choice == "1":
            choice_1(cleaned_sequence)  
        elif choice == "2":
            print(f"Error rate: {error_rate}%")
        elif choice == "3":
            choice_3(cleaned_sequence)
        elif choice == "4":
            choice_4(cleaned_sequence)
        elif choice == "5":
            addition = input("Enter another DNA sequence to splice: ")
            cleaned_sequence = di.splice_sequence(cleaned_sequence, addition)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")

def main():
    cleaned_sequence, error_rate = input_functions()
    input_while(cleaned_sequence, error_rate)

if __name__ == "__main__":
    main()
