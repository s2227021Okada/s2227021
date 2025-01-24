from flask import Flask, render_template, request

app = Flask(__name__)

# 教科ごとの単位数を設定
COURSES = {
    "デジタルコンテンツ論": 2,
    "Webシステム構築": 2,
    "プロジェクトマネジメント論": 2,
    "3DCAD応用": 2,
    "就職活動実践講座": 2,
    "データベース応用": 2,
    "情報技術と職業": 2,
    "組込み演習": 2,
    "研究ゼミナールB": 2,
    "生涯スポーツ指導": 1,
    "情報メディア総合演習": 2,
    "大分の地域ブランド創造体験": 2,
    "海外文化体験": 1
}

@app.route('/')
def index():
    return render_template('index.html', courses=COURSES)

@app.route('/calculate', methods=['POST'])
def calculate():
    selected_courses = request.form.getlist('courses')
    total_credits = sum(COURSES[course] for course in selected_courses if course in COURSES)
    return render_template('result.html', total_credits=total_credits, selected_courses=selected_courses)

if __name__ == '__main__':
    app.run(debug=True)

