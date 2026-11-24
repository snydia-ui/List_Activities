#Activity 1 – Student Quiz Score Analyzer
quizzes = []
for i in range(1,6):
    quizzes.append(int(input(f"Enter Quiz {i} score: ")))

print(f"""===== QUIZ SCORE REPORT =====
Quiz Scores: {quizzes}
Number of Quizzes: {len(quizzes)}
Total Score: {sum(quizzes)}
Average Score: {sum(quizzes)/len(quizzes):.2f}
Highest Score: {max(quizzes)}
Lowest Score: {min(quizzes)}
Ascending:  {sorted(quizzes)}
Descending: {sorted(quizzes, reverse=True)}
Original Scores:{quizzes} """)
