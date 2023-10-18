# WebScreenshot 

Dockerで使い指定したURLのスクリーンショットを作成  
スクリーンショットの取得方法はPlaywright for pythonを使用しています

## 推奨環境
* Ubuntu 22.04
* Docker

## 使い方

1. コンテナイメージの作成
    ```
    cd WebScreenshot
    sudo docker build -t webscreenshot .
    ```

2. コンテナ起動
    ```
    sudo docker container run -i -v ./screenshot:/screenshot --rm webscreenshot [URL]
    ```
    ※ ./screenshotの部分でスクリーンショットを作成するディレクトリを指定しているので環境に合わせて変更する
