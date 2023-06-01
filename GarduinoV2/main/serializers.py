from rest_framework import serializers
from main.models import PlantData
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class ArduinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantData
        fields = ['name', 'temp', 'humidity', 'next_spray', 'fertilizer_level', 'led_intensity', 'time_to_sundown', 'status']

    def create(self, validated_data):
        """
        Create a new plant with required data
        """
        return PlantData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update existing data of model
        """
        instance.name = validated_data.get('name', instance.name)
        instance.temp = validated_data.get('temp', instance.temp)
        instance.humidity = validated_data.get('humidity', instance.humidity)
        instance.next_spray = validated_data.get('next_spray', instance.next_spray)
        instance.fertilizer_level = validated_data.get('fertilizer_level', instance.fertilizer_level)
        instance.led_intensity = validated_data.get('led_intensity', instance.led_intensity)
        instance.time_to_sundown = validated_data.get('time_to_sundown', instance.time_to_sundown)
        instance.status = validated_data.get('status', instance.status)

        instance.save()
        return instance