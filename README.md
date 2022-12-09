# thesis-template

## Usage

1. 各ディレクトリを以下のようにリネームしてください。

   - `/texfiles_sample` -> `/texfiles`
   - `/settings_sample` -> `/settings`
   - `/figs_sample` -> `/figs`

2. `abstract_sample.tex`と`main_sample.tex`末尾の`_sample`を削除してください。
3. `abstract.tex`と`main.tex`中の`\newcommand{\texfiles}{texfiles_sample}`と`\newcommand{\settings}{settings_sample}`を編集してください。

   ```main_sample.tex
   \newcommand{\texfiles}{texfiles_sample} % change this line: "_sample" -> ""
   \newcommand{\settings}{settings_sample} % change this line: "_sample" -> ""
   ```

4. 文献スタイルを変更する場合は，`/texfiles/99.references.tex`中の`\newcommand{\citationstyle}{bst/jIEEEtran}`を編集してください。

   ```texfiles_sample/99.references.tex
   \newcommand{\citationstyle}{bst/jIEEEtran}
   ```

以上を一括で行うには，`setup.py`を実行してください。

   ```
   python3 setup.py
   ```
