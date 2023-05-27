import pandas

data = pandas.read_csv("squirrel_data.csv")

# knowing the count of the number of squirrels for each color
color_data = pandas.DataFrame(data['Primary Fur Color'].value_counts())

#exporting the data frame into a csv file
color_data_csv = color_data.to_csv(r'/mnt/sda1/Programming/Python/Udemy/day25/squirrel/squirrel_color_count.csv')
