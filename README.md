🔐 Task Description

This task demonstrates a basic method of image encryption and decryption using Python. The script inverts each pixel’s RGB values (255 - value) to create a scrambled version of the image. Since the process is reversible, running the same script again on the encrypted image restores the original. It’s a beginner-friendly way to explore pixel-level manipulation and symmetric operations in image processing.

🔓 Decryption

This task also supports a simple decryption method since the operation is reversible. Applying the same script again on the encrypted image restores the original image.

📁 File Used

image_encrypt.py – the same script is used for both encryption and decryption.

🧠 Concepts Used:

Reversible mathematical operations
Pixel-level RGB manipulation
Symmetric encryption (same process for encrypt/decrypt)

⚙️ How It Works:

1. Open the encrypted image.
2. Read each pixel’s RGB value.
3. Apply the inversion formula again (255 - value).
4. Save the restored output as decrypted_image.png.

🔄 Example:

Encrypted RGB: (155, 105, 55)
Decrypted RGB: (100, 150, 200)

💻 How to Run on Kali Linux:

🔸 Step 1: Place your encrypted image in the project directory as encrypted_image.png.
🔸 Step 2: Run the script again:
```bash
python3 image_encrypt.py
 ```
🔸 Step 3: The original image will be restored as decrypted_image.png.
