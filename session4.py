import random
class Qualean:
    '''
        Write a Qualean class that is inspired by Boolean+Quantum concepts.
        We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1)
        but it internally picks an imaginary state. The moment you assign it a real number,
        it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with
        it and stores that number internally after using Bankers rounding to 10th decimal place
    '''

    def __init__(self,q):
        if (q !=0 and q !=1 and q !=-1):
            raise ValueError('You can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1)')
        self.q = round(q*random.uniform(-1, 1),10)

    def __and__(self , other):
        if isinstance(other, Qualean):
            if self.__bool__==True and other.__bool__==True:
                    return True
            else:
                return False
        else:
            return  False

    def __or__(self, other):
        if isinstance(other, Qualean):
            return Qualean(int(self) | int(other))
        else:
            return self.__or__(self, other)

    def __repr__(self):
        return 'Qualean={0}'.format(self.q)

    def __str__(self):
        return 'Qualean={0}'.format(self.q)

    def __add__(self, other):
        if isinstance(other, Qualean):
            return float(self.q) + float(other.q)
        else:
            raise NotImplementedError()

    def __eq__(self, other):
        return float(self.q) == float(other.q)

    def __float__(self):
        return float(self.q)

    def __ge__(self, other):
        if isinstance(other, Qualean):
            return float(self.q) >= float(other.q)
        else:
            raise NotImplementedError()

    def __gt__(self, other):
        if isinstance(other, Qualean):
            return float(self.q) > float(other.q)
        else:
            raise NotImplementedError()

    def __invertsign__(self):
        return -1*self.q

    def __le__(self, other):
        if isinstance(other, Qualean):
            return float(self.q) <= float(other.q)
        else:
            raise NotImplementedError()

    def __lt__(self, other):
        if isinstance(other, Qualean):
            return float(self.q) < float(other.q)
        else:
            raise NotImplementedError()

    def __mul__(self, other):
        return float(self.q) * float(other.q)

    def __sqrt__(self):
        if self.q>=0:
            return float(self.q)**0.5
        else:
            return '{0}i' .format(float(-1*self.q)**0.5)

    def __bool__(self):
        if float(self.q) != 0:
            return True
        return False
