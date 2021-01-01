import cv2

img = cv2.imread(filename)
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)
if bbox is not None:
    print(f"QRCode data:\n{data}")
    n_lines = len(bbox)
    for i in range(n_lines):
        a = tuple(bbox[i][0])
        b = tuple(bbox[(i+1) % n_lines][0])
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
