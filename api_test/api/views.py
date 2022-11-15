from rest_framework.generics import (ListCreateAPIView,UpdateAPIView, CreateAPIView, ListAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from api.models import Category
from users.models import User
from api.license import IsOwnerProfileOrReadOnly
from api.serializers import UserSerializer, CategorySerializer, TransactionsSerializer
from rest_framework import filters



class UserProfileListCreateView(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

class CategoryCreateView(CreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsOwnerProfileOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryUpdateView(UpdateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryDelateView(DestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class userProfileDetailView(ListAPIView):
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]
    def get(self, request, *args, **kwargs):
        self.queryset=User.objects.filter(id=self.request.user.id)
        self.serializer_class=UserSerializer
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)

class UserTransactionsDetailView(ListAPIView):
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)

    def get(self, request, *args, **kwargs):
        self.queryset=User.objects.filter(id=self.request.user.id)
        self.serializer_class=TransactionsSerializer
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)
    
class TransactionsCreateView(CreateAPIView):
    permission_classes=[IsOwnerProfileOrReadOnly, IsAuthenticated]
    serializer_class=TransactionsSerializer    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        data = dict(request.POST)
        user = User.objects.filter(id = self.request.user.id).values('salary')
        total_sum = int(user[0]['salary']) + int(data['amount'][0])
        user.update(salary = total_sum)
        return self.create(request, *args, **kwargs)

class TransactionsWriteOffView(CreateAPIView):
    permission_classes=[IsOwnerProfileOrReadOnly, IsAuthenticated]
    serializer_class=TransactionsSerializer    

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        data = dict(request.POST)
        user = User.objects.filter(id = self.request.user.id).values('salary')
        total_sum = int(user[0]['salary']) - int(data['amount'][0])
        user.update(salary = total_sum)
        return self.create(request, *args, **kwargs)

