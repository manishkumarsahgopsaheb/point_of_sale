# The polls are stored in a list in the received order. Then two lists are created,
# which store the candidate names and the number of votes of the corresponding candidate.
# The program can determine the number of candidates from the list of polls. Finally,
# the candidates with the highest vote are displayed. The program can show two or more
# candidates when they all have the same highest votes.

poll = []
Aadhar = []
print('\n\n***********welcome to Bihar Legislative Assembly Election*************\n\n')
print('\t\t\t\t\t\t\t\tINSTRUCTIONS:\n\n'
      '\t\tif voting have been completed then type any Aadhar Number which is\n'
      '\t\talready been submitted after doing this you will get the option to \n'
      '\t\tshow the Result\n\n')

print('\t\t\t\t\t\t\t--------vote here---------\n\n')


def election():
    while 1:
        aadhar_num = input('\t\tEnter your Aadhar: ')
        if aadhar_num not in Aadhar:
            Aadhar.append(aadhar_num)
            leader_name = input('\t\tYou are voting for: ')
            print('\t\tvoted successfully\n\n')
            poll.append(leader_name)

        else:
            print('**System says: you are not allowed to vote again**')
            again = input('\t\tnow its turn of next voter:type ok to continue \n'
                          '\t\tif voting is done then type result to show the result\n\n')
            if again == 'ok':
                election()
            elif again == 'result':
                break


election()

candidate_list = []
vote_list = []

for candidate in poll:
    if candidate not in candidate_list:
        candidate_list.append(candidate)
        # storing vote corresponding to the same index of candidate_name in candidates_list
        vote_list.append(1)
    else:
        candidate_index = candidate_list.index(candidate)
        vote_list[candidate_index] += 1


#  as in this program we can have multiple winners with the same vote
max_vote = 0
max_candidate = []

for i in range(len(vote_list)):
    if vote_list[i] > max_vote:
        max_vote = vote_list[i]
        candidate = candidate_list[i]
        # if next time it updated again we can not have more than one candidate in this
        # case so i will make empty max_candidate all the time
        max_candidate = []
        max_candidate.append(candidate)
    elif vote_list[i] == max_vote:
        candidate = candidate_list[i]
        max_candidate.append(candidate)

print('\n\n\t\tThe highest vote goes to:\n')
print('\t\t', *max_candidate, sep='\n')

if len(max_candidate) > 1:
    print(f'Each person has {max_vote} votes')
else:
    print(f'{max_candidate[0]} has {max_vote} vote')
