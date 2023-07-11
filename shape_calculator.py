class Rectangle:

  #constrcutor with instance variables width and height
  def __init__(self,width,height):

    self.width = width
    self.height = height

  # setter function for width
  def set_width(self, width):
    self.width = width

  # setter function for height
  def set_height(self, height):
    self.height = height

  # getter function for the area
  def get_area(self):

    total = self.width * self.height

    return total

  # getter function for the perimeter
  def get_perimeter(self):

    perimeter = (2 * self.width + 2 * self.height)

    return perimeter
  
  # getter function for the diagonal
  def get_diagonal(self):

    diagonal = ((self.width ** 2 + self.height ** 2) ** .5)

    return diagonal

  # getter function for the picture
  def get_picture(self):
    
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    
    else:
      
      picture = "*" * self.width + "\n"
      
      picture *= self.height
      
      return picture
      
  # getter function for the amount inside
  def get_amount_inside(self, shape):
        if isinstance(shape, Rectangle):
            width_ratio = self.width // shape.width
            height_ratio = self.height // shape.height
            return width_ratio * height_ratio
          
        elif isinstance(shape, Square):
            side_ratio = self.width // shape.width
            return side_ratio * side_ratio
          
        else:
            return 0
  #override __str__ method for correct string representation
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

# create inherited subclass Square from superclass Rectangle
class Square (Rectangle):

  def __init__(self, width):

# pass in 1 argument becuase square has equal sides. Use Rectangle super class constructor. Square objects take the width values
    super().__init__(width,width)
      
  def set_side(self, side):
    self.width = side
    self.height = side

  #override __str__ method for correct string representation
  def __str__(self):
    return f"Square(side={self.width})"