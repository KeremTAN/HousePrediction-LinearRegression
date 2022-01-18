# HousePrediction-LinearRegression

## How did we implement it?
First of all, we included the necessary libraries for processing our data and using our algorithm (lines 1-6). </br>
After included our libraries, we loaded the prices.csv file as a dataframe into the data variable </br>
and created the linearReg object to implementation linear regression (line 9 and 12). </br>
Afterwards, we pre-process our data and assign our feature data and the data </br>
we want to predict according to our features as dataframes to two separate variables (line 15 and 17). </br>
After the above processes, our data is divided into 20% for testing and 80% for training (line 19). </br>
We tried to learn the values of y_train by values of x_train with using the fit method with the linearReg object. </br>
We predicted our y_test data according to our x_test data using the predict method with </br>
the linearReg object and assigned our prediction to the y_predictions variable (line 21 and 22).


## Output
![UML](https://github.com/KeremTAN/HousePrediction-LinearRegression/blob/master/img/output.png)
