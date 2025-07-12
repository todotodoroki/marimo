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
├── app.wsgi                   # Apache mod_wsgi設定ファイル
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

2. **システム全体に依存関係をインストール:**
   ```bash
   # システム全体にパッケージをインストール
   pip3 install -r requirements.txt --break-system-packages
   ```

3. **アプリケーションを実行:**
   ```bash
   python3 app.py
   ```

4. **ブラウザでアクセス:**
   `http://localhost:8080` にアクセス

## 🌐 Apache での本番運用

### Apache + mod_wsgi でのセットアップ

1. **必要なパッケージのインストール:**
   ```bash
   sudo apt update
   sudo apt install apache2 libapache2-mod-wsgi-py3 python3-pip
   sudo pip3 install flask w1thermsensor --break-system-packages
   ```

2. **プロジェクトの配置:**
   ```bash
   sudo cp -r /path/to/marimo-temperature-monitor /var/www/marimo
   sudo chown -R www-data:www-data /var/www/marimo
   sudo chmod -R 755 /var/www/marimo
   ```

3. **app.wsgiファイルの作成:**
   ```python
   # /var/www/marimo/app.wsgi
   #!/usr/bin/python3
   import sys
   import os

   # プロジェクトディレクトリをパスに追加
   sys.path.insert(0, '/var/www/marimo/')

   # 環境変数を設定
   os.environ.setdefault('FLASK_ENV', 'production')

   try:
       from app import app as application
   except ImportError as e:
       # エラー時のフォールバック
       def application(environ, start_response):
           status = '500 Internal Server Error'
           headers = [('Content-type', 'text/html; charset=utf-8')]
           start_response(status, headers)
           error_html = f'''
           <html>
           <head><title>Import Error</title></head>
           <body>
           <h1>Import Error</h1>
           <p>Cannot import app module: {e}</p>
           <p>Check the Apache error log for details.</p>
           </body>
           </html>
           '''
           return [error_html.encode('utf-8')]

   if __name__ == "__main__":
       application.run()
   ```

4. **Apache設定ファイルの作成:**
   ```bash
   sudo nano /etc/apache2/sites-available/marimo-temperature-monitor.conf
   ```
   
   設定内容:
   ```apache
   <VirtualHost *:80>
       ServerName marimo-monitor.local
       ServerAlias localhost
       DocumentRoot /var/www/marimo
       
       # WSGIアプリケーションを最優先に
       WSGIScriptAlias / /var/www/marimo/app.wsgi
       WSGIApplicationGroup %{GLOBAL}
       
       # DocumentRootディレクトリの設定
       <Directory /var/www/marimo>
           # 静的ファイルの自動インデックスを無効化
           Options -Indexes
           AllowOverride None
           Require all granted
           
           # DirectoryIndexを無効化（WSGIを優先）
           DirectoryIndex disabled
       </Directory>
       
       # 静的ファイル（CSS、JS、画像）のみを直接配信
       Alias /static /var/www/marimo/static
       <Directory /var/www/marimo/static>
           Options -Indexes
           AllowOverride None
           Require all granted
           # 静的ファイルはApacheが直接配信
           SetHandler None
       </Directory>
       
       # ログの設定
       ErrorLog ${APACHE_LOG_DIR}/marimo_error.log
       CustomLog ${APACHE_LOG_DIR}/marimo_access.log combined
       LogLevel info
   </VirtualHost>
   ```

5. **サイトの有効化:**
   ```bash
   # デフォルトサイトを無効化
   sudo a2dissite 000-default.conf
   
   # 新しいサイトを有効化
   sudo a2ensite marimo-temperature-monitor.conf
   sudo a2enmod wsgi
   
   # Apache設定をテスト
   sudo apache2ctl configtest
   
   # Apacheを再起動
   sudo systemctl restart apache2
   ```

6. **権限設定:**
   ```bash
   # www-dataユーザーがセンサーにアクセスできるように設定
   sudo usermod -a -G gpio www-data
   sudo systemctl restart apache2
   ```

7. **アクセス:**
   `http://localhost` または `http://RaspberryPiのIPアドレス`

### 🐞 Apache運用時のデバッグ方法

#### よくある問題と対処法

**1. Target WSGI script not found エラー**
```bash
# app.wsgiファイルが存在するか確認
ls -la /var/www/marimo/app.wsgi

# ファイル権限を確認
sudo chmod 644 /var/www/marimo/app.wsgi
sudo chown www-data:www-data /var/www/marimo/app.wsgi
```

**2. ModuleNotFoundError: No module named 'app' エラー**
```bash
# app.pyファイルが存在するか確認
ls -la /var/www/marimo/app.py

# プロジェクトファイルを再コピー
sudo cp -r /home/stodo/marimo/marimo-temperature-monitor/* /var/www/marimo/
sudo chown -R www-data:www-data /var/www/marimo/
```

**3. index.htmlが表示される問題**
```bash
# 不要なindex.htmlファイルを削除
sudo rm -f /var/www/marimo/index.html

# Apache設定でDirectoryIndexを無効化していることを確認
grep -i "DirectoryIndex disabled" /etc/apache2/sites-available/marimo-temperature-monitor.conf
```

#### デバッグコマンド

**エラーログの確認:**
```bash
# リアルタイムでエラーログを監視
sudo tail -f /var/log/apache2/marimo_error.log

# アクセスログも確認
sudo tail -f /var/log/apache2/marimo_access.log
```

**Apache設定の確認:**
```bash
# 設定ファイルの構文チェック
sudo apache2ctl configtest

# 有効なサイトの確認
sudo a2ensite

# Apacheの状態確認
sudo systemctl status apache2
```

**Python環境のテスト:**
```bash
# www-dataユーザーでモジュールインポートをテスト
sudo -u www-data python3 -c "import sys; sys.path.insert(0, '/var/www/marimo/'); import app; print('Import successful')"

# 必要なパッケージの確認
python3 -c "import flask; print('Flask OK')"
python3 -c "import w1thermsensor; print('w1thermsensor OK')"
```

**権限の確認:**
```bash
# ファイル権限の確認
ls -la /var/www/marimo/

# www-dataユーザーのグループ確認
groups www-data

# センサーアクセス権限の確認
ls -la /sys/bus/w1/devices/
```

#### パフォーマンス監視

**リソース使用量の確認:**
```bash
# CPU・メモリ使用量
top

# Apache プロセスの確認
ps aux | grep apache

# ディスク使用量
df -h
```

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
- **Web Server**: Apache + mod_wsgi (本番環境)
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