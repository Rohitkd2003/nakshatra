from rest_framework import serializers
from .models import Meal, MealIngredient, MealLog, CalorieEntry

class MealIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealIngredient
        fields = ['name','quantity','unit']

class MealListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id','name','description','calories','condition','preparation_time','servings','image_url','created_at']

class MealDetailSerializer(serializers.ModelSerializer):
    ingredients = MealIngredientSerializer(many=True, read_only=True)
    nutrition_info = serializers.SerializerMethodField()

    class Meta:
        model = Meal
        fields = ['id','name','description','calories','condition','ingredients','nutrition_info','preparation_time','servings','image_url']

    def get_nutrition_info(self, obj):
        # simple breakdown (example). You can extend logic as needed.
        protein = int(obj.calories * 0.15 // 1)
        carbs = int(obj.calories * 0.55 // 1)
        fat = int(obj.calories * 0.30 // 1)
        fiber = max(0, int(obj.calories * 0.03 // 1))
        return {'protein': protein, 'carbs': carbs, 'fat': fat, 'fiber': fiber}


class MealLogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealLog
        fields = ['meal','date','time','quantity','custom_calories']

    def create(self, validated_data):
        request = self.context['request']
        meal = validated_data.get('meal')
        meal_name = meal.name if meal else validated_data.get('meal_name','Unknown')
        calories = validated_data.get('custom_calories') or (meal.calories if meal else 0)
        ml = MealLog.objects.create(
            patient = request.user,
            meal = meal,
            meal_name = meal_name,
            date = validated_data['date'],
            time = validated_data['time'],
            quantity = validated_data.get('quantity',1.0),
            calories = calories,
            custom_calories = validated_data.get('custom_calories')
        )
        return ml


class MealLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealLog
        fields = ['id','patient','meal','meal_name','date','time','quantity','calories','custom_calories','logged_at']
        read_only_fields = ['id','patient','meal_name','calories','logged_at']


class CalorieEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CalorieEntry
        fields = ['id','patient','food_description','calories','date','time','created_at']
        read_only_fields = ['id','patient','created_at']

    def create(self, validated_data):
        request = self.context['request']
        return CalorieEntry.objects.create(patient=request.user, **validated_data)

from rest_framework import serializers
from .models import MealPlan, Meal
from .models import Meal, MealLog, CalorieEntry, MealPlan, MealPlanItem

class MealPlanItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlanItem
        fields = ['id', 'mealplan', 'meal', 'servings']
        read_only_fields = ['mealplan']

from rest_framework import serializers
from .models import MealPlanItem, Meal

class MealPlanAddFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlanItem
        fields = ['meal', 'servings']
