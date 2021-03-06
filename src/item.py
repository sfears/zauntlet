from src.static import Value, Image
from src.gameobject import GameObject
class Items (GameObject):
    """
        Walls are gameObjects that the player can pickup.
    """

    def __init__ (self, x, y, itemImage, itemSize=Value.GENERIC_ITEM_SIZE):
        super().__init__(x, y, itemSize)
        self.image.blit(itemImage, (0,0))

    def onPickup (self, data):
        """
            Called on item pickup by the player. Override by the type of item.
        """
        data.groups.items.remove(self)

class HeartContainer (Items):
    """
        Heart containers add player HP back.
    """

    def __init__ (self, row, col):
        super().__init__(row, col, Image.HEART, Value.HEART_CONTAINER_SIZE)

    def onPickup (self, data):
        """
            Add player HP
        """
        data.player.addHP(data)
        data.groups.items.remove(self)

class FoodOfYendor (Items):
    """
        The fabled FoodOfYendor.
    """

    def __init__ (self, row, col):
        super().__init__(row, col, Image.FOODOFYENDOR, Value.FOODOFYENDOR_SIZE)

    def onPickup (self, data):
        """
            End the game.
        """
        data.winGameSequence(data)
