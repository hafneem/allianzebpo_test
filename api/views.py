from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, get_object_or_404
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
        return get_object_or_404(Branches, ifsc=self.request.GET.get('ifsc'))


class FilteredBranchesApiView(ListAPIView):
    """
    API for fetching details of a transaction
    """
    permission_classes = [AllowAny]
    serializer_class = FilteredBranchesSerializer

    def get_queryset(self):
        bank = get_object_or_404(Banks, ifsc=self.request.GET.get('bank_name'))
        return Branches.objects.filter(bank=bank, city=self.request.GET.get('city'))
