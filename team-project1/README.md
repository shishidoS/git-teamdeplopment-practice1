# チーム自己紹介アプリ

このアプリは、Flask を使って作成された **チームメンバーの自己紹介ページ** です。トップページからメンバーを選択し、それぞれの自己紹介ページを見ることができます。

## 📁 ディレクトリ構成

team-project1/
├── app.py # Flaskアプリの本体
├── templates/
│ ├── index.html # トップページ（メンバー一覧）
│ └── profiles/
│ ├── rei_shishido.html # 宍戸さんの自己紹介ページ
│ └── ... # 他メンバーのHTMLをここに追加
└── README.md # このファイル


## 🚀 起動方法

### 1. 必要なパッケージをインストール

Python 3 がインストールされた環境で、Flask をインストールします。

```bash
pip install flask

2. アプリを起動
python3 app.py

起動後、以下のURLにアクセスしてください：
http://localhost:5000/

👤 自己紹介ページの追加方法
templates/profiles/ フォルダ内に、以下の形式でHTMLファイルを作成します。

例: yamada.html

app.py 内の PROFILE_LINKS に、次のように追加します。

PROFILE_LINKS = {
    "rei_shishido": "宍戸",
    "yamada": "山田"
}
アプリを再起動すれば、トップページに山田さんが表示され、リンク先に遷移できます。


💡 補足
ページが表示されない場合は、HTMLファイルを正しく templates/profiles/ に配置しているか確認してください。

URLは /profiles/<ファイル名> です。拡張子 .html は不要です。

🛠 開発者向け
このプロジェクトはPython + Flaskの学習目的で作られました。チームでのGit管理や、テンプレートの使い方を学ぶのに最適です。

yaml
コピーする
編集する
