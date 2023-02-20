# This program demonstrates polymorphism.

import f_animals as animals

def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()


    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    show_mammal_info(mammal)

    print()

    show_mammal_info(dog)

    print()

    show_mammal_info(cat)

def show_mammal_info(m):
        if isinstance(m, animals.Mammal):
            m.show_species()
            m.make_sound()
        else:
             print(f"{m} is not part of the mammal class.")

# Call the main function.
main()
