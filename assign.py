import pandas as pd
import collections
import csv

class people:
    
    def __init__(self,personID,skillID,name):
        """
        Defining the class for ppl that includes the 3 parameters
        @params:
        personID : the ID associated with the person
        skillID : the array of skills that the person has
        name : the name of the person
        """
        self.personID=personID
        self.skillID=skillID
        self.name=name

class task:

    def __init__(self,taskID,skillID,priority):
        """
        Defining the class for tasks that includes the 3 parameters
        @params:
        taskID : the ID associated with the task that needs to be done
        skillID : the skill ID that is req. to complete the task
        priority : priority of the task (True: for urgent,False: for less urgent)
        """
        self.taskID=taskID
        self.skillID=skillID
        self.priority=priority


def add_val_tasks(data_tasks):
    """
    This method returns a list of task values sorted based on priority
    """
    tasks=[]
    for i in range(len(data_tasks)):
        taskID=data_tasks.loc[i]['Id']
        skillID=data_tasks.loc[i]['SkillRequired']
        priority=data_tasks.loc[i]['IsPriority']
        tasks.append(task(taskID,skillID,priority))
    tasks.sort(key= lambda x:x.priority,reverse=True)
    return tasks

def add_val_ppl(data_ppl):
    """
    This method returns a list of people values 
    """
    ppl=[]
    for i in range(len(data_ppl)):
        id=data_ppl.loc[i]['Id']
        name=data_ppl.loc[i]['Name']
        skill=data_ppl.loc[i]['Skills']
        ppl.append(people(personID=id,skillID=skill,name=name))
    return ppl

def addSkills(data,length):
    """
    This returns a dictionary of the list of skills that each person has
    """
    arr={}
    for i in range(1,length+1):
        arr[i]=[]
    for i in range(len(data)):
        personId=int(data.loc[i]['PersonId'])
        skillId=int(data.loc[i]['SkillId'])
        arr[personId].append(skillId)
    return arr

def makeDict(data,skill_num):
    """
    returns a dictionary of skillID vs the list of people that have those skills
    """
    d={}
    for i in range(1,skill_num[0]+1):
        d[i]=[]
    for i in range(len(data)):
        id=data[i].personID
        skills=data[i].skillID
        for i in skills:
            d[i].append(id)
    return d



def takeInput(ppl,skills,tasks):
    """
    This method takes input from diff files and returns 
    ppl: the list of people with IDs,skills and names
    tasks: the list of tasks with IDs,skill req and priority
    skill_num : the max skillID
    """

    data_ppl=pd.read_csv(ppl)
    data_skills=pd.read_csv(skills)
    data_tasks=pd.read_csv(tasks)
    data_ppl['Skills']=addSkills(data_skills,len(data_ppl)).values()
    skill_num=data_ppl['Skills'].max()

    ppl=add_val_ppl(data_ppl)
    tasks=add_val_tasks(data_tasks)    

    return ppl,tasks,skill_num
    


def assign(ppl_data,skills_data,tasks_data):
    """
    assigns the tasks to people and returns an orderedDict of taskID vs the personID and the day assigned
    """
    ppl,tasks,skill_num=takeInput(ppl_data,skills_data,tasks_data)
    data=makeDict(ppl,skill_num) # makes a dictionary of skills vs personID

    main_assign={}
    main_check=[0]*len(tasks)
    day=1
    while (sum(main_check)<len(tasks)):
        person_assign=[0]*len(ppl)
        i=0
        while (sum(person_assign)<len(ppl)) and (i<len(tasks)):
            if main_check[i]==0:
                task_id=tasks[i].taskID
                skill_req=tasks[i].skillID
                for x in data[skill_req]:
                    if person_assign[x-1]==0:
                        person_assign[x-1]=1
                        main_assign[task_id]=[x,day]
                        main_check[i]=1
                        break
            i+=1
        day+=1

    return collections.OrderedDict(sorted(main_assign.items()))

def write_csv(data,filename):
    """
    writes to the csv file
    """
    fields=['TaskID','PersonID','Day']

    with open(filename,'w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(fields)
        for row in data:
            writer.writerow([row,data[row][0],data[row][1]])
