from rest_framework import serializers
from .models import CustomUser


# Serializer for registering a new user
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, write_only=True)
    password2 = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    def create(self, validated_data):
        # Hash the password before saving
        if validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        validated_data.pop('password2')
        password = validated_data.pop('password')  # Remove password from validated data
        user = CustomUser(**validated_data)
        user.set_password(password)  # Hash the password
        user.save()  # Save the user to the database
        return user
    

# Seriallizer for Logging in a user
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)


# Serializer for User Profile
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']