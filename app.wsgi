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
