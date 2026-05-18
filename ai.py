import requests

def get_ai_response(query):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi",
                "prompt": f"""
Give short answer in 3-5 points.
Each point new line.

User: {query}
""",
                "stream": False
            }
        )

        return response.json()["response"]

    except:
        return "AI not available"