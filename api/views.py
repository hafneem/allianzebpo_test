from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from api.models import Branches, Banks
from api.serializers import BankDetailSerializer, FilteredBranchesSerializer


class RetrieveBranchDetailApiView(RetrieveAPIView):
    """
    API for fetching details of a transaction
    """
    permission_classes = [AllowAny]
    serializer_class = BankDetailSerializer

    def get_object(self):
        return Branches.objects.get(ifsc=self.request.GET.get('ifsc'))


class FilteredBranchesApiView(ListAPIView):
    """
    API for fetching details of a transaction
    """
    permission_classes = [AllowAny]
    serializer_class = FilteredBranchesSerializer

    def get_queryset(self):
        bank = Banks.objects.get(name=self.request.GET.get('bank_name'))
        return Branches.objects.filter(bank=bank, city=self.request.GET.get('city'))
