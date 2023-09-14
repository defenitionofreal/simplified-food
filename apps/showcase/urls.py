from django.urls import path, include
from apps.showcase.api import (
    analytics,
    design,
    social_links,
    extra_phone_client_list,
    work_hours_viewset,
    requisites,
    delivery_client_list,
    address_list,
    delivery_zone_list,
    payment_type_list,
    queue_screen)

from apps.showcase.api import (menu_viewset, category_viewset, banners_viewset)

from apps.showcase.api.customer_actions import (delivery_info_create)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('menu', menu_viewset.MenuViewSet, basename='menu')
router.register('categories', category_viewset.CategoryViewSet, basename='categories')
router.register('banners', banners_viewset.BannerViewSet, basename='banners')
router.register('work-hours', work_hours_viewset.WorkHoursViewSet, basename='work-hours')


app_name = 'showcase'

urlpatterns = [
    path('<str:domain>/', include(router.urls)),
    # main page
    path('<str:domain>/analytics/', analytics.AnalyticsAPIView.as_view()),
    path('<str:domain>/design/', design.DesignAPIView.as_view()),
    # company info
    path('<str:domain>/social-links/', social_links.SocialLinksAPIView.as_view()),
    path('<str:domain>/extra-phones/', extra_phone_client_list.ExtraPhoneClientListAPIView.as_view()),
    path('<str:domain>/requisites/', requisites.RequisitesAPIView.as_view()),
    # order (cart) detail/add/delete
    path('<str:domain>/order/', include('apps.order.urls', namespace='order')),
    # payment
    path('payment/', include('apps.payment.urls', namespace='payment')),
    # delivery todo refactor all delivery
    path('<str:domain>/delivery/', delivery_client_list.DeliveryClientListAPIView.as_view()),
    path('<str:domain>/delivery-info/add/', delivery_info_create.DeliveryInfoAPIView.as_view()),
    path('<str:domain>/address/', address_list.AddressListAPIView.as_view()),
    path('<str:domain>/delivery-zone/', delivery_zone_list.DeliveryZoneListAPIView.as_view()),
    # payment
    path('<str:domain>/payment/type/', payment_type_list.PaymentTypeClientListAPIView.as_view()),
]
