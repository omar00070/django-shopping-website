from django.urls import path
from .views import ProductListView, ProductCreateView
from . import views as shop_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('new-product/', ProductCreateView.as_view(), name='product-create'),
    path('about/', shop_views.about, name='about'),
    path('collection', shop_views.collection, name='collection')
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)