"""Module for ML Algorithms"""

# TO-DO: Get movies from file or from database

from faker import Faker


def simple_recommender(num = 10):
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
    print(simple_recommender(5))