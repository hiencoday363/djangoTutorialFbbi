from django.contrib import admin

from apps.User.models import Image_path
from .FormModel import EventForm
from .models import *


# Register your models here.
class ImgPathModelInline(admin.StackedInline):
    readonly_fields = ['created_at']
    model = Image_path
    extra = 0


class PerformanceInline(admin.StackedInline):
    model = Performance
    extra = 0


class TicketInline(admin.StackedInline):
    model = Ticket
    extra = 0


class EventsAdmin(admin.ModelAdmin):
    form = EventForm
    list_display = ("title", 'type', 'is_private_custom')
    search_fields = ('title',)
    list_filter = ('is_private',)
    ordering = ['-created_at']

    # create another record of model inline
    inlines = [ImgPathModelInline, ]

    # custom queryset để hiện thị data
    def get_queryset(self, request):
        qs = super(EventsAdmin, self).get_queryset(request)
        return qs.filter(is_archived=1)

    # custom display field private
    def is_private_custom(self, obj):
        return 'Yes' if obj.is_private else 'No'

    is_private_custom.short_description = "Private"


class TicketAdmin(admin.ModelAdmin):
    list_display = ("name", 'price')
    search_fields = ('name',)
    ordering = ['-created_at']


class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("name", 'start_datetime', 'end_datetime')
    search_fields = ('name',)
    ordering = ['-created_at']

    inlines = [TicketInline, ]


admin.site.register(Events, EventsAdmin)

admin.site.register(Event_authorized_user)
admin.site.register(Performance, PerformanceAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Ticket_purchase_revervation)
admin.site.register(Ticket_purchase_history)
admin.site.register(User_ticket)
admin.site.register(Drawing)
