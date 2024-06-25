print("Welcome to Quiz Game!")

Playing = input("Do you want to play? ")

score = 0
total_score = 0
total_questions = 4


if Playing.lower() != "yes":
   quit()

print("Okay! Let's play :)")

answer = input("what does CPU Stand for? ")
if answer.lower() == "central processing unit" :
    print("correct..!🙂")
    score += 1
    total_score += 100

else:
    print("Wrong..!🙃")

answer = input("what does RAM Stand for? ")
if answer.lower() == "random access memory" :
    print("correct..!🙂")
    score += 1
    total_score += 100

else:
    print("Wrong..!🙃")

answer = input("what does GPU Stand for? ")
if answer.lower() == "graphic processing unit" :
    print("correct..!🙂")
    score += 1
    total_score += 100
else:
    print("Wrong..!🙃")

answer = input("what does ROM Stand for? ")
if answer.lower() == "read only memory" :
    print("correct..!🙂")
    score += 1
    total_score += 100

else:
    print("Wrong..!🙃")

total_percentage = (score/total_questions) * 100

print(f"You got {score} ✅ out of 4 questions correct!")
print(f"You total score: {total_score}")
print(f"You total percentage: {total_percentage:.2f} %")




# Determine ranking
if total_percentage > 75:
    print("Ranking: Top 1")
elif 50 < total_percentage <= 75:
    print("Ranking: Top 2")
elif 30 < total_percentage <= 50:
    print("Ranking: Top 3")
else:
    print("Ranking: Not Qualified")


print("Thanks for Playing...!! 😊")

   
