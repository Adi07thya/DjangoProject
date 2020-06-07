from rest_framework.routers import DefaultRouter

from . import apiview

""" connecting to DefaultRouter where  each-viewsets is registered with the router with given prefix """
router = DefaultRouter()
router.register(r'Customer', apiview.CustomerViewset)
router.register(r'Bookmark', apiview.BookmarkViewset)
router.register(r'users', apiview.UserViewSet)
