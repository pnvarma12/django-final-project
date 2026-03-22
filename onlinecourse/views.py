from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Question, Choice, Submission, Enrollment
from django.contrib import messages

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Retrieve all question IDs from the post data
        question_ids = request.POST.getlist('question')
        total_score = 0
        
        # In a real app, we'd find the specific enrollment for the user
        # For this project, we'll grab the first one or create a mock one
        enrollment = Enrollment.objects.filter(course=course).first()
        
        submission = Submission(enrollment=enrollment)
        submission.save()

        for q_id in question_ids:
            question = get_object_or_404(Question, pk=q_id)
            selected_choice_id = request.POST.get(f'choice_{q_id}')
            if selected_choice_id:
                choice = get_object_or_404(Choice, pk=selected_choice_id)
                submission.choices.add(choice)
                if choice.is_correct:
                    total_score += question.grade
        
        submission.save()
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)
    
    return render(request, 'onlinecourse/course_details_bootstrap.html', {'course': course})

def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Calculate total possible score
    total_possible = sum(q.grade for q in course.question_set.all())
    # Calculate user score
    user_score = sum(choice.question.grade for choice in submission.choices.filter(is_correct=True))
    
    # Check if passed (70% threshold)
    percentage = (user_score / total_possible) * 100 if total_possible > 0 else 0
    passed = percentage >= 70

    context = {
        'course': course,
        'submission': submission,
        'score': user_score,
        'total_possible': total_possible,
        'passed': passed
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
