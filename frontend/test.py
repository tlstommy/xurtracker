import json
import requests
import os

def download_json(url, filepath):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        # Ensure the directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Write the JSON data to the file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f'File downloaded successfully and saved to {filepath}')
    except requests.exceptions.RequestException as e:
        print(f'Error downloading the file: {e}')

if __name__ == "__main__":
    url = 'https://www.xurtracker.com/api/get-data'
    filepath = os.path.join('src', 'destinyData-test-run.json')  # Ensure this path is correct
    download_json(url, filepath)
