# Tower of Hanoi
def tower_of_hanoi(num, source, destination, auxiliary):
    # Base Case
    if num == 1:
        print(f"Move Disk {num} from Peg {source} to Peg {destination}")
        return
    else:
        # Move Disk (1 to n - 1) from source to auxiliary
        # Using destination as the auxiliary 
        tower_of_hanoi(num - 1, source, auxiliary, destination)
        # Move the largest disk (n) from source to destination
        print(f"Move Disk {num} from Peg {source} to Peg {destination}")
        # Move smaller disk from auxiliary to source
        tower_of_hanoi(num - 1, auxiliary, destination, source)


# C is the auxiliary, In order Peg A, Peg B and Peg C
print("Tower of Hanoi")
number = int(input("Enter number of disks: "))
tower_of_hanoi(number, "A", "C", "B")
