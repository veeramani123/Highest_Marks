# Time - O(n) | Space - O(n), where n is the number of rows in the csv file.
import csv

def largestnums(max_score, three_ranks, total, name):
    if  max_score[2]==0 or total > max_score[2]:
        shiftm(max_score,total,three_ranks,2,name)
    elif max_score[1]==0 or total > max_score[1]:
        shiftm(max_score,total,three_ranks,1,name)
    elif max_score[0]==0 or total > max_score[0]:
        shiftm(max_score,total,three_ranks,0,name)
    else:
        return
def shiftm(max_score, total,three_ranks, pos,name):
    for i in range(pos+1):
        if i==pos:
            max_score[pos] = total
            three_ranks[pos] = name
        else:
            max_score[i] = max_score[i+1]
            three_ranks[i] = three_ranks[i+1]

with open('Student_marks_list.csv','r') as file:
	
	reader = csv.reader(file, delimiter = ',')
	headings = next(reader)
	Output = []
	for row in reader:
		Output.append(row[:])

max_score  = [0,0,0]
three_ranks = ["","",""]
subjects_max = ["","","","","",""]
scores_max = [0,0,0,0,0,0]
for tuples in enumerate(Output):
    rows = tuples[1]
    total = 0
    total = total + int(rows[1]) + int(rows[2]) + int(rows[3]) + int(rows[4]) + int(rows[5]) + int(rows[6])
    largestnums(max_score,three_ranks,total, rows[0])
    if(int(rows[1])>scores_max[0]):
        scores_max[0] = int(rows[1])
        subjects_max[0] = rows[0]
    if(int(rows[2])>scores_max[1]):
        scores_max[1] = int(rows[2])
        subjects_max[1] = rows[0]
    if(int(rows[3])>scores_max[2]):
        scores_max[2] = int(rows[3])
        subjects_max[2] = rows[0]
    if(int(rows[4])>scores_max[3]):
        scores_max[3] = int(rows[4])
        subjects_max[3] = rows[0]
    if(int(rows[5])>scores_max[4]):
        scores_max[4] = int(rows[5])
        subjects_max[4] = rows[0]
    if(int(rows[6])>scores_max[5]):
        scores_max[5] = int(rows[6])
        subjects_max[5] = rows[0]
print("Topper in Maths is",subjects_max[0])
print("Topper in Biology is",subjects_max[1])
print("Topper in English is",subjects_max[2])
print("Topper in Physics is",subjects_max[3])
print("Topper in Chemistry is",subjects_max[4])
print("Topper in Hindi is",subjects_max[5])
print("Best students in the class are",three_ranks[2],",",three_ranks[1], ",", three_ranks[0])

	
