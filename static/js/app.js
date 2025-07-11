// マリモ水温モニターのJavaScriptコード

document.addEventListener('DOMContentLoaded', function() {
    // 温度表示要素が存在する場合のみ実行
    if (document.getElementById('temperature')) {
        function fetchTemperature() {
            fetch('/api/temperature')
                .then(response => response.json())
                .then(data => {
                    // 温度の値のみを更新（°Cは重複しないように）
                    document.getElementById('temperature').innerText = data.temperature;
                    
                    // ステータスを更新
                    const statusText = document.querySelector('.status-text');
                    if (statusText) {
                        statusText.innerText = '最終更新: ' + new Date().toLocaleTimeString('ja-JP');
                    }
                })
                .catch(error => {
                    console.error('温度取得エラー:', error);
                    const statusText = document.querySelector('.status-text');
                    if (statusText) {
                        statusText.innerText = '接続エラー';
                    }
                });
        }

        // 5秒ごとに温度を更新
        setInterval(fetchTemperature, 5000);
        fetchTemperature(); // 初回実行
    }
});