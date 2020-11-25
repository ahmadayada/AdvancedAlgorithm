import profile
from time import time
from recursive import counter_call, memorising


@counter_call
@memorising
def dynamic_edit_distance(string1, string2):
    dynamic_programming_array = [[0 for x in range(len(string2) + 1)] for x in range(len(string1) + 1)]
    for a in range(len(string1) + 1):
        for b in range(len(string2) + 1):

            # if length of the string1 is zero
            # minimum operation is length of string2
            if a == 0:
                dynamic_programming_array[a][b] = b
            # if length of the second array is zero
            # minimum operation is length of string1
            elif b == 0:
                dynamic_programming_array[a][b] = a

            elif string1[a - 1] == string2[b - 1]:
                dynamic_programming_array[a][b] = dynamic_programming_array[a - 1][b - 1]

            else:
                dynamic_programming_array[a][b] = 1 + min(dynamic_programming_array[a][b - 1],
                                                          dynamic_programming_array[a - 1][b],
                                                          dynamic_programming_array[a - 1][b - 1])
    return dynamic_programming_array[len(string1)][len(string2)]


'''_________________________________________________________________________________________________________________'''
'''
                            **  TESTING PART **
    Here we can un comment the line to se the result in  command prompt terminal (or command line in windows)
    the last to line in this page code show you all the calling has been called in this document
    ! PLEASE UNCOMMENT THE NECESSARY LINES BELLOW THE SEE THE RESULTS OR RUN THE GUI VERSION
    THANK YOY
'''
'''_________________________________________________________________________________________________________________'''

# AAM63747 cl 6
# string1 = "MASSSALALRRLLLDPFTPTRSLSQMLNFMDQVSEIPLVSATRGMGASGVRRGWNVKEKDDALHLRIDMPGLSREDVKLALEQNTLV" \
#          "IRGEGETEEGEDVSGDGRRFTSRIELPEKVYKTDEIKAEMKNGVLKVVIPKIKEDERNNIRHINVD"
# AAM67165_cl_2

# string2 = "MSAVAINHFFGLPETVEEERTLVIKSNGKRKRDDDESEEGSKYIRLERRLAQNLVKKFRLPEDADMASVTAKYQEGILTVVIKKLPPQPPKPKTVQIAVS"
# starting_time = time()
# print('minimum operations:', dynamic_edit_distance(string1, string2))
# ending_time = time()
# print('run time          : %3f seconds' % (ending_time - starting_time))

# test with show how many time
# profile.run('print(dynamic_edit_distance(string1,string2)); print()')
# print("The function was called " + str(dynamic_edit_distance.calls) + " times!")
