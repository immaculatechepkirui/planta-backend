# plantaai/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PredictionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='predictions', null=True, blank=True)
    prediction_date = models.DateTimeField(auto_now_add=True)
    
    # --- Input Features (Mirroring your CSV columns/Encoded features) ---
    # The names must match the columns in your one-hot encoded DataFrame (X)
    Hectares = models.FloatField()
    Seedrate_in_Kg = models.FloatField()
    LP_Mainfield_in_Tonnes = models.FloatField()
    Nursery_area_Cents = models.FloatField()
    LP_nurseryarea_in_Tonnes = models.FloatField()
    DAP_20days = models.FloatField()
    Weed28D_thiobencarb = models.FloatField()
    Urea_40Days = models.FloatField()
    Potassh_50Days = models.FloatField()
    Micronutrients_70Days = models.FloatField()
    Pest_60Day_in_ml = models.FloatField()
    d30DRain_in_mm = models.FloatField()
    d30DAI_in_mm = models.FloatField()
    d30_50DRain_in_mm = models.FloatField()
    d30_50DAI_in_mm = models.FloatField()
    d51_70DRain_in_mm = models.FloatField()
    d51_70AI_in_mm = models.FloatField()
    d71_105DRain_in_mm = models.FloatField()
    d71_105DAI_in_mm = models.FloatField()
    Min_temp_D1_D30 = models.FloatField()
    Max_temp_D1_D30 = models.FloatField()
    Min_temp_D31_D60 = models.FloatField()
    Max_temp_D31_D60 = models.FloatField()
    Min_temp_D61_D90 = models.FloatField()
    Max_temp_D61_D90 = models.FloatField()
    Min_temp_D91_D120 = models.FloatField()
    Max_temp_D91_D120 = models.FloatField()
    Inst_Wind_Speed_D1_D30_in_Knots = models.FloatField()
    Inst_Wind_Speed_D31_D60_in_Knots = models.FloatField()
    Inst_Wind_Speed_D61_D90_in_Knots = models.FloatField()
    Inst_Wind_Speed_D91_D120_in_Knots = models.FloatField()
    Relative_Humidity_D1_D30 = models.FloatField()
    Relative_Humidity_D31_D60 = models.FloatField()
    Relative_Humidity_D61_D90 = models.FloatField()
    Relative_Humidity_D91_D120 = models.FloatField()
    Trash_in_bundles = models.FloatField()
    
    # --- Encoded Categorical Features (placeholders for the one-hot encoded columns) ---
    # These represent the *presence* of a specific category combination
    # The exact field names will depend on how pandas get_dummies named them. 
    # E.g., 'Variety_Variety B' becomes 'Variety_Variety_B' here
    # You might need to adjust these names based on your final feature list joblib file!
    # These are illustrative examples:
    Agriblock_encoded = models.FloatField(default=0.0)
    Variety_encoded = models.FloatField(default=0.0)
    Soil_Type_encoded = models.FloatField(default=0.0)
    Wind_Direction_D1_D30_encoded = models.FloatField(default=0.0)
    
    # --- Output/Result ---
    predicted_yield_kg = models.FloatField(null=True, blank=True)
    recommended_variety = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Prediction {self.id} for {self.user.username if self.user else 'Guest'}"

