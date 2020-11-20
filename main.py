import time
from assign import write_csv,assign
# for 14 tasks
start=time.time()
ppl='data/in/people.csv'
skills='data/in/skillMatrix.csv'
tasks='data/in/tasks-small.csv'
filename='data/out/assignments-small.csv'
write_csv(assign(ppl,skills,tasks),filename)
end=time.time()
print('Time taken for 14 tasks: ',end-start)

# for 300 tasks
start=time.time()
ppl='data/in/people.csv'
skills='data/in/skillMatrix.csv'
tasks='data/in/tasks-large.csv'
filename='data/out/assignments-large.csv'
write_csv(assign(ppl,skills,tasks),filename)
end=time.time()
print('Time taken for 300 tasks: ',end-start)