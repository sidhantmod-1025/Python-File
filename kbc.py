question =[
  ["India ki captial kya hai ?\n"," Option A :- Mumbai \n", " option B :- haryana\n","Option C :- nepal\n","Option d :- Delhi"],
  ["Python kis type ke language hai ?","Option A :- language","Option B :- Application","Option c :-non", "Option d :- Programming"],
  ["2*2 kitne hote hai ?", "5","3","2","4"]
]

amount =[10000,500000,100000]
won =0

for i in range (len(question)):
  print("\n Question : ",question[i][0],question[i][1] ,
question[i][2] , 
question[i][3] ,
question[i][4], )

  answer = input("Your Answer :")

  if(answer.lower()==question[i][4].lower()):
    print("Correct");
    won = amount[i]
  else:
    print("Wrong Answer ")
    break
print("\n App ghar jaa sakte hoo",won)    