import datetime
from django.shortcuts import render
from rest_framework import generics
from . import serializers, models, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework import status


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
    serializer_class = serializers.ExpenditureCreateUpdateSerializer
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
    serializer_class = serializers.ExpenditureCreateUpdateSerializer
    queryset = models.Expenditure.objects.all()

    permission_classes = [IsAuthenticated]


class ExpenditureDeleteAPIView(generics.DestroyAPIView):
    serializer_class = serializers.ExpenditureSerializer
    queryset = models.Expenditure.objects.all()

    permission_classes = [IsAuthenticated]

class ExpenditureRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ExpenditureSerializer  # Используйте ваш сериализатор RevenueSerializer
    queryset = models.Expenditure.objects.all()  # Получите все объекты Revenue

    permission_classes = [IsAuthenticated]  # Установите нужные разрешения, включая IsAuthenticated


class RevenueRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.RevenueSerializer  # Используйте ваш сериализатор RevenueSerializer
    queryset = models.Revenue.objects.all()  # Получите все объекты Revenue

    permission_classes = [IsAuthenticated]  # Установите нужные разрешения, включая IsAuthenticated


# class ReportRevenueAPIView(views.APIView):
    # pass


# class ReportExpenditureAPIView(views.APIView):
#     pass

@api_view(['POST', ])
def reportRevenue_API_view(request):
    start_date_str = request.data.get('start_date')
    end_date_str = request.data.get('end_date')
    print(start_date_str,end_date_str)
    revenues = models.Revenue.objects.filter(
    user=request.user,
    revenue_date__range=(start_date_str, end_date_str)
    ).values('category_id', 'category__name').annotate(
    total_sum=Sum('sum')
    ).order_by('category_id')
    serializer = serializers.ReportRevenueSerializer(revenues, many=True)
    serialized_data = serializer.data

    return Response(serialized_data)


@api_view(['POST', ])
def reportExpenditure_API_view(request):
    start_date_str = request.data.get('start_date')
    end_date_str = request.data.get('end_date')
    print(start_date_str,end_date_str)
    revenues = models.Expenditure.objects.filter(
    user=request.user,
    expenditure_date__range=(start_date_str, end_date_str)
    ).values('category_id', 'category__name').annotate(
    total_sum=Sum('sum')
    ).order_by('category_id')
    serializer = serializers.ReportExpenditureSerializer(revenues, many=True)
    serialized_data = serializer.data

    return Response(serialized_data)


