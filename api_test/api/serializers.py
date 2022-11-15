from rest_framework import serializers
from .models import Category, Transactions
from users.models import User


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Category
        fields = ('id', 'name', 'owner',)

class UserSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model=User
        fields = ('id', 'salary', 'category')

    def get_category(self, obj):
        customer_account_query = Category.objects.filter(
            owner_id=obj.id)
        serializer = CategorySerializer(customer_account_query, many=True)
        return serializer.data

class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = ("amount", 'category', 'organization', 'description', 'user')




