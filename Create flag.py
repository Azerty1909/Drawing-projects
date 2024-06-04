import matplotlib.pyplot as plt
from PIL import Image

self = Image.new("RGB",(600,400),(255,255,255))
print("Choisissez trois couleurs pour créer votre drapeau sur la base du drapeau français.")
print("Pour les couleurs vous avez différent choix:jaune, violet, bleu, rouge, orange, vert ou indigo.")
choix1 = input("Quelle couleur vous voulez à gauche du drapeau ?")
choix2 = input("Quelle couleur vous voulez au centre du drapeau ?")
choix3 = input("Quelle couleur vous voulez à droite du drapeau ?")
color_map = {
    "jaune": (255, 255, 0),
    "violet": (153, 0, 204),
    "bleu": (0, 0, 255),
    "rouge": (255, 0, 0),
    "orange": (255, 153, 51),
    "vert": (51, 204, 51),
    "indigo": (75, 0, 130)
}
for col in range (0,600):
  for ligne in range(0,400):
    if col<200:
      self.putpixel((col, ligne), color_map.get(choix1, (0, 0, 0)))
    if col>=200 and col<400:
      self.putpixel((col, ligne), color_map.get(choix2, (0, 0, 0)))
    if col>=400:
      self.putpixel((col, ligne), color_map.get(choix3, (0, 0, 0)))

plt.imshow(self)
plt.show()