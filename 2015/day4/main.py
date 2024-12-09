import hashlib

secret_key = "iwrupvqb"
answer = 0

while True:
    possibility = secret_key + str(answer) 
    md5_hash = hashlib.md5(possibility.encode()).hexdigest()
    
    if md5_hash.startswith("000000"):
        print(answer)
        break  # Stop the loop once you find the answer
    else:
        answer += 1

