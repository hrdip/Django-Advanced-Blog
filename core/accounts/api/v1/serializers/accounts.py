from rest_framework import serializers
from ....models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "password1"]

    # data sent from the user is valid or not
    def validate(self, attrs):
        # check password matching
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError({"detail": "password doesn't  match"})
        # check password complexity
        try:
            validate_password(attrs.get("password"))
        except serializers.ValidationError as err:
            raise serializers.ValidationError({"password": list(err.messages)})
        return super().validate(attrs)

    # save user data after validation
    def create(self, validated_data):
        validated_data.pop("password1", None)
        # create a user with the given email and password with the create_user function written in the model
        return User.objects.create_user(**validated_data)


# copy AuthTokenSerializer as parent class and used email instead of user for login
class CustomAuthTokenSerializer(serializers.Serializer):
    # change user to email
    email = serializers.CharField(label=_("Email"), write_only=True)
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=_("Token"), read_only=True)

    def validate(self, attrs):
        username = attrs.get("email")
        password = attrs.get("password")

        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )
            # The authenticate call simply returns None for is_active=False users. (Assuming the default ModelBackend authentication backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
            # check validation user
            if not user.is_verified:
                raise serializers.ValidationError({"detail": "User is not verified."})
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")
        attrs["user"] = user
        return attrs


# custom jwt token serializer for custom jwt class view, return email and user_id
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        # check validation user
        if not self.user.is_verified:
            raise serializers.ValidationError({"detail": "User is not verified."})
        # in parent class have query for user and we just use that
        # one of main reason we overwrite TokenObtainPairSerializer parent class here instead of view class parent is query for user are existed in this class
        validated_data["email"] = self.user.email
        validated_data["user_id"] = self.user.id
        return validated_data


class TestEmailSendSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class ActivationResendSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        # get email of user
        email = attrs.get("email")
        try:
            # searching for find user by email
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"details": "user does not exist"})
        if user_obj.is_verified:
            raise serializers.ValidationError(
                {"details": "user is already activated and verified"}
            )
        # when finding user, pass user in user_obj
        attrs["user"] = user_obj
        return super().validate(attrs)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        # check password matching
        if attrs.get("new_password") != attrs.get("new_password1"):
            raise serializers.ValidationError({"detail": "password dose not match"})
        try:
            # check password complexity
            validate_password(attrs.get("new_password"))
        except serializers.ValidationError as err:
            raise serializers.ValidationError({"new_password": list(err.messages)})
        return super().validate(attrs)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        # get email of user
        email = attrs.get("email")
        try:
            # searching for find user by email
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"details": "user does not exist"})
        # when finding user, pass user in user_obj
        attrs["user"] = user_obj
        return super().validate(attrs)


class ResetPasswordConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        # check password matching
        if attrs.get("new_password") != attrs.get("new_password1"):
            raise serializers.ValidationError({"detail": "password dose not match"})
        try:
            # check password complexity
            validate_password(attrs.get("new_password"))
        except serializers.ValidationError as err:
            raise serializers.ValidationError({"new_password": list(err.messages)})
        return super().validate(attrs)
