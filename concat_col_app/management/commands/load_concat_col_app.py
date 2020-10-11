from django.core.management import BaseCommand

from concat_col_app.factories import ColorFactory, AppleFactory


class Command(BaseCommand):
    def handle(self, *args, **options):
        red = ColorFactory(name='赤')
        yellow = ColorFactory(name='黄')
        green = ColorFactory(name='緑')

        AppleFactory(name='祝', color=green, breeding='不明')
        AppleFactory(name='夏あかり', color=red, breeding='さんさ x 陽光')
        AppleFactory(name='シナノレッド', color=red, breeding='ツガル x ビスタベラ')
        AppleFactory(name='ブラムリー', color=green, breeding='不明')
        AppleFactory(name='トキ', color=yellow, breeding='王林 x 紅月')
        AppleFactory(name='もりのかがやき', color=yellow, breeding='ツガル x ガラ')
        AppleFactory(name='ツガル', color=red, breeding='ゴ－ルデンデリシャス x 紅玉')
        AppleFactory(name='シナノドルチェ', color=red, breeding='ゴールデンデリシャス x 千秋')

        AppleFactory(name='秋映', color=red, breeding='千秋 x ツガル')
        AppleFactory(name='シナノスイート', color=red, breeding='フジ x ツガル')

        AppleFactory(name='グラニースミス', color=green,
                     breeding='Malus domestica x Malus sylvestris')
        AppleFactory(name='王林', color=yellow, breeding='ゴ－ルデンデリシャス x 印度')
        AppleFactory(name='フジ', color=red, breeding='国光 x デリシャス')
        AppleFactory(name='シナノゴールド', color=yellow, breeding='ゴ－ルデンデリシャス x 千秋')

        print('投入完了')
