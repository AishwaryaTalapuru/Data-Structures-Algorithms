class Solution(object):
    def countStudents(self, students, sandwiches):
        if len(students)==0:
            return 0
        if len(sandwiches)==0:
            return len(students)
        if students == sandwiches:
            return 0
        while (len(set(students))==1 and students[0]!=sandwiches[0])==False:
            if students == sandwiches:
                return 0
            if students[0] != sandwiches[0]:
                elem = students[0]
                students = students[1:]+[elem]
            else:
                students = students[1:]
                sandwiches = sandwiches[1: ]
        return len(students)
sol_obj = Solution()
students = [[1,1,1,0,0,1], [1,1,0,0]]
sandwiches = [[1,0,0,0,1,1], [0,1,0,1]]
for item in range(len(students)):
    print("The number of students in ", students[item], " unable to have sandwiches in ", sandwiches[item], " is: ", sol_obj.countStudents(students[item], sandwiches[item]))
#Time Complexity - O(n) where n is the size of the input (students, sandwiches)
#Space Complexity - O(1)