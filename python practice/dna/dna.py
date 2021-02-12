from csv import reader
from csv import DictReader
from sys import argv
from cs50 import get_string

# TODO
# Open CSV file and DNA sequence
# Read them into memory.
# f.read(), sys.argv, reader, dict reader

# For each of the STR, return no of consective runs in DNA
# For each position in the DNA sequence, how many times the STR repeats from that position
# For each position keep checking the next substring until it does not repeat (counter)
# find largest counter to know the longest consecutive run.

# Compare CSV DNA STR count with  DNA Sequence
# Save STR counts in some data structure (list, dict) (int(x) returns integer value)
# For each row in data check STR count
# If match return name of person, else return Not found.
def main ():
    if len(argv) != 3:
        print("Error occured")
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # Opening csv database file
    # Put that data into a Dictionary we can call from
    csv_file = open(argv[1])
    data = DictReader(csv_file)

    with open(argv[2]) as dna_file:
        sequence = dna_file.read()

    # curly brackets as we want str_counts to be {value, value, value}
    str_counts = {}

    # subseq is the column of DNA Markers AGAT, using [1:] so we dont take in "Name"
    for subseq_str in data.fieldnames[1:]:
        # function of get_longest_match will find return value of longest match in DNA sequence
        # of specific STR marker
        str_counts[subseq_str] = get_longest_match(sequence, subseq_str)
    # Now we have array of STR counts for each DNA marker
    # We can interate this array through the Database to find a match

    for names in data:
        # If all values of STR counts match integer value of STR database for each column
        # if all(str_counts[columns] == int(names[columns]) for columns in str_counts):
        tmp_count = 0
        for subseq_str in str_counts:
            if str_counts[subseq_str] == int(names[subseq_str]):
                tmp_count += 1
            else:
                break
        if tmp_count == len(str_counts):
            print(names["name"])
            csv_file.close()
            return 0

    print("No match")
    csv_file.close()
    return 1

def get_longest_match(sequence, subseq_str):
    # TODO
    # Variables to get longest chain no, and length of DNA marker
    longest_chain = 0
    str_length = len(subseq_str)

    # Loop for each start letter of the sequence

    for i in range(len(sequence)):

        # Variable to count each length of chain of Marker
        count = 0

        # While loop to find length of each chain for each marker
        while True:
            # Making a DNA market window
            # Start position will be the start of the i
            # End position will be length of DNA marker from start position
            # If match found count 1
            # start position updates to the end of that last marker
            # end will be length of dna marker from new start position
            # If no DNA marker match, break out of while loop
            # start loop again from next letter on
            start = i + str_length * count
            end = start + str_length

            if sequence[start:end] == subseq_str:

                count += 1

            else:

                break

        longest_chain = max(longest_chain, count)

    return longest_chain

main()
