install.packages("e1071")
library(e1071)
Train <- read.csv(file.choose())
Test <- read.csv(file.choose())
model <- naiveBayes(WILLWAIT ~ ., data = Train)
class(model)
model
pred <- predict(model, Test)
table(pred)
