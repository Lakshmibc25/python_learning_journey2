try:
    boy = input("who do you want to marry ? -- ")
    if boy != "chandan":
        raise exit("you can only marry chandan. select him")
except Exception as e:
    print(f"Error: {e}")
else:
    print("yes! chandan is ready")