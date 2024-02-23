import os
import hashlib
import binascii
from wordlist import WORDLIST as wordlist
import fire
from termcolor import colored

def generate_seed_phrase(seed_phrase_length=12, verbose=False):
    """
    Generate a BIP-39 seed phrase.

    Args:
        seed_phrase_length (int): Length of the seed phrase (must be one of [12, 15, 18, 21, 24]).
        verbose (bool): If True, print additional information including the binary representation of the seed phrase.

    Raises:
        ValueError: If the seed phrase length is invalid.
    """
    # Validate seed phrase length
    if seed_phrase_length not in [12, 15, 18, 21, 24]:
        raise ValueError("Invalid seed phrase length. Must be one of [12, 15, 18, 21, 24].")

    # Calculate the number of bits of entropy required
    entropy_bits = seed_phrase_length * 32 // 3

    # Generate entropy
    entropy = os.urandom(entropy_bits // 8)

    # Convert entropy to binary string
    entropy_bin = bin(int(binascii.hexlify(entropy), 16))[2:].zfill(entropy_bits)

    # Calculate checksum
    checksum_length = entropy_bits // 32
    checksum_bin = bin(int(hashlib.sha256(entropy).hexdigest(), 16))[2:].zfill(256)[:checksum_length]

    # Combine entropy and checksum
    combined_bin = entropy_bin + checksum_bin

    # Convert to seed phrase
    seed_phrase = []
    for i in range(0, len(combined_bin), 11):
        index = int(combined_bin[i:i + 11], 2)
        seed_phrase.append(wordlist[index])

    # Print warnings and instructions
    print(colored("WARNING: Write down this seed phrase on paper and DO NOT copy it to the clipboard. This is a SECRET. Close session when done.", "red"))
    print(colored("Keep it in a safe place. Do not share it with anyone. Do not take pictures of it. This seed phrase is the key to your wallet.", "grey"))

    # Print the seed phrase in green
    print(colored(' '.join(seed_phrase), "green"))

    # Verbose mode: print the seed phrase as bits
    if verbose:
        print("\nVerbose Output:")
        for i in range(0, len(combined_bin), 11):
            word_bin = combined_bin[i:i + 11]
            word = wordlist[int(word_bin, 2)]
            if i < len(entropy_bin):
                word_bin_colored = colored(word_bin, "blue")
            else:
                word_bin_colored = colored(word_bin, "magenta")
            print(f"{word:>12} : {word_bin_colored}")

if __name__ == '__main__':
    fire.Fire(generate_seed_phrase)


