
from rest_framework import serializers
from login_app.models import conn

class Connection_Serializer(serializers.ModelSerializer):
    class Meta:
        model = conn
        fields = "__all__"
