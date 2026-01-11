from transformers import pipeline

bot = pipeline(
    "text2text-generation",
    model="google/flan-t5-large"
)

print("🤖 LLM Chat Bot Ready (type 'exit')\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Bot: Allah Hafiz 👋")
        break

    prompt = f"""Answer the question clearly.
Question: {question}
Answer:"""

    response = bot(
        prompt,
        max_new_tokens=100,
        do_sample=False,
        repetition_penalty=1.8
    )

    print("Bot:", response[0]["generated_text"], "\n")
