from django.test import TestCase
from .models import Product, Manufacturer, Category
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.


class ModelsTest(TestCase):
    """Models test"""

    def test_save_models(self):
        manufacturer = Manufacturer.objects.create(name='Nike', slug='nike')
        category = Category.objects.create(name='Кроссовки', slug='krossovki')
        product = Product.objects.create(name='Air Max 270', slug='air-max-270', price=1000, stock=10,
                                            manufacturer=manufacturer, category=category)

        self.assertEqual(product.name, 'Air Max 270')
        self.assertEqual(product.slug, 'air-max-270')
        self.assertEqual(product.price, 1000)
        self.assertEqual(product.stock, 10)

        self.assertEqual(manufacturer.name, 'Nike')
        self.assertEqual(manufacturer.slug, 'nike')

        self.assertEqual(category.name, 'Кроссовки')
        self.assertEqual(category.slug, 'krossovki')

        self.assertEqual(product.get_absolute_url(), reverse('shop:product_detail', args=[product.id, product.slug]))
        self.assertEqual(product.get_add_to_cart_url(), reverse('shop:add_to_cart', args=[product.id]))

        self.assertEqual(product.get_manufacturer_url(), reverse('shop:manufacturer_products', args=[manufacturer.slug]))
        self.assertEqual(product.get_category_url(), reverse('shop:category_products', args=[category.slug]))

        self.assertEqual(product.get_add_to_wishlist_url(), reverse('shop:add_to_wishlist', args=[product.id]))
        self.assertEqual(product.get_remove_from_wishlist_url(), reverse('shop:remove_from_wishlist', args=[product.id]))

        self.assertEqual(product.get_add_to_compare_url(), reverse('shop:add_to_compare', args=[product.id]))
        self.assertEqual(product.get_remove_from_compare_url(), reverse('shop:remove_from_compare', args=[product.id]))

        self.assertEqual(product.get_add_to_favorite_url(), reverse('shop:add_to_favorite', args=[product.id]))
        self.assertEqual(product.get_remove_from_favorite_url(), reverse('shop:remove_from_favorite', args=[product.id]))

