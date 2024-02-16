import mediapipe as mediapipe
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

BaseOptions = mediapipe.tasks.BaseOptions
GestureRecognizer = mediapipe.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mediapipe.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mediapipe.tasks.vision.RunningMode

model_path = '/Users/sarthakbhardwaj/Desktop/projects/pythonopencv/gesture_recognizer.task'

base_options = mediapipe.tasks.BaseOptions(model_asset_path=model_path)

#create a gesture recognizer instance with the video mode:
options = GestureRecognizerOptions(
    base_options,
    running_mode = VisionRunningMode.VIDEO
)
with GestureRecognizer.create_from_options(options) as recognizer: