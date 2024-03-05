from .models import Category


def mylinks(request):
    links=Category.objects.all()
    return dict(links=links)