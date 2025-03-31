# This file can import all model classes so they can be registered easily

from .user_model import User
from .vendor_model import Vendor
from .product_model import Product
from .order_model import Order

# Then you can do e.g. Base.metadata.create_all(...) if using base models.
