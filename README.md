## イントロ
タイトルの通りです。
例として今回紹介するチケット管理システムの場合、従業員がサブミットしたチケットに従業員の名前が自動でつくようにしたいという事ですね。
この場合に従業員モデルですべての従業員をドロップダウンで表示するのは無駄ですよね。

では早速やり方を紹介していきます。

## ライブラリ

https://django-crum.readthedocs.io/en/latest/#
今回はDjango-CRUMというライブラリを使っていきます。
CRUMはCurrent Request User Middlewareの略だそうです。

ちなみにGitHubリポは66スターしかないのでちょっと不安でした。
しかし、このオープンソースの提供者はアメリカのノースカロライナ州にある9分だけっていう会社で管理しているようです。
まあ、いいか。



とりあえずインストールの仕方を説明します。
コマンドラインから↓
```
pip install django-crum
```

次にSettings.pyのミドルウェアの最後らへんにこれを追加しましょう↓
```
MIDDLEWARE += ('crum.CurrentRequestUserMiddleware',)
```

get_current_user()
今回はこのget_current_user()というモジュールを使用して現在Djangoアプリにログインしているユーザーを取得していきます。
こちらが参考のコードになります。
```
from django.db import models
from crum import get_current_user

class Thing(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', blank=True, null=True,
                                   default=None)
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey('auth.User', blank=True, null=True,
                                    default=None)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super(Thing, self).save(*args, **kwargs)
```

では、この後にDjangoのモデルをマイグレーションし直し、Adminパネルでログインし、新しいデータを作成しましょう。
データをセーブするとDjangoにログインしたユーザーでセーブされましたね！

お疲れ様です！
