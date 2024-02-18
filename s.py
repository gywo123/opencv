import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blurred, threshold1=30, threshold2=100)

    dilated_edges = cv2.dilate(edges, None, iterations=2)

    edges_colored = np.zeros_like(frame)
    edges_colored[dilated_edges != 0] = [0, 0, 255]

    frame_with_edges = cv2.addWeighted(frame, 1, edges_colored, 1, 0)

    cv2.imshow('Webcam with Red Edges', frame_with_edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
