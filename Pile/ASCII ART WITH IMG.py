from Pile import Image

# Remplace le chemin avec le chemin de ton image
image_path = 'C:/Users/salli/OneDrive/Images/Captures d’écran/Capture d\'écran 2023-09-30 111052.png'

# Taille souhaitée pour l'ASCII art (ajuste selon tes préférences)
width, height = 100, 60

# Ouvre l'image et redimensionne-la
img = Image.open(image_path)
img = img.resize((width, height))

# Convertit l'image en niveaux de gris
img = img.convert('L')

# Liste de caractères ASCII, du plus foncé au plus clair
ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Convertit chaque pixel en caractère ASCII en fonction de l'intensité lumineuse
pixels = img.getdata()
ascii_str = ""
for pixel_value in pixels:
    ascii_str += ascii_chars[pixel_value // 25]

# Divise la chaîne ASCII en lignes de la largeur souhaitée
ascii_str_len = len(ascii_str)
ascii_img = ""
for i in range(0, ascii_str_len, width):
    ascii_img += ascii_str[i:i+width] + "\n"

# Affiche l'ASCII art
print(ascii_img)
