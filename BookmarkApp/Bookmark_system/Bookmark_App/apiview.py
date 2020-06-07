from rest_framework import generics
from rest_framework import authentication, permissions, viewsets,filters
from .models import Customer,Bookmark,CustomerBookmark
from .serializer import CustomerSerializer,BookmarkSerializer,CustomerBookmarkSerializer,UserSerializer
from django.contrib.auth import get_user_model


class DefaultsMixin(object):
    """ Default mixin is used to develop default setting like permissions,authentication,filters"""

    authentication_classes = (authentication.BasicAuthentication,authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (

        filters.SearchFilter,
        filters.OrderingFilter,
    )

User = get_user_model()



class BookmarkViewset(DefaultsMixin, viewsets.ModelViewSet):
    """ API end points which does all the CRUD functionalities for Bookmark Model including search and sort fields"""

    queryset = Bookmark.objects.all()
    serializer_class= BookmarkSerializer
    search_fields= ('title','urls','source_name')
    ordering_fields = '__all__'


class CustomerViewset(DefaultsMixin, viewsets.ModelViewSet):
    """ API end point which does all the CRUD functionalities for Customers Model including search and sort fields"""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    search_fields = ('id','latitude','longitude')
    ordering_fields = '__all__'



class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    """ API end point which can be used to retrieve Authorized User """

        
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
