empty_space="           blah            "
print(len(empty_space))
print(empty_space.rstrip())
print("length with lstrip" +" "+ str(len(empty_space.rstrip())))
print(empty_space.lstrip())
print("length with lstrip" +" "+ str(len(empty_space.lstrip())))
print(empty_space.strip())
print("length with strip" +" "+ str(len(empty_space.strip())))

website = "www.python.org"
print(website.lstrip("w",))
print(website.lstrip("org"))
print(website.strip(".worg"))

