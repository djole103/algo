#'date' : 'year-month-day' , 'sender' : int, 'receiver' : int

def insert(lst, args):
        d = {'date': args[0], 'sender' : args[1], 'receiver' : args[2]}
        lst.append(d)

TEST_VALS = [
('2015-01-01', 1, 2),
('2015-01-01', 3, 4),
('2015-03-05', 1, 4),
('2016-01-01', 4, 2)]
        
l = []
for val in TEST_VALS:
        insert(l, val)

newL = [ d for d in l if d['sender'] == 1]
newL = filter(lambda x: x['sender'] == 1, l)
print(newL)
