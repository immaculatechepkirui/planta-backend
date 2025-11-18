from rest_framework import serializers
from plantaai.models import PredictionHistory
from rest_framework import serializers
from django.contrib.auth.models import User


class PredictionInputSerializer(serializers.Serializer):
    Hectares = serializers.FloatField()
    Seedrate_in_Kg = serializers.FloatField()
    LP_Mainfield_in_Tonnes = serializers.FloatField()
    Nursery_area_Cents = serializers.FloatField()
    LP_nurseryarea_in_Tonnes = serializers.FloatField()
    DAP_20days = serializers.FloatField()
    Weed28D_thiobencarb = serializers.FloatField()
    Urea_40Days = serializers.FloatField()
    Potassh_50Days = serializers.FloatField()
    Micronutrients_70Days = serializers.FloatField()
    Pest_60Day_in_ml = serializers.FloatField()
    d30DRain_in_mm = serializers.FloatField()
    d30DAI_in_mm = serializers.FloatField()
    d30_50DRain_in_mm = serializers.FloatField()
    d30_50DAI_in_mm = serializers.FloatField()
    d51_70DRain_in_mm = serializers.FloatField()
    d51_70AI_in_mm = serializers.FloatField()
    d71_105DRain_in_mm = serializers.FloatField()
    d71_105DAI_in_mm = serializers.FloatField()
    Min_temp_D1_D30 = serializers.FloatField()
    Max_temp_D1_D30 = serializers.FloatField()
    Min_temp_D31_D60 = serializers.FloatField()
    Max_temp_D31_D60 = serializers.FloatField()
    Min_temp_D61_D90 = serializers.FloatField()
    Max_temp_D61_D90 = serializers.FloatField()
    Min_temp_D91_D120 = serializers.FloatField()
    Max_temp_D91_D120 = serializers.FloatField()
    Inst_Wind_Speed_D1_D30_in_Knots = serializers.FloatField()
    Inst_Wind_Speed_D31_D60_in_Knots = serializers.FloatField()
    Inst_Wind_Speed_D61_D90_in_Knots = serializers.FloatField()
    Inst_Wind_Speed_D91_D120_in_Knots = serializers.FloatField()
    Relative_Humidity_D1_D30 = serializers.FloatField()
    Relative_Humidity_D31_D60 = serializers.FloatField()
    Relative_Humidity_D61_D90 = serializers.FloatField()
    Relative_Humidity_D91_D120 = serializers.FloatField()
    Trash_in_bundles = serializers.FloatField()
    Agriblock_encoded = serializers.FloatField()
    Variety_encoded = serializers.FloatField()
    Soil_Type_encoded = serializers.FloatField()
    Wind_Direction_D1_D30_encoded = serializers.FloatField()

    
class PredictionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionHistory
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user


class PredictionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionHistory
        fields = ['id', 'prediction_date', 'predicted_yield_kg', 'recommended_variety'] 