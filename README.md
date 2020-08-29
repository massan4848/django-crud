以下のdjango解説動画を利用して日記アプリをつくった  
https://www.youtube.com/watch?v=2ttBx0pOLP0&list=PL8EQJPo_jL6tyqlYPB4xaH4b0iC21wETt&index=1  

仮想環境を使っているため、`pipenv shell`で仮想環境に入ってから、`python manage.py runserver`でアプリを確認できる。  
会員登録と記事編集ができる。  
作成していないページあり。  



*** 以下メモ ***  

# startproject状態でのファイルの説明 sec0
​​manage.py コマンド   
\_\_init\_\_.py パッケージ  
setting.py  
url.py urlをつくる  
wisgi.py  

# djangoの構成 sec1
プロジェクトに複数のアプリをつくる。  
共通のトップページをつくる。  
## ファイルの説明
djangoの練習フォルダdjango-crudにはconfigというプロジェクトがある。  
そして、blogというアプリケーションが入っている。 

# modelの設計(ORM) sec 2
object  
Relational  
Mapper  
object言語をdatabase言語に変換  

# migration sec 3
model.pyを変更したらmigrationする。  
`python manage.py makemigration`  

migrate : (migration file から)データベースを自動でつくる。  
`python manage.py migrate`  

違い：  
https://qiita.com/frosty/items/8c715a53d7920c9cd1eb  
makemigration: model.pyの情報をもとに、マイグレーションファイルをつくる。  
migrate: マイグレーションファイルの情報をもとにデータベースの構成を変更  

admin　pageは /admin  

views.py 作成したpostを表示させる。  
記述パターン
- function based view
- class based view (今回利用) 　 

view.py内でclassをつくるときはdjango.views.genericからクラスを継承させる。  
つまり、クラスに存在する変数の確認が必要になる。[1]

urlとファイルをつなぐために、url.pyにurlを追加する。  
どんどんurlを加えると長くなるので、別の場所で作って、それをincludeする。  

urlを書くときに、CBVの場合は.as_view()が必要  
[1] ListViewでのtemplate_nameでは自分で作ったtemplateフォルダ内のファイルにアクセスする。
今回は、templateフォルダ内に新たにblogフォルダをつくり、home.htmlを作っている。

# Frontend sec4
front end はテンプレートを使っていく。  
setting.pyに`STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]`を追記  
pathを書き換えずに済むようにする。  
static folderにjs,css,imgファイルを作る。全体で統一したものをつくる。  
https://www.free-css.com/  
https://www.free-css.com/free-css-templates/page244/debut
これから、css,js,imgをダウンロード  
___linkがdjango用ではないので、変更する___  
書き方check  
___`{% load static %}`を最初の行に入れること___  
jpgは"static/"を加える。
png,css,jsは"{%static "XXX" %}"のように書く。

# filter  sec5
ログイン機能
formやurlが必要   
新しくアプリを作って管理する。  
___新しくアプリを作ったらsetting.pyを編集___   

# signup sec6  
動画を見て
https://www.youtube.com/watch?v=kGFGJzu3hsM&list=PL8EQJPo_jL6tyqlYPB4xaH4b0iC21wETt&index=7   
一度書いたhtmlを継承させると、django用にhtmlを書き直す手間が減る。  
`{% extend %}`  
djangoにはformタグがあるので、利用を考える。  
`<form method='POST' role="form" action="" class="login-form">`  
`    {% csrf_token %}`  
`    {{ form }}`  
`    <button type="submit" class="btn">Sign me up!</button>`  
`</form>`   

# Crispy Form sec 7
formを見やすくするために、django-crispy-formsを導入  
https://django-crispy-forms.readthedocs.io/en/latest/install.html  
pip install のあとも、setting.pyに追加 
思い通りのレイアウトについてのtechnic  
動画で確認   
documentationで知識を入れる必要がある。  

# github sec 8  

# login logout sec 9  
defaultのdjangoログイン機能を使うと、profileというページに飛ぶので、settingを変更  
`LOGIN_REDIRECT_URL = 'blog-home'`  
`LOGIN_URL = 'login'`  

 