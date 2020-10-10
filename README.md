poetryで単体のパッケージ開発のフロー

- https://gist.github.com/nnashiki/35dc67d787079e5b8094c0426fcdeec7

# Introduction

- `poetry new ecdemo`
   - パッケージを作成する
- `cd ecdemo`
- `poetry shell`
    - virtual env を作成する
- `poetry add fire`
    - fireパッケージを追加する
- `poetry show`
    - 仮想環境にinstallされているパッケージを確認する
- `pytest tests/test_ecdemo.py`
    - テストが成功する事を確認する
- `cd ../`
    - プロジェクトトップに移動する
- `cat /Users/niten.nashiki/ghq/github.com/github/gitignore/Python.gitignore >> .gitignore`
    - `github/gitignore/Python.gitignore` からignoreを作成してキャッシュを入れないようにする
- `cd ecdemo`
- `poetry export -f requirements.txt --output requirements.txt`
    - 本番用のrequirements.txtを書き出す
- `poetry export -f requirements.txt --dev --output requirements_dev.txt`
- `touch Dockerfile`
    - dockerのテストコンテナを書く
- `docker build . -t ecdemo:0.1`
- `docker run --rm -it ecdemo:0.1`
- CIファイルを書く
