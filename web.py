from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/show/info')
def index():
    # return "中国移动"
    return render_template('index.html')

@app.route('/get/news')
def get_news():
    return render_template('news.html')

@app.route('/submit', methods=['POST'])
def submit():
 
    return f"""
    <h1>提交成功</h1>
    <p>用户名：{name}</p>
    <p>密码：{'*' * len(pwd) if pwd else ''}</p>
    <p>性别：{gender}</p>
    <p>爱好：{hobby}</p>
    <p>城市：{city}</p>
    <p>简介：{bio}</p>
    <a href="/get/news">返回</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
