# Know many hour will be spend for work today
# Know many task that will be done in one day
# Know number of block that can be used to seperated task 
#example, divided email task into two block, one in morning and in noon.

import itertools as it #import itertools
import random

def taskBlock_Assign(number_Hour, number_Task, number_Block):
 # 0.5 jam
  time_Todo = number_Hour / number_Task
  time_Todo_minute = time_Todo * 60 #conversion hour to minute

  Hour = int(time_Todo_minute / 60) #divided minute by 60 to get hour
  Minute = int(time_Todo_minute % 60) #modulo 60, to get minute
  
  return Hour, Minute

def Combination_Task(Task):
  List_Task = list(it.permutations(Task)) #permutation the task

  Many_Set = 0 #count how many permutation task, 4! = 24
  for iterate in List_Task:
    Many_Set += 1
  
  pick_Random = random.randint(0, (Many_Set - 1)) 
  # take 0 - 23 list, array start at 0 so we need to normalize it


  return List_Task[pick_Random]
  # pick permutation task, based on random number pick by computer
  
def TaskVisualize (ListOftask,Hour, Minute):
  number = 1

  for iterate in ListOftask:
    print("Task ", number," :", " ", iterate)
    print("time: ", Hour, " Jam ", Minute, " Menit")
    number += 1
    


# Run Loop of Code Here

hour = 6 #hour allocated per day
Data_task = [ "Email","Study", "Sleeping", "Singing"] #how many task per day
Many_task = 0 # counter to count how many task
block = 2 #number of block assign for spesific task that can be divided 

for task in Data_task: #count many task
  Many_task += 1


assign_Hour, assign_Minute = taskBlock_Assign(hour,Many_task,block)

print("Number of task: ", Many_task)


print("Time need to acomplish each task: ", assign_Hour, "Hour", assign_Minute ,"Minute")

Task_Today = Combination_Task(Data_task)

print("Today Task: ", Task_Today)

TaskVisualize(Task_Today, assign_Hour, assign_Minute )

  

