def favouriteRestaurant(restaurant_1, restaurant_2):
        scoreAndShared = {}
        for i in range(len(restaurant_1)):
                scoreAndShared[restaurant_1[i]] = [i+1, False]

        min_score = 999999
        option = ""
        for i in range(len(restaurant_2)):
                if restaurant_2[i] in scoreAndShared:
                        score = scoreAndShared[restaurant_2[i]][0] + (i+1)
                        if score < min_score:
                                min_score = score
                                option = restaurant_2[i]

        if option == "":
                return "Yelpwich" #yum
        else:
                return option

r1 = ["Burgers", "Pizza", "Tacos"]
r2 = ["Pizza","Candy"]

assert favouriteRestaurant(r1, r2) == "Pizza"

r3 = ["Spaghetti"]
r4 = ["Icecream"]

assert favouriteRestaurant(r3, r4) == "Yelpwich"
