from django.core.paginator import Paginator, EmptyPage
from rest_framework import generics
from django.http import Http404
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Common.CustomPermission.CustomPermission import UserPermission
from apps.User.models import User
from apps.User.serializers import UserSerializer
from .models import Events, Ticket, Performance
from .paginator import EventPagination
from .serializer import EventSerializer, TicketSerializer, PerformanceSerializer, TicketPerformSerializer, \
    DrawSerializer


def checkTicket(ticket, ticket_id, user_serializer):
    '''
    function check ticket
    param:
    ticket (TicketPerformSerializer)
    ticket_id : ticket_id (number) to check
    user_serializer: user (UserSerializer) to get client_id to check
    return true if all field of ticket pass else false
    '''
    if ticket['id'] != ticket_id:
        return False
    if ticket['performance']['events']['client_id'] != user_serializer.data[0]['client_id']:
        return False
    if ticket['performance']['events']['is_archived'] != 0:
        return False
    if ticket['performance']['ticket_available_flag'] != 1:
        return False
    if ticket['drawing_application_deadline_check'] != 1:
        return False

    return True


def craeteDrawing(data):
    '''
    create drawing
    param:
    data: data type json {"ticket": id, "user": id}
    return True if save success else False
    '''
    draw_serializer = DrawSerializer(data=data)
    if draw_serializer.is_valid(raise_exception=True):
        draw_serializer.save()
        return True
    return False


# Create your views here.
class EventViewSet(generics.ListAPIView):
    permission_classes = [UserPermission]

    serializer_class = EventSerializer
    pagination_class = EventPagination

    def get_queryset(self):
        # get current page
        # pagenum = self.request.query_params.get('page')

        events = Events.objects.filter()  # is_archived=0

        keyword = self.request.query_params.get('keyword')
        if keyword is not None:
            events = events.filter(title__icontains=keyword)

        type = self.request.query_params.get('type')
        if (type == '1' or type == '2'):
            events = events.filter(type=type)
        elif (type == ''):
            events = events.filter(type__in=['1', '2'])

        return events

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventApiView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer

    def get(self, request):
        # save the queries (prefer to use)
        events = Events.objects.prefetch_related('img_path').filter(is_deleted=False)
        # filter
        keyword = self.request.query_params.get('keyword')
        if keyword is not None:
            events = events.filter(title__icontains=keyword)
        type = self.request.query_params.get('type')
        if (type == '1' or type == '2'):
            events = events.filter(type=type)
        elif (type == ''):
            events = events.filter(type__in=['1', '2'])

        # pagination
        page_size = self.request.query_params.get('perpage ', 3)

        page_number = self.request.query_params.get('page')
        if page_number is None:
            page_number = 1

        paginator = Paginator(events, page_size)
        try:
            serializer = EventSerializer(paginator.page(page_number), many=True)
        except EmptyPage:
            serializer = EventSerializer(paginator.page(1), many=True)

        return Response(serializer.data)


class DetailEventApiView(APIView):
    """
       Retrieve, update or delete a Event instance.
    """
    permission_classes = [UserPermission]

    def get_object(self, pk):
        try:
            return Events.objects.get(pk=pk)
        except Events.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print('deleted')
        event = self.get_object(pk)
        event.is_deleted = True
        event.save()
        return Response({"message": "the item deleted!"}, status=status.HTTP_200_OK)


# ticket

class TicketListApiView(APIView):
    permission_classes = [UserPermission]

    serializer_class = TicketSerializer
    query_set = Ticket.objects.select_related('performance_id').all()

    def get(self, request):
        serializer = self.serializer_class(self.query_set, many=True)
        return Response(serializer.data)


class TicketApiView(APIView):
    permission_classes = [IsAuthenticated]

    serializer_class = TicketSerializer
    ticket_serializer_check = TicketPerformSerializer

    def get_object(self, pk):
        try:
            ticket = Ticket.objects.prefetch_related('performance_id').filter(id=pk).first()
            return ticket
        except Ticket.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        try:
            user_id = int(request.data.get('user_id'))
            ticket_id = int(request.data.get('ticket_id'))
            if not user_id or not ticket_id:
                raise Exception('Miss something important!')
        except:
            raise Exception('Something went wrong! Try again later!!!')

        # check user
        users = User.objects.filter(id=user_id, is_archived=0, isAuthenticated=1, user_type=1)
        user_serializer = UserSerializer(users, many=True)

        if len(user_serializer.data) <= 0:
            raise User.DoesNotExist("User does not exist!")

        # check ticket
        tickets = Ticket.objects.select_related('performance_id').filter(drawing_flag=1, drawing_status=0)
        ticket_serializer = self.ticket_serializer_check(tickets, many=True).data

        for ticket in ticket_serializer:
            if checkTicket(ticket, ticket_id, user_serializer):
                # create draw here
                # if not craeteDrawing({"ticket": ticket_id, "user": user_id}):
                #     raise Exception('Something went wrong! Try again later!!!')
                # create success return
                serializer = self.serializer_class(self.get_object(pk))
                return Response(serializer.data)

        raise Performance.DoesNotExist("Performance does not exist!")


class TicketCheckApiView(APIView):
    permission_classes = [IsAuthenticated]

    serializer_class = TicketPerformSerializer
    query_set = Ticket.objects.select_related('performance_id').filter()

    def get(self, request):
        serializer = self.serializer_class(self.query_set, many=True)

        return Response(serializer.data)


class PerformanceListApiView(APIView):
    permission_classes = [IsAuthenticated]

    serializer_class = PerformanceSerializer
    query_set = Performance.objects.prefetch_related('event_id').all()

    def get(self, request):
        serializer = self.serializer_class(self.query_set, many=True)
        return Response(serializer.data)
