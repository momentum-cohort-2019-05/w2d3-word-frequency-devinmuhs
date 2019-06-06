STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

import re


def print_word_freq(file):
    f = open(file)
    all_the_txt = (f.read())
    lower_case = all_the_txt.lower()
    no_punctuation = re.sub('[^A-Za-z]', ' ', lower_case)
    splitter = no_punctuation.split()

    remove_stop_words = []

    for x in splitter:
        if x not in STOP_WORDS:
            remove_stop_words.append(x)
    print(remove_stop_words)


    word_counter = {}

    for word in remove_stop_words:
        if word not in word_counter:
            word_counter[word]= 1
        else:
            word_counter[word] += 1
    print(word_counter)
    
    """Read in `file` and print out the frequency of words in that file."""
    pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
