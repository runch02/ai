install.packages("rpart")
library(rpart)

install.packages("rpart.plot")
library(rpart.plot)

# Get the current working directory
getwd()

# Set the working directory
setwd("D:/AIPRAC")

# Read the dataset
d <- read.csv("restaurant.csv")

# Create the decision tree model
mytree <- rpart(Wait ~ ., data = d, minsplit = 1, minbucket = 1)

# Plot the decision tree
rpart.plot(mytree)

# Make predictions
p <- predict(mytree)
p


prac_3
