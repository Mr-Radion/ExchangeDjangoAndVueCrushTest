from abc import ABC  # абстрактный метод, от которого напрямую не создаемм экземпляры
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


# 1 cgjcj, схож с модельками, повторять модельки опять, но это сложнее
# class User(serializers.Serializer):
#     username = serializers.CharField()
#     email = serializers.EmailField()


# по сути сериализаторы смахивают на dto, где для каждой операции создается класс, в отличии от моделек
class UserSerializer(serializers.Serializer, ABC):
    class Meta:  # Meta класс особенность Django
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']  # какие поля мы возвращаем по апи


class ExecutorSerializer(serializers.Serializer, ABC):
    user = UserSerializer()

    class Meta:
        model = Executor
        fields = '__all__'


# эти дтошки создания по сути считывают данные с фронта и переводят в понятный язык в понятные модельки для бд
class CreateExecutorSerializer(serializers.Serializer, ABC):
    class Meta:
        model = Executor
        fields = '__all__'


class CustomerSerializer(serializers.Serializer, ABC):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = '__all__'


class CreateCustomerSerializer(serializers.Serializer, ABC):
    class Meta:
        model = Customer
        fields = '__all__'


class ServiceSerializer(serializers.Serializer, ABC):
    executor = ExecutorSerializer()

    class Meta:
        model = Service
        fields = '__all__'


class CreateServiceSerializer(serializers.Serializer, ABC):
    class Meta:
        model = Service
        fields = '__all__'


class OrderSerializer(serializers.Serializer, ABC):
    executor = CustomerSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class CreateOrderSerializer(serializers.Serializer, ABC):
    class Meta:
        model = Order
        fields = '__all__'


class TagSerializer(serializers.Serializer, ABC):
    executor = ServiceSerializer()

    class Meta:
        model = Tag
        fields = '__all__'


class CreateRagSerializer(serializers.Serializer, ABC):
    class Meta:
        model = Tag
        fields = '__all__'


