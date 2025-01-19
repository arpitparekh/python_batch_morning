import cv2

cap= cv2.VideoCapture(0)   # 30 fps
success,prev_img = cap.read()
prev_img = cv2.cvtColor(prev_img,cv2.COLOR_BGR2GRAY)


while True:
  success,next_img = cap.read()

  if not success:
    break

  # img = cv2.flip(img,1)
  next_img = cv2.cvtColor(next_img,cv2.COLOR_BGR2GRAY)

  diff = cv2.absdiff(prev_img,next_img)

  cv2.imshow("diff",diff)

  prev_img = next_img

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
