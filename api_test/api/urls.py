from django.urls import path
from api.views import (UserProfileListCreateView, 
                    userProfileDetailView, 
                    CategoryCreateView, 
                    CategoryDelateView, 
                    CategoryUpdateView, 
                    UserTransactionsDetailView,
                    TransactionsCreateView,
                    TransactionsWriteOffView
                    )

urlpatterns = [
    path("all-profiles/",UserProfileListCreateView.as_view(),name="all-profiles"),
    path("profile/",userProfileDetailView.as_view(),name="profile"),
    path("profile/category/add", CategoryCreateView.as_view(), name="category"),
    path("profile/category/update/<int:pk>", CategoryUpdateView.as_view(), name="category_update"),
    path("profile/category/delate/<int:pk>", CategoryDelateView.as_view(), name="category_delate"),
    path("profile/transactions/", UserTransactionsDetailView.as_view(), name="transactions"),
    path("profile/transactions/accrual", TransactionsCreateView.as_view(), name="transactions_add"),
    path("profile/transactions/writeoff", TransactionsWriteOffView.as_view(), name="transactions_min"),
    
]