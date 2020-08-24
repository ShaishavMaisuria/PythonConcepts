import random

randNumber=random.random()
print("random ()",randNumber)
randomNumber= random.randint(100,1500)
#100-1500
print("Random Integer ",randomNumber)
#range, length list  200-800. 10
randomList=random.sample(range(200,800),10)
print("List", randomList)
print("List length",randomList.__len__())