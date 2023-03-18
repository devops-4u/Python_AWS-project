import boto3 #boto3 is library used to connect aws with python
s3 = boto3.resource('s3')   #This is used to access s3
c=0
for bucket in s3.bucket.all():
    print(bucket)  #This will show all buckets name
    c = c+1   #This will show number of buckets
print (c)

s3.Bucket("dyeops_7011").downlaod_file("abc.txt","abcd.txt")  #This will download my txt file from bucket into local with the name abcd.txt