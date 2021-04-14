import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

# from many.models import Person, Course, Membership
from unesco.models import Site, Category, Region, State, Iso

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    # Person.objects.all().delete()
    # Course.objects.all().delete()
    # Membership.objects.all().delete()

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        # p, created = Person.objects.get_or_create(email=row[0])
        # c, created = Course.objects.get_or_create(title=row[2])

        # r = Membership.LEARNER
        # if row[1] == 'I':
        #     r = Membership.INSTRUCTOR
        # m = Membership(role=r, person=p, course=c)
        # m.save()


        c, created = Category.objects.get_or_create(name=row[7])
        r, created = Region.objects.get_or_create(name=row[9])
        I, created = Iso.objects.get_or_create(name=row[10])
        s, created = State.objects.get_or_create(name=row[8], iso=I, region=r)

        try:
            y = int(row[3])
        except:
            y = None

        try:
            d = row[1]
        except:
            d = None

        try:
            a = float(row[6])
        except:
            a = None

        try:
            lo = float(row[4])
        except:
            lo = None

        try:
            la = float(row[5])
        except:
            la = None

        site = Site(name=row[0], description=d, justification=row[2], year=y, longitude=lo, latitude=la, area_hectares=a, category=c, state=s, iso=I)
        site.save()



