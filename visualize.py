import matplotlib.pyplot as plt

def visualize_seed_phrase_bits(seed_phrase_bits, border_width=1, font_size=4, enum_offset=-1.5):
    # Define the figure and axis
    fig, ax = plt.subplots(figsize=(20, 3))  # Adjust the figure width as necessary

    # Create a list for colors for each word (11 bits per word)
    colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A5', '#A533FF', '#33FFC5',
              '#FFC533', '#33D4FF', '#FF5733', '#33FF57', '#3357FF', '#FF33A5']  # Colors for words

    # The checksum bits will be black, and their numbers will be green
    checksum_color = 'black'
    checksum_number_color = 'green'

    # Set the background to white
    ax.set_facecolor('white')

    # Convert the string of bits into a list of integers (1s and 0s)
    bit_list = [int(bit) for bit in seed_phrase_bits]

    # Calculate the total length of the bit string
    total_bits = len(seed_phrase_bits)

    # Set the aspect of the plot box to 1 (equal scaling) to make squares appear square-shaped
    ax.set_aspect(aspect=1)

    # Set the limits of the plot
    ax.set_xlim(-0.5, total_bits - 0.5)
    ax.set_ylim(enum_offset - 0.5, 0.5)  # Extend the y-axis lower bound to give space for text

    # Remove the axes
    ax.axis('off')

    # Plot each bit as a square with a border and add the annotations
    for index, bit in enumerate(bit_list):
        # Determine the color based on the index
        color = colors[index // 11] if index < 128 else checksum_color
        
        # Create a square for each bit
        square = plt.Rectangle((index, -0.5), 1, 1, facecolor=color if bit == 1 else 'white', 
                               edgecolor='black', lw=border_width)
        ax.add_patch(square)

        # Annotate each square with the bit value (0 or 1)
        ax.text(index + 0.5, 0, str(bit), color='black', ha='center', va='center', fontsize=font_size)

        # Annotate below each square with its index
        # Checksum numbers are green, other numbers are black
        text_color = checksum_number_color if index >= 128 else 'black'
        ax.text(index + 0.5, enum_offset, str(index), color=text_color, ha='center', va='center', fontsize=font_size)

    # Adjust layout to ensure squares and text are displayed correctly
    plt.tight_layout()

    # Show the plot
    plt.show()

# Example usage
# Create an example bit string for a 12-word seed phrase with 128 bits + 4 checksum bits
seed_phrase_bits = '101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010'
visualize_seed_phrase_bits(seed_phrase_bits)
