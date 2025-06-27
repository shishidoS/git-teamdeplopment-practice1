from flask import Flask, render_template
from pathlib import Path  # ← これを追加

app = Flask(__name__)

# 自己紹介ページへのリンク情報
PROFILE_LINKS = {
    "sample_user": "サンプルユーザー",
    "rei_shishido": "宍戸",  # ← 拡張子「.html」はキーに含めないよう統一した方がよい
    "takashi": "タカシ"
}

@app.route("/")
def index():
    """
    名前を選択するトップページ
    """
    return render_template("index.html", profile_links=PROFILE_LINKS)

@app.route("/profiles/<filename>")
def profile(filename):
    """
    自己紹介ページを表示
    """
    # templates/profiles/ ディレクトリを正しく扱うため pathlib を使用
    profiles_dir = Path(app.template_folder) / "profiles"
    html_files = [f.name for f in profiles_dir.iterdir() if f.is_file()]
    
    if filename + ".html" in html_files:
        return render_template(f"profiles/{filename}.html")
    else:
        return "指定されたページは見つかりません", 404

if __name__ == "__main__":
    app.run(debug=True)
