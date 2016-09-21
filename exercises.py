import struct
import random
from os import urandom

################################################################################
# START: Do not modify code in this section
################################################################################
COLOURS = {
    "BRN": "Brown",
    "BLK": "Black",
    "BLD": "Blonde",
    "WHT": "White",
    "RED": "Red"
}

dog_names = ["Snowy", "Duke", "Mojo", "Blacky", "Zorro", "Blue", "Spot"]


def get_random_dog_name():
    """Generate a random string of characters and just pretend they are a dog's name."""
    magic_number = random.randint(3, 8)
    if magic_number % 3:
        return random.choice(dog_names)

    word ='abcdefghijklmnopqrstuvwxyz'
    suffixes = ["o", "ey", ""]
    chars = []
    for li in range(magic_number):
        val = struct.unpack('=i', urandom(4))[0] % len(word)
        chars.append(word[val:val+1])
    return ''.join(chars).capitalize() + random.choice(suffixes)


class Dog(object):
     
    def __init__(self, name, colour_id):
        self.name = name
        self.colour_id = colour_id


dogs = [
     Dog("Snowy", "BLK"),
     Dog("Blacky", "WHT"),
     Dog("Blue", "RED"),
     Dog("Spot", "BLD"),
     Dog("Zorro", "WHT"),
     Dog("Duke", "BLK"),
     Dog("Mojo", "BLK"),
]

################################################################################
# End: Do not modify code in the above section
################################################################################


class Dogs(object):

    def __init__(self, dogs):
        self.dogs = dogs

    # Add code for Question 5 here
    # (Provide an iterator interface for the Dogs class)
    def __iter__(self):
    	for d in self.dogs:
    		yield d

    def new_name(self):
        """Define a simple generator of dog names that are not in this collection"""
        # Add code for Question #6 here
        existing_names = [d.name for d in dogs]
        new_name = get_random_dog_name()
        if new_name not in existing_names:
        	yield new_name

    def search(self, colour_id):
        """Return a generator expression of all dogs with supplied colour"""
        # Add code for Question #7 here
        for d in dogs:
        	if d.colour_id == colour_id:
        		yield d


def question_1(dogs):
    """Get all the unique colour names from the dogs list"""
    # Add your code here
    return set([d.colour_id for d in dogs])


def question_2(dogs):
    """Get all the black dogs"""
    # Add your code here
    return [d for d in dogs if d.colour_id == "BLK"]


def question_3(dogs):
    """Build a map between dog colour id to dog name set"""
    # Add your code here
    colours = COLOURS.keys()
    ans = dict(zip(colours, [set() for i in range(len(colours))]))
    for d in dogs:
        ans[d.colour_id].add(d.name)
    return ans

def question_4():
    """Modify the Dog class to simplify getting the colour **name**"""
    # Define your new Dog class here
    class Dog(object):
     
        def __init__(self, name, colour_id):
            self.name = name
            self.colour_id = colour_id
            self.colour_name = COLOURS[colour_id]


def main():
    black_dogs = {dogs[0], dogs[5], dogs[6]}

    # Run question 1
    question_1_result = question_1(dogs)
    assert set(question_1_result) == {"WHT", "RED", "BLD", "BLK"}, "Question 1 Failed!"

    # Run question 2
    question_2_result = question_2(dogs)
    assert set(question_2_result) == black_dogs, "Question 2 Failed!"

    # Run question 3
    question_3_result = question_3(dogs)
    assert question_3_result == {
        "BLK": {"Snowy", "Duke", "Mojo"},
        "WHT": {"Blacky", "Zorro"},
        "RED": {"Blue"},
        "BLD": {"Spot"},
        "BRN": set()
    }, "Question 3 Failed!"

    dog_collection = Dogs(dogs)

    # Run question 5
    assert list(dog_collection) == dogs, "Question 5 Failed"

    # Run question 6
    names = ["Snowy", "Duke", "Mojo", "Blacky", "Zorro", "Blue", "Spot"]
    i = 0
    for name in dog_collection.new_name():
        assert (name is not None and
                len(name) >= 3 and
                name not in names), "Question 6 Failed! %s"
        i += 1
        if i == 1000:
            break

    # Run question 7
    question_7_result = dog_collection.search("BLK")
    assert (hasattr(question_7_result, '__iter__') and not
            hasattr(question_7_result, '__len__')), "Question 7 Failed!"
    assert set(question_7_result) == black_dogs, "Question 7 Failed!"


if __name__=='__main__':
    main()
