from colorama import init, Fore, Style
from PIL import Image
import pywhatkit as kit

from typing import Optional

#intialize colorama
init()

#Stolen 
def image_to_ascii_art(
    img_path: str, output_file: Optional[str] = "pywhatkit_asciiart"
) -> str:
    """Convert an Image to ASCII Art"""

    img = Image.open(img_path).convert("L")

    width, height = img.size
    aspect_ratio = height / width
    new_width = 60
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))

    pixels = img.getdata()

       #chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    chars = ["#", "#", "#", ":", ":", ":", ".", ".", ".", " ", " "]
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = "".join(new_pixels) #concatena el array en un str

    new_pixels_count = len(new_pixels) #lenght
    ascii_image = [
        new_pixels[index : index + new_width] 
        for index in range(0, new_pixels_count, new_width)
    ] #Mapping str to matrix, sublist por each row and new_width pace 
    ascii_image = "\n".join(ascii_image) #saltos de linea
    return ascii_image


"""
    with open(f"{output_file}.txt", "w") as f:
        f.write(ascii_image)
""" 

"""
# Function to convert image to ASCII art

def image_to_ascii(image_path):
    # Resize the image to reduce the number of characters
    img = Image.open(image_path)
    width, height = img.size
    aspect_ratio = height/width
    new_width = 5 
    new_height = int(aspect_ratio * new_width * 0.55)
    img = img.resize((new_width, new_height))
    
    # Create temp file and save img
    temp_path = "temp.png"
    img.save(temp_path)
    # Convert the resized image to ASCII art
    ascii_art = kit.image_to_ascii_art(temp_path)
    return ascii_art

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
"""
# Path to the image fil
image_path = "image5.webp"

# Convert the image to ASCII art
ascii_art = image_to_ascii_art(image_path)

print(Fore.CYAN + ascii_art + Style.RESET_ALL)
    
