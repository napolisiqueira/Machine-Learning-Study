import cv2
import numpy as np

img = cv2.imread('sua_imagem.jpg')

if img is None:
    print("Erro ao carregar a imagem. Verifique o caminho do arquivo.")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, bin = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow('Imagem Original (Colorida)', img)

    cv2.imshow('Imagem em Tons de Cinza', gray)

    cv2.imshow('Imagem Binarizada (Preto e Branco)', bin)

    cv2.waitKey(0)
    cv2.destroyAllWindows()