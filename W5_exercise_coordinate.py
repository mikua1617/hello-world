
def __eq__(self, other):
        if self.getX()==other.getX() and self.getY()==other.getY():
            return True
        else:
            return False
            
def __repr__(self):
        return "Coordinate(%d, %d)" % (self.getX(), self.getY())

