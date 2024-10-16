install.packages("neuralnet")
library(neuralnet)
getwd()
setwd("D:/AIPRAC")
d <- read.csv("restaurantnn.csv")
d
net <- neuralnet(WILLWAIT ~ ALT + BAR + FRI + HUN + PAT + PRICE + RAIN + RES + TYPE + EST, 
                 data = d, 
                 hidden = 3)
plot(net)
prediction(net)
