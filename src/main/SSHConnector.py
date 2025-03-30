from EmptionDetection import deepFaceAnalysis
import sys

# Get image path from command-line
image_path = sys.argv[1]


# Run analysis and print emotion
emotion = deepFaceAnalysis(image_path)
print(emotion)