import requests
import time

def test_app():
    print("Testing /api/health...")
    try:
        r = requests.get('http://127.0.0.1:5000/api/health')
        print("Health Check:", r.json())
    except Exception as e:
        print("Health Check Failed:", e)

    print("\nTesting /api/analyze...")
    test_email = "Dear team, let's schedule a meeting for tomorrow at 2 PM."
    try:
        r = requests.post('http://127.0.0.1:5000/api/analyze', json={
            "email": test_email,
            "tone": "Professional"
        })
        print("Analyze Result:", r.json())
    except Exception as e:
        print("Analyze Failed:", e)

if __name__ == '__main__':
    # Wait for server to be fully up
    time.sleep(2)
    test_app()
