from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Course, Lesson, Question, Choice, Submission
from django.utils import timezone

# Create your views here.


def index(request):
    """
    Display all available courses
    """
    latest_course_list = Course.objects.all()
    context = {'latest_course_list': latest_course_list}
    return render(request, 'course/index.html', context)


def course_detail(request, course_id):
    """
    Display course details with lessons and assessment questions
    """
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lesson_set.all().order_by('order')

    context = {
        'course': course,
        'lessons': lessons,
    }
    return render(request, 'course/course_detail_bootstrap.html', context)


def submit(request, lesson_id):
    """
    Handle exam submission and redirect to results
    """
    if request.method == 'POST':
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        questions = lesson.question_set.all()

        # Create or get submission for current user
        if request.user.is_authenticated:
            # Delete existing submission for this lesson by this user
            Submission.objects.filter(
                enrollment=request.user, lesson=lesson).delete()

            # Create new submission
            submission = Submission.objects.create(
                enrollment=request.user,
                lesson=lesson
            )

            # Process submitted answers
            selected_choices = []
            for question in questions:
                choice_id = request.POST.get(f'choice_{question.id}')
                if choice_id:
                    try:
                        choice = Choice.objects.get(
                            pk=choice_id, question=question)
                        selected_choices.append(choice)
                    except Choice.DoesNotExist:
                        pass

            # Add choices to submission
            submission.choices.set(selected_choices)
            submission.save()

            return redirect('course:show_exam_result', lesson_id=lesson_id, submission_id=submission.id)
        else:
            messages.error(
                request, 'You must be logged in to submit an assessment.')
            return redirect('course:detail', course_id=lesson.course.id)
    else:
        return redirect('course:detail', course_id=lesson.course.id)


def show_exam_result(request, lesson_id, submission_id):
    """
    Display exam results with detailed feedback
    """
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    # Get all questions for this lesson
    questions = lesson.question_set.all()

    # Calculate results
    total_score = sum([question.grade for question in questions])
    score = 0
    correct_answers = 0
    wrong_answers = 0
    total_questions = questions.count()

    question_results = []

    for question in questions:
        # Get user's selected choice for this question
        selected_choice = submission.choices.filter(question=question).first()

        # Check if answer is correct
        is_correct = False
        if selected_choice and selected_choice.is_correct:
            is_correct = True
            score += question.grade
            correct_answers += 1
        else:
            wrong_answers += 1

        question_results.append({
            'question': question,
            'selected_choice': selected_choice,
            'is_correct': is_correct,
        })

    # Calculate percentage
    percentage = (score / total_score * 100) if total_score > 0 else 0

    context = {
        'lesson': lesson,
        'submission': submission,
        'score': score,
        'total_score': total_score,
        'percentage': percentage,
        'correct_answers': correct_answers,
        'wrong_answers': wrong_answers,
        'total_questions': total_questions,
        'question_results': question_results,
    }

    return render(request, 'course/exam_result.html', context)

# Authentication views


def user_login(request):
    """
    User login view
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to 'next' parameter if available, otherwise go to index
            next_page = request.POST.get('next') or request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return redirect('course:index')
        else:
            messages.error(request, 'Invalid username or password.')

    # Pass the 'next' parameter to the template
    next_page = request.GET.get('next', '')
    return render(request, 'course/login.html', {'next': next_page})


def user_logout(request):
    """
    User logout view
    """
    logout(request)
    return redirect('course:index')


def user_signup(request):
    """
    User registration view
    """
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            user = User.objects.create_user(
                username=username, password=password1, email=email)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('course:index')

    return render(request, 'course/signup.html')
