from django.core.management import BaseCommand

from search_app.factories import ColorFactory, AppleFactory


class Command(BaseCommand):
    def handle(self, *args, **options):
        red = ColorFactory(name='赤')
        yellow = ColorFactory(name='黄')
        green = ColorFactory(name='緑')

        AppleFactory(name='祝', color=green, born_in_nagano=False)
        AppleFactory(name='夏あかり', color=red, born_in_nagano=True)
        AppleFactory(name='シナノレッド', color=red, born_in_nagano=True)
        AppleFactory(name='ブラムリー', color=green, born_in_nagano=False)
        AppleFactory(name='トキ', color=yellow, born_in_nagano=False)
        AppleFactory(name='もりのかがやき', color=yellow, born_in_nagano=False)
        AppleFactory(name='ツガル', color=red, born_in_nagano=False)
        AppleFactory(name='シナノドルチェ', color=red, born_in_nagano=True)
        AppleFactory(name='秋映', color=red, born_in_nagano=True)
        AppleFactory(name='シナノスイート', color=red, born_in_nagano=True)
        AppleFactory(name='グラニースミス', color=green, born_in_nagano=False)
        AppleFactory(name='王林', color=yellow, born_in_nagano=False)
        AppleFactory(name='フジ', color=red, born_in_nagano=False)
        AppleFactory(name='シナノゴールド', color=yellow, born_in_nagano=True)

        print('投入完了')
