from django.db import models

class Book(models.Model):
	branch=(('cse','CSE'),('ece','ECE'),('eee',"EEE"),('Mech',"MECH"))
	
	bookid=models.CharField(max_length=50,unique=True)
	name=models.CharField(max_length=300)
	authorname=models.CharField(max_length=100)
	dept=models.CharField(max_length=100,choices=branch)
	edition=models.CharField(max_length=20)
	publisher=models.CharField(max_length=300)
	quantity=models.IntegerField()
	def __str__(self):
		# return self.name+" ~ "+self.bookid+" ~ "+str(self.quantity)
		return self.name


class Student(models.Model):
	# bookname=models.ForeignKey(Book,on_delete=models.CASCADE)
	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	rollno=models.CharField(max_length=20,unique=True)
	fathername=models.CharField(max_length=300)
	gender=models.CharField(max_length=10)
	mobileno=models.CharField(max_length=12)
	emailId=models.CharField(max_length=100)
	
	def __str__(self):
		return self.rollno

class IssueBook(models.Model):
	student=models.ForeignKey(Student,on_delete=models.CASCADE)
	book=models.ForeignKey(Book,on_delete=models.CASCADE)
	issue_date=models.DateField(max_length=10)
	mailed_Date=models.DateField(blank=True, null=True)
	expired=models.DateField(max_length=10)
	status=models.IntegerField(default=0)

	def __str__(self):
		return str(self.student)
class Notify(models.Model):
	student=models.ForeignKey(Student,on_delete=models.CASCADE)
	book=models.ForeignKey(Book,on_delete=models.CASCADE)
	issueBook=models.ForeignKey(IssueBook,on_delete=models.CASCADE)
	mailDate=models.DateField(blank=True,null=True)
	status=models.IntegerField(default=0)
	def __str__(self):
		return str(self.student)+" ~ "+str(self.book)

class Registers(models.Model):
	rollno=models.CharField(max_length=200,unique=True)
	name=models.CharField(max_length=200)
	gender=models.CharField(max_length=10)
	mobile=models.CharField(max_length=12)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=200)

	def __str__(self):
		return self.rollno
# class signup(models.Model):
# 	# g=(('m',"MALE"),('f',"FEMALE"))
# 	# u=(('admin',"admin"),("staff","staff"),("student","student"))

# 	name=models.CharField(max_length=200)
# 	rollno=models.CharField(max_length=20,unique=True)
# 	fathername=models.CharField(max_length=500)
# 	gender=models.CharField(max_length=10)
# 	mobileno=models.CharField(max_length=12)
# 	emailId=models.CharField(max_length=200)
# 	password=models.CharField(max_length=200)
# 	user=models.CharField(max_length=100)

# 	def __str__(self):
# 		return self.name

