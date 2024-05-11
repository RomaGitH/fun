from colorama import init, Fore, Style
from PIL import Image
import pywhatkit as kit
#intialize colorama
init()

# Function to convert image to ASCII art
def image_to_ascii(image_path):
    # Resize the image to reduce the number of characters
    img = Image.open(image_path)
    width, height = img.size
    aspect_ratio = height/width
    new_width = 100
    new_height = int(aspect_ratio * new_width * 0.55)
    img = img.resize((new_width, new_height))

    # Convert the resized image to ASCII art
    ascii_art = kit.image_to_ascii_art(image_path)
    return ascii_art

# Path to the image fil
image_path = "image2.png"

# Convert the image to ASCII art
ascii_art = image_to_ascii(image_path)

# Define mapping of characters to their replacements
char_map = {
    ".": " ",  # Replace "." with empty space
    ":": " ",  # Replace ":" with empty space
    "!": ". ",  # Replace "#" with empty space
    "@": "!",  # Replace "@" with "."
    "*": ":",  # Replace "*" with ":"
    "X": "W",  # Replace "X" with "W"
}

# Modify ASCII art according to the mapping
ascii_art_modified = "".join(char_map.get(char, char) for char in ascii_art)
#ascii_art = ascii_art.replace("."," ").replace(":"," ")
# Print the ASCII art

print(Fore.GREEN + ascii_art_modified + Style.RESET_ALL)
    
