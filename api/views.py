from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.models import Branches, Banks
from api.serializers import BankDetailSerializer, FilteredBranchesSerializer


class RetrieveBranchDetailApiView(RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = BankDetailSerializer

    def get_object(self):
        return get_object_or_404(Branches, ifsc=self.request.GET.get('ifsc'))


class FilteredBranchesApiView(ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = FilteredBranchesSerializer

    def get_queryset(self):
        bank = get_object_or_404(Banks, name=self.request.GET.get('bank_name'))
        return Branches.objects.filter(bank=bank, city=self.request.GET.get('city'))
