class PageValidationError(Exception):
    """Raised when a page can't be validated by 
       the presence of the element it looks for."""
   
        
class ItemValidationError(Exception):
    """Raised when an item's page doesn't match 
       the item selected in the inventory page."""


class ItemQuantityError(Exception):
    """Raised when the shopping cart's item
    count does not match the quantity of items added."""