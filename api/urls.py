from django.urls import path, include
from api import views

urlpatterns = [
    path('bank-details/', views.RetrieveBranchDetailApiView.as_view(), name='bank_details'),
    path('bank-details/filtered/', views.FilteredBranchesApiView.as_view(), name='filtered_bank_details')
]