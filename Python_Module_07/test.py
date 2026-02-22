# class Meta(type):

#     def __new__(cls, name, bases, namespace):
#         print("class created")
#         print(namespace)
#         return super().__new__(cls, name, bases, namespace)

# class BB():
#     def __new__(cls):
#         print("class created from BB")

# class B(BB):
#     g = 30

# class A(metaclass=Meta):
#     x = 5
#     y = 10

# import time

# class LoadTimeMeta(type):
#     base_time = time.perf_counter()

#     def __new__(mcs, name, bases, namespace):
#         namespace['__class_load_time__'] = time.perf_counter() - LoadTimeMeta.base_time
#         print(mcs, name, bases, namespace)
#         return super().__new__(mcs, name, bases, namespace)


# class  A(metaclass=LoadTimeMeta):
#     pass


# class B(A):
#     pass

# print(A.__class_load_time__)
# print(B.__class_load_time__)
# def main():
#     a = A()
#     print(f'{type(a)=}')
#     print(f'{type(A)=}')

# main()

from abc import ABC, abstractmethod

class A(ABC):
    # @abstractmethod
    # def run(self):
    #     pass
    
    @property
    def value(self):
        return 20

class H(A):
    pass



print(H().value)#
#  print(A.__abstractmethods__)