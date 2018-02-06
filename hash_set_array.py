
# Imports
from copy import deepcopy
# Use any appropriate data structure here.
from list_array import List
# Define the new_slot slot creation function.
new_slot = List

# Constants
SEP = '-' * 40


class HashSet:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, slots):
        """
        -------------------------------------------------------
        Initializes an empty HashSet of size slots.
        Use: hs = HashSet(slots)
        -------------------------------------------------------
        Precondition:
            size - number of initial slots in hashset (int > 0)
        Postconditions:
            Initializes an empty HashSet.
        -------------------------------------------------------
        """
        self._slots = slots
        self._table = []

        for i in range(self._slots):
            self._table.append(new_slot())
            
        self._count = 0
        
        return
    
    

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the hashset.
        Use: n = len( hs )
        -------------------------------------------------------
        Postconditions:
            Returns the number of values in the hashset.
        -------------------------------------------------------
        """
        return self._count
    
    

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the hashset is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Postconditions:
            Returns True if the hashset is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0
    
    

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot( key )
        -------------------------------------------------------
        Postconditions:
            returns:
            slot - list at the position of hash key in self._slots
        -------------------------------------------------------
        """
        
        hashkey = hash(key) % self._slots
        slot = self._table[hashkey]
        return slot
    
    

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the hashset contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            Returns True if the hashset contains key, False otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        return key in slot
    
    

    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the hashset, allows only one copy of value.
            Calls _rehash if the hashset _LOAD_FACTOR is exceeded 
            (i.e. if it equals the load factor).
        Use: inserted = hs.insert( value )
        -------------------------------------------------------
        Preconditions:
            value - a comparable data element (?)
        Postconditions:
            returns
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        
        slot = self._find_slot(value)
        
        if value not in slot:
            slot.insert_front(deepcopy(value))
            inserted = True
            
            self._count = self._count + 1
            
            if self._count > self._LOAD_FACTOR * self._slots:
                self._rehash()
        
        else:
            inserted = False
        
        
        return inserted
        
        

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns the value identified by key.
        Use: value = hs.find( key )
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            value - if it exists in the hashset, None otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)
        value = slot.find(key)
        return value
    
    

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the hashset, if it exists.
        Use: value = hs.remove( key )
        -------------------------------------------------------
        Preconditions:
            key - a comparable data element (?)
        Postconditions:
            returns:
            value - if it exists in the hashset, None otherwise.
        -------------------------------------------------------
        """
        slot = self._find_slot(key)

        value = slot.remove(key)
        
        if value is not None:
            self._count = self._count - 1

        return value
        
        

    def _rehash(self):
        """
        ---------------------------------------------------------
        Increases the number of slots in the hashset and reallocates 
        the existing data within the hashset to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Postconditions:
            Existing data is reallocated amongst the hashset table.
        -------------------------------------------------------
        """
        # save the old list, and create a new temporary list
        # new items are inserted into the front of the list
        
        self._slots = self._slots * 2 + 1
        
        temp_list = []
        
        for slot in self._table:
            for movie in slot:
                temp_list.append(movie)
            
        self._table = []
        for i in range(self._slots):
            self._table.append(new_slot())
            
        self._count = 0
        
        
        for movie in temp_list:
            slot = self._find_slot(movie)
        
            if movie not in slot:
                slot.insert_front(deepcopy(movie))
                self._count = self._count + 1
        
        return

