# 🌱 マリモ水温モニター

マリモの水温を温度計で測定し、リアルタイムでダッシュボードに表示するFlaskウェブアプリケーションです。インスタ風のポップなデザインで、波のようなゆらぎアニメーションが特徴です。

## ✨ 特徴

- 🌊 波のゆらぎをイメージしたアニメーション
- 🧡 オレンジ系の暖かみのある配色
- 📱 レスポンシブデザイン
- 🔄 5秒ごとの自動温度更新
- 🎨 インスタグラム風のモダンなUI

## 📁 プロジェクト構造

```
marimo-temperature-monitor/
├── app.py                     # Flask アプリケーションのメインファイル
├── templates/                 # HTML テンプレート
│   ├── base.html              # ベーステンプレート
│   └── dashboard.html         # ダッシュボードページ
├── static/                    # 静的ファイル (CSS, JavaScript)
│   ├── css/
│   │   └── style.css          # スタイルシート
│   └── js/
│       └── app.js             # JavaScript (温度更新機能)
├── utils/                     # ユーティリティ関数
│   ├── __init__.py            # Python パッケージ初期化
│   └── temperature_sensor.py   # 温度センサー機能
├── requirements.txt           # プロジェクト依存関係
└── README.md                  # プロジェクトドキュメント
```

## 🚀 セットアップ手順

1. **リポジトリをクローン:**
   ```bash
   git clone <repository-url>
   cd marimo-temperature-monitor
   ```

2. **仮想環境を作成 (推奨):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **依存関係をインストール:**
   ```bash
   pip install -r requirements.txt
   ```

4. **アプリケーションを実行:**
   ```bash
   python3 app.py
   ```

5. **ブラウザでアクセス:**
   `http://127.0.0.1:5000` または `http://localhost:8080` にアクセス

## 🎯 使用方法

- ダッシュボードで現在のマリモの水温をリアルタイムで確認
- 温度は5秒ごとに自動更新
- 波のような美しいアニメーションで視覚的に楽しめる

## 🛠️ 技術スタック

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Design**: グラデーション、アニメーション、レスポンシブデザイン
- **Font**: Noto Sans JP (日本語対応)

## 🤝 貢献

プロジェクトの改善提案やバグ報告は、IssueやPull Requestでお気軽にお知らせください。

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。