from school.models import Student, Course, Enrollment
from school.serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer, ListEnrollmentSerializerPerStudent, ListEnrollmentSerializerPerCourse
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class StudentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing student instances.
    """

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing course instances.
    """

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing course instances.
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class ListEnrollmentPerStudent(generics.ListAPIView):
    """
    A viewset for listing enrollments per student.
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ListEnrollmentSerializerPerStudent

    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    
class ListEnrollmentPerCourse(generics.ListAPIView):
    """
    A viewset for listing enrollments per course.
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ListEnrollmentSerializerPerCourse

    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset