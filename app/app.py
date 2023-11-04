from flask import Flask, render_template, redirect, url_for
import mysql.connector, random
import openai
import config as c


openai.organization = c.openai_org_id
openai.api_key = c.openai_secret_key

app = Flask(__name__)
app.secret_key = c.flask_secret_key

DATABASE_TABLE = 'question'
db = mysql.connector.connect(
    host = c.mysql_hostname,
    user = c.mysql_username,
    password = c.mysql_password,
    database = c.mysql_database
)
cursor = db.cursor()

TYPES = {
    'movie' : 1,
    'tv' : 2,
    'book' : 3, 
    'game' : 4,
}
GENRES = {
    'action' : 1,
    'comedy' : 2,
    'horror' : 3,
    'romance' : 4,
    'fantasy' : 5
}

DIFFICULTIES = {
    'easy' : 1,
    'medium' : 2,
    'hard' : 3
}

@app.route('/')
def index():
    return render_template('index.html')

def get_questions(n, type, genre, difficulty):
    cursor.execute(
        f"SELECT * FROM {DATABASE_TABLE} WHERE Genre = %s AND Type = %s AND Difficulty = %s",
        (type, genre, difficulty)
    )

    return [{'content': row[4], 'answer': row[5]} for row in random.sample(cursor.fetchall(), n)]

def gpt_api():
    pass
    # prompt = "tell me a joke"

    # # Make the API request
    # response = openai.Completion.create(
    #     engine="davinci",
    #     prompt=prompt,
    #     max_tokens=50,  # Adjust max tokens as needed
    # )

    # print(response)
    # print()
    # joke = response.choices[0].text.strip()
    # print(joke)

if __name__ == '__main__':
    # for question in get_questions(1, 1, 4, 3):
    #    print(question['content'] + " : " + question['answer'])
    app.run(debug=True)






