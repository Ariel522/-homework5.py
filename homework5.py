immutable_var = [ 'irina', '31', 'lena', '12']
print (immutable_var)
immutable_var .append(44)
print (immutable_var)
immutable_var .extend('apple')
print (immutable_var)
mutable_list = ['banana', 'bool', 'onion']
print (mutable_list)
mutable_list .remove('bool')
print (mutable_list)
mutable_list .append('bread')
print (mutable_list)
mutable_list .extend([immutable_var])
print (mutable_list)