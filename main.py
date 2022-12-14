# ****************************************************************
# Third mini project
# learning python basics 
# learning for loops, lists, basic mathematics and statistics operations
# ****************************************************************
import statistics
# Taskn 1
print("Task 1")
print() # indicates a space
# A program that loops the list of items in Bill Gate's list
# Bill Gate list of items for his journey
Bill_items = ["Medications", "Clothes", "Books", "Food", "Camera", "Water", "Money", "Compass", "Chocolates", "Pen"]
# Using for loop to print out items in bill's list
for item in range(0, 10):
  print(f"Item {item + 1} is {Bill_items[item]}")
# Reminding Bill to take all his items for the journey
  print()  # indicates a space
print("Bill, remember to take all your items for this journey")
print() # indicates a space
# Copying all items in Bill_items in a new list
new_lists = Bill_items[:]  # new list

# Removing 5 items from Bill_items using slices and del
del Bill_items[0:5]  # deletes 5 items from Bills original list
print(Bill_items)  # current list in Bill_items
print() # indicates a space
print(new_lists)  # current list in new_lists
print() # indicates a space

# Task 2
print("Task 2")
print() # indicates a space
# A program that list the number 1 to 1000 using a for loop
# printing values 1 to 1000 using a for loop
number = list(range(1,1001)) 
len_number = len(number)  # indicates length of the variable number
for i in range(0, len_number):  # it starts from index 0 and index zero in number is 1 and the length of number is 1000. This why the loop started with 1 and ended with 1000.
  print(number[i])  # values 1 to 1000 printed
print() # indicates a space
# printing min(), max() and sum() to find the smallest, largest, and combined total
print(min(number))  # minimum value is 1
print() # indicates a space
print(max(number))  # maximum value of 1000
print() # indicates a space
print(sum(number))  # combined total is 500500
# My begining number is 1 and I ended up with this number because it is the least value i.e the minimum value.
# My ending number is 1000 because it is the highest value in the loop
print() # indicates a space
# Task 3
print("Task 3")
print() # indicates a space
# A program that prints odd, even and multiples of 3
# A list of odd numbers between 1 and 40
for odd in range(1,40,2):
  print(odd)  #prints odd numbers
print() # indicates a space
# A list of even numbers between 1 and 40
for even in range(2,41,2):
  print(even)  #prints even numbers
# A list of multiples of 3 between 3 and 30
print() # indicates a space
for multiples in range(3,30,3):
  print(multiples)  #prints multiples of 3 betwwen values 3 and 30
print() # indicates a space
# Task 4
print("Taskn 4")
print() # indicates a space
# A program that prints out my age in dog age
dog_age = 7  # dog age value per human year
her_age = 10  # my age
age_in_dog_age = her_age * dog_age # my age in dog age
print("My age in dog age is " + str(age_in_dog_age) + ".")
print() # indicates a space
# Task 5
print("Task 5")
print() # indicates a space
# A program that adds prices of pizza items using fstring and slices
pizza_prices = [8.0,12.0,9.9,1.1,5.0,4.5,3.5,6.4,10.0] #9 prices of pizza items
first_3 = sum(pizza_prices[0:3])#stores the first 3 prices in first_3 variable
print(f"The prices of the first three items in the pizza list is {first_3}")
print() # indicates a space
second_3 = sum(pizza_prices[3:6])  #stores the second 3 prices in second_3 variable
print(f"The prices of the second three items in the pizza list is {second_3}")
print() # indicates a space
last_3 = sum(pizza_prices[6:]) #stores the last 3 prices in last_3 variable
print(f"The prices of the first three items in the pizza list is {last_3}")
# Task 6
print("Task 6")
print() # indicates a space
# A program that prints a list of kfc food I love in a tuple
kfc_foods = ("Chicken", "Fries", "Burger", "Orange juice", "Marinara sauce")
# Using for loop to print the items in kfc_foods
for i in kfc_foods:
  print(i) # prints kfc foods
# replacing two items in kfc_foods
kfc_foods = ("Chicken", "Fries", "Burger", "Salad", "Pasta")
print(kfc_foods) # prints replaced kfc_foods
# lists are mutable that means you can change items in it.
# tuple are immutable that means you can't change items in it.
print() # indicates a space
# Task 7
print("Task 7")
print() # indicates a space
print() # indicates a space
#A dataset of the monthly average value of Bangladesh temperature and rain from 1901 to 2015 copied into python
#Dataset from https://www.kaggle.com/yakinrubaiat/bangladesh-weather-dataset/data

