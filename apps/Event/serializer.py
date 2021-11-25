from rest_framework import serializers
from django.utils import timezone

from .models import Events, Performance, Ticket, Drawing


class DrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        fields = ['ticket', 'user', 'is_elected', 'is_purchased']

        extra_kwargs = {
            'is_elected': {'required': False},
            'is_purchased': {'required': False}
        }

    # def validate_user(self, value):
    #     return value

    def create(self, validated_data):
        draw = Drawing.objects.create(**validated_data)
        return draw


class EventSerializer(serializers.ModelSerializer):
    # img_path = ImgPathSerializer(many=True, read_only=True)

    is_locked = serializers.SerializerMethodField()
    img_path = serializers.SerializerMethodField()

    class Meta:
        model = Events
        fields = ['id', 'title', 'body', 'client_id', 'type', 'is_private', 'is_locked', 'img_path']

    def get_is_locked(self, instance):
        if instance.is_private == 1 and len(instance.eau.all()) == 0:
            return False
        return True

    def get_img_path(self, instance):
        dict = instance.img_path.all()
        if len(dict) > 0:
            return dict[0].image_url if dict else ""
        return ""

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if instance.is_private == 1:
    #         event_authorized_user = Event_authorized_user.objects.filter(event_id=instance.id).first()
    #         if event_authorized_user is None:
    #             representation['is_locked'] = True
    #         else:
    #             representation['is_locked'] = False
    #     else:
    #         representation['is_locked'] = False
    #     return representation


class TicketSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    start_datetime = serializers.SerializerMethodField()
    end_datetime = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ['id', 'name', 'price', 'quantity', 'start_datetime', 'end_datetime', 'total_price']

    def get_start_datetime(self, instance):
        start_date = instance.performance_id.start_datetime
        return start_date.strftime('%d/%m/%Y %H:%M') if start_date else "Null"

    def get_end_datetime(self, instance):
        end_date = instance.performance_id.end_datetime

        return end_date.strftime('%d/%m/%Y %H:%M') if end_date else "Null"

    def get_quantity(self, instance):
        return 1

    def get_total_price(self, instance):
        return instance.price * 1


class PerformanceEventSerializer(serializers.ModelSerializer):
    quantity = serializers.SerializerMethodField()

    class Meta:
        model = Performance
        fields = "__all__"


class EventForPerformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'client_id', 'is_archived', 'title']


class PerformanceSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()

    class Meta:
        model = Performance
        fields = ['id', 'events', 'ticket_available_flag']

    def get_events(self, instance):
        event = instance.event_id
        serializer = EventForPerformSerializer(event)
        return serializer.data if serializer else "Null"


class TicketPerformSerializer(serializers.ModelSerializer):
    performance = serializers.SerializerMethodField()
    drawing_application_deadline_check = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ['id', 'performance', 'drawing_flag', 'drawing_application_deadline_check', 'drawing_status']

    def get_performance(self, instance):
        performance = instance.performance_id
        serializer = PerformanceSerializer(performance)
        return serializer.data if serializer else "Null"

    def get_drawing_application_deadline_check(self, instance):
        deadline = instance.drawing_application_deadline
        now = timezone.now()
        return 1 if now < deadline else 0
