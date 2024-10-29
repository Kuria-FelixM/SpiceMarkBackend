from rest_framework import serializers
from .models import (
    User,Vendor,Category,Product,Order,OrderItem,Cart,CartItem,Shipping,Payment
    ,Coupon,Review,WishList,Notification,Blog,Contact,FAQ,Analytics,Configuration,
    Tax,Subscription,Refund)
from .serializers import (
    UserSerializer,VendorSerializer,CategorySerializer,ProductSerializer
    ,OrderSerializer,OrderItemSerializer,CartSerializer,CartItemSerializer
    ,ShippingSerializer,PaymentSerializer,CouponSerializer,ReviewSerializer
    ,WishListSerializer,NotificationSerializer,BlogSerializer,ContactSerializer
    ,FAQSerializer,AnalyticsSerializer,ConfigurationSerializer,TaxSerializer
    ,SubscriptionSerializer,RefundSerializer
)

class UserViewSet(viewset.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VendorViewSet(viewset.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class CategoryViewSet(viewset.ModelViewSet):    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewset.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewset.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewset.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class CartViewSet(viewset.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewset.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class ShippingViewSet(viewset.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

class PaymentViewSet(viewset.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer    

class CouponViewSet(viewset.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

class ReviewViewSet(viewset.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class WishListViewSet(viewset.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer

class NotificationViewSet(viewset.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class BlogViewSet(viewset.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ContactViewSet(viewset.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class FAQViewSet(viewset.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class AnalyticsViewSet(viewset.ModelViewSet):   
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer

class ConfigurationViewSet(viewset.ModelViewSet):   
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer

class TaxViewSet(viewset.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer

class SubscriptionViewSet(viewset.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class RefundViewSet(viewset.ModelViewSet):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer