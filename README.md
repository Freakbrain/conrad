# conrad

This is a simple streaming for a prediction. 

I used the xgboost model on the iris data set. 
It is based on flask and accepted only POST Requests. 


The input are the four varialbes sepal_length, spepal_width, pedal_lenght and pedal_width with the values between 0 and 10
The output is a probility distribution of with of the three different Iris (Iris setosa, Iris versicolor, Iris virginica) 


The api can be called via the comand line with

curl -i -H "Content-Type: application/json" -X POST -d '{"sepal_length" : 5, "sepal_width" : 5, "pedal_length" : 5, "pedal_width" : 5}' http://localhost:5000/prediction
