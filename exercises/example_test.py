import pytest
import System
import Professor
import Student
import TA

username = 'akend3'
password = '123454321'
usernameP = 'calyam'
passwordP = '#yeet'
username2 = 'hdjsr7'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

## 1. check login
def test_login(grading_system):
	users = grading_system.users
	grading_system.login('calyam', '#yeet')
	grading_system.__init__()
	if users[usernameP]['role'] != 'professor':
		assert False

## 2. check_password - System.py
def test_check_password(grading_system):
	test = grading_system.check_password(usernameP, passwordP)
	test2 = grading_system.check_password(usernameP, '#yeet')
	test3 = grading_system.check_password(usernameP, 'alkjdf;klsdjf')
	if(test == test3 or test2 == test3):
		assert False
	if test != test2:
		assert False

## fail test
## 3. change_grade - Staff.py 
def test_change_grade(grading_system):
	grade = 90
	users = grading_system.users
	grading_system.login('goggins', 'augurrox')
	grading_system.usr.change_grade('hdjsr7', 'cloud_computing', 'assignment1', grade)
	assert grading_system.users['hdjsr7']['courses']['cloud_computing']['assignment1']['grade'] == 90

## 4. create_assignment Staff.py
def test_create_assignment(grading_system):
	assignmentName = "assignment3"
	dueDate = '2/7/20'
	grading_system.login('goggins', 'augurrox')
	grading_system.usr.create_assignment(assignmentName, dueDate, 'cloud_computing')
	assert grading_system.courses['cloud_computing']['assignments'][assignmentName]['due_date'] == dueDate
#fail test			
## 5. add_student - Professor.py
def test_add_student(grading_system):
	username = 'ytehgfdfjg91'
	course = grading_system.courses
	grading_system.login('goggins', 'augurrox')
	grading_system.usr.add_student(username, course[0])
	assert grading_system.users[username]['courses'][course] == 'cloud_computing'

## 6. drop_student Professor.py
def test_drop_student(grading_system):
	grading_system.login('goggins', 'augurrox')
	grading_system.usr.drop_student('akend3', 'databases')
	hiscourse = grading_system.users['akend3']['courses']
	for course in hiscourse: 
		if(course == 'databases'):
			assert False
#failed test
## 7. submit_assignment - Student.py
def test_submit_assignment(grading_system):
	course = 'cloud_computing'
	assignment_name = "assignment3"
	grading_system.login('yted91', 'imoutofpasswordnames')
	grading_system.usr.submit_assignment(course, assignment_name, "aksjdf", '3/3/1990')
	assert grading_system.users[username]['courses'][course][assignment_name]['submission_date'] == '3/5/1990'
# failed test
## 8. check_ontime - Student.py
def test_ontime(grading_system):
	grading_system.login(username, password)
	#always return true, so does not always work
	ontime = grading_system.usr.check_ontime('3/5/20', '3/8/20')
	if(ontime and '3/8/20' > '3/5/20'):
		assert False
#filed test	
## 9. check_grades - Student.py
def test_grades(grading_system):
	grading_system.login('hdjsr7', 'pass1234' )
	grades = grading_system.usr.check_grades('cloud_computing')
	assert grading_system.users['hdjsr7']['courses']['cloud_computing']['assignment1']['grade'] == grades[0]

## 10. view_assignments - Student.py
def test_view_assignments(grading_system):
	grading_system.login('hdjsr7', 'pass1234')
	assignments = grading_system.usr.view_assignments('cloud_computing')
	assert grading_system.courses['comp_sci']['assignments']['assignment1']['due_date']

def test_username_length(grading_system):
	users = grading_system.users
	for user in users:
		if len(user) < 5:
			assert False

def test_password_length(grading_system):
	users = grading_system.users
	for user in users:
		if len(grading_system.users[user]['password']) > 10:
			assert False

def test_teacher_change_student_grade_not_in_class(grading_system):
	grading_system.login('goggins', 'augurrox')
	grading_system.usr.change_grade('hdjsr7', 'cloud_computing', 'assignment1', 30)
	if(grading_system.users['hdjsr7']['courses']['cloud_computing']['assignment1']['grade'] == 0):
		#Goggins does not have privilage for the cloud computing class
		assert False;

def test_teacher_drop_student_not_in_class(grading_system):
	grading_system.login('goggins', 'augurrox')
	grading_system.usr.drop_student('hdjsr7', 'cloud_computing')
	for course in grading_system.users['hdjsr7']['courses']:
		if(course != 'cloud_computing'):
		#Goggins does not have privilage to cloud computing class	
			assert False

def test_teacher_create_assignment_not_for_class(grading_system):
	grading_system.login('goggins', 'augurrox')
	grading_system.usr.create_assignment('oliviaIsTheBest', '3/2/3035', 'cloud_computing')
	if(grading_system.courses['cloud_computing']['assignments']['oliviaIsTheBest']['due_date'] == '3/2/3035'):
		assert False
	#Goggins does not have privilage to create this assignment
