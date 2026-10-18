from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Event, Registration
from .serializers import EventSerializer


@api_view(["GET", "POST"])
def event_list(request):
    if request.method == "GET":
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



@api_view(["GET"])
def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(
            {"error": "Event not found"},
            status=404
        )

    serializer = EventSerializer(event)
    return Response(serializer.data)


@api_view(["GET", "POST", "DELETE"])
def event_registration(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(
            {"error": "Event not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "GET":
        registrations = Registration.objects.filter(event=event)
        data = [
            {
                "id": registration.id,
                "username": registration.user.username,
                "event": registration.event.title,
                "registered_at": registration.registered_at
            }
            for registration in registrations
        ]
        return Response(data)

    if request.method == "POST":
        user_id = request.data.get("user_id")

        if not user_id:
            return Response(
                {"error": "user_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        from django.contrib.auth.models import User

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if Registration.objects.filter(user=user, event=event).exists():
            return Response(
                {"error": "User is already registered for this event"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if Registration.objects.filter(event=event).count() >= event.capacity:
            return Response(
                {"error": "Event is full"},
                status=status.HTTP_400_BAD_REQUEST
            )

        registration = Registration.objects.create(
            user=user,
            event=event
        )

        return Response(
            {
                "message": "Registration successful",
                "registration_id": registration.id,
                "username": user.username,
                "event": event.title
            },
            status=status.HTTP_201_CREATED
        )

    
    if request.method == "DELETE":
        user_id = request.data.get("user_id")

        if not user_id:
            return Response(
                {"error": "user_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            registration = Registration.objects.get(
                user_id=user_id,
                event=event
            )
        except Registration.DoesNotExist:
            return Response(
                {"error": "Registration not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        registration.delete()

        return Response(
            {"message": "Registration cancelled successfully"},
            status=status.HTTP_200_OK
        )



