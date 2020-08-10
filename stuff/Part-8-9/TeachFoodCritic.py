# TeachFoodCritic.py

def food_critic_perceptron(ice_cream, ketchup, weight_ice_cream, weight_ketchup):
    # Define the perceptron calculation
    x = ice_cream*weight_ice_cream + ketchup*weight_ketchup
    # Apply the threshold,
    if x > 0:
        output = 1
    else:
        output = 0
    return output

# Let's teach it!
import random

w_yum  = 1;               #Our first guess for weights.
w_yuck = 1;
learning_constant = 0.1;

for k in range(1000):
    
    # Get a random combination of inputs
    ice_cream = random.choice([True, False])
    ketchup   = random.choice([True, False])

    desired_output = [???]
    perceptron_output = [???]
    error = [???]
    
    w_yum  = w_yum  + error*ice_cream*learning_constant
    w_yuck = w_yuck + error*ketchup*learning_constant

print(w_yum, w_yuck)

# Let's check it?
print('Check it')
ice_cream,ketchup = 1,0
print('ice_cream =', ice_cream, ', ketchup =', ketchup, ', perceptron =', food_critic_perceptron(ice_cream, ketchup, w_yum, w_yuck))
ice_cream,ketchup = 0,1
print('ice_cream =', ice_cream, ', ketchup =', ketchup, ', perceptron =', food_critic_perceptron(ice_cream, ketchup, w_yum, w_yuck))
ice_cream,ketchup = 1,1
print('ice_cream =', ice_cream, ', ketchup =', ketchup, ', perceptron =', food_critic_perceptron(ice_cream, ketchup, w_yum, w_yuck))
ice_cream,ketchup = 0,0
print('ice_cream =', ice_cream, ', ketchup =', ketchup, ', perceptron =', food_critic_perceptron(ice_cream, ketchup, w_yum, w_yuck))
