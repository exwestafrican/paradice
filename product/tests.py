from django.test import TestCase

# Create your tests here.
from utils.constants import BLACK, EXTRA_LARGE, SMALL, WHITE

Product.objects.create(
    name="Iron Fist",
    price=2000,
    units_available=4,
    product_variation={"sizes": [SMALL, EXTRA_LARGE], "colors": [BLACK, WHITE]},
)

product = Product.objects.first()

Image.objects.create(
    product=product,
    img_variation={
        "sm": "",
        "md": "https://res.cloudinary.com/paradice-parade/image/upload/v1620471667/3_Floral_pattern_revere_Front_lowsize_lcapu7.png",
        "lg": "",
    },
)
