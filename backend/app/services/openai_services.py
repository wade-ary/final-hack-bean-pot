import openai
import json
from app.config import settings  # ✅ Securely import API key

async def analyze_carbon_footprint(data: dict):
    """
    Sends user's carbon footprint data to OpenAI and returns structured insights.
    """
    prompt = f"""
    The user provided the following carbon footprint data:
    - Travel: {data.get("travel", {})}
    - Car Usage: {data.get("car_usage", {})}
    - Public Transport: {data.get("public_transport", {})}
    - Active Travel: {data.get("active_travel", {})}

    Your task:
    1. Estimate the user's carbon footprint in **kg CO2e**.
    2. Suggest **two personalized recommendations** to reduce their footprint.

    **Return ONLY this JSON format (NO extra text!):**
    {{
      "carbon_score": (numeric value),
      "recommendations": ["Tip 1", "Tip 2"]
    }}
    """

    try:
        # ✅ Correct way to use OpenAI API key from settings
        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)  

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        raw_result = response.choices[0].message.content
        print("🔍 OpenAI Raw Response:", raw_result)  # ✅ Debugging Output

        # ✅ Strip unwanted text & enforce valid JSON
        if "{" in raw_result and "}" in raw_result:
            raw_result = raw_result[raw_result.index("{"): raw_result.rindex("}") + 1]

        result = json.loads(raw_result)

        return result.get("carbon_score", 0.0), result.get("recommendations", [])

    except json.JSONDecodeError:
        print("❌ JSON Parsing Error: OpenAI returned invalid JSON")
        return 0.0, ["Invalid AI response", "Try again later"]

    except Exception as e:
        print("❌ OpenAI API Error:", str(e))
        return 0.0, ["Error processing your request.", "Please try again later."]


