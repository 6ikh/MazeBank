class User():
  def __init__(self,name,age,gender):
    self.name = name
    self.age = age
    self.gender = gender

  def displayInfo(self):
    print("User Information")
    print("")
    print("Name", self.name)
    print("Age", self.age)
    print("Gender", self.gender)

class MZBANK(User):

  def __init__(self,name,age,gender):

    self.name = name
    self.age = age
    self.gender = gender
    self.balance = 0

  def deposit(self, amount):
    self.balance = self.balance + amount
    print("New Balance Amount" , self.balance)

  def withdraw(self, amount):
    self.amount = amount

    if(self.amount > self.balance):
      print("You can not overdraw your account, please try again later")

    else:
      self.balance = self.balance - amount
      print("New balance Amount", self.balance)

  def loanapplication(self,creditscore,incomeAmount):
    self.creditscore = creditscore
    self.incomeAmount = incomeAmount

    if(creditscore < 500):
      print("Your Application Has Been Declined! Your Credit Score is Too Low!")
    else:
      print("Congrats You Have Been Approved")
      self.creditLimit = self.incomeAmount / 15
      print("You Credit limit", self.creditLimit)


print("Welcome To the Maze Bank!")

name = input("What Is Your Name?")

print("To Get Started At Maze Bank,", name , ",You Need an Account!")
print("Lets Get Started With the Account Creation!")

age = int(input("What is Your Age?:"))
gender = input("What is Your Gender:?")

USER1 = MZBANK(name,age,gender)
USER1.displayInfo()

loopCheck = True

optionsList = ["[1] Make A Deposit", "[2] Make A Withdrawal",
"[3] Apply For A Loan Application", "[4] End The Program"]

while(loopCheck == True):

  for i in optionsList:
    print(i)

  selection = int(input("Please Select What You Would Like to Do:"))

  if (selection == 1):

    depositAmount = int(input("How Much Would You Like To Deposit:"))
    USER1.deposit(depositAmount)

  elif(selection == 2):

    withdrawalAmount = int(input("How Much Would You Like To Withdraw:"))
    USER1.withdraw(withdrawalAmount)

  elif(selection == 3):

    creditScore = int(input("What is Your Credit Score?:"))
    incomeAmount = int(input("What is Your Annual Income?:"))
    USER1.loanapplication(creditScore,incomeAmount)

  else:
    loopCheck = False


