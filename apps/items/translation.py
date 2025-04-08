from modeltranslation import translator

from apps.items.models import Category, Item, SubCategory


@translator.register(Category)
class CategoryTranslations(translator.TranslationOptions):
    fields = ("name",)


@translator.register(Item)
class ItemsTranslations(translator.TranslationOptions):
    fields = (
        'image',
        'title',
        'description',
        'price',
        'production',
        'model',
        'is_available',
        'color',
    )


@translator.register(SubCategory)
class SubCategoryTranslations(translator.TranslationOptions):
    fields = ('category', 'name')