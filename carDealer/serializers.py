from django.shortcuts import render
from rest_framework import serializers

from carDealer.models import Item, ItemImage

class ItemsImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = "__all__"

class ItemSerializers(serializers.ModelSerializer):
    images =  ItemsImageSerializers(many=True, read_only=True)
    profile = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Item
        fields = [ "profile", "make", "year", "model", "suspension",
                  "baseprice","currentprice", "buyitnow","description", "status","start_date", "images"
                  ]

    def create(self, validated_data):
        profile = validated_data.pop("profile")
        product = Item.objects.create(**validated_data)

        for image in profile:
            ItemImage.objects.create(product=product, image=image)

       
    
        return product

