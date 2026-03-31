from transformers import pipeline

# Load model
generator = pipeline("text-generation", model="gpt2")

def generate_email(topic):
    try:
        prompt = f"Write a professional email about: {topic}\n\nEmail:"

        result = generator(
            prompt,
            max_new_tokens=120,   # ✅ use this instead of max_length
            num_return_sequences=1,
            pad_token_id=50256    # ✅ avoids warning
        )

        return result[0]["generated_text"]

    except Exception as e:
        print("Error generating email:", e)
        return None