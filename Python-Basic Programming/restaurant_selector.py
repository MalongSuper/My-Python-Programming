# This program displays the restaurants that you can take your group of friends out
# Input if any person in your group is a vegetarian, a vegan or gluten-free
Vegetarian = str(input("Is anyone in your party a vegetarian? "))
if ((Vegetarian != 'Yes') and (Vegetarian != 'No')
        and (Vegetarian != 'no') and (Vegetarian != 'yes')):
    print("Error: You must type in either Yes or No. "
          "'Please proceed and try again")
else:
    Vegan = str(input("Is anyone in your party a vegan? "))
    if ((Vegan != 'Yes') and (Vegan != 'No')
            and (Vegan != 'no') and (Vegan != 'yes')):
        print("Error: You must type in either Yes or No. "
              "'Please proceed and try again")
    else:
        GluttenFree = str(input("Is anyone in your party gluten-free? "))
        if ((GluttenFree != 'Yes') and (GluttenFree != 'No')
                and (GluttenFree != 'no') and (GluttenFree != 'yes')):
            print("Error: You must type in either Yes or No. "
                  "'Please proceed and try again")
        else:
            print("Here are your restaurant choices")
            # From the list, display only the restaurants that are suitable for your group
            # Joe’s Gourmet Burgers — Vegetarian: No, Vegan: No, Gluten-Free: No
            if (((Vegetarian == 'No') and (Vegan == 'No') and (GluttenFree == 'No'))
                    or ((Vegetarian == 'no') and (Vegan == 'no') and (GluttenFree == 'no'))):
                print("Joe's Gourmet Burgers")
            # Main Street Pizza Company — Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
            if (((Vegetarian == 'Yes') and (Vegan == 'No') and (GluttenFree == 'Yes'))
                    or ((Vegetarian == 'yes') and (Vegan == 'no') and (GluttenFree == 'yes'))):
                print("Main Street Pizza Company")
            # Even if you are not any of the above, you can still eat at Main Street Pizza Company
            if (((Vegetarian == 'No') and (Vegan == 'No') and (GluttenFree == 'No'))
                    or ((Vegetarian == 'no') and (Vegan == 'no') and (GluttenFree == 'no'))):
                print("Main Street Pizza Company")
            if (((Vegetarian == 'No') and (Vegan == 'No') and (GluttenFree == 'Yes'))
                    or ((Vegetarian == 'no') and (Vegan == 'no') and (GluttenFree == 'yes'))):
                print("Main Street Pizza Company")
            if (((Vegetarian == 'Yes') and (Vegan == 'No') and (GluttenFree == 'No'))
                    or ((Vegetarian == 'yes') and (Vegan == 'no') and (GluttenFree == 'no'))):
                print("Main Street Pizza Company")
            # Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
            if (((Vegetarian == 'Yes') and (Vegan == 'Yes') and (GluttenFree == 'Yes'))
                    or ((Vegetarian == 'yes') and (Vegan == 'yes') and (GluttenFree == 'yes'))):
                print("Corner Café")
            # Even if you are not any of the above, you can still eat at Corner Café
            if (((Vegetarian == 'No') and (Vegan == 'No') and (GluttenFree == 'No'))
                    or ((Vegetarian == 'no') and (Vegan == 'no') and (GluttenFree == 'no'))):
                print("Corner Café")
            if (((Vegetarian == 'No') and (Vegan == 'Yes') and (GluttenFree == 'Yes'))
                    or ((Vegetarian == 'no') and (Vegan == 'yes') and (GluttenFree == 'yes'))):
                print("Corner Café")
            if (((Vegetarian == 'Yes') and (Vegan == 'No') and (GluttenFree == 'Yes'))
                    or ((Vegetarian == 'yes') and (Vegan == 'no') and (GluttenFree == 'yes'))):
                print("Corner Café")
            if (((Vegetarian == 'Yes') and (Vegan == 'Yes') and (GluttenFree == 'No'))
                    or ((Vegetarian == 'yes') and (Vegan == 'yes') and (GluttenFree == 'no'))):
                print("Corner Café")
            if (((Vegetarian == 'No') and (Vegan == 'No') and (GluttenFree == 'Yes'))
                    or ((Vegetarian == 'no') and (Vegan == 'no') and (GluttenFree == 'yes'))):
                print("Corner Café")
            if (((Vegetarian == 'No') and (Vegan == 'Yes') and (GluttenFree == 'No'))
                    or ((Vegetarian == 'no') and (Vegan == 'yes') and (GluttenFree == 'no'))):
                print("Corner Café")
            if (((Vegetarian == 'Yes') and (Vegan == 'No') and (GluttenFree == 'No'))
                    or ((Vegetarian == 'yes') and (Vegan == 'no') and (GluttenFree == 'no'))):
                print("Corner Café")
            # Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
            if (((Vegetarian == 'Yes') and (Vegan == 'No') and (GluttenFree == 'No'))
                    or ((Vegetarian == 'yes') and (Vegan == 'no') and (GluttenFree == 'no'))):
                print("Mama's Fine Italian")
            # Even if you are not any of the above, you can still eat at Mama's Fine Italian
            if (((Vegetarian == 'No') and (Vegan == 'No') and (GluttenFree == 'No'))
                    or ((Vegetarian == 'no') and (Vegan == 'no') and (GluttenFree == 'no'))):
                print("Mama's Fine Italian")
            # The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
            if (((Vegetarian == 'Yes') and (Vegan == 'Yes') and (GluttenFree == 'Yes'))
                    or ((Vegetarian == 'yes') and (Vegan == 'yes') and (GluttenFree == 'yes'))):
                print("The Chef's Kitchen")
            # Even if you are not any of the above, you can still eat at The Chef's Kitchen
            if (((Vegetarian == 'No') and (Vegan == 'No') and (GluttenFree == 'No'))
                    or ((Vegetarian == 'no') and (Vegan == 'no') and (GluttenFree == 'no'))):
                print("The Chef's Kitchen")
            if (((Vegetarian == 'No') and (Vegan == 'Yes') and (GluttenFree == 'Yes'))
                    or ((Vegetarian == 'no') and (Vegan == 'yes') and (GluttenFree == 'yes'))):
                print("The Chef's Kitchen")
            if (((Vegetarian == 'Yes') and (Vegan == 'No') and (GluttenFree == 'Yes'))
                    or ((Vegetarian == 'yes') and (Vegan == 'no') and (GluttenFree == 'yes'))):
                print("The Chef's Kitchen")
            if (((Vegetarian == 'Yes') and (Vegan == 'Yes') and (GluttenFree == 'No'))
                    or ((Vegetarian == 'yes') and (Vegan == 'yes') and (GluttenFree == 'no'))):
                print("The Chef's Kitchen")
            if (((Vegetarian == 'No') and (Vegan == 'No') and (GluttenFree == 'Yes'))
                    or ((Vegetarian == 'no') and (Vegan == 'no') and (GluttenFree == 'yes'))):
                print("The Chef's Kitchen")
            if (((Vegetarian == 'No') and (Vegan == 'Yes') and (GluttenFree == 'No'))
                    or ((Vegetarian == 'no') and (Vegan == 'yes') and (GluttenFree == 'no'))):
                print("The Chef's Kitchen")
            if (((Vegetarian == 'Yes') and (Vegan == 'No') and (GluttenFree == 'No'))
                    or ((Vegetarian == 'yes') and (Vegan == 'no') and (GluttenFree == 'no'))):
                print("The Chef's Kitchen")
            # If you type Yes and No, you should either type all in capitals or all in non-capitals
            # Otherwise, the program will not display the results








