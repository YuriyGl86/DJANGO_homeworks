import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):
    courses = course_factory(_quantity=10, make_m2m=True)

    for course in courses:
        url = reverse('courses-detail', kwargs={'pk': course.id})
        response = client.get(url)
        data = response.json()

        assert response.status_code == 200
        assert  data['name'] == course.name


