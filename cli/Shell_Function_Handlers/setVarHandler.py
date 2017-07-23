###########################################################
#   File Details
###########################################################
#   Provides additional support to the shell for the setting
#   variable.
#   Created by Kyle Erwin - 20/07/2017
from MatrixTree.Matrix import Matrix
from printColors import *


class SetVarHandler():
    args = []
    def __init__(self, _args):
        _args = _args.split()
        self.args = _args

    ###########################################################
    #   Validation Methods
    ###########################################################
    def validateArguments(self, errorMessage):
        valid = True

        if len(self.args) == 0:
            return False

        if len(self.args) > 1:
            valid = False

        if not str(self.args[0]).isalpha():
            valid = False

        if errorMessage and not valid:
            print(PrintColors.FAIL + "Invalid input." + PrintColors.ENDC)
            print("Correct Format as follows...")
            print(PrintColors.OKBLUE + "set [name]" + PrintColors.ENDC)

        return valid

    ###########################################################
    #   Get Methods
    ###########################################################
    def getName(self):
        return self.args[0]

    ###########################################################
    #   Input Values
    ###########################################################
    def inputValues(self, dimensions):
        tree = Matrix()
        tree.build(dimensions)
        points = tree.getPoints()

        values = []

        for point in points:
            value = "AAAA"
            while str(value).isalpha():
                value =  input("Enter value for point " + str(point) + ": ")

                if str(value).isalpha():
                    print(PrintColors.FAIL + "ERROR: Please enter numerical value" + PrintColors.ENDC)

            values.append(value)

        tree.detlete()
        return values

