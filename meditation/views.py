from rest_framework import generics
from .models import MeditationPlan, MeditationSession
from .serializers import MeditationPlanSerializer, MeditationSessionSerializer

# POST create session
class MeditationSessionCreateView(generics.CreateAPIView):
    serializer_class = MeditationSessionSerializer

    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)  # user = patient

# GET list sessions
class MeditationSessionListView(generics.ListAPIView):
    queryset = MeditationSession.objects.all()
    serializer_class = MeditationSessionSerializer

# GET list plans
class PlanListView(generics.ListAPIView):
    queryset = MeditationPlan.objects.all()
    serializer_class = MeditationPlanSerializer
