from PIL import Image
import os
import hashlib

def process_image(file_path):
    img = Image.open(file_path).convert('1') 
    pixels = img.load()
    width, height = img.size
    
    data = []
    for y in range(height):
        for x in range(width):
            if pixels[x, y] == 0: 
                data.append((x, y))
    return data

def main():
    folder = r"Folder_Location" 
    combined_data = ""

    for file_name in sorted(os.listdir(folder)):
        if file_name.endswith(".png"):
            file_path = os.path.join(folder, file_name)
            data = process_image(file_path)
            combined_data += str(data)

    flag = hashlib.sha256(combined_data.encode()).hexdigest()
    print(f"flag: ctf{{{flag}}}")

if __name__ == "__main__":
    main()
