from polls.models import Question, Choice

q_template = {
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "pub_date": "2022-02-13T05:00:00Z"
}
c_template = {
    "question": 1,
    "choice_text": "a1",
    "votes": 0
}
Question.objects.all().delete()
result = [
    Question(**{**q_template, 'question_text': f'Question {i+1}'})
    for i in range(20_000)
]
questions = Question.objects.bulk_create(result)


Choice.objects.all().delete()
result = []
for i, q in enumerate(questions):
    result.append(Choice(**{"question_id": q.id, "choice_text": f"a{i*3+1}", "votes": 0}))
    result.append(Choice(**{"question_id": q.id, "choice_text": f"b{i*3+1}", "votes": 1}))
    result.append(Choice(**{"question_id": q.id, "choice_text": f"c{i*3+1}", "votes": 2}))

_ = Choice.objects.bulk_create(result)
