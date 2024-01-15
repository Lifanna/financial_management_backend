"""financial_management_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path("auth/signin", TokenObtainPairView.as_view(), name="create-token"),
    path("auth/signup", views.UserCreateAPIView.as_view(), name="create-user"),
    path("auth/refresh", TokenRefreshView.as_view(), name="refresh-token"),
    path("auth/verify", TokenVerifyView.as_view(), name="verify-token"),

    # categories
    path("categories", views.CategoryListAPIView.as_view(), name="list-category"),
    path("categories/new", views.CategoryCreateAPIView.as_view(), name="create-category"),

    # revenue
    path("revenue", views.RevenueListAPIView.as_view(), name="list-revenue"),
    path("revenue/new", views.RevenueCreateAPIView.as_view(), name="create-revenue"),
    path("revenue/update/<int:pk>", views.RevenueUpdateAPIView.as_view(), name="update-revenue"),
    path("revenue/<int:pk>", views.RevenueRetrieveAPIView.as_view(), name="index-revenue"),
    path("revenue/delete/<int:pk>", views.RevenueDeleteAPIView.as_view(), name="delete-revenue"),

    # expenditure
    path("expenditure", views.ExpenditureListAPIView.as_view(), name="list-expenditure"),
    path("expenditure/new", views.ExpenditureCreateAPIView.as_view(), name="create-expenditure"),
    path("expenditure/<int:pk>", views.ExpenditureUpdateAPIView.as_view(), name="update-expenditure"),
    path("expenditure/delete/<int:pk>", views.ExpenditureDeleteAPIView.as_view(), name="delete-expenditure"),

    # report
    path("reports/revenue", views.ReportRevenueAPIView.as_view(), name="report-revenue"),
    path("reports/expenditure", views.ReportExpenditureAPIView.as_view(), name="report-expenditure"),
]
