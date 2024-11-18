import requests

# Substitua pela sua chave e URL do serviço cognitivo
SUBSCRIPTION_KEY = "SUA_CHAVE_AQUI"
ENDPOINT = "SUA_URL_AQUI"  # URL do seu serviço cognitivo no Azure

def analyze_image(image_path):
    image_url = image_path  # Para simplificação, usamos o caminho local da imagem

    # Cabeçalhos da requisição
    headers = {
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
        'Content-Type': 'application/json'
    }

    params = {
        'returnFaceId': 'true'
    }

    # Enviar a requisição
    try:
        response = requests.post(f"{ENDPOINT}/detect", params=params, headers=headers, json={"url": image_url})
        response.raise_for_status()  # Verifica se houve erro na requisição
        faces = response.json()
        # Se houver pelo menos uma face detectada
        return len(faces) > 0
    except requests.exceptions.RequestException as e:
        print(f"Erro na API de reconhecimento de imagem: {e}")
        return False
