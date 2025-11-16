from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Question, DailyQuestion

def question_of_the_day(request):
    dq = DailyQuestion.get_today()
    q = dq.question

    # If the user clicked "Submit"
    if request.method == "POST":
        user_answer = request.POST.get("answer")
        correct = (user_answer == q.answer)
        return render(request, "quizaplikacja/question_result.html", {
            "question": q,
            "correct": correct,
            "user_answer": user_answer,
        })

    # Otherwise just show the question
    return render(request, "quizaplikacja/question_of_the_day.html", {"question": q})

def add_question(request):
    if request.method == "POST":
        text = request.POST.get("text")
        choices = request.POST.getlist("choices")
        answer = request.POST.get("answer")

        if answer not in choices:
            return render(request, "add_question.html", {
                "error": "Correct answer must be one of the choices"
            })

        Question.objects.create(
            text=text,
            choices=choices,
            answer=answer,
        )
        return redirect("add_question")

    return render(request, "quizaplikacja/add_question.html")
