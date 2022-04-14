# Imagine the following scenario: You are a data analyst at an organisation. You have been given a data set and asked to 
# create a meaningful data visualisation using this data. Using the ggplotin-built data sets in RStudio and the qplot function, 
# get your creative juices flowing and create a meaningful and impactful data visualisation using your preferred data set.

# 1. Write an R program to create three vectors a, b, c with 5 integers. Combine the three vectors to become a 3×5 matrix 
# where each column represents a vector. Print the content of the matrix. Plot a graph and label correctly.

a<-c(1,2,3)
b<-c(4,5,6)
c<-c(7,8,9)
m<-cbind(a,b,c)
print(m)

matplot(t(m),
        type = "l",
        lwd = 2,
        main="The Rows of a Matrix",
        ylab="Value")

# 2. Write a R program to create a Data frames which contain details of 5 employees and display the details. 
# (Name, Age, Role and Length of service).

employee.data <- data.frame(
  employee_id = c (1:5), 
  employee_name = c("Charlie","Harry","Laura","Eloise","Simon"),
  age = c(30,28,40,48,27),
  role = c("business analyst", "sales executive", "CEO", "COO", "CFO"),
  length_of_service = (c(3, 5, 8, 4, 6)),
  stringsAsFactors = FALSE
)

print(employee.data) 

# 3. Import the GGPLOT 2 library and plot a graph using the qplot function. X axis is the sequence of 1:20 and the y axis 
# is the x ^ 2. Label the graph appropriately. install.packages("ggplot2", dependencies = TRUE)

# Import Libraries
library(ggplot2)

x <- c(1:20)
print(x)

y <- x^2
print(y)

qplot(x, y)

# 4. Create a simple bar plot of five subjects

Grades = c(75, 95, 65, 55, 80)
barplot(Grades,
        main = "Grades of 5 Subjects",
        xlab = "Subject",
        ylab = "Grades",
        names.arg = c("English", "Science", "Business.", "Mathematics", "Psychology."),
        col = "gray",
        horiz = FALSE)

# 1. Write a R program to take input from the user (name and age) and display the values.

name = readline(prompt="Input your name: ")
age =  readline(prompt="Input your age: ")
print(paste("My name is",name, "and I am",age ,"years old."))

# 2. Write a R program to create a sequence of numbers from 20 to 50 and find the mean of numbers from 20 to 50 and sum of
# numbers.

print(seq(20,50))
print(mean(20:50))
print(sum(20:50))

# 3. Write a R program to create a vector which contains 10 random integer values between -50 and +50

x = sample(-50:50, 10)
print(x)
