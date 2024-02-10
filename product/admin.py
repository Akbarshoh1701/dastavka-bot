from django.contrib import admin
from product.models import Product, Category, SubCategory
# Register your models here.


class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1


class ProductInline(admin.TabularInline):
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = "id", "title"
    inlines = [SubCategoryInline]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']
    list_display_links = ['id', 'title']
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_display_links = ['id', 'title', 'price']
    #

