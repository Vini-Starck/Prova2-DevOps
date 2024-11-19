import requests

def verify_face(photo_path):
    endpoint = "https://brazilsouth.api.cognitive.microsoft.com/"
    subscription_key = "b6d97d4a-1734-48ef-ae23-22fba0b5badf"

    face_api_url = endpoint + "face/v1.0/detect"
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}

    with open(photo_path, 'rb') as image:
        response = requests.post(face_api_url, headers=headers, data=image)

    if response.status_code != 200:
        return False

    faces = response.json()
    return len(faces) > 0
