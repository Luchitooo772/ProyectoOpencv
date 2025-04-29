import cv2

# Cargar imagen
img = cv2.imread('prueba.jpg')

# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar detector de bordes de Canny
bordes = cv2.Canny(gray, 100, 200)

# Mostrar imagen original y bordes
cv2.imshow('Original', img)
cv2.imshow('Bordes Canny', bordes)

cv2.waitKey(0)
cv2.destroyAllWindows()