poetryで単体のパッケージ開発のフロー

- https://gist.github.com/nnashiki/35dc67d787079e5b8094c0426fcdeec7

# 初期化
- プロジェクトトップに移動する
- `cat /Users/niten.nashiki/ghq/github.com/github/gitignore/Python.gitignore >> .gitignore`
    - `github/gitignore/Python.gitignore` からignoreを作成してキャッシュを入れないようにする
- `poetry new ecdemo`
   - パッケージを作成する
- `cd ecdemo`
- `poetry shell`
    - virtual env が作成される
- インタープリタをvenvにする
- `poetry add fire`
    - fireパッケージを追加する
- `poetry show`
    - 仮想環境にinstallされているパッケージを確認する

# 続きから
- `poetry install`
   - toml の内容をinstallする
- `pytest tests/test_ecdemo.py`
    - テストが成功する事を確認する

# CI や docker での実行

- `cd ecdemo`
- `poetry export -f requirements.txt --output requirements.txt`
    - 本番用(docker用)のrequirements.txtを書き出す
- `poetry export -f requirements.txt --dev --output requirements_dev.txt`
    - ついでにdev用(docker用)のrequirements.txtを書き出す
- プロジェクトトップに移動する
- `touch Dockerfile`
    - dockerのテストコンテナを書く
- docker をテストrunする
    - `docker build . -t ecdemo:0.1`
    - `docker run --rm -it ecdemo:0.1`
- `mkdir -p .github/workflows`
- CIファイルを書く
   - `touch .github/workflows/lint_build_test.yaml`

# lint とかやってみる
- list format ツールを足す。試す。
   - `poetry add --dev mypy`
   - `poetry add --dev black`
   - `poetry add --dev isort`
   - `poetry show`
   - `mypy ecdemo`
   - `black -l 100 ecdemo`
   - `black -l 100 --check ecdemo`
   - `isort ecdem --diff`
- list format ツールの組み合わせを設定
    - https://blog.hirokiky.org/entry/2019/06/03/202745
- list format のコマンドを Makefile にまとめる
    - touch Makefile

# 参考
- poetry
    - https://cocoatomo.github.io/poetry-ja/cli/#add
- isort
    - https://github.com/PyCQA/isort
- black
    - https://blog.hirokiky.org/entry/2019/06/03/202745
    - https://org-technology.com/posts/python-black.html
    - https://github.com/psf/black
    - https://speakerdeck.com/aodag/pycon-kyushu-2019-pythondefalsekai-fa-woxiao-lu-de-nijin-merutamefalseturushe-ding?slide=18
- github actions
    - https://docs.github.com/ja/free-pro-team@latest/actions/quickstart
    - https://github.com/actions/starter-workflows/blob/main/ci/docker-image.yml
    - https://github.com/actions/starter-workflows/blob/main/ci/pylint.yml

