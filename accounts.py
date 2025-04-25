def add(l: list, d: dict):
    l.append(d)
def read(l: list):
    for x in l:
        print(x)
if __name__ == "__main__":
    ps = []
    p = int(input("how many accounts? ")) + 1
    for i in range(1,p):
        ps.append({input(f"username #{i}: "):input(f"password #{i}: ")})
    read(ps)