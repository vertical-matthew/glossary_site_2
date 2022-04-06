from django.core.management.base import BaseCommand
import pandas as pd
from block.models import Material, Color, Category, Condition, Geometry, Unit, Symbol, Photo, Block
import uuid
# https://www.youtube.com/watch?v=TL6qLQoJLsw


class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Database Connections here
        df = pd.read_csv("VA Codekey library.csv", encoding='latin-1')

        # for AGE, FARE, NAME in zip(df.Age, df.Fare, df.Name):
        #     models = Contact(age=AGE, fare=FARE, name=NAME)
        #     models.save()

        Material.objects.all().delete()
        Color.objects.all().delete()
        Category.objects.all().delete()
        for MATERIAL in df.Material.unique():
            models = Material(title=MATERIAL)
            models.save()

        self.stdout.write(f"Populated {Material.objects.all().count()} materials")

        color_df = df.drop_duplicates(subset=['Color'])
        for COLOR, R, G, B in zip(color_df.Color, color_df.R, color_df.G, color_df.B):
            models = Color(name=COLOR, R=R, G=G, B=B)
            models.save()

        self.stdout.write(f"Populated {Color.objects.all().count()} colors")
        cat_df = df.drop_duplicates(subset=["Category"])
        for CATEGORY, COLOR in zip(cat_df.Category, cat_df.Color):
            color_id = Color.objects.get(name=COLOR)
            models = Category(title=CATEGORY, color=color_id)
            models.save()

        self.stdout.write(f"Populated {Category.objects.all().count()} categories")
        cond_df = df.drop_duplicates(subset=["Condition"])

        Condition.objects.all().delete()
        for CONDITION, CODE in zip(cond_df.Condition, cond_df.Code):
            models = Condition(title=CONDITION, code=CODE)
            models.save()

        self.stdout.write(f"Populated {Condition.objects.all().count()} conditions")

        Geometry.objects.all().delete()
        geo_df = df.drop_duplicates(subset=["Geometry Type"])
        # for GEOMETRY, AMT, SEV in zip(geo_df["Geometry Type"], geo_df["Amount Units"], geo_df["Severity Units"]):
        #     models = Geometry(title=GEOMETRY, amount_units=AMT, severity_units=SEV)
        #     models.save()
        for GEOMETRY in geo_df["Geometry Type"]:
            models = Geometry(title=GEOMETRY)
            models.save()

        self.stdout.write(f"Populated {Geometry.objects.all().count()} geometries")
        Unit.objects.all().delete()
        amt = df["Amount Units"].unique()
        sev = df["Severity Units"].unique()
        unique_units = set([*amt,*sev])

        for unit in unique_units:
            models = Unit(title=unit)
            models.save()

        self.stdout.write(f"Populated {Unit.objects.all().count()} units")

        Symbol.objects.all().delete()
        for symb in df.ChartSymbol.unique():
            models = Symbol(title=symb)
            models.save()

        self.stdout.write(f"Populated {Symbol.objects.all().count()} symbols")


#### adding blocks
        Block.objects.all().delete()
        dd = df.drop_duplicates(subset=["bc"])

        for NAME, DESC, MAT, CAT, COND, SYM, AMT, SEV in zip(dd.bc, dd.Description, dd.Material, dd.Category, dd.Condition, dd.ChartSymbol, dd["Amount Units"], dd["Severity Units"]):
            MAT = Material.objects.get(title=MAT)
            CAT = Category.objects.get(title=CAT)
            COND = Condition.objects.get(title = COND)
            SYM = Symbol.objects.get(title = SYM)
            AMT = Unit.objects.get(title=AMT)
            SEV = Unit.objects.get(title=SEV)
            SLUG = uuid.uuid1()
            models = Block(name=NAME, slug=SLUG, description=DESC, material=MAT, category=CAT, condition=COND, symbol=SYM, amount_units=AMT, severity_units=SEV)
            models.save()


        self.stdout.write(f"Populated {Block.objects.all().count()} blocks")

        Photo.objects.all().delete()
        pics = pd.read_json("photodf.json")
        for BLOCK, PIC in zip(pics.block, pics.photo):
            BLOCK = Block.objects.get(name=BLOCK)
            models = Photo(title=PIC, block=BLOCK)
            models.save()

        self.stdout.write(f"Populated {Photo.objects.all().count()} photos")




        self.stdout.write(f"Database has been cleaned and repopulated")
