import asyncio

import openai
import pyperclip
from flask import Flask, render_template, request

from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


async def rewrite_text(input_text):
    # prompt = (f"Please rewrite the following text: \n\n{input_text}\n\nRewritten text:")
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "user", "content": f"Please rewrite the following text: {input_text}"}])
    return response.choices[0].message.content


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
async def home():
    if request.method == "POST":
        input_text = request.form["input_text"]
        output_text = await rewrite_text(input_text)
        pyperclip.copy(output_text)
        return render_template("index.html", output_text=output_text)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(openai.api_instance.verify()))  # Verify OpenAI API credentials
    app.run(debug=True, port=5000)
