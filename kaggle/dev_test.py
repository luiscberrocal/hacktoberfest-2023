
def parse(sequence_str: str) -> str:
    key_mappings = {
        '0': ' ',
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
    }
    sequences = sequence_str.split(' ')
    s = {}
    v = []
    for seq in sequences:
        for n in seq:
            if s.get(n) is None:
                s[n] = 0
            else:
                s[n] += 1

    print(s)


def text_from_numbers(number_string):
    # Mapping of number to letters
    num_to_letters = {
        '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }

    # Split the input string into chunks (one for each letter)
    chunks = number_string.split()

    # Convert chunks to letters
    message = ""
    for chunk in chunks:
        # The letter is determined by the length of the chunk
        # and the first number in the chunk
        message += num_to_letters[chunk[0]][len(chunk) - 1]

    return message


if __name__ == '__main__':
    test = [
        '44 444',
        '4 2 8 666'
    ]
    t = text_from_numbers(test[1])
    print(t)