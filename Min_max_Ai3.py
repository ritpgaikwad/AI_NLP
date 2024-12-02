import math

def minimax (curDepth, nodeIndex, maxTurn, scores, targetDepth):

	# base case : targetDepth reached
	if (curDepth == targetDepth): 
		return scores[nodeIndex]
	
	if (maxTurn):
		return max(minimax(curDepth + 1, nodeIndex * 2, 
					False, scores, targetDepth), 
				minimax(curDepth + 1, nodeIndex * 2 + 1, 
					False, scores, targetDepth))
	
	else:
		return min(minimax(curDepth + 1, nodeIndex * 2, 
					True, scores, targetDepth), 
				minimax(curDepth + 1, nodeIndex * 2 + 1, 
					True, scores, targetDepth))
	

#scores = [3, 5, 2, 9, 13, 18, 23, 23]



a = int(input("Enter size of input list"))
score = []
for i in range(0, a):
    b = int(input())
    score.append(b)
treeDepth = math.log(len(score), 2)

print("The optimal value is : ", end = "")
print(minimax(0, 0, True, score, treeDepth))
