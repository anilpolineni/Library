from django.urls import path
from . import views
app_name="lbook"
urlpatterns=[
	path("",views.home,name="home"),
	# path("home",views.home1,name="homes"),
	path("Clientbook",views.clientBookSearches,name="Clientsearches"),


	path("book",views.book,name="book"),
	path("bookSearch",views.bookSearch,name="bookSearch"),
	path("addBook",views.addBook,name="addBook"),	
	path("issueBook",views.issueBook,name="issueBook"),
	path("IssuedBook",views.viewIssueBook,name="viewIssueBook"),
	path("issueNewBook",views.issueNewBook,name="issueNewBook"),
	path("Student",views.addStudent,name="addStudent"),
	path("StudentIssuedBook",views.StudentIssuedBook,name="StudentIssuedBook"),
	path("returnBook",views.returnBook,name="returnBook"),
	path("warnMail",views.warningMails,name="warningMails"),
	path("viewWarns",views.viewWarningMails,name="viewWarningMails"),

	path("signup",views.signup,name="signup"),
	path("login",views.login,name="login"),
	path("logout",views.logout,name="logout"),
]