from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

img = Image.open("Mangalarga-marchador.jpg")
img_np = np.array(img)

model = YOLO("yolo26n-seg.pt")
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

img = Image.open("Teste2.jpeg")
img_np = np.array(img)

model = YOLO("yolo26n-seg.pt")
results = model.predict(img)

result = results[0]

output = img_np.copy()

h, w = img_np.shape[:2]

if result.masks is not None:
    for mask in result.masks.data:
        mask = mask.cpu().numpy()

        # REDIMENSIONA a máscara pro tamanho original
        mask_resized = cv2.resize(mask, (w, h))

        # aplica cor vermelha
        output[mask_resized > 0.5] = [255, 0, 0]

cv2.imwrite("resultado.png", cv2.cvtColor(output, cv2.COLOR_RGB2BGR))

print("Imagem salva com sucesso!")