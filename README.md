# Alembic を CodeBuild で動かしてみる

## poetry の設定変更

pylint で追加ライブラリを認識するのに、poetry はプロジェクトのルートディレクトリにライブラリをインストールする方が使いやすいので、poetry の設定を変えます。

```bash
poetry config virtualenvs.in-project true
poetry env remove python # 既存の仮想環境を削除
```

## ライブラリのインストール

```bash
poetry install
```
