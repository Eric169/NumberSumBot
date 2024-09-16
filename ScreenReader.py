import cv2
from paddleocr import PaddleOCR
import pyscreenshot
import numpy as np

def enlarge_img(img_path, scale_factor):
    image = cv2.imread(img_path)
    return cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
    

def read_numbers(x, y):
    img_path = r"images\screenTable.png"

    image = pyscreenshot.grab(bbox=(x, y, 940, 980)) 

    image.save(img_path)

    # Image optimizations that are apparently worse for some reason.
    # image = cv2.imread(img_path)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # cv2.imwrite(img_path, binary)

    ocr = PaddleOCR(use_angle_cls=True)

    scale_factor = 1.45
    enlarged_img = enlarge_img(img_path, scale_factor)

    result = ocr.ocr(enlarged_img)

    # In the game there are 3 kind of tables and for the smaller ones
    # is better to scale less for the ocr.
    if len(result[0])==48:
        print('scale 1.2')
        scale_factor = 1.2
        enlarged_img = enlarge_img(img_path, scale_factor)
        result = ocr.ocr(enlarged_img)
    if len(result[0])==63:
        print('scale 1.3')
        scale_factor = 1.3
        enlarged_img = enlarge_img(img_path, scale_factor)
        result = ocr.ocr(enlarged_img)

    # Boxes contains the center of rectangles of numbers found
    boxes = []
    for i, box in enumerate(result[0]):
        box = np.array(box[0]).astype(np.int32)
        x_min = min(box[:, 0])
        y_min = min(box[:, 1])
        x_max = max(box[:, 0])
        y_max = max(box[:, 1])
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2
        boxes.append([x_center/scale_factor, y_center/scale_factor])

    numbers = [line[1][0] for line in result[0]]
    for i in range(len(numbers)):
        # Sometimes ones ar read as 'L'
        if numbers[i] == 'L': numbers[i] = 1
        else: numbers[i] = int(numbers[i])
    return [numbers, boxes]

if __name__=="__main__":
    img_path = r"images\sampleTable6.png"

    print(read_numbers(img_path))
