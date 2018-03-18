

from node_db import Node, NodeStorage


def main_menu_usage():
    print ("\n\n"
           "------------------------------------------------------\n"
           "|               Divice Database                        |\n"
           "------------------------------------------------------"
           "\n\nSelect from one of these options:\n\n"
           "(1) Add Device\n"
           "(2) Remove Device\n"
           "(3) Create device inventory report\n"
           "(4) Quit\n")


def main_menu():

    while True:
        main_menu_usage()
        try:
            answer = int(input("Option: "))
            print("\nOption selected: {}\n\n".format(answer))
        except ValueError:
            answer = 0
            print("\n\n****ERROR: Please choose a numeric option****\n\n")
            continue

        if answer == 4:
            print("\nQuiting.....")
            break

        elif answer == 1:
            node_id = input("Device name: ").strip().upper()
            site_id = input("Site: ").strip().upper()
            management_ip = input("Management IP: ").strip()
            console_id = input("Console server: ").strip().upper()
            vendor_id = input("Vendor: ").strip().upper()
            platform_id = input("Platform: ").strip().upper()
            os_id = input("SW Version: ").strip()
            #import pdb; pdb.set_trace()
            device = ds.find_node(node_id)
            if device is None:
                device = Node(node_id, site_id, management_ip, console_id, vendor_id, platform_id, os_id)
                print("--------------------------")
                print(device.description)
                print("--------------------------")
                print("\n\n Please review and confirm above device information\n")
                confirmation = input(str("\ny/n: ").strip())
                if confirmation == "y":
                    add_device = ds.add_node(device)
                # device = ds.add_node(node_id, site_id, management_ip, console_id, vendor_id, platform_id, os_id)
                    print("\n\nDevice has been added to database\n\n")
                else:
                    continue

            else:
                print("\n\nDevice {} already exist in databse with below information\n\n".format(device.node_id))
                print("--------------------------")
                print(device.description)
                print("--------------------------")
            # print("\nAdding Device to Database...\n\n\n")
            # print("Generating Thank you note...\n\n\n")


        elif answer == 2:
            node_id = input("Device name: ").strip().upper()
            rm_device = ds.find_node(node_id)
            if rm_device is None:
                print("\n\nDevice {} does not exist...".format(node_id))
            else:
                rm_device = ds.remove_node(node_id)
                print("\n\nDevice {} has been removed".format(node_id))

        elif answer == 3:
            ds.generate_report()

        else:
            print("\n\n****ERROR:  Invalid selection*******\n\n")




if __name__ == "__main__":
    print("\n\nProgram starting...  \n\n")
    ds = NodeStorage()
    main_menu()

