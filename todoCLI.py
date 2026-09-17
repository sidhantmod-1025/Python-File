print ("========TODO CLI APP========")

tasks =[]
while True:
  print("1. Add Task : ")
  print("2.View TAsk : ")
  print("3. Delete TAsk : ")
  print("4.Mark Task Complete : ")
  print("5. Exit :")

  choice = input("Enter your choice : ")
#print ("You Selected Task  : ",choice)
 
  if choice == "1": 
    print ("========TODO CLI APP========")
    task = input("Enter task : ")
    tasks.append ({
      "name":task,
      "complete":False
     })
    print("Task added successfully!")

  
  elif choice =="2":
    print ("========TODO CLI APP========")
    for i in enumerate(tasks,start=1):
      print(i,tasks)
   
  elif choice=="3":
     for i, task in enumerate(tasks, start=1):
        print(i, task["name"]) 
        task_number = int(input("Enter task number to delete : "))
        tasks.pop(task_number-1)
        print("Task deleted successfully !")
  elif choice=="4":
     print ("========TODO CLI APP========")
     for i,task in enumerate(tasks,start=1):
        if task["complete"]==True:
           print(i,task["name"],"completed")
        else:
           print(i,task["name"],"Pending")
           
     task_number = int(input("Enter task numbeer to completed : "))  
     tasks[task_number-1]["complete"]= True
     print("Task Completed")  

  elif choice =="5":
     print ("========TODO CLI APP========")
     print("Thank you for using Todo App!")      
     break 

