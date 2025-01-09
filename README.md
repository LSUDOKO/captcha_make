# CAPTCHA Implementation Using Python

This project demonstrates how to create and validate CAPTCHAs (Completely Automated Public Turing tests to tell Computers and Humans Apart) using Python. CAPTCHAs are used to distinguish between human users and bots, providing an additional layer of security for web applications.

## Features
- 🖼️ Generate image-based CAPTCHAs with random text.
- ✅ Validate user input against generated CAPTCHA text.
- 🎨 Customizable CAPTCHA settings (e.g., text length, font, background).

## Requirements
To run this project, you need the following Python libraries installed:

- `Pillow`: For generating CAPTCHA images.
- `random`: For generating random strings.
- `os`: For handling file paths (optional).

Install dependencies using pip:
```bash
pip install pillow
```

## Getting Started

1. 📂 Clone this repository or download the source files.
2. 💻 Open the terminal or command prompt in the project directory.
3. ▶️ Run the Python script to generate a CAPTCHA and validate user input.

## How It Works

### 1. Generating the CAPTCHA
The CAPTCHA text is generated using a combination of random letters and numbers. The `Pillow` library is used to render this text as an image, optionally applying noise or distortion to make it harder for bots to decipher.

### 2. Validating User Input
The script compares the user's input with the generated CAPTCHA text. If the two match, the user passes the CAPTCHA test.

## Example Code
```python
from PIL import Image, ImageDraw, ImageFont
import random
import string

def captcha_decorator(func):
    def wrapper(*args, **kwargs):
        print("🔄 Generating CAPTCHA...")
        result = func(*args, **kwargs)
        print("✅ CAPTCHA generation completed.")
        return result
    return wrapper

@captcha_decorator
def generate_captcha(text_length=6):
    characters = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choices(characters, k=text_length))

    # Create image
    width, height = 200, 70
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Load font
    font = ImageFont.truetype("arial.ttf", size=36)

    # Add text to image
    text_width, text_height = draw.textsize(captcha_text, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    draw.text((text_x, text_y), captcha_text, font=font, fill='black')

    # Save image
    image.save("captcha.png")
    print("🖼️ CAPTCHA saved as captcha.png")
    return captcha_text

# Generate and display CAPTCHA
captcha_text = generate_captcha()
user_input = input("Enter the CAPTCHA text: ")
if user_input == captcha_text:
    print("🎉 CAPTCHA validated successfully!")
else:
    print("❌ CAPTCHA validation failed.")
```

## Customization
- **Text Length**: Change the `text_length` parameter in `generate_captcha`.
- **Font**: Replace `arial.ttf` with the path to another font file.
- **Dimensions**: Adjust `width` and `height` for different image sizes.

## Future Enhancements
- 🔊 Add support for audio CAPTCHAs.
- 🌐 Implement a web-based interface using Flask or Django.
- 🌀 Add noise, distortion, or obfuscation to increase CAPTCHA difficulty.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

**Author**: [Your Name]  
**Date**: January 10, 2025
