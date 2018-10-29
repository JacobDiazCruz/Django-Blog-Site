from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
# from cart.views import cart_pending_orders, add_to_cart
from cart.views import cart_pending_orders, add_to_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('register/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    # path('cart/', cart_pending_orders.as_view(), name='cart')
    # path('/cart/<int:pk>/', add_to_cart.as_view(), name='add-to-cart')
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
