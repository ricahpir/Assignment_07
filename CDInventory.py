#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# rcaphair, 2030-Jan-01, Edited File
# Created FileProcessor function defined as write_file
# Created IO function defined as del_Row
# Created DataProcessor function defined as add_Row()
# Added info doclines for new user to read 
# Updated Docstrings 
# Modified add_Row function with error exception to print warning message
# Updated read_file function to user pickle.load
#251 - 254 provided exception to File_Processor.read_file to pass 
#274 - 278 provided exception to File_Processor.read_file to pass 
#313 - 316 provided ValueError exception to intIDDel  
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.dat'  # data storage file
objFile = None  # file object



import pickle

# -- PROCESSING -- #
class DataProcessor:
    # Completed function for processing add
   
       """Function to process data from user to appended list of dictionaries

        Reads the data from user and adds into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
           str_id
           str_title
           str_artist
           table

        Returns:
            None."""
            
       @staticmethod     
       def add_Row(str_id, str_title, str_artist, table):
           """Function to allow user to pass new data to table.
           
           Args:
               str_id
               str_title
               str_artist 
               table.
               
            Returns:
                none. 
                
                """ 
           int_id = ''   
           try:
            int_id = int(str_id)    
           except ValueError:
            print('WARNING!!!! Be certain to enter ID numbers correctly!!!! \
                  If you fail to do so, the newest entry will be stuck in the data file \
                      THIS MEANS YOU WILL EITHER HAVE TO INPUT NOTHING WHEN PROMPTED \
                          WHEN TRYING TO DELETE THE CD -OR- YOU WILL HAVE TO DELETE THE CD FROM \
                              THE FILE ITSELF!!!')
                            
           dicRow = {'ID': int_id, 'Title': str_title, 'Artist': str_artist}
           table.append(dicRow)   
           
       @staticmethod
       def remove_row(id_to_remove, table):
           """Function to allow user to delete row. 
           
           Args:
               id_to_remove
               table
           
            Returns:
                blnCDRemoved
                
                """
           
           intRowNr = -1
           blnCDRemoved = False
           for row in table:
               intRowNr += 1
               if row['ID'] == id_to_remove:
                   del table[intRowNr]
                   blnCDRemoved = True
                   break
               
           return blnCDRemoved
            
class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        with open (file_name, 'rb') as fileObj:
             data = pickle.load(fileObj)
             return data
        
        
        # table.clear()  # this clears existing data and allows to load data from file
        # objFile = open(file_name, 'rb')
        
        # for line in objFile:
        #     data = line.strip().split(',')
        #     data = bytes(data)
        #     dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
        #     table.append(dicRow)
        # pickle.load(table, objFile)

    @staticmethod
    def write_file(file_name, table):
        """Function allows user to overwrite current lstTbl in txt file 

        Overwrites previously saved txt file data inputted by user into a 2D table list of txt or 
        (list of dicts) FYI one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        with open(file_name, 'wb') as fileObj:
            pickle.dump(table, fileObj)
        # objFile = open(file_nab')
        # for row in table:
        #     lstValues = list(row.values())
        #     lstValues[0] = bytes(lstValues[0])
        #     # objFile.write(',' .join(lstValues) + '\n') 
        #     # circle back here to work on formating 
        # pickle.dump(table, objFile)
        

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')


    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')


    @staticmethod
    def del_row_input():
        """Prompts user to input ID of inventory they would like to delete in lstTbl 
       
        Args:
            None.

        Returns:
            id_to_remove(int): a number the user provides to delete the appropriate dicRow.

        """
        
        id_to_remove = int(input('Which ID would you like to delete? ').strip())
       
        return id_to_remove
    
            
    @staticmethod
    def add_cd_input():
        """Takes user input of: ID, Title and Artist to be added to inventory file
        
        Args:
            None.
    
        Returns:
            str_id, str_title, str_artist
        """
       
        str_id = input('Enter ID: ').strip()
        str_title = input('What is the CD\'s title? ').strip()
        str_artist = input('What is the Artist\'s name? ').strip()
         
        return str_id, str_title, str_artist




    # Completed - I/O function del_Row added to complete 'delete' functionality

# 1. When program starts, read in the currently saved Inventory
try:
    FileProcessor.read_file(strFileName, lstTbl)
except Exception:
    pass

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            
            try:
                FileProcessor.read_file(strFileName, lstTbl)
            except Exception:
                print('Nothing found in file')
            
            
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
       
        strID, strTitle, strArtist = IO.add_cd_input()
       
        # 3.3.2 Add item to the table
        # Resolved 3-4 - moved processing code into function
        DataProcessor.add_Row(strID, strTitle, strArtist, lstTbl)

        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
        
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
        
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove  
        intIDDel = ''
        try:
         intIDDel = IO.del_row_input()
        except ValueError:
            print('Please enter an integer value')
        #(intDEL cut from here)
        # 3.5.2 search thru table and delete CD

        # Resolved - 2 - moved processing code into function
        
        blnCDRemoved = DataProcessor.remove_row(intIDDel, lstTbl)
    
        if blnCDRemoved:
             print('The CD was removed')
        else:
             print('Could not find this CD!')
        
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
        
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data

            # Resolved - 1 - moved processing code into function defined as write_file

            FileProcessor.write_file(strFileName, lstTbl)

        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')







