import time
start_time = time.time()
from cuckoopy import CuckooFilter
from random import shuffle 
# Initialize a cuckoo filter with 10000 buckets with bucket size 4 and fingerprint size of 1 byte
cf = CuckooFilter(capacity=10000, bucket_size=4, fingerprint_size=1)
word_present = ['abound','abounds','abundance','abundant','accessable', 
                'bloom','blossom','bolster','bonny','bonus','bonuses', 
                'coherent','cohesive','colorful','comely','comfort', 
                'gems','generosity','generous','generously','genial'] 
word_absent = ['bluff','cheater','hate','war','humanity', 
               'racism','hurt','nuke','gloomy','facebook', 
               'geeksforgeeks','twitter'] 
for item in word_present: 
    cf.insert(item) 
shuffle(word_present) 
shuffle(word_absent) 
test_words = word_present[:10] + word_absent 
shuffle(test_words)
for word in test_words: 
    if cf.contains(word): 
        if word in word_absent: 
            print("'{}' is a false positive!".format(word)) 
        else: 
            print("'{}' is probably present!".format(word)) 
    else: 
        print("'{}' is definitely not present!".format(word)) 

print("--- %s seconds ---" % (time.time() - start_time))