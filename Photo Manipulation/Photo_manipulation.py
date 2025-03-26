from PIL import Image, ImageEnhance, ImageFilter
import os

def load_image():
    while True:
        file_path = input("Enter image path: ")
        if os.path.exists(file_path):
            return Image.open(file_path)
        print("File not found. Please try again.")

def show_menu():
    print("\nPhoto Editor Options:")
    print("1. Adjust Brightness")
    print("2. Adjust Contrast")
    print("3. Apply Blur")
    print("4. Apply Sharpen")
    print("5. Convert to Grayscale")
    print("6. Save and Quit")
    return input("Select option (1-6): ")

def edit_photo():
    print("Simple Photo Editor")
    img = load_image()
    img.show()
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            factor = float(input("Enter brightness factor (0.1-2.0): "))
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(factor)
            
        elif choice == "2":
            factor = float(input("Enter contrast factor (0.1-2.0): "))
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(factor)
            
        elif choice == "3":
            radius = int(input("Enter blur radius (1-10): "))
            img = img.filter(ImageFilter.GaussianBlur(radius))
            
        elif choice == "4":
            img = img.filter(ImageFilter.SHARPEN)
            
        elif choice == "5":
            img = img.convert("L")
            
        elif choice == "6":
            save_path = input("Enter filename to save: ")
            img.save(save_path)
            print("Image saved successfully")
            break
            
        else:
            print("Invalid selection")
        
        img.show()

if __name__ == "__main__":
    edit_photo()