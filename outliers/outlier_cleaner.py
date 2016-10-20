#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    errors = predictions - net_worths
    
    ages = ages.tolist()
#    print "type of ages:",type(ages)
#    print "type of ages[0]:",type(ages[0])
    predictions = predictions.tolist()
    net_worths = net_worths.tolist()
    errors = errors.tolist()
    
    cleaned_data = []
    
    for i in range (len(predictions)):

        temp_age = ages[i][0]
#        print "type of temp_age:",type(temp_age)
        temp_net_worth = net_worths[i][0]
        temp_error = abs(errors[i][0])
        temp_tuple = (temp_age,temp_net_worth,temp_error)
        cleaned_data.append(temp_tuple)
#    print cleaned_data
#    print "now let's sort it-----------------------------------------------"
    
    sorted_data = sorted(cleaned_data, key=lambda x: x[2])
#    print sorted_data
    
    cleaned_data = sorted_data[:81]    
    return cleaned_data    