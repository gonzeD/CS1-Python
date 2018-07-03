#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import inspect

import CorrZooGame as corr
import zoo


class TestZooGame(unittest.TestCase):
    def check_existences(self):
        try:
            tmp = zoo.Animal("")
        except NameError:
            self.assertTrue(False, _("Does the class `Animal` exist?"))
        try:
            tmp = zoo.Lion("")
        except NameError:
            self.assertTrue(False, _("Does the class `Lion` exist?"))
        try:
            tmp = zoo.Owl("")
        except NameError:
            self.assertTrue(False, _("Does the class `Owl` exist?"))
        try:
            tmp = zoo.Giraffe("", 1.0)
        except NameError:
            self.assertTrue(False, _("Does the class `Giraffe` exist?"))
        animal = zoo.Animal("")
        self.assertTrue(hasattr(animal, "name"), _("Your class `Animal` does not have an attribute `name`."))
        self.assertTrue(hasattr(animal, "diurnal"), _("Your class `Animal` does not have an attribute `diurnal`."))
        self.assertTrue(hasattr(animal, "nb_legs"), _("Your class `Animal` does not have an attribute `nb_legs`."))
        self.assertTrue(hasattr(animal, "asleep"), _("Your class `Animal` does not have an attribute `asleep`."))
        try:
            my_zoo = zoo.Zoo()
            self.assertTrue(hasattr(my_zoo, "animals"), _("Your class `Zoo` does not have an attribute `animals`."))
            self.assertTrue(hasattr(my_zoo, "add_animal"), _("Your class `Zoo` does not have a method named `add_animal`."))
            self.assertTrue(hasattr(zoo, "create_my_zoo"), _("Does the class `create_my_zoo()` exists?"))
        except NameError:
            self.assertTrue(False, _("Does the class `Zoo` exist?"))

    def test_Animal_constructor(self):
        self.check_existences()
        name = "Pablo"
        animal = zoo.Animal(name)
        self.assertEqual(name, animal.name, _("The name passed to the constructor of `Animal` does not get stored in the attribute `name`."))
        self.assertEqual(None, animal.diurnal, _("The attribute `diurnal` of `Animal` is not set to `None` by default."))
        self.assertEqual(None, animal.nb_legs, _("The attribute `nb_legs` of `Animal` is not set to `None` by default."))
        self.assertFalse(animal.asleep, _("The attribute `asleep` of `Animal` is not set to `False` by default."))

    def test_Animal_name(self):
        names = ["John", "Jack", "William", "Averell", ""]
        for name in names:
            animal = zoo.Animal(name)
            self.assertEqual(name, animal.name, _("The name passed to the constructor of `Animal` is not stored in the attribute `name`."))

    def test_Animal_sleep(self):
        animal = zoo.Animal("Luke")
        animal.sleep()
        self.assertTrue(animal.asleep, _("Calling ``sleep()`` on your animals doesn't set their attribute ``asleep`` to ``True``"))
        animal.wake_up()
        self.assertFalse(animal.asleep, _("Calling ``wake_up()`` on your animals doesn't set their attribute ``asleep`` to ``False``"))

        self.assertRaises(RuntimeError, animal.wake_up)
        animal.sleep()
        self.assertRaises(RuntimeError, animal.sleep)

    def test_Lion(self):
        self.check_existences()
        names = ["John", "Jack", "William", "Averell", ""]
        for name in names:
            lion = zoo.Lion(name)
            self.assertTrue(isinstance(lion, zoo.Animal), _("Your class `Lion` is not a subclass of `Animal`."))
            self.assertEqual(name, lion.name, _("The name passed to the constructor of `Lion` does not get stored in the attribute `name`."))
            self.assertEqual(4, lion.nb_legs, _("Lions have 4 legs."))
            self.assertTrue(lion.diurnal, _("Lions are active during day time"))
            self.assertFalse(lion.asleep, _("`Lion` should be awake after its creation."))
            self.assertTrue(hasattr(lion, "roar"), _("Did you make a `roar()` method in your class `Lion`?"))

    def test_Owl(self):
        self.check_existences()
        names = ["John", "Jack", "William", "Averell", ""]
        for name in names:
            owl = zoo.Owl(name)
            self.assertTrue(isinstance(owl, zoo.Animal), _("Your class `Owl` is not a subclass of `Animal`."))
            self.assertEqual(name, owl.name, _("The name passed to the constructor of `Owl` does not get stored in the attribute `name`."))
            self.assertEqual(2, owl.nb_legs, _("Owls have 2 legs."))
            self.assertFalse(owl.diurnal, _("Owls are inactive during day time"))
            self.assertFalse(owl.asleep, _("`Owl` should be awake after its creation."))
            self.assertTrue(hasattr(owl, "fly"), _("Did you put a `fly()` method in your class `Owl`?"))

    def test_Giraffe(self):
        self.check_existences()
        names = ["John", "Jack", "William", "Averell", ""]
        neck_lengths_valid = [1, 1.5, 2]
        neck_lengths_invalid = [-8, "slt", zoo.Lion("Alex")]
        for i in range(len(names)):
            giraffe = zoo.Giraffe(names[i], neck_lengths_valid[i%len(neck_lengths_valid)])
            self.assertTrue(isinstance(giraffe, zoo.Animal), _("Your class `Giraffe` is not a subclass of `Animal`."))
            self.assertEqual(names[i], giraffe.name, _("The name passed to the constructor of `Giraffe` does not get stored in the attribute `name`."))
            self.assertEqual(4, giraffe.nb_legs, _("Giraffes have 4 legs."))
            self.assertTrue(giraffe.diurnal, _("Giraffes are active during day time"))
            self.assertFalse(giraffe.asleep, _("`Giraffe` should be awake after its creation."))
            self.assertTrue(hasattr(giraffe, "neck_length"), _("Did you add a `neck_length` attribute to your class `Giraffe`?"))
        for i in range(len(neck_lengths_invalid)):
            self.assertRaises(ValueError, zoo.Giraffe, names[i%len(names)], neck_lengths_invalid[i])

    def test_Zoo(self):
        self.check_existences()
        my_zoo = zoo.Zoo()
        animal = zoo.Animal("Olga")
        my_zoo.add_animal(animal)
        lion = zoo.Lion("Alex")
        my_zoo.add_animal(lion)
        owl = zoo.Owl("Hedwige")
        my_zoo.add_animal(owl)
        giraffe = zoo.Giraffe("Melman", 2)
        my_zoo.add_animal(giraffe)
        self.assertIn(animal, my_zoo.animals, _("Calling `add_animal(animal)` did not add an animal in the list `animals`."))
        self.assertIn(lion, my_zoo.animals, _("Calling `add_animal(lion)` did not add a lion in the list `animals`."))
        self.assertIn(owl, my_zoo.animals, _("Calling `add_animal(owl)` did not add an owl in the list `animals`."))
        self.assertIn(giraffe, my_zoo.animals, _("Calling `add_animal(giraffe)` did not add a giraffe in the list `animals`."))

    def test_student_zoo(self):
        self.check_existences()
        student_zoo = zoo.create_my_zoo()
        self.assertEqual(4, len(student_zoo.animals), _("Your zoo is missing animals (you need 1 lion, 1 owl and 2 giraffes)."))


if __name__ == '__main__':
    unittest.main()
