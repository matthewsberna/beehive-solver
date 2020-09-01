import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('outer_letters', type=str, help='The letters around the outside of the "hive"')
    parser.add_argument('central_letter', type=str, help='The letter at the center of the "hive"')
    args = parser.parse_args()

    # Compile the set of our letters.
    my_letters = set(args.outer_letters).union(set(args.central_letter))
    print('Our letters:  ' + repr(my_letters))

    # Read the wordlist.
    words_to_check = []
    wordfile_path = os.path.join(os.getcwd(), 'wordlist.txt')
    with open(wordfile_path, 'r') as wordfile:
        lines = wordfile.readlines()
        print('Read {} lines from word list.'.format(len(lines)))
        # Words to check must be at least 4 chars long and must contain the central letter.
        words_to_check = [line.strip() for line in lines if len(line.strip()) >= 4 and args.central_letter in line.strip()]
        print('Found {} words to check.'.format(len(words_to_check)))

    # A word is a valid answer if the set of its letters is a subset of our letters.
    answers = [word for word in words_to_check if set(word) - my_letters == set()]

    # A word is a PANGRAM if it uses all our letters.
    pangrams = [word for word in words_to_check if my_letters == set(word)]

    # Write the solutions file.
    output_path = os.path.join(os.getcwd(), 'solutions.txt')
    with open(output_path, 'w') as solutions_file:
        solutions_file.write('--------------------------------\n')
        solutions_file.write('PANGRAMS\n')
        solutions_file.write('--------------------------------\n')
        for word in pangrams:
            solutions_file.write(word + '\n')
        solutions_file.write('\n')
        solutions_file.write('--------------------------------\n')
        solutions_file.write('All solutions\n')
        solutions_file.write('--------------------------------\n')
        for word in answers:
            solutions_file.write(word + '\n')


if __name__ == '__main__':
    main()