# This program prints out the min, max, standard deviation, the mean and the median for Bangladesh data.
weather = [16.976, 19.9026, 24.3158, 28.1834, 27.8892, 28.8925, 28.3327, 27.9243, 27.6057, 27.0887, 22.1671, 18.5574, 18.5455, 20.1252, 25.5508, 26.5562, 27.3165, 28.266, 27.6247, 28.1001, 27.7271, 26.0153, 21.9907, 18.2532, 17.7023, 19.5474, 24.3562, 28.0898, 28.5913, 27.906, 28.6851, 27.5889, 27.7468, 26.8644, 22.4298, 18.3745, 17.7866, 19.9656, 25.0148, 27.3117, 27.1157, 27.8145, 27.4404, 27.9148, 27.9551, 26.2871, 22.1525, 18.7779, 17, 17.8269, 22.9851, 25.4188, 27.1236, 29.0868, 27.8607, 27.4862, 27.8164, 26.5021, 22.6873, 18.6721, 17.5423, 19.4317, 23.0485, 27.9907, 28.4449, 28.2983, 28.3345, 27.4695, 28.3886, 26.428, 22.7998, 19.2146, 19.0642, 19.7055, 23.1507, 26.1498, 27.6634, 27.8377, 27.8421, 28.1978, 27.8996, 26.7797, 22.7542, 18.6971, 17.2889, 20.212, 25.0639, 29.3307, 28.0869, 28.3117, 27.9535, 28.0517, 28.0101, 26.5604, 22.174, 18.3258, 18.6933, 20.1593, 25.9954, 26.4867, 27.9672, 27.2679, 28.1115, 27.414, 28.3398, 26.8933, 23.6615, 19.1166, 17.7787, 19.9987, 24.3738, 26.912, 27.8941, 27.3892, 27.3739, 27.8772, 28.2254, 26.2802, 22.3027, 18.1829, 19.0692, 19.6118, 23.8229, 26.9944, 27.6235, 27.5065, 28.14, 27.754, 27.7117, 26.023, 22.1109, 17.7475, 18.2763, 20.9062, 24.4209, 26.0439, 27.7741, 28.3068, 27.6907, 27.7733, 27.9862, 26.2671, 22.3421, 18.3319, 18.1365, 20.7171, 23.7257, 27.9796, 27.0109, 26.8354, 28.0541, 27.7176, 27.8885, 26.0772, 21.7421, 18.151, 17.9978, 20.6822, 24.4306, 25.8496, 27.4998, 27.9523, 28.0274, 27.5587, 27.6911, 25.4273, 22.4916, 19.2066, 18.8711, 20.2688, 24.1828, 27.5293, 27.6441, 27.7751, 28.176, 28.1829, 27.7224, 28.1302, 24.4903, 19.089, 17.8694, 20.4223, 25.6592, 27.315, 28.9475, 27.6135, 27.5322, 27.8663, 28.052, 26.6718, 23.0187, 18.2218, 17.4937, 19.8716, 23.8486, 26.9286, 27.1785, 27.4378, 27.777, 27.8983, 27.6864, 26.5464, 22.9189, 18.5966, 17.1998, 20.0129, 24.9119, 26.6262, 27.6326, 26.4861, 28.2649, 27.4965, 28.0696, 26.5865, 22.6765, 18.4667, 18.9095, 19.706, 25.8395, 27.1635, 28.165, 28.0003, 27.7889, 28.3777, 27.3902, 26.4084, 23.1173, 18.9201, 18.7317, 19.8729, 24.0729, 27.0365, 27.7238, 28.6608, 28.4222, 27.8438, 27.968, 26.9096, 23.1647, 19.6288, 19.0034, 20.4179, 25.4407, 27.5527, 28.8115, 27.7312, 28.1502, 27.9259, 28.1141, 25.4904, 22.401, 19.1064, 18.621, 21.033, 25.7471, 28.5568, 28.8271, 27.3527, 27.9223, 27.8164, 27.915, 25.9622, 23.0288, 19.0427, 18.6312, 19.8836, 24.9515, 27.8685, 28.1951, 28.7014, 27.8902, 28.1404, 28.085, 26.1335, 22.9939, 19.4361, 18.4881, 20.5691, 26.6422, 28.7039, 28.2107, 29.0303, 27.8485, 27.8401, 27.397, 27.2626, 22.7645, 19.0319, 16.9382, 19.0482, 24.7465, 27.0765, 27.1711, 27.9974, 27.6439, 28.0744, 27.5406, 25.8388, 22.5173, 18.4914, 18.0436, 20.7124, 23.8361, 26.692, 27.8134, 28.874, 27.8577, 27.9764, 28.0988, 26.6226, 21.9718, 19.622, 18.0251, 19.7421, 23.1684, 27.5302, 27.4235, 28.3215, 28.2326, 27.9566, 27.6875, 26.8392, 22.7253, 19.4851, 18.5036, 21.1361, 25.5137, 27.8824, 27.8043, 27.5143, 27.978, 28.1385, 28.4182, 26.5972, 22.4865, 19.461, 18.3725, 19.683, 25.1633, 27.4018, 28.3855, 28.2485, 27.9211, 27.8708, 27.9973, 26.2202, 22.3896, 18.5883, 17.1308, 20.2585, 24.836, 27.5107, 28.2023, 27.7208, 28.0704, 27.8828, 28.1845, 26.5011, 22.5794, 18.6454, 19.2912, 20.5581, 24.6265, 28.3371, 27.7868, 28.8507, 27.7335, 28.6073, 27.6722, 26.9166, 22.3272, 19.425, 18.7903, 19.2857, 25.3485, 27.8492, 27.9615, 28.2926, 27.9526, 28.0368, 28.1666, 27.2559, 23.2841, 19.3707, 17.267, 20.9302, 25.4578, 26.6786, 27.5726, 27.705, 27.8826, 27.7244, 28.0191, 26.7932, 22.5782, 19.0815, 17.9754, 20.2944, 25.0594, 27.9356, 28.2405, 27.5306, 28.1013, 28.0593, 28.4278, 26.2628, 22.1819, 19.0272, 17.6546, 20.6904, 25.3797, 27.3559, 29.3369, 28.5321, 28.4028, 27.5299, 28.0197, 26.8749, 23.2079, 19.0876, 17.6556, 19.9519, 25.6072, 28.1323, 27.7471, 27.1586, 27.9088, 28.2978, 27.8549, 26.127, 23.7141, 19.6911, 17.1468, 20.2496, 24.3094, 28.0696, 27.8123, 28.2435, 28.5889, 27.9099, 28.2349, 26.6222, 22.6849, 19.1976, 19.2664, 19.4212, 26.1933, 29.1067, 27.2286, 27.6996, 27.7973, 28.1085, 28.5279, 27.2116, 21.8681, 18.9308, 18.9613, 21.0936, 24.8663, 28.8783, 28.411, 28.1074, 27.7214, 27.9175, 27.7891, 26.6052, 22.8798, 19.4199, 17.8246, 20.392, 23.1225, 27.9876, 27.9565, 28.3484, 27.8575, 28.2643, 27.9643, 27.0944, 23.9458, 19.7315, 18.4257, 20.9764, 26.2475, 28.4779, 28.3179, 27.7471, 28.1991, 28.3456, 28.1701, 26.4394, 22.4904, 20.364, 18.5173, 20.887, 25.4426, 27.5847, 28.9374, 28.9074, 28.4444, 27.8112, 27.5892, 27.0809, 23.8591, 19.2302, 19.4068, 19.539, 24.4346, 26.0894, 28.1733, 27.9244, 27.8151, 27.7138, 28.1217, 27.0109, 23.7047, 20.2734, 18.4048, 20.1012, 25.0431, 26.5521, 29.1642, 28.895, 28.2518, 28.3515, 27.9998, 26.8679, 22.9212, 20.3914, 18.2015, 19.3508, 25.7198, 27.5778, 27.8711, 28.6697, 28.3827, 28.2371, 28.5058, 26.2761, 22.875, 18.7336, 18.7904, 22.2759, 25.2807, 26.1737, 27.7316, 27.8769, 27.7379, 28.3153, 28.0705, 26.1231, 23.7298, 20.0773, 18.4592, 20.8343, 25.3178, 28.6075, 28.4113, 28.5211, 28.12, 28.0557, 28.0439, 26.1121, 23.1268, 20.073, 18.8595, 20.5453, 24.3332, 27.3178, 27.2727, 28.3304, 27.6623, 27.9189, 28.1084, 26.2712, 23.4262, 18.6645, 18.691, 20.196, 24.974, 25.4455, 26.6293, 27.9464, 27.7579, 27.877, 27.8519, 27.2007, 22.2315, 17.6854, 18.5486, 20.1997, 24.4553, 27.7109, 28.4808, 27.8493, 27.7724, 27.3795, 28.1418, 26.6353, 22.3076, 19.193, 17.7884, 20.5543, 24.8184, 27.2714, 28.2118, 28.0756, 27.7922, 28.3824, 28.1077, 27.2955, 23.2622, 20.3254, 18.9548, 21.9137, 24.0828, 27.0739, 27.5969, 28.4238, 27.7268, 28.033, 27.7437, 26.9695, 23.0584, 19.0419, 17.715, 21.4254, 26.0308, 28.252, 28.0526, 27.7573, 27.7162, 28.1521, 27.7436, 26.4653, 22.6183, 20.5814, 17.2898, 22.1992, 25.2363, 29.126, 28.893, 27.2109, 27.8235, 28.0071, 28.1271, 25.7316, 21.666, 19.3207, 17.988, 20.2242, 25.517, 27.234, 28.6394, 28.1113, 27.3639, 27.6166, 27.976, 27.0494, 23.0927, 18.576, 18.2806, 19.802, 25.3792, 27.949, 28.0995, 27.1197, 27.6612, 27.9301, 27.6135, 26.8891, 22.9846, 19.3905, 18.6476, 19.5143, 24.0236, 28.3691, 29.2739, 28.4367, 28.0674, 28.4941, 28.1995, 26.4778, 22.6556, 19.6706, 19.7673, 20.7237, 25.5715, 28.5818, 28.8361, 29.4177, 28.4789, 27.9477, 28.3228, 27.4873, 23.6633, 20.1148, 18.5213, 19.8572, 24.6577, 28.165, 28.2968, 28.168, 28.0668, 27.9072, 27.3399, 26.1549, 22.3988, 19.419, 18.0893, 22.1152, 23.957, 29.2185, 29.2217, 28.6191, 27.5236, 28.4533, 27.8695, 26.882, 22.4092, 19.7958, 19.0652, 19.0658, 26.0556, 28.555, 28.4711, 27.9452, 28.0834, 28.2561, 27.8613, 26.8185, 22.0269, 17.5351, 17.0844, 20.6306, 25.1073, 28.0974, 27.9313, 27.9382, 28.6468, 27.8838, 28.3854, 26.4392, 22.4533, 19.1662, 17.7822, 21.9651, 24.9482, 26.9333, 27.1739, 27.9536, 28.0948, 28.296, 28.4266, 26.5765, 22.9553, 19.7094, 17.9709, 21.1238, 26.2558, 27.2635, 27.8866, 28.2793, 27.3133, 28.2281, 28.1808, 27.1473, 23.5157, 19.7899, 18.6764, 20.4685, 23.8589, 27.4561, 28.676, 28.0528, 27.5588, 27.1909, 27.7401, 26.5774, 23.1994, 19.7873, 18.4824, 22.1565, 25.1246, 28.5128, 29.1766, 27.728, 28.2117, 27.9247, 27.6962, 25.7202, 23.7204, 19.1252, 18.6105, 21.2856, 23.8405, 26.5681, 28.1967, 28.1625, 28.075, 27.9847, 27.4322, 26.1048, 21.6477, 19.6023, 17.9779, 19.643, 24.9615, 27.1675, 28.0834, 26.9702, 27.7856, 28.0264, 28.4405, 26.4382, 23.1298, 19.5489, 17.8455, 21.0472, 25.8095, 27.8697, 28.6643, 28.1842, 28.131, 27.3112, 28.0775, 26.4501, 23.2061, 19.5562, 17.8687, 20.8429, 25.1381, 28.1814, 28.8184, 28.1102, 27.7758, 28.0489, 27.7837, 26.3453, 22.8516, 19.17, 18.1881, 19.7759, 24.4476, 26.2185, 27.4486, 27.438, 27.1886, 26.9405, 27.8165, 26.6511, 22.2256, 19.3208, 18.7213, 18.6849, 25.0857, 27.1956, 29.0864, 28.2846, 28.3326, 27.4792, 28.1104, 26.6273, 23.1532, 19.4455, 18.8691, 21.9105, 24.1362, 28.5821, 27.042, 27.8315, 28.2071, 27.9847, 27.6703, 26.7585, 22.9698, 19.0137, 17.631, 20.1513, 24.6152, 27.2181, 27.6897, 27.8498, 27.0471, 27.9089, 27.4488, 27.6097, 24.1236, 18.2645, 18.0454, 20.7283, 25.4553, 28.2002, 28.0144, 28.3837, 27.1209, 27.9833, 27.5182, 27.4014, 22.4417, 18.307, 18.3264, 21.1868, 25.5237, 27.7962, 27.4224, 27.5163, 27.8497, 27.3903, 27.8908, 26.592, 24.3715, 19.1128, 17.9541, 20.3662, 26.3199, 26.1722, 26.4029, 27.1542, 27.9848, 28.1256, 28.3048, 26.0245, 23.717, 19.1805, 16.8006, 20.2042, 24.0473, 27.0655, 27.3758, 27.4932, 27.9215, 28.6085, 27.6907, 27.517, 24.0292, 19.7649, 19.1725, 20.0549, 24.9246, 28.2364, 29.526, 28.8, 28.2819, 28.2275, 28.0401, 26.9451, 25.1142, 20.0687, 18.2739, 20.6525, 25.0401, 28.7934, 27.1723, 28.2177, 28.1036, 28.1573, 28.396, 26.4103, 23.3395, 20.3604, 18.3163, 20.644, 24.1726, 25.7174, 27.1297, 28.551, 27.6783, 28.462, 27.9154, 27.2273, 23.4404, 19.0389, 18.9885, 20.5124, 23.7499, 26.815, 28.9711, 27.9965, 28.5086, 27.9058, 28.1703, 27.0648, 22.5962, 18.8501, 18.0039, 19.7179, 24.6127, 26.9736, 27.4698, 28.7935, 28.5904, 28.1526, 28.1086, 27.015, 23.8313, 18.8622, 17.7947, 19.9473, 25.536, 28.2474, 27.654, 27.886, 27.7393, 28.1933, 27.4938, 27.5528, 23.0039, 19.6511, 18.8171, 20.6197, 26.2622, 28.3044, 27.6409, 28.2298, 27.3083, 28.3917, 27.8588, 27.0872, 23.0949, 20.4398, 18.8875, 21.0747, 25.6098, 27.0516, 27.6381, 28.897, 27.8074, 28.4925, 27.3405, 26.1029, 23.6914, 20.0478, 18.9032, 21.7238, 24.8017, 27.4476, 28.508, 29.253, 28.0107, 28.1384, 28.2602, 27.3458, 24.2419, 20.36, 19.2634, 21.7809, 25.117, 28.2212, 27.9454, 28.0714, 28.1468, 28.1171, 28.5791, 27.4519, 24.2705, 21.0501, 17.5061, 20.8075, 25.0341, 28.4778, 29.0168, 28.2459, 28.1345, 28.5109, 28.1385, 27.0998, 23.3839, 19.0009, 19.473, 21.1088, 23.7713, 26.5503, 28.0107, 28.5531, 27.9207, 28.5019, 28.2556, 26.2772, 24.5595, 20.1132, 17.4518, 21.7874, 25.9068, 27.3361, 27.5258, 27.6036, 28.1626, 28.0767, 27.4425, 26.5558, 22.5562, 18.5561, 17.4191, 19.3065, 25.1958, 28.3228, 27.3386, 28.3549, 27.6078, 28.0492, 27.7278, 26.5026, 23.0168, 18.2444, 18.1609, 21.0757, 23.4808, 26.4466, 27.0991, 27.6713, 27.8916, 27.867, 27.4283, 26.6738, 23.2391, 19.9446, 18.7418, 19.7401, 25.03, 27.1263, 28.5911, 28.0515, 28.3919, 28.3, 28.3021, 26.7137, 23.1254, 19.0129, 17.7492, 20.8723, 25.2876, 28.5657, 29.2967, 28.8511, 27.984, 28.1941, 27.9357, 27.2994, 23.7156, 19.1235, 18.5789, 20.6901, 26.0952, 27.8947, 28.6148, 28.0299, 28.1341, 27.7894, 28.2475, 26.6539, 23.5364, 19.4872, 17.9503, 19.7434, 25.302, 25.8287, 28.2268, 28.2152, 28.0691, 28.2508, 27.6086, 26.2579, 23.9015, 18.8273, 17.7704, 21.3817, 23.833, 27.4558, 28.848, 29.2008, 28.1453, 28.2394, 28.6324, 28.6631, 24.228, 19.9801, 18.9055, 22.7454, 26.2573, 29.5091, 27.9702, 28.5738, 27.9209, 27.8719, 27.7741, 27.2434, 23.7157, 20.4159, 17.8553, 19.8796, 24.1766, 26.9379, 27.5459, 28.1653, 28.2621, 28.1104, 27.5094, 27.0526, 23.7323, 19.4021, 19.1684, 22.1418, 25.2322, 28.0317, 28.0056, 27.9112, 28.1778, 28.4513, 28.6358, 27.4927, 24.3786, 20.0203, 18.7662, 21.7798, 25.6658, 27.3997, 27.9866, 28.2914, 27.8864, 27.9693, 28.0888, 26.9426, 24.0238, 20.2395, 17.9398, 20.9849, 24.4467, 28.153, 28.1068, 28.1032, 28.2792, 28.8776, 28.7275, 27.7419, 23.9283, 19.2162, 18.2838, 20.9799, 26.7782, 27.3832, 29.1106, 28.3582, 27.6765, 28.5187, 28.2945, 26.3711, 23.2019, 20.5304, 18.7742, 22.0334, 25.8596, 27.9591, 28.0449, 29.1435, 28.2297, 28.597, 28.3883, 26.9262, 23.3981, 20.1779, 19.4921, 23.6292, 26.212, 27.6793, 28.4904, 28.458, 28.6736, 28.6002, 28.5336, 27.4515, 23.9783, 20.7727, 19.093, 20.5513, 25.1484, 28.0036, 28.793, 28.5409, 28.1274, 28.8106, 28.3902, 27.8778, 24.1285, 20.1536, 19.1005, 19.783, 25.6679, 28.4216, 28.5943, 27.8427, 28.0989, 28.1792, 28.5522, 27.0175, 23.7862, 21.0141, 20.3262, 22.7193, 25.9696, 29.1815, 28.5577, 29.1754, 28.8393, 28.5917, 28.964, 27.6979, 24.4304, 20.2116, 18.6795, 21.7631, 27.0261, 29.1543, 28.8466, 28.723, 28.7615, 28.9236, 28.6092, 27.9208, 25.1333, 19.8122, 18.0523, 21.2404, 25.5009, 27.67, 28.2986, 28.5389, 28.2877, 28.0651, 28.4788, 27.474, 23.5306, 20.4366, 16.8493, 20.0185, 25.6603, 26.6947, 28.7705, 28.5034, 28.0643, 28.4723, 27.879, 26.1542, 23.0322, 19.6466, 17.7546, 20.6546, 25.3696, 27.366, 27.2544, 28.894, 28.3869, 27.8884, 28.0005, 26.4168, 22.1847, 18.5529, 17.1088, 19.2051, 24.4777, 28.5882, 28.7169, 28.2088, 28.5261, 27.9512, 27.9355, 26.6371, 22.6934, 18.3739, 17.8343, 20.3632, 24.6581, 26.3966, 28.3603, 28.2169, 27.8557, 28.0642, 28.123, 26.8624, 23.1842, 18.7124]
print(min(weather)) # prints the minimum value of the data
print() # indicates a space
print(max(weather))# prints the maximum value of the data
print() # indicates a space
print(statistics.stdev(weather))  # prints the standard devaition of the data
print() # indicates a space
print(statistics.mean(weather))  # prints the mean of the data
print() # indicates a space
print(statistics.median(weather))  #prints the median of the data






