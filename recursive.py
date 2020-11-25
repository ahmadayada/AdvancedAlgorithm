from time import time
import profile

'''
    Longest Common Subsequence Problem (LCS) 
    Recursive Algorithm name lcs_recursive
    counter Algorithm count how many time function or method have called 
'''


def counter_call(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)

    helper.calls = 0
    helper.__name__ = func.__name__
    return helper


def memorising(func):
    mem = {}

    def memorise(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in mem:
            mem[key] = func(*args, **kwargs)
        return mem[key]

    return memorise


@counter_call
@memorising
def lcs_recursive(string1, string2):
    # get the length for each string
    m = len(string1)
    n = len(string2)
    # if length of both arrays are zero
    if m == 0 and n == 0:
        return 0
    # if length of the first array is zero
    if m == 0:
        return n
    # if length of the second array is zero
    if n == 0:
        return m

    if string1[m - 1] == string2[n - 1]:
        return lcs_recursive(string1[:-1], string2[:-1])

    return 1 + min(lcs_recursive(string1, string2[:-1]),  # Insert
                   lcs_recursive(string1[:-1], string2),  # Remove
                   lcs_recursive(string1[:-1], string2[:-1])  # Replace
                   )


'''_________________________________________________________________________________________________________________'''
'''
                                    *** TESTING PART ***
    Here we can un comment the line to se the result in  command prompt terminal (or command line in windows)
    the last to line in this page code show you all the calling has been called in this document
    PLEASE UNCOMMENT THE NECESSARY LINES BELLOW THE SEE THE RESULTS OR RUN THE GUI VERSION
    THANK YOY
'''

# AAM63747 cl 6
# string1 = # "MASSSAL"

# "ALRRLLLDPFTPTRSLSQMLNFMDQVSEIPLVSATRGMGASGVRRGWNVKEKDDALHLRIDMPGLSREDVKLALEQNTLV" \
# "IRGEGETEEGEDVSGDGRRFTSRIELPEKVYKTDEIKAEMKNGVLKVVIPKIKEDERNNIRHINVD"

# AAM67165_cl_2
# string2 ="ATTACGAT" # "MSAVA"

# "INHFFGLPETVEEERTLVIKSNGKRKRDDDESEEGSKYIRLERRLAQNLVKKFRLPEDADMASVTAKYQEGILTVVIKKLPPQPPKPKTVQIAVS"

# starting_time = time()
# print('minimum operations:', lcs_recursive(string1, string2))
# ending_time = time()
# print('run time          : %3f seconds'%(ending_time-starting_time))

# test with show how many time
# profile.run('print(lcs_recursive("AGGACAT","ATTACGAT")); print()')
# print("The function was called " + str(lcs_recursive.calls) + " times!")
