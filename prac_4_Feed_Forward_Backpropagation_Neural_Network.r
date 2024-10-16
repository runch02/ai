install.packages("neuralnet")
library(neuralnet)

# Get the current working directory
getwd()

# Set the working directory
setwd("D:/AIPRAC")

# Read the dataset
d <- read.csv("restaurantnn.csv")
d

# Create the neural network model
net <- neuralnet(WILLWAIT ~ ALT + BAR + FRI + HUN + PAT + PRICE + RAIN + RES + TYPE + EST, 
                 data = d, 
                 hidden = 3)

# Plot the neural network
plot(net)

# Make predictions (Note: Ensure the correct function is used here)
prediction(net)


prac_4
