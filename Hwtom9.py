# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:35:45 2017

@author: TomJoseph
"""

import unittest
from prettytable import PrettyTable
from collections import defaultdict


class Student():
    
    def __init__(self,CWID,Name, Major):
        self.CWID=CWID
        self.Name=Name
        self.Major=Major
        self.Takencourse= dict() 
        
        #dd = defaultdict(int)
        #l = [i.split() for i in fname.readlines() 
              #  if i.startswith("From") and i.find("@")>0 and len(i.split())>2]
         
    def courses_taken(self):
        return sorted(self.Takencourse.keys())
    
    def add_course(self, name, grade):
        self.Takencourse[name]= grade
    
   
class Instructor():
        
    def __init__(self , CWID, Name, Department ):
        self.CWID=CWID
        self.Name=Name
        self.Department=Department
        self.coursesTaught=defaultdict(int) 
        
    def add_course(self, name):
        self.coursesTaught[name] += 1
        #fh = open("instructors.txt","r")
        #if len(fname) < 1 : fname = "instructors.txt"
        #dic={}
       # dd = defaultdict(int)
        #l = [i.split() for i in fh.readlines() 
                #if i.startswith("From") and i.find("@")>0 and len(i.split())>2]

    def courses_taught(self):
        return self.coursesTaught.keys()
    
    

class Repository():
    def __init__(self):
        self.student= dict() 
        #self.id = stuid
        #self.sname = sname
        self.instructor= dict()
             #  self.insid = instid
             #   self.iname =iname
        
        self.grades= list()
        
        self.read_student()
        self.read_instructor()
        self.read_grades()
        
        self.process_grades()
        self.stud_summary()
        self.inst_summary()
        
    def read_student(self):
        try:
            f=open('students.txt', 'r')
            #dd = defaultdict(int)
       # l = [i.split() for i in fname.readlines() 
               # if i.startswith("From") and i.find("@")>0 and len(i.split())>2]
        #dd.add(l)
        except FileNotFoundError:
            print(" We can’t open students file")
        else:
           with f:
               for line in f:
                   CWID, name, major= line.strip().split('\t')
                   
                   self.student[CWID] = Student(CWID,name,major)

                  
    def read_instructor(self):
        try:
            f=open('instructors.txt', 'r')
            #df = defaultdict(int)
       # l = [i.split() for i in fname.readlines() 
               # if i.startswith("From") and i.find("@")>0 and len(i.split())>2]
        except FileNotFoundError:
            print(" We can’t open instructor file")
        else:
            with f:
                for line in f:
                    CWID, name, depart = line.strip().split('\t')
                    
                    self.instructor[CWID] = Instructor(CWID, name,depart)
                    
                    

    def read_grades(self):
       try:
           f=open('grades.txt', 'r')
       except FileNotFoundError:
           print(" We can’t open grades file")
       else:   #Studentid ,coursename,Grade, Instructorid
            with f:
                for line in f:
                    CWID ,coursename, Grade, Instructorid = line.strip().split('\t')
                    self.grades.append(Grades(CWID,coursename,Grade,Instructorid))

    def stud_summary(self):
            r1=PrettyTable(field_names=['CWID', 'Name','Completed Courses'])
         #p = PrettyTable(field_names=['CWID', 'Name','Completed courses'])
         #for i in l:
            #stuid, sname, coursestaken = c(fi)
            #p.add_row([stuid, sname,coursestaken])

            for student in self.student.values():
                r1.add_row([student.CWID, student.Name, student.courses_taken()])
            print(r1)
        
    def inst_summary(self):
            r2=PrettyTable(field_names=['CWID', 'Name', 'Dept','Course',' Students'])
         # p = PrettyTable(field_names=['CWID', 'Name','Dept','course','Students'])
            for instructor in self.instructor.values():
                for taught in  instructor.coursesTaught:
                    r2.add_row([instructor.CWID, instructor.Name, instructor.Department, taught,  instructor.coursesTaught[taught]])
            print(r2)
            
    def process_grades(self):
        for grade in self.grades:
           CWID= grade.Studentid
           course=grade.coursename
           lettergrade=grade.Grade
           inst=grade.Instructorid
           self.student[CWID].add_course(course, lettergrade)
           self.instructor[inst].add_course(course)
                    
        
class Grades():
    def __init__(self, Studentid ,coursename,Grade, Instructorid):
        self.Studentid=Studentid
        self.coursename=coursename
        self.Grade=Grade
        self.Instructorid=Instructorid
        
   # def gradeAvg(self):
       # grade=getGrade(avg)
             #if(grade=='A'):
                 #gradeA=gradeA+1
             #elif(grade=='B'):
                # gradeB=gradeB+1
             #elif(grade=='C'):
                # gradeC=gradeC+1
             #elif(grade=='D'):
                 #gradeD=gradeD+1
            # elif(grade=='F'):
                # gradeF=gradeF+1
        #print( grade)
        

class FilesTest(unittest.TestCase):
     def test_repository(self):
         t=Repository()
         self.assertEqual(t.student['11788'].courses_taken(), ['SSW 540'])
         self.assertEqual(t.instructor['98765'].coursesTaught['SSW 567'], 4)
        
def main():
    Repository()
                
if __name__ == '__main__':
    main()
    unittest.main(exit=False, verbosity=2)