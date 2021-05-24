from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from rest_live.routers import RealtimeRouter
from django.contrib import admin
from django.urls import path, include


router = RealtimeRouter()

websockets = AuthMiddlewareStack(
    URLRouter([
        path("ws/subscribe/", router.as_consumer(), name="subscriptions"), 
        path('admin/', admin.site.urls),
        path('api/', include('profiles.urls'))
    ])
)
application = ProtocolTypeRouter({
    "websocket": websockets
})