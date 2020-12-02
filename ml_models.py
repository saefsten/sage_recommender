"""Module for ML Algorithms"""

# TO-DO: Get movies from file or from database

from faker import Faker

def one_and_only_recommender():
    """This is the best recommendation function. There are no others.
        You don't even need a single parameter. It just works. True story."""

    worst_movies_2010ies = ["Birdemic: Shock and Terror", "The Last Airbender","Bucky Larson: Born to Be a Star"]

    return worst_movies_2010ies

def simple_recommender(num = 100):
    fake = Faker()
    fake_names = [fake.name() for i in range(num)]

    conflict = "I love conflicts and 100 is more than 10."

    return fake_names


def nmf_recommender():
    """Write your own code for NMF Here"""
    pass


def cosim_recommender():
    pass


if __name__ == "__main__":
    print(one_and_only_recommender())