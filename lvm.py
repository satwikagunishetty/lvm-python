import os
from time import sleep
print()

os.system("tput setaf 3")
while(1):
 print("Welcome to automated lvm")

 os.system("tput setaf 7")

 print("\t\t..........................................................")

 os.system("tput setaf 6")

 print("""
 press 1: To show the available harddisk partition
 press 2: To create a physical volume
 press 3: To display available physical volume
 press 4: To create volume group
 press 5: To display available  volume groups
 press 6: To create, format, mount lvm
 press 7: To display available lvm
 press 8: To extend lvm
 press 9: To decrease lvm size
 press 10: To delete pv
 press 11: Exit
 """
 )
 os.system("tput setaf 3")
 choice=input("Enter your choice(1-10): ")

 if (choice == "1"):
   os.system("lsblk")
   sleep(2)
 elif (choice == "2"):
   disk_name= input("please specify the disk name:")
   os.system(f"pvcreate {disk_name}")
   sleep(2)
 elif (choice == "3"):
   os.system("pvdisplay")
   sleep(2)

 elif (choice == "4"):
   vgname = input("Name the volume group: ")
   disks = input("Please specify all the DiskNames ( with spaces ): ")
   os.system(f"vgcreate {vgname} {disks}")
   sleep(2)
 elif (choice == "5"):
   os.system("vgdisplay")
   sleep(2)
 elif (choice == "6"):
   vgname = input("Name of the Volume Group: ")
   lvmname = input("Name of the LVM: ")
   size = input("Enter the size in GB: ")
   db=input("Create a Directory:- Name it:")
   os.system(f"mkdir /{db}")
   mount_point = input("Specify the Mount Point: ")
   os.system(f"lvcreate --size {size}G --name {lvmname} {vgname}")
   os.system(f"mkfs.ext4 /dev/{vgname}/{lvmname}")
   os.system(f"mount /dev/{vgname}/{lvmname} {mount_point}")
   sleep(2)
 elif (choice == "7"):
   os.system("lvdisplay")
   sleep(2)

 elif (choice == "8"):
   vgname = input("Specify the name of the Volume Group: ")
   lvmname = input("Specify the name of the LVM: ")
   size = input("Size to be increased in GB: ")
   os.system(f"lvextend --size +{size}G /dev/{vgname}/{lvmname}")
   os.system(f"resize2fs /dev/{vgname}/{lvmname}")
   sleep(2)
 elif (choice == "9"):
   reduced_size=int(input("How much actual size you need (in GB): "))
   mounted_point= input("Specify the directory ")
   vgname = input("Name of the Volume Group: ")
   lvmname = input("Name of the LVM: ")
   os.system("umount /{mounted_point}")
   os.system(f"e2fsck -f /dev/mapper/{vgname}-{lvmname}")
   os.system(f"resize2fs /dev/mapper/{vgname}-{lvmname} {reduced_size}G")
   os.system(f"lvreduce -f --size {reduced_size}G /dev/mapper/{vgname}-{lvmname} -y")
   os.system(f"mount /dev/{vgname}/{lvmname} /{mounted_point}")
   sleep(2)
 elif (choice == "10"):
  mount_point = input(" Enter mount point")
  vgname= input("Enter vgname: ")
  lvmname = input("Enter lvmname: ")
  disks = input("Please specify all the DiskNames ( with spaces ): ")
  #unmount mount point
  os.system(f"umount /{mount_point}")
  #disable lvm
  os.system(f"lvchange -an /dev/{vgname}/{lvmname}")
  #delete lvm volume
  os.system(f"lvremove /dev/{vgname}/{lvmname}")
  #disable volumme group
  os.system(f"vgchange -an {vgname}")
  #delete volume group
  os.system(f"vgremove {vgname}")
  #delete pv
  os.system(f"pvremove {disks}")

 elif (choice == "11"):
   print("Exiting Lvm configuration....please wait")
   sleep(2)
   break
