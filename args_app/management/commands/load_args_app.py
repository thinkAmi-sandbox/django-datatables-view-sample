from django.core.management import BaseCommand

from args_app.factories import ColorFactory, AppleFactory


class Command(BaseCommand):
    def handle(self, *args, **options):
        red = ColorFactory(name='赤')
        yellow = ColorFactory(name='黄')
        green = ColorFactory(name='緑')

        AppleFactory(name='祝', color=green)
        AppleFactory(name='夏あかり', color=red)
        AppleFactory(name='シナノレッド', color=red)
        AppleFactory(name='ブラムリー', color=green)
        AppleFactory(name='トキ', color=yellow)
        AppleFactory(name='もりのかがやき', color=yellow)
        AppleFactory(name='ツガル', color=red)
        AppleFactory(name='シナノドルチェ', color=red)

        AppleFactory(name='秋映', color=red)
        AppleFactory(name='シナノスイート', color=red)

        AppleFactory(name='グラニースミス', color=green)
        AppleFactory(name='王林', color=yellow)
        AppleFactory(name='フジ', color=red)
        AppleFactory(name='シナノゴールド', color=yellow)

        print('投入完了')
