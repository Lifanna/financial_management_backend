from django.shortcuts import render
from rest_framework import generics
from . import serializers, models, permissions
from rest_framework.permissions import IsAuthenticated


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.CustomUserSerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.CategorySerializer


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class RevenueCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.RevenueCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class RevenueListAPIView(generics.ListAPIView):
    serializer_class = serializers.RevenueSerializer
    queryset = models.Revenue.objects.all()

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = models.Revenue.objects.filter(user=self.request.user)

        return queryset


class RevenueUpdateAPIView(generics.UpdateAPIView):
    serializer_class = serializers.RevenueCreateUpdateSerializer
    queryset = models.Revenue.objects.all()

    permission_classes = [IsAuthenticated]


class RevenueDeleteAPIView(generics.DestroyAPIView):
    serializer_class = serializers.RevenueSerializer
    queryset = models.Revenue.objects.all()

    permission_classes = [IsAuthenticated]


class ExpenditureCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.ExpenditureSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ExpenditureListAPIView(generics.ListAPIView):
    serializer_class = serializers.ExpenditureSerializer
    queryset = models.Expenditure.objects.all()

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = models.Expenditure.objects.filter(user=self.request.user)

        return queryset


class ExpenditureUpdateAPIView(generics.UpdateAPIView):
    serializer_class = serializers.ExpenditureSerializer
    queryset = models.Expenditure.objects.all()

    permission_classes = [IsAuthenticated]


class ExpenditureDeleteAPIView(generics.DestroyAPIView):
    serializer_class = serializers.ExpenditureSerializer
    queryset = models.Expenditure.objects.all()

    permission_classes = [IsAuthenticated]


class RevenueRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.RevenueSerializer  # Используйте ваш сериализатор RevenueSerializer
    queryset = models.Revenue.objects.all()  # Получите все объекты Revenue

    permission_classes = [IsAuthenticated]  # Установите нужные разрешения, включая IsAuthenticated
