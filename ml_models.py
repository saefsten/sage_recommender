"""Module for ML Algorithms"""

# TO-DO: Get movies from file or from database

from faker import Faker


def print_i():
    print('i')

def one_and_only_recommender():
    """This is the best recommendation function. There are no others.
        You don't even need a single parameter. It just works. True story."""

    worst_movies_2010ies = ["Birdemic: Shock and Terror", "The Last Airbender","Bucky Larson: Born to Be a Star"]

    return worst_movies_2010ies


def simple_recommender(num = 100):
    '''Returns a list of fake names
    Parameter
    ---------
    num: int
    number of fake names. default value = 10

    Return
    ------
    list of names with length num
    '''
    fake = Faker()
    return [fake.name() for i in range(num)]



def nmf_recommender():
    """Write your own code for NMF Here"""
    pass


def cosim_recommender():
    pass


if __name__ == "__main__":
    print(one_and_only_recommender())