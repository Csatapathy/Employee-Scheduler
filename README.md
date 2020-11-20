# Employee-Scheduler

## Objectives:
1. Create a working schedule that is fair and is equally distributed.
2. Take in consideration the skill assets of the people and the skills required to complete certain tasks.
3. Take in consideration the priority level of the tasks and schedule those first.

## Data:
The data required is in the data/in in the repository.
### 1. Employees:
There are 6 employees that have different skill sets.Each employee is designated to have one or more skills as documented in the following skills matrix:

![People and their skill set](https://user-images.githubusercontent.com/68659873/99768673-35bb7d80-2b2b-11eb-951f-4022886279ed.png)
### 2. Tasks:
The department receives a list of tasks that detail the work to be done. Each task takes one person a full day to complete and must be performed by someone with a certain skill.
Some of the tasks are marked as having priority and should be completed as early as possible.

![Tasks](https://user-images.githubusercontent.com/68659873/99768774-5edc0e00-2b2b-11eb-875e-a43a210e49e9.png)
### 3. Skills:
The skill level is an indication of the relative difficulty of obtaining that skill and roughly correlates to the scarcity of the skill and, therefore, the cost of employing someone with that skill.The following is a list of all the skills:

![Skill vs skill level](https://user-images.githubusercontent.com/68659873/99768847-774c2880-2b2b-11eb-89ca-4843305b50cd.png)

## What to generate:
The plan we are being asked to generate needs to identify which tasks will be performed on which day and by whom. An example looks like this:

![image](https://user-images.githubusercontent.com/68659873/99769024-bf6b4b00-2b2b-11eb-8545-dad435b2787e.png)

Some additional information that will help generate a valid plan:
* Each task takes a full day to perform.
* Each task requires a single person to perform it

## The code:
1. There are two classes: people and task. These two take in the input and sort them according to the skill levels and the priority of the tasks.
2. The assign function takes in this input then assigns the work to each worker according to the skill required to complete the task and the skill assets of the worker.
3. The high priority jobs take precedence and are assigned first.
4. Then the schedule is outputted to the csv files in data/out

## Data Analysis:
These are metrics that management are interested in when evaluating the plan:
### 1. For 14 tasks:
1. The number of days it takes to complete all the high priority jobs=1 day for 6 high priority tasks
2. The number of days it takes to complete the whole list of jobs= 3 days
3. How effectively each person’s skill set it being utilized= min days required was 14/6=2.3 days..we did it in the same time. So the utilisation is maximum.
4. How long it takes to generate the plan=0.02830362319946289 seconds
### 2. For 300 tasks:
1. The number of days it takes to complete all the high priority jobs= 6 days for 36 high priority tasks
2. The number of days it takes to complete the whole list of jobs= 50 days
3. How effectively each person’s skill set it being utilized=  min days required was 300/6=50 days.we did it in the same time. So the utilisation is maximum.
4. How long it takes to generate the plan=0.15445661544799805 seconds
