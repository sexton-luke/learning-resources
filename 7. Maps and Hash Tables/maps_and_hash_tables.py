from reference_classes.reference_maps_and_hash_tables import ChainHashMap, ProbeHashMap

# Question 1
print("1. (R-10.9) Draw the 11-entry hash table that results from using the hash function, h(i) = (3i+5) mod 11, "
      "to hash the keys 12, 44, 13, 88, 23, 94, 11, 39, 20, 16, and 5, assuming collisions are handled by chaining.")

# Create initial hash table
hash_table = ChainHashMap()
keys = {12: 1, 44: 2, 13: 3, 88: 4, 23: 5, 94: 6, 11: 7, 39: 8, 20: 9, 16: 10, 5: 11}

# Set items to buckets in hash table
for key, value in keys.items():
    buckets = []
    print('Key:', key)
    bucket = hash_table.hash_function(key)  # perform hash function on all keys creating bucket destination
    buckets.append(bucket)
    for bucket in buckets:  # Set key and values to bucket destination
        hash_table._bucket_setitem(bucket, key, value)
        print('Bucket:', bucket)
        print('Value:', value, '\n')

# Question 2
print("\n2. (R-10.10) What is the result of the previous exercise, assuming collisions are handled by linear probing?")
hash_table = ProbeHashMap()
keys = {12: 1, 44: 2, 13: 3, 88: 4, 23: 5, 94: 6, 11: 7, 39: 8, 20: 9, 16: 10, 5: 11}

for key, value in keys.items():
    buckets = []
    print('Key:', key, '--', 'Value:', value, )
    bucket = hash_table.hash_function(key)  # perform hash function on all keys creating bucket destination
    buckets.append(bucket)
    for bucket in buckets:  # Set key and values to bucket destination
        availability = hash_table._is_available(bucket)
        print('Is bucket', bucket, 'available?', availability)
        while availability == False:
            bucket += 1
            if bucket > 10:
                bucket = 0
                availability = hash_table._is_available(bucket)
            availability = hash_table._is_available(bucket)
            print('Checking bucket..', bucket)
        else:
            hash_table._bucket_setitem(bucket, key, value)
            print('Key is stored in bucket:', bucket, '\n')

# Question 3
print('\n3. (R-10.11) Show the result of Exercise R-10.9, assuming collisions are handled by quadratic probing,'
      'up to the point where the method fails')
hash_table = ProbeHashMap()
keys = {12: 1, 44: 2, 13: 3, 88: 4, 23: 5, 94: 6, 11: 7, 39: 8, 20: 9, 16: 10, 5: 11}

for key, value in keys.items():
    quadratic_factor = 0
    buckets = []
    print('Key:', key, '--', 'Value:', value, )
    bucket = hash_table.quadratic_hash_function(key, quadratic_factor)
    buckets.append(bucket)
    for bucket in buckets:  # Set key and values to bucket destination
        availability = hash_table._is_available(bucket)
        print('Is bucket', bucket, 'available?', availability)
        while not availability:
            quadratic_factor += 1
            print('Try again with quadratic factor:', quadratic_factor)
            bucket = hash_table.quadratic_hash_function(key, quadratic_factor)
            availability = hash_table._is_available(bucket)
            print('Is bucket', bucket, 'available?', availability)

            if quadratic_factor == 10:
                print('Unable to find available bucket to store key... try using larger quadratic factors...')
                break
        else:
            hash_table._bucket_setitem(bucket, key, value)
            print('Key is stored in bucket:', bucket, 'using a quadratic factor of', quadratic_factor, '\n')

# Question 4
print("\n4. (R-10.12) What is the result of Exercise R-10.9 when collisions are handled by double hashing using the "
      "secondary hash function h(k) = 7 − (k mod 7)?")
hash_table = ProbeHashMap()
keys = {12: 1, 44: 2, 13: 3, 88: 4, 23: 5, 94: 6, 11: 7, 39: 8, 20: 9, 16: 10, 5: 11}

for key, value in keys.items():
    multiplier = 0
    buckets = []
    print('Key:', key, '--', 'Value:', value, )
    bucket = hash_table.hash_function(key)
    buckets.append(bucket)
    for bucket in buckets:  # Set key and values to bucket destination
        availability = hash_table._is_available(bucket)
        print('Is bucket', bucket, 'available?', availability)
        while not availability:
            multiplier += 1
            print('Try again with secondary hash function with multiplier:', multiplier)
            bucket = hash_table.secondary_hash_function(key, multiplier)
            availability = hash_table._is_available(bucket)
            print('Is bucket', bucket, 'available?', availability)
        else:
            hash_table._bucket_setitem(bucket, key, value)
            print('Key is stored in bucket:', bucket, '\n')

# Question 5
print("\n5. (R-10.14) Show the result of rehashing the hash table shown below into a table of size 19 using the new "
      "hash function h(k) = 3k mod 17")
hash_table = ChainHashMap(19)
keys = {54: 1, 28: 2, 41: 3, 18: 4, 10: 5, 36: 6, 25: 7, 38: 8, 12: 9, 90: 10}

# Set items to buckets in hash table
for key, value in keys.items():
    buckets = []
    print('Key:', key, '--', 'Value:', value, )
    bucket = hash_table.rehash_function(key)  # perform hash function on all keys creating bucket destination
    buckets.append(bucket)
    for bucket in buckets:  # Set key and values to bucket destination
        hash_table._bucket_setitem(bucket, key, value)
        print('Bucket:', bucket, '\n')
