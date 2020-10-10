from django.core.management import BaseCommand

from sort_app.factories import ColorFactory, AppleFactory, UserFactory


class Command(BaseCommand):
    def handle(self, *args, **options):
        UserFactory()

        red = ColorFactory(name='赤')
        yellow = ColorFactory(name='黄')
        green = ColorFactory(name='緑')

        AppleFactory(name='祝', color=green, breeding='不明', season=8,
                     born_in_nagano=False)
        AppleFactory(name='夏あかり', color=red, breeding='さんさ x 陽光', season=8,
                     born_in_nagano=True)
        AppleFactory(name='シナノレッド', color=red, breeding='ツガル x ビスタベラ', season=8,
                     born_in_nagano=True)

        AppleFactory(name='ブラムリー', color=green, breeding='不明', season=9,
                     born_in_nagano=False)
        AppleFactory(name='トキ', color=yellow, breeding='王林 x 紅月', season=9,
                     born_in_nagano=False)
        AppleFactory(name='もりのかがやき', color=yellow, breeding='ツガル x ガラ', season=9,
                     born_in_nagano=False)
        AppleFactory(name='ツガル', color=red, breeding='ゴ－ルデンデリシャス x 紅玉', season=9,
                     born_in_nagano=False)
        AppleFactory(name='シナノドルチェ', color=red, breeding='ゴールデンデリシャス x 千秋', season=9,
                     born_in_nagano=True)

        AppleFactory(name='秋映', color=red, breeding='千秋 x ツガル', season=10,
                     born_in_nagano=True)
        AppleFactory(name='シナノスイート', color=red, breeding='フジ x ツガル', season=10,
                     born_in_nagano=True)

        AppleFactory(name='グラニースミス', color=green,
                     breeding='Malus domestica x Malus sylvestris', season=11,
                     born_in_nagano=False)
        AppleFactory(name='王林', color=yellow, breeding='ゴ－ルデンデリシャス x 印度', season=11,
                     born_in_nagano=False)
        AppleFactory(name='フジ', color=red, breeding='国光 x デリシャス', season=11,
                     born_in_nagano=False)
        AppleFactory(name='シナノゴールド', color=yellow, breeding='ゴ－ルデンデリシャス x 千秋',
                     season=11, born_in_nagano=True)

        print('投入完了')
