print("Welcome to the Savings Calculator.")
# Welcome screen
# How much do you make in a week input
earningsinput = input("How many dollars do you make in a week on average?\n")
earnings = int(earningsinput)
# How much you are trying to save (percent) input
percentsavingsinput = input(
    "What percentage are you able to save every week?\n---Write this in decimal form.---\n")
percentsavings = float(percentsavingsinput)
# savings goal input
goal_input = input("What is your savings goal (in dollars)?\n")
goal = int(goal_input)
# formula to calulate
weekly_savings = earnings * percentsavings
# count represents how many weeks it will take to achieve goal
count = 0
# earnings times percent times x = goal,
# x is number of weeks to reach goal
# while loop to count number of weeks to reach goal
while goal > 0:
    goal = goal - weekly_savings

    count += + 1
    # answer is how long it will take to save and how much you need to save
print("By saving", weekly_savings, "dollars per week,")
print("It would take", count, "weeks to complete your savings goal!")
