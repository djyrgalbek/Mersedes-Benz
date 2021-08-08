from .models import Category


def get_category(request):
    categories = Category.objects.filter(parent__isnull=True)
    return {'categories': categories}