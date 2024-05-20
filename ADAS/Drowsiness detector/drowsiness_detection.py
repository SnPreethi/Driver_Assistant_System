from scipy.spatial import distance
from imutils import face_utils
from pygame import mixer
import imutils
import dlib
import cv2

# Initialize the mixer and load the alert sound
mixer.init()
mixer.music.load("alarm_music.wav")

# Function to calculate the Eye Aspect Ratio (EAR)
def calculate_ear(eye_points):
    vertical_1 = distance.euclidean(eye_points[1], eye_points[5])
    vertical_2 = distance.euclidean(eye_points[2], eye_points[4])
    horizontal = distance.euclidean(eye_points[0], eye_points[3])
    ear_value = (vertical_1 + vertical_2) / (2.0 * horizontal)
    return ear_value

# Set thresholds and initialize dlib's face detector and facial landmarks predictor
ear_threshold = 0.21
consecutive_frames = 20
face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

(left_eye_start, left_eye_end) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(right_eye_start, right_eye_end) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

# Initialize the video capture object
video_capture = cv2.VideoCapture(0)
drowsiness_counter = 0

while True:
    # Read frame from the video capture
    ret, frame = video_capture.read()
    frame = imutils.resize(frame, width=450)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detected_faces = face_detector(gray_frame, 0)

    for face in detected_faces:
        facial_landmarks = landmark_predictor(gray_frame, face)
        facial_landmarks_np = face_utils.shape_to_np(facial_landmarks)
        left_eye_points = facial_landmarks_np[left_eye_start:left_eye_end]
        right_eye_points = facial_landmarks_np[right_eye_start:right_eye_end]
        left_ear = calculate_ear(left_eye_points)
        right_ear = calculate_ear(right_eye_points)
        average_ear = (left_ear + right_ear) / 2.0

        left_eye_hull = cv2.convexHull(left_eye_points)
        right_eye_hull = cv2.convexHull(right_eye_points)
        cv2.drawContours(frame, [left_eye_hull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [right_eye_hull], -1, (0, 255, 0), 1)
        cv2.putText(frame, "E.A.R: {:.2f}".format(average_ear), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        if average_ear < ear_threshold:
            drowsiness_counter += 1
            if drowsiness_counter >= consecutive_frames:
                cv2.putText(frame, "DROWSINESS ALERT!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                mixer.music.play()
        else:
            drowsiness_counter = 0

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
video_capture.release()
