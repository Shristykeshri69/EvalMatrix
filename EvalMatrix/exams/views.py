from .models import SuspiciousActivity
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Exam, Question
from .models import ExamAttempt
from django.contrib.auth.views import LoginView
from .forms import RegisterForm


def home_page_view(request):
    exams = Exam.objects.all()
    return render(request, 'exams/home.html', {'exams': exams})


from django.contrib.auth import login

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after register
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


  

@login_required
def start_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)

    # 🔒 Check if already attempted
    if ExamAttempt.objects.filter(user=request.user, exam=exam).exists():
        return render(request, 'exams/already_attempted.html', {'exam': exam})

    questions = Question.objects.filter(exam=exam)

    if request.method == "POST":
        score = 0

        for question in questions:
            selected_option_id = request.POST.get(f"question_{question.id}")

            if selected_option_id:
                selected_option = question.option_set.get(id=selected_option_id)

                if selected_option.is_correct:
                    score += 1

        # ✅ Save attempt
        ExamAttempt.objects.create(
            user=request.user,
            exam=exam,
            score=score,
            total=questions.count()
        )

        return render(request, 'exams/result.html', {
            'exam': exam,
            'score': score,
            'total': questions.count()
        })

    return render(request, 'exams/start_exam.html', {
        'exam': exam,
        'questions': questions
    })


@login_required
def my_results(request):
    attempts = ExamAttempt.objects.filter(user=request.user)

    return render(request, 'exams/my_results.html', {
        'attempts': attempts
    })


@login_required
def log_activity(request):
    if request.method == "POST":
        activity_type = request.POST.get("activity_type")
        exam_id = request.POST.get("exam_id")

        exam = None
        if exam_id:
            exam = Exam.objects.filter(id=exam_id).first()

        SuspiciousActivity.objects.create(
            user=request.user,
            exam=exam,
            activity_type=activity_type,
            description=f"{activity_type} detected"
        )

        return JsonResponse({"status": "logged"})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_invalid(self, form):
        SuspiciousActivity.objects.create(
            user=None,
            exam=None,
            activity_type="Failed Login Attempt",
            description=f"Username: {self.request.POST.get('username')}"
        )
        return super().form_invalid(form)


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

