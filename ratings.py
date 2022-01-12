"""Restaurant rating lister."""


def reading_scores():
    restaurant_ratings = open("scores.txt")
    scores = {}

    for line in restaurant_ratings:
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)

    return scores


def adding_new_restaurant_rating(scores):
    print('Hello and welcome to the restaurant rating tool')
    print('Please give type the name of the restaurant')
    restaurant = input('(type restaurant name)')

    print('Please give this restaurant a rating')
    rating = input('type restaurant rating')

    scores[restaurant] = rating


def printed_scores(scores):
    for restaurant, rating in sorted(scores.items()):
        print(f'{restaurant} has a rating of {rating}')


scores = reading_scores()
adding_new_restaurant_rating(scores)
printed_scores(scores)
