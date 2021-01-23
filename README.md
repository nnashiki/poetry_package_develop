poetryでライブラリ開発のフロー

- https://gist.github.com/nnashiki/35dc67d787079e5b8094c0426fcdeec7

# はじめに
- モジュール、パッケージ、ライブラリの違い
   - https://netdekagaku.com/module-package-lybrary/
- アプリ、ライブラリの違い
   - https://www.m3tech.blog/entry/python-packaging
   - 個人的にはライブラリライクに作ってエンドポイント(cli, webserver)を分けるのが良い
- [Pythonインポート周り徹底理解への道 - Qiita](https://qiita.com/papi_tokei/items/bc34d798dc7a6d49df30)
    - インポートしたパッケージ内のモジュールは自動的にインポートされない
- poetry を使わない場合
    - setup.cfg, setup.py
       - パッケージ名
       - バージョン
       - 依存関係
    - MANIFEST.in 
       - 配布物に含めるものを指定

# poetry の準備
- [pipxを使用したpoeryの導入.md](https://gist.github.com/nnashiki/2e5b8e70f33cad2c978e42a80d5c066b)
- 設定確認
   - `poetry config --list`

# 初期化
- プロジェクトトップに移動する
- `cat /Users/niten.nashiki/ghq/github.com/github/gitignore/Python.gitignore >> .gitignore`
    - `github/gitignore/Python.gitignore` からignoreを作成してキャッシュを入れないようにする
- `poetry new workspace --name ecdemo`
   - パッケージを作成する
- `cd workspace`
- `poetry shell`
    - virtual env が作成される
- エディタのインタープリタをvenvに変更する
- `poetry add fire`
    - fireパッケージを仮想環境にinstallする
- `poetry show`
    - 仮想環境にinstallされているパッケージを確認する

# 続きから
- `poetry install`
   - toml, lock の内容をinstallする
- `pytest tests/test_ecdemo.py`
    - テストが成功する事を確認する

# CI や docker での実行

- `cd workspace`
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
   -  toml に tool.black, tool.isort を追加する
   - `mypy ecdemo`
   - `black -l 100 ecdemo`
   - `black -l 100 --check ecdemo`
   - `isort ecdem --diff`
- list format ツールの組み合わせを設定
    - https://blog.hirokiky.org/entry/2019/06/03/202745
- list format のコマンドを Makefile にまとめる
    - touch Makefile

# 注意点
- 現段階ではsubdirctoryにsetup.pyがあるやつはpoetry addできない
   - [python 3.x - How to add subfolder package in poetry for a git repository? - Stack Overflow](https://stackoverflow.com/questions/63182754/how-to-add-subfolder-package-in-poetry-for-a-git-repository)
   - > nstalling packages in a subfolder of git is currently not supported by poetry. There is already a feature request for it (#755) and I started to work on that (#1822).
       - [Install package from Version Control System (git) where setup.py is in subdirectory · Issue #1915 · python-poetry/poetry](https://github.com/python-poetry/poetry/issues/1915)
       - [support git subfolder (#755) by finswimmer · Pull Request #1822 · python-poetry/poetry](https://github.com/python-poetry/poetry/pull/1822)
       - [support git subfolder (#755) by finswimmer · Pull Request #2242 · python-poetry/poetry](https://github.com/python-poetry/poetry/pull/2242)

# 参考
- poetry
    - [日本語](https://cocoatomo.github.io/poetry-ja/)
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

