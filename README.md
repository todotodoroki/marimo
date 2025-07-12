# 🌱 マリモ水温モニター

マリモの水温を**DS18B20温度センサー**で測定し、リアルタイムでダッシュボードに表示するFlaskウェブアプリケーションです。インスタ風のポップなデザインで、波のようなゆらぎアニメーションが特徴です。

## ✨ 特徴

- 🌊 波のゆらぎをイメージしたアニメーション
- 🧡 オレンジ系の暖かみのある配色
- 📱 レスポンシブデザイン
- 🔄 5秒ごとの自動温度更新
- 🎨 インスタグラム風のモダンなUI
- 🌡️ **DS18B20センサーによる実際の温度測定**

## 🛠️ 必要なハードウェア

- **Raspberry Pi** (推奨: Pi 3 以上)
- **DS18B20 温度センサー** (防水タイプ推奨)
- **4.7kΩ抵抗** (プルアップ用)
- **ジャンパーワイヤー**
- **ブレッドボード** (オプション)

### 🔌 配線図

```
DS18B20 センサー -> Raspberry Pi
VCC (赤)         -> 3.3V (Pin 1)
GND (黒)         -> GND (Pin 6)
DATA (黄)        -> GPIO 4 (Pin 7)
```

**重要**: DATA線と3.3V間に4.7kΩのプルアップ抵抗を接続してください。

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

### 1. ハードウェアの準備

1. **Raspberry Pi OS のセットアップ**
   ```bash
   # 1-Wire インターフェースを有効化
   sudo raspi-config
   # 3 Interface Options > P7 1-Wire > Yes を選択
   # 再起動
   sudo reboot
   ```

2. **DS18B20センサーの接続**
   - 上記の配線図に従って接続
   - 防水センサーの場合は、水槽内に設置

3. **センサー動作確認**
   ```bash
   # センサーが認識されているか確認
   ls /sys/bus/w1/devices/
   # 28-xxxxxxxxxxxx のようなフォルダが表示されればOK
   ```

### 2. ソフトウェアのセットアップ

1. **リポジトリをクローン:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/marimo-temperature-monitor.git
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
   `http://localhost:8080` にアクセス

## 🔧 トラブルシューティング

### センサーが認識されない場合
- 1-Wireが有効になっているか確認: `sudo raspi-config`
- 配線を再確認（特にプルアップ抵抗）
- センサーの動作確認: `cat /sys/bus/w1/devices/28-*/w1_slave`

### 権限エラーの場合
```bash
# ユーザーをgpioグループに追加
sudo usermod -a -G gpio $USER
# 再ログイン
```

### 開発・テスト用のシミュレーションモード
実際のセンサーなしでテストしたい場合は、`utils/temperature_sensor.py`の`get_temperature()`関数を以下のように変更：
```python
def get_temperature():
    # テスト用: ランダムな温度を返す
    temperature = read_temperature()  # read_temperature_real() から変更
    return temperature
```

## 🎯 使用方法

- ダッシュボードで現在のマリモの水温をリアルタイムで確認
- 温度は5秒ごとに自動更新
- 波のような美しいアニメーションで視覚的に楽しめる
- **実際のDS18B20センサーから正確な温度を測定**

## 🛠️ 技術スタック

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Hardware**: Raspberry Pi + DS18B20 温度センサー
- **Sensor Library**: w1thermsensor (1-Wire protocol)
- **Design**: グラデーション、アニメーション、レスポンシブデザイン
- **Font**: Noto Sans JP (日本語対応)

## 🌡️ センサー仕様

- **DS18B20 特徴**:
  - 測定範囲: -55°C～+125°C
  - 精度: ±0.5°C (10°C～85°C)
  - 分解能: 9～12ビット (設定可能)
  - 防水バージョン利用可能
  - 1-Wire プロトコル対応

## 🤝 貢献

プロジェクトの改善提案やバグ報告は、IssueやPull Requestでお気軽にお知らせください。

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。