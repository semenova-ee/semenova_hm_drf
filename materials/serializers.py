from members.models import CourseSubscription
from rest_framework import serializers
from .models import Course, Lesson
from .validators import validate_allowed_domains


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        extra_kwargs = {
            'video_link': {'validators': [validate_allowed_domains]},
        }



class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')
    subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'preview', 'description', 'lessons', 'lessons_count', 'subscribed']

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()

    def get_subscribed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return CourseSubscription.objects.filter(user=user, course=obj).exists()
        return False
