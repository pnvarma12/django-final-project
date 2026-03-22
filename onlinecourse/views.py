from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Choice, Submission, Enrollment

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        selected_ids = request.POST.getlist('choice')
        enrollment = Enrollment.objects.get(user=request.user, course=course)
        submission = Submission.objects.create(enrollment=enrollment)
        for choice_id in selected_ids:
            submission.choices.add(get_object_or_404(Choice, pk=choice_id))
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    selected_ids = [choice.id for choice in submission.choices.all()]
    total_score = 0
    for question in course.question_set.all():
        if question.is_get_score(selected_ids):
            total_score += question.grade
    
    return render(request, 'onlinecourse/exam_result_bootstrap.html', {
        'course': course,
        'score': total_score,
        'selected_ids': selected_ids,
        'submission': submission
    })
