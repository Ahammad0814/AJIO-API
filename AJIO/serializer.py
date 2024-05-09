from rest_framework.serializers import ModelSerializer
from .models import MensData,WomensData,KidsData,LoginData,OrdersData

class MenSerializer(ModelSerializer):
    class Meta:
        model = MensData
        fields = '__all__'
        
class WomenSerializer(ModelSerializer):
    class Meta:
        model = WomensData
        fields = '__all__'
        
class KidsSerializer(ModelSerializer):
    class Meta:
        model = KidsData
        fields = '__all__'
        
class LoginSerializer(ModelSerializer):
    class Meta:
        model = LoginData
        fields = '__all__'
        
class OrdersSerializer(ModelSerializer):
    class Meta:
        model = OrdersData
        fields = '__all__'