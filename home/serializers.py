from rest_framework import serializers
from home.models import *
from django.contrib.auth.models import User
#serializer for User table
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=('id','username','first_name','last_name','email')
		
#Serializer for Personnel table
class PersonnelSerializer(serializers.ModelSerializer):
	class Meta:
		model=Personnel
		fields=('Person_ID','LDAP','Role','Dept')
#Serializer for Department table
class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Department
		fields=('Dept_ID','Dept_Name')

class RolesSerializer(serializers.ModelSerializer):
	class Meta:
		model=Roles
		fields=('Role_ID','Role_name','level')
#Serializer for Courses table
class CoursesSerializer(serializers.ModelSerializer):
	class Meta:
		model=Courses
		fields=('Course_ID','Course_Name','Course_description','Course_Credits','Course_Year','Course_Status')
#Serializer for Document table
class DocumentsSerializer(serializers.ModelSerializer):
	class Meta:
		model=Documents
		fields=('Doc_ID','Doc_Name','Document')

#Serializer for Assignment table
class AssignmentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Assignment
		fields=('Assign_ID','Assignment_File','Course_ID','Start_Time','End_Time')

#Serializer for Submission table
class SubmissionsSerializer(serializers.ModelSerializer):
	class Meta:
		model=Submissions
		fields=('Sub_ID','Assign_ID','Student_ID','Sub_Time','Score')

class ICSerializer(serializers.ModelSerializer):
	class Meta:
		model=Instructors_Courses
		fields=('IC_id','Course_ID','Inst_ID','Start_Date','End_Date')

class SCSerializer(serializers.ModelSerializer):
	class Meta:
		model=Students_Courses
		fields=('SC_ID','Student_ID','Course_ID','Reg_Date')

class EventsSerializer(serializers.ModelSerializer):
	class Meta:
		model=Events
		fields=('Event_ID','Event_Date','Event_Name')

class SPSerializer(serializers.ModelSerializer):
	class Meta:
		model=Student_Period
		fields=('Student_ID','Start_Year','End_Year')
#Serializer for Attendance table
class AttendanceSerializer(serializers.ModelSerializer):
	class Meta:
		model=Attendance
		fields=('Student_ID','ASession_ID','Date_time','Marked')

#Serializer for Attendance table
class Attendance_SessionSerializer(serializers.ModelSerializer):
	class Meta:
		model=Attendance_Session
		fields=('Session_ID','Course_Slot','Date_time','Status','Location')

#Serializer for Timetable table
class TimetableSerializer(serializers.ModelSerializer):
	class Meta:
		model=Timetable
		fields=('T_days','Start_time','End_time','Course_ID','Class_ID')
