import sys
import cv2
import matplotlib.pyplot as plt

if len(sys.argv) < 3:
  print("Expected arguments: input_image output_image")
  exit()

img = cv2.imread(sys.argv[1])
edges = cv2.Canny(img, 100, 200, 3, L2gradient=True)
plt.figure()
plt.imsave(sys.argv[2], edges, cmap='copper', format='png')
plt.imshow(edges, cmap='copper')
plt.show()