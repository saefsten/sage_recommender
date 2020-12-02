"""Module for ML Algorithms"""

# TO-DO: Get movies from file or from database

from faker import Faker

def one_and_only_recommender():

    worst_movies_2010ies = ["Birdemic: Shock and Terror", "The Last Airbender","Bucky Larson: Born to Be a Star"]
    return worst_movies_2010ies

def simple_recommender(num):
    fake = Faker()
    fake_names = [fake.name() for i in range(num)]
    return fake_names


def nmf_recommender():
    """Write your own code for NMF Here"""
    pass


def cosim_recommender():
    pass


if __name__ == "__main__":
    print(one_and_only_recommender())