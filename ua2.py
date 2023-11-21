#ua2
import cv2
from deepface import DeepFace  # bina import karne toh hoga nahi
import os
from information import file_path

KNOWN_IMAGES_FOLDER = file_path  # Actual path se replace karna warna nahi chalega


def authenticate_face(unknown_image_path):
    try:
        known_images = [os.path.join(KNOWN_IMAGES_FOLDER, file) for file in os.listdir(KNOWN_IMAGES_FOLDER) if
                        file.lower().endswith(('.png', '.jpg', '.jpeg'))]

        for known_image in known_images:
            try:
                result = DeepFace.verify(known_image, unknown_image_path)
                if result["verified"]:
                    print(f"Face recognized. Authentication successful with {os.path.basename(known_image)}.")
                    return True
            except Exception as e:
                print(f"An error occurred during face verification: {e}")

        print("Face not recognized in the known images. Authentication failed.")  # error nahi hai baas output mein btna hai

        return False
    except cv2.error as e:
        print(f"An OpenCV error occurred: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# catching an exception
def capture_and_authenticate_face():
    try:
        video_capture = cv2.VideoCapture(0)

        _, frame = video_capture.read()

        cv2.imwrite("unknown_face.jpg", frame)  # code thoda mid hai dekh lena

        video_capture.release()
        print("Image captured successfully.")
    except cv2.error as e:
        print(f"An OpenCV error occurred while capturing the image: {e}")  # cv mein error toh aayegana
    except Exception as e:  # ecxception hai
        print(f"An error occurred while capturing the image: {e}")


def main():
    print("Please position yourself in front of the camera for face recognition.")
    input("Press Enter when ready...")

    capture_image_from_camera()

    unknown_image_path = "unknown_face.jpg"
    authentication_result = authenticate_face(unknown_image_path)

    if authentication_result:
        print("User authenticated. Perform further actions.")
    else:
        print("Authentication failed. Please try again.")
    try:
        os.remove(unknown_image_path)
    except OSError as e:
        print(f"Error removing the unknown face image: {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



