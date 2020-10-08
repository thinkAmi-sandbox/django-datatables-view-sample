from django.core.management import BaseCommand

from fk_app.factories import FamilyFactory, SpeciesFactory, CultivarsFactory


class Command(BaseCommand):
    def handle(self, *args, **options):
        convolvulaceae = FamilyFactory(name='ヒルガオ科')
        rosaceae = FamilyFactory(name='バラ科')

        sweet_potato = SpeciesFactory(name='サツマイモ', family=convolvulaceae)
        apple = SpeciesFactory(name='リンゴ', family=rosaceae)
        pear = SpeciesFactory(name='梨', family=rosaceae)

        CultivarsFactory(name='紅あずま', species=sweet_potato)
        CultivarsFactory(name='紅はるか', species=sweet_potato)
        CultivarsFactory(name='安納芋', species=sweet_potato)
        CultivarsFactory(name='シルクスイート', species=sweet_potato)

        CultivarsFactory(name='二十世紀', species=pear)
        CultivarsFactory(name='南水', species=pear)
        CultivarsFactory(name='サザンスイート', species=pear)

        CultivarsFactory(name='フジ', species=apple)
        CultivarsFactory(name='シナノゴールド', species=apple)
        CultivarsFactory(name='トキ', species=apple)
        CultivarsFactory(name='秋映', species=apple)
        CultivarsFactory(name='もりのかがやき', species=apple)

        print('投入完了')

