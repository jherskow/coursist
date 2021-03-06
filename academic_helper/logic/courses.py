from django.db.models import Q

from academic_helper.models import Course, Teacher, CourseClass
from academic_helper.utils.logger import log, wrap


def search_teacher(name: str):
    teachers = Teacher.objects.filter(name__contains=name)
    classes = CourseClass.objects.filter(teacher__in=teachers)
    field = "group__occurrence__course__course_number"
    course_numbers = classes.values(field).distinct()
    course_numbers = [n[field] for n in course_numbers]
    return Course.objects.filter(course_number__in=course_numbers)


def search(text: str, department: str = "", faculty: str = ""):
    log.info(f"Searching for {wrap(text)}, department {wrap(department)}, faculty {wrap(faculty)}")
    courses = Course.objects.filter(
        (Q(name__contains=text) | Q(course_number__icontains=text))
        & Q(department__name__contains=department)
        & Q(department__faculty__name__contains=faculty)
    )
    if len(text) >= 3:
        courses |= search_teacher(text)
    return courses
