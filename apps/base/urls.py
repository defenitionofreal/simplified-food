from django.urls import path

from . import views
from .api import (user_view,
                  yoomoney_notification,
                  session
                  )

app_name = 'base'

urlpatterns = [
    path('session/', session.SessionAPIView.as_view(), name='session'),

    path('', views.index, name='index'),
    # check payment status (yoomoney)
    # TODO: (yoomoney) убрать в более базовый урл без приставки auth
    path('yoomoney-notification/', yoomoney_notification.YooMoneyHttpNotificationAPIView.as_view())
]


