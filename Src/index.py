import cv2
from pyzbar.pyzbar import decode
from PIL import Image
import time

# -------- Step 1: Open camera for 10 seconds --------
cap = cv2.VideoCapture(0)

start_time = time.time()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    cv2.imshow("Laptop Camera", frame)
    
    # If 10 seconds passed, break and save frame
    if time.time() - start_time >= 10:
        captured_path = "qrCode.png"
        cv2.imwrite(captured_path, frame)
        print("Picture taken and saved as qrCode.png")
        # Decode QR code
        decoded_objects = decode(image)

        for obj in decoded_objects:
            print("Type:", obj.type)
            print("Data:", obj.data.decode("utf-8"))
        break


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# Load the image
