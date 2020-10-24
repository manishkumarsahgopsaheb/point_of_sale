import string
import random

if __name__ == '__main__':
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)

    psw_len = int(input('Enter Password Length: '))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # there is a differnece between append and extend i.e. suppose i have two list, list a and list b
    # a = [1,2,3]
    # b = [5,6,7]
    # if i write
    # a.append(b)
    # and print(a)
    # then output is like =>   a = [1,2,3,[5,6,7]]
    # here in list a list b is append as a list
    # but i will use extend instead of append
    # means if
    # a = [1, 2, 3]
    # b = [5, 6, 7]
    # a.extend(b)
    # print(a)
    # then output is => a = [1,2,3,5,6,7]
    # so extend will insert the list b into into list a not as a list b but the element of b will insert in list a
    random.shuffle(s)
    print("your password is: ", end="")
    print("".join(s[0:psw_len]))

    # print("".join(random.sample(s,psw_len)))   # isko bhi use kr skte the suffle k jagah

    # print(s)
