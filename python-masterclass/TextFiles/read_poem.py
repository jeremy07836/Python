# jabber = open('Jabberwocky.txt', 'r')
#
# for line in jabber:
#     print(line.rstrip())
#     # print(line.strip())
#     # print(line, end='')
#     # print(len(line))
#
# jabber.close()

with open('Jabberwocky.txt', 'r') as jabber:
    for line in jabber:
        print(line.rstrip())
