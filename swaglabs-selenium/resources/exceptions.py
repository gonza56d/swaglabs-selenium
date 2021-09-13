class PageValidationError(Exception):
    """Raised when a page can't be validated by 
       the presence of the element it looks for."""
   
        
class ItemValidationError(Exception):
    """Raised when an item's page doesn't match 
       the item selected in the inventory page."""
    