# main funcion
def main():
    # cipher dictionary
    cipher_dict = {
        'A': 'N',
        'B': 'O',
        'C': 'A',
        'D': 'T',
        'E': 'R',
        'F': 'B',
        'G': 'E',
        'H': 'C',
        'I': 'F',
        'J': 'U',
        'K': 'X',
        'L': 'D',
        'M': 'Q',
        'N': 'G',
        'O': 'Y',
        'P': 'L',
        'Q': 'K',
        'R': 'H',
        'S': 'V',
        'T': 'I',
        'U': 'J',
        'V': 'M',
        'W': 'P',
        'X': 'Z',
        'Y': 'S',
        'Z': 'W',
        'a': 'n',
        'b': 'o',
        'c': 'a',
        'd': 't',
        'e': 'r',
        'f': 'b',
        'g': 'e',
        'h': 'c',
        'i': 'f',
        'j': 'u',
        'k': 'x',
        'l': 'd',
        'm': 'q',
        'n': 'g',
        'o': 'y',
        'p': 'l',
        'q': 'k',
        'r': 'h',
        's': 'v',
        't': 'i',
        'u': 'j',
        'v': 'm',
        'w': 'p',
        'x': 'z',
        'y': 's',
        'z': 'w',
    }
    
    # get plain text inputted from user
    plain_text = input("Enter plain text: ")
    
    # store cipher text
    cipher_text = ""
    
    # loop through each letter of 'plain_text' and get the corresponding cipher letter from 'cipher_dict' and append to 'cipher_text'
    for letter in plain_text:
        try:
            cipher_text += cipher_dict[letter]
        except:
            cipher_text += letter
            
    return plain_text, cipher_text
             
    
# control flow starts here
if __name__ == "__main__":
    PT, CT = main()
    print("\nPlain text: {0}\nCipher text: {1}\n".format(PT,CT